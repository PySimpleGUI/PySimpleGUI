from inspect import getmembers, isfunction, isclass, getsource, signature, _empty
from datetime import datetime
import PySimpleGUIlib
import click
import logging
import json
import re
import os
TAB_char = '    '
TABLE_TEMPLATE='''
                    Parameter Descriptions:

                        |Name|Meaning|
                        |---|---|
                        {md_table}
                        {md_return}
                        
                        '''
TABLE_ROW_TEMPLATE = '|{name}|{desc}|'
TABLE_RETURN_TEMPLATE = '|||\n| **return** | {return_guy} |'
TABLE_Only_table_RETURN_TEMPLATE = '''|Name|Meaning|\n|---|---|\n| **return** | $ |'''

from collections import namedtuple
special_case = namedtuple('special_case', 'ok sig table just_text'.split(' '))


"""
injection_points:
injection_point structure cal look like this:

FUNCTION

    {
        "tag" : "<!-- <+func.hello+> -->",
        "function_object" : "<function hello at 0x7fdcfd888ea0>",
        "parent_class" : None,
        "part1" : "func",
        "part2" : "hello",
        "number" : ""
    }
    {
        "tag" : "<!-- <+func.1hello+> -->",
        "function_object" : "<function hello at 0x7fdcfd888ea0>",
        "parent_class" : None,
        "part1" : "func",
        "part2" : "hello",
        "number" : "1"
    }

CLASS

    {
        "tag" : "<!-- <+Mike_Like.__init__+> -->",
        "function_object" : <function Mike_Like.__init__ at 0x7fdcfd888ea0>,
        "parent_class" : <class '__main__.Mike_Like'>,
        "part1" : "Mike_Like",
        "part2" : "__init__",
        "number" : ""
    }
    {
        "tag" : "<!-- <+Mike_Like.2__init__+> -->",
        "function_object" : <function Mike_Like.__init__ at 0x7fdcfd888ea0>,
        "parent_class" : <class '__main__.Mike_Like'>,
        "part1" : "Mike_Like",
        "part2" : "__init__",
        "number" : "2"
    }
"""

def get_params_part(code: str) -> dict:
    """
    Find ":param " part in given "doc string".

    from __doc__ to {
        'parameter' :  'desctiption',
        'parameter2' : 'desctiption2',
        'parameter3' : 'desctiption3',
    }
    """
    code = code.strip()
    
    # if doc_string is empty
    if code == None:           return {}
    elif '' == code.strip():   return {}
    elif ':param' not in code: return {}
    elif ':return' in code: # strip ':return:'
        new_code = code[:code.index(':return:')]
        
        regg_ = re.compile(r':return[\d\D]*?:param', flags=re.MULTILINE)
        if len(list(regg_.finditer(new_code))) > 0:
            if versbose:
                print(f'warning-> ":return" MUST BY AT THE END. FIX IT NOW in {name_}!!!\nBut i will try to parse it...')
            code = re.sub(regg_, r':param', code)
        else:
            code = new_code

    try:
        only_params = code[code.index(':param'):]  # get_only_params_string(code)
    except Exception as e:
        if versbose: print(f'SORRY, fail at parsing that stuff in {name_}')
        return {}





    # making dict
    param_lines = only_params.split(':param ')
    param_lines = [re.sub(r'[ ]{2,}', ' ', i.strip(' ').strip('\t').replace('\n', '  '), flags=re.MULTILINE)
                   for i in param_lines if i.strip()]  # filter empty lines

    args_kwargs_pairs = {}
    for index, i in enumerate(param_lines):

        cols = i.split(':')
        param_name, els = cols[0], '\n'.join(
            [j.strip() for j in ':'.join(cols[1:]).split('\n')])
        # param_name, els = cols[0],  ' '.join([j.strip() for j in ':'.join(cols).split('\n')]) # can be this:

        param_name, els = param_name.strip(), els.strip()
        args_kwargs_pairs[param_name] = els

    return args_kwargs_pairs


def get_return_part(code: str, line_break=None) -> str:
    """ Find ":return:" part in given "doc string"."""
    if not line_break:
        line_break = ' <br> '

    if ':return:' not in code:
        return ''
    return code[code.index(':return:')+len(':return:'):].strip().replace('\n', line_break)


def special_cases(function_name, sig, doc_string, line_break=None):


    doca, params_names = doc_string.strip(), list(dict(sig).keys())
    if 'self' in params_names and len(params_names) == 1 and not doca:
        """
        def Get(self):
            ''' '''

        ->
        ```python
        Get()
        ```
        """
        return special_case(ok=True, just_text=f'\n\n```python\n{function_name}()\n```\n\n', sig='', table='')

    # -return -param
    elif 'self' in params_names and len(params_names) == 1 and doca and ':param' not in doca and ':return:' not in doca:
        """
        def Get(self):
            ''' 
            blah blah blah
            '''

        ->

        ```python
        Get() # blah blah blah
        ```

        """
        return special_case(ok=True, just_text=f'\n\n{doca}\n\n```python\n{function_name}()\n```\n\n', sig='', table='')

    # +return -param
    elif 'self' in params_names and len(params_names) == 1 and doca and ':param' not in doca and ':return:' in doca:
        """
        def Get(self):
            ''' 
            blah blah blah
            :return: blah-blah
            '''

        ->

        ```python
        Get()
        ```

        *table*

        """
        return_part, desc = get_return_part(doca, line_break=line_break), get_doc_desc(doca)
        return special_case(ok=True, just_text='',
                                     sig=f'\n\n{desc}\n\n`{function_name}()`\n\n',
                                     table=TABLE_Only_table_RETURN_TEMPLATE.replace('$', return_part) + '\n\n')

    # +return -param
    elif 'self' in params_names and len(params_names) == 1 and doca and ':param' not in doca and ':return:' in doca:
        """
        def SetFocus(self, elem):
            ''' 
            blah blah blah
            
            :param elem: qwerty
            '''
        """
        return special_case(ok=False, just_text='', sig='', table='')
    return special_case(ok=False, just_text='', sig='', table='')


def get_doc_desc(doc_string):

    if ':param' in doc_string:  doc_string = doc_string[:doc_string.index(':param')]
    if ':return:' in doc_string: doc_string = doc_string[:doc_string.index(':return:')]
    if ':param' in doc_string:  doc_string = doc_string[:doc_string.index(':param')]
    if ':return:' in doc_string: doc_string = doc_string[:doc_string.index(':return:')]

    desc = doc_string.strip().replace('    ', '')

    return f'\n{desc}' if desc else ''


def get_sig_table_parts(function_obj, function_name, doc_string, logger=None, is_method=False, line_break=None, insert_md_section_for__class_methods=False):
    """
    Convert "function + __doc__" tp "method call + params table" in MARKDOWN
    """

    doc_string = doc_string.strip()

    # qpqpqpqpqpqpqpqpqpqpqpqpqpqpqpqpqpqpqpqpqpqpqpqpqp
    # 0   0            Making INIT_CALL          0   0 #
    # qpqpqpqpqpqpqpqpqpqpqpqpqpqpqpqpqpqpqpqpqpqpqpqpqp

    try:
        sig, rows = signature(function_obj).parameters, []
    except Exception as e:
        if logger: logger.error(f'PROBLEM WITH "{function_obj}" "{function_name}":\nit\'s signature is BS. Ok, I will just return \'\' for \'signature\' and \'param_table\'\nOR BETTER - delete it from the 2_readme.md.\n======')
        return '', ''
    for index, key in enumerate(sig):
        val = sig[key].default
        if 'self' == str(key):
            continue
        if val == _empty:        rows.append(key)
        elif val == None:        rows.append(f'{key}=None')
        elif type(val) is int:   rows.append(f'{key}={val}')
        elif type(val) is str:   rows.append(f'{key}="{val}"')
        elif type(val) is tuple: rows.append(f'{key}={val}')
        elif type(val) is bool:  rows.append(f'{key}={val}')
        else:
            raise Exception(f'IDK this type -> {key, val}')


    sig_content = f',\n{TAB_char}'.join(rows) if len(rows) > 2 else f', '.join(rows)
    # # # make 2 line signature into 1-line
    # # # sig_content = f',\n{TAB_char}'.join(rows)
    # # # if sig_content.count('\n') < 3: sig_content = re.sub(r'\n[ \t]{,8}', ' ', sig_content, flags=re.MULTILINE)

    sign = "\n\n{0}\n\n```\n{1}({2})\n```".format(get_doc_desc(doc_string), function_name, sig_content)

    if is_method:
        if insert_md_section_for__class_methods:
            sign = "#### {1}\n\n{0}\n\n```\n{1}({2})\n```".format(get_doc_desc(doc_string), function_name, sig_content)
        else:
            sign = "{0}\n\n```\n{1}({2})\n```".format(get_doc_desc(doc_string), function_name, sig_content)
    # --------------
    # SPECIAL CASES
    # --------------
    result = special_cases(function_name, sig, doc_string, line_break=line_break)
    if result.ok:
        if result.just_text:
            return result.just_text, ''
        else:
            return result.sig, result.table
    # qpqpqpqpqpqpqpqpqpqpqpqpqpqpqpqpqpqpqpqpqpqpqpqpqp
    # 0   0          Making params_TABLE         0   0 #
    # qpqpqpqpqpqpqpqpqpqpqpqpqpqpqpqpqpqpqpqpqpqpqpqpqp

    # 1
    return_guy = get_return_part(doc_string, line_break=line_break)
    if not return_guy:
        md_return = return_guy = ''
    else:
        return_guy = return_guy.strip()
        md_return = TABLE_RETURN_TEMPLATE.format(return_guy=return_guy)
        # return_guy = f'\n\nreturn value: {return_guy}\n'
        # return_guy_val_str = return_guy

    
    # 2
    md_table = '\n'.join([TABLE_ROW_TEMPLATE.format(name=name, desc=desc)
                           for name, desc in
                           get_params_part(doc_string).items()])

    # 3
    params_TABLE = TABLE_TEMPLATE.format(md_table=md_table, md_return=md_return).replace(TAB_char, '').replace('    ', '').replace('\t', '')

    # 1 and N
    # if len(get_params_part(doc_string).items()) == 1:
    #     params_TABLE = TABLE_TEMPLATE.replace('Parameters Descriptions:', 'Parameter Description:').format(md_table=md_table, md_return=md_return).replace(TAB_char, '').replace('    ', '').replace('\t', '')
    # else:
    #     params_TABLE = TABLE_TEMPLATE.format(md_table=md_table, md_return=md_return).replace(TAB_char, '').replace('    ', '').replace('\t', '')

    if not md_table.strip():
        params_TABLE = ''
        
        if return_guy:
            sign = sign[:-4] + f' -> {return_guy}\n```\n'

    return sign, params_TABLE


def pad_n(text): return f'\n{text}\n'


def render(injection, logger=None, line_break=None, insert_md_section_for__class_methods=False):
    if injection['part1'] == 'func':  # function
        sig, table = get_sig_table_parts(function_obj=injection['function_object'],
                                         function_name=injection['part2'],
                                         insert_md_section_for__class_methods=insert_md_section_for__class_methods,
                                         doc_string=injection['function_object'].__doc__, logger=logger, line_break=line_break)
    else:  # class method
        function_name = injection['parent_class'].__name__ if injection['part2'] == '__init__' else injection['part2']
        sig, table = get_sig_table_parts(function_obj=injection['function_object'],
                                         function_name=function_name, is_method=True,
                                         insert_md_section_for__class_methods=insert_md_section_for__class_methods,
                                         doc_string=injection['function_object'].__doc__, logger=logger, line_break=line_break)


    if injection['number'] == '':
        return pad_n(sig) + pad_n(table)
    elif injection['number'] == '1':
        return pad_n(sig)
    elif injection['number'] == '2':
        return pad_n(table)
    else:
        if logger: logger.error(f'Error in processing {injection}')


def readfile(fname):
    with open(fname, 'r', encoding='utf-8') as ff:
        return ff.read()


def main(do_full_readme=False, files_to_include: list = [], logger=None, output_name=None, delete_html_comments=True, delete_x3_newlines=True, allow_multiple_tags=True, line_break=None, insert_md_section_for__class_methods=True, remove_repeated_sections_classmethods=False):

    """
    Goal is:
    1) load 1_.md 2_.md 3_.md 4_.md
    2) get memes - classes and functions in PSG
    3) find all tags in 2_
    4) structure tags and REAL objects
    5) replaces classes, functions.
    6) join 1 big readme file

    :param do_full_readme: if False - use only 2_readme.md
    :param files_to_include: list of markdown files to include in output markdown
    :param logger: logger object from logging module
    :param delete_html_comments: flag for preprocessing input markwon text e.g. deleting every html tag, that is injection_point
    :param allow_multiple_tags: flag for replacing every tag in "input markdown text"
    :param delete_x3_newlines: flag for deleting '\\n\\n\\n' in final output makrdown text
    :param output_name: base filename of output markdown file
    :param line_break: linebreak_character in "return part"
    """
    if logger: logger.info(f'STARTING')

    # 888888888888888888888888888888888888888888
    # ===========  1 loading files =========== #
    # 888888888888888888888888888888888888888888
    HEADER_top_part = readfile('1_HEADER_top_part.md')  # 1
    readme          = readfile('2_readme.md')           # 2
    FOOTER          = readfile('3_FOOTER.md')           # 3
    Release_notes   = readfile('4_Release_notes.md')    # 4


    # 8888888888888888888888888888888888888888888888888888888888888888888888888
    # ===========  2 GET classes, funcions, varialbe a.k.a. memes =========== #
    # 8888888888888888888888888888888888888888888888888888888888888888888888888
    psg_members = getmembers(PySimpleGUIlib)

    psg_funcs = [o for o in psg_members if isfunction(o[1])]
    psg_classes = [o for o in psg_members if isclass(o[1])]
    psg_classes_ = list(set([i[1] for i in psg_classes]))  # filtering
    psg_classes = list(zip([i.__name__ for i in psg_classes_], psg_classes_))

    # IlilIlilIlilIlilIlilIlilIlilIlilIlilIlIlIl
    # ilIli-                       | |    -ilIli
    # ilIli-   _ __ ___   ___  __ _| |_   -ilIli
    # ilIli-  | '_ ` _ \ / _ \/ _` | __|  -ilIli
    # ilIli-  | | | | | |  __/ (_| | |_   -ilIli
    # ilIli-  |_| |_| |_|\___|\__,_|\__|  -ilIli

    # 8888888888888888888888888888888888888888888888888888888
    # ===========  3 find all tags in 2_readme  =========== #
    # 8888888888888888888888888888888888888888888888888888888

    # strip top of the file head
    started_mark = '<!-- Start from here -->'
    if started_mark in readme:
        readme = readme[readme.index(started_mark)+len(started_mark):]

    # find with regex
    regex_pattern = re.compile(r'<!-- <\+[a-zA-Z_]+[\d\w_]*\.([a-zA-Z_]+[\d\w_]*)\+> -->')
    mark_points = [i for i in readme.split('\n') if regex_pattern.match(i)]

    # if there are REPEATED tags -> show them.
    # if not allow_multiple_tags and len(list(set(mark_points))) != len(mark_points):
    #     [mark_points.remove(x) for x in set(mark_points)]
    #     if logger:
    #         logger.error("You have repeated tags! \n {0}".format(
    #             ','.join(mark_points)))
    #     return ''

    # 8888888888888888888888888888888888888888888888888888888888888
    # ===========  4 structure tags and REAL objects  =========== #
    # 8888888888888888888888888888888888888888888888888888888888888

    injection_points = []
    classes_method_tags = [j for j in mark_points if 'func.' not in j]
    func_tags = [j for j in mark_points if 'func.' in j]

    # 0===0 functions 0===0
    for tag in func_tags:

        try:
            __, function_name = tag.split('.')
            function_name = function_name.split('+')[0]
            part2 = function_name

            # {{{{{{{{{ filter number }}}}}}}}}
            number = ''
            if part2[0] in ['1', '2']:
                number, part2 = part2[0], part2[1:]

            # {{{{{{{{{ find function }}}}}}}}}
            founded_function = [func for func_name,
                                func in psg_funcs if func_name == function_name]
            if not founded_function:
                if logger: logger.error(f'function "{function_name}" not found in PySimpleGUI')
                continue
            if len(founded_function) > 1:
                if logger: logger.error(f'more than 1 function named "{function_name}" found in PySimpleGUI')
                continue

            # {{{{{{{{{ collect }}}}}}}}}
            injection_points.append({
                "tag": tag,
                "function_object": founded_function[0],
                "parent_class": None,
                "part1": 'func',
                "part2": part2,
                "number": number,
            })
        except Exception as e:
            if logger:
                logger.error(f'               {str(e)}')
            continue

    # 0===0 classes 0===0
    for tag in classes_method_tags:
        try:
            class_name, method_name = tag.split('.')
            class_name, method_name = class_name.split('+')[-1], method_name.split('+')[0]
            part1, part2 = class_name, method_name

            # {{{{{{{{{ filter number }}}}}}}}}
            number = ''
            if part2[0] in ['1', '2']:
                number, method_name = part2[0], part2[1:]

            # {{{{{{{{{ find class }}}}}}}}}
            founded_class = [a_class_obj for a_class_name,
                             a_class_obj in psg_classes if a_class_name == class_name]
            if not founded_class:
                if logger: logger.error(f'class "{tag}" not found in PySimpleGUI')
                continue
            if len(founded_class) > 1:
                if logger: logger.error(f'more than 1 class named "{tag}" found in PySimpleGUI')
                continue

            # {{{{{{{{{ find method }}}}}}}}}
            try:
                if method_name != 'doc':
                    founded_method = getattr(founded_class[0], method_name)
                    # GLG.append([founded_method, founded_class[0], method_name])
                    # string_type = str(type(founded_method))
                    # if 'property' in string_type or 'bound' in string_type:
                    #     print(string_type)
                    #     # import pdb; pdb.set_trace();
                    #     if logger:
                    #         logger.error(f'Property "{founded_method}" is not parsed.')
                    #     continue
                else:
                    founded_method = None
            except AttributeError as e:
                if logger: logger.error(f'METHOD not found!: {str(e)}')
                continue
            except Exception as e:
                if logger: logger.error(str(e))
                continue

            # {{{{{{{{{ collect }}}}}}}}}
            injection_points.append({
                "tag": tag,
                "function_object": founded_method,
                "parent_class": founded_class[0],
                "part1": part1,
                "part2": part2,
                "number": number,
            })
        except Exception as e:
            if logger:
                logger.error(f'```````````````````````{str(e)}')
            continue

    # 888888888888888888888888888888888888888
    # ===========  5 injecting  =========== #
    # 888888888888888888888888888888888888888

    success_tags = []
    bad_tags = []
    for injection in injection_points:
        if injection['part2'] == 'doc':  # our special snowflake "doc"
            readme = readme.replace(injection['tag'], injection['parent_class'].__doc__)
        else:
            tag = injection['tag']
            content = render(injection, logger=logger, line_break=line_break, insert_md_section_for__class_methods=insert_md_section_for__class_methods,)
            if content:
                success_tags.append(f'{tag} - COMPLETE')
            else:
                bad_tags.append(f'{tag} - FAIL')
            readme = readme.replace(injection['tag'], content)
    if logger:
        success_tags_str    = '\n'.join(success_tags).strip()
        bad_tags_str        = '\n'.join(bad_tags).strip()
        good_message        = f'DONE {len(success_tags)} TAGS:\n' + '\n'.join(success_tags) if success_tags_str else 'All tags are wrong//'
        bad_message         = f'FAIL WITH {len(bad_tags)} TAGS:\n' + '\n'.join(bad_tags) if bad_tags_str else 'No bad tags, YES!'
        logger.info(good_message)
        logger.info(bad_message)
    # 8888888888888888888888888888888888
    # ===========  6 join  =========== #
    # 8888888888888888888888888888888888

    files = []
    if 0 in files_to_include: files.append(HEADER_top_part)
    if 1 in files_to_include: files.append(readme)
    if 2 in files_to_include: files.append(FOOTER)
    if 3 in files_to_include: files.append(Release_notes)

    Joined_MARKDOWN = '\n\n'.join(files) if do_full_readme or files else readme

    if output_name:
        with open(output_name, 'w', encoding='utf-8') as ff:
            curr_dt = datetime.today().strftime('<!-- CREATED: %Y-%m-%d %H.%M.%S -->\n')
            content = curr_dt + Joined_MARKDOWN

            # {{{{{{{{{ html removing }}}}}}}}}
            if delete_html_comments:
                if logger: logger.info('Deleting html comments')

                # remove html comments
                filt_readme = re.sub(
                    r'<!--([\s\S]*?)-->', '\n', content, flags=re.MULTILINE)

                for i in range(5):
                    filt_readme = filt_readme.replace('\n\n\n', '\n\n')

                # add staked_edit
                if '<!--stackedit_data:' in content:
                    stackedit_data = content[content.index(
                        '<!--stackedit_data:'):]
                    filt_readme += stackedit_data

                content = filt_readme

            # {{{{{{{{{ filter multiple multilines EVERYWHERE }}}}}}}}}
            if delete_x3_newlines:

                # removing spaces
                content = re.sub(r'^[ ]+$', '', content, flags=re.MULTILINE)
                # removing \n
                content = re.sub(r'\n{3,}', '\n\n',
                                 content, flags=re.MULTILINE)

            # {{{{{{{{{ remove repeated sections classmethods }}}}}}}}}
            if remove_repeated_sections_classmethods:

                rega = re.compile(r'((\#+\s\w+)\n\s){2}', flags=re.MULTILINE)
                for index, i in enumerate(re.finditer(rega, content)):
                    print(f'{index} - > {i.group(0)}')
                    print(f'{index} - > {i.group(1)}')
                    content = content.replace(i.group(0), i.group(1))
                # re
                # content = re.sub(rega, r'\1', content, flags=re.MULTILINE)

            # FINISH
            content = content.strip()
            ff.write(content)

        if logger: logger.info(f'ending. writing to a file///////////////')
        return content

    if logger: logger.error(f'Error in main')


@click.command()
@click.option('-nol', '--no_log',                   is_flag=True, help='Disable log')
@click.option('-rml', '--delete_log',               is_flag=True, help='Delete log file after generating')
@click.option('-rmh', '--delete_html_comments',     is_flag=True, help='Delete html comment in the generated .md file')
@click.option('-o', '--output_name',                default='FINALreadme.md',   type=click.Path(), help='Name for generated .md file')
@click.option('-lo', '--log_file',                  default='LOGS.log',         type=click.Path(), help='Name for log file')
def cli(no_log, delete_log, delete_html_comments, output_name, log_file):
    # --------------------
    # ----- logging setup-
    # --------------------

    logger = logging.getLogger(__name__)
    if no_log:
        logger.setLevel(logging.CRITICAL)
        # delete_log = True
    else:
        logger.setLevel(logging.DEBUG)

    my_file = logging.FileHandler(log_file, mode='w')
    my_file.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s>%(levelname)s: %(message)s')

    my_file.setFormatter(formatter)
    logger.addHandler(my_file)

    main(logger=logger,
         files_to_include=[0, 1, 2, 3],
         output_name=output_name,
         delete_html_comments=delete_html_comments)

    # --------------------
    # ----- POST process--
    # --------------------

    if delete_log:
        # delete log file
        log_file = os.path.join(os.path.dirname(
            os.path.abspath(__file__)), log_file)
        if os.path.exists(log_file):
            try:
                os.remove(log_file)
            except Exception as e:
                logger.error(str(e))

if __name__ == '__main__':
    # my_mode = 'cli-mode'
    # my_mode = 'debug-mode'
    my_mode = 'debug-mode2'

    if my_mode == 'cli-mode':
        cli()
    elif my_mode == 'debug-mode':
        main(files_to_include=[0, 1, 2, 3],
             output_name='johnson_n_johnson.txt',
             delete_html_comments=True)
    elif my_mode == 'debug-mode2':
        import logging; logger = logging.getLogger(__name__); logger.setLevel(logging.DEBUG)
        my_file = logging.FileHandler('usage.log.txt', mode='w'); my_file.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s>%(levelname)s: %(message)s')
        my_file.setFormatter(formatter); logger.addHandler(my_file);
        main(logger=logger, files_to_include=[1],
             output_name='johnson_n_johnson.txt',
             delete_html_comments=True)
