from inspect import getmembers, isfunction, isclass, getsource, signature, _empty, isdatadescriptor
from datetime import datetime
import PySimpleGUIlib
import click
import logging
import json
import re
import os

########################################################
#     _                       _       _                #
#    | |                     | |     | |               #
#    | |_ ___ _ __ ___  _ __ | | __ _| |_ ___  ___     #
#    | __/ _ \ '_ ` _ \| '_ \| |/ _` | __/ _ \/ __|    #
#    | ||  __/ | | | | | |_) | | (_| | ||  __/\__ \    #
#     \__\___|_| |_| |_| .__/|_|\__,_|\__\___||___/    #
#                      | |                             #
#                      |_|                             #
########################################################
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
TABLE_Only_table_RETURN_TEMPLATE = '''|Name|Meaning|\n|---|---|\n| **return** | $ |''' # $ - is the part for return value

##############################################################################
#                    _                         _                             #
#                   | |                       | |                            #
#      ___ _   _ ___| |_ ___  _ __ ___     ___| | __ _ ___ ___  ___  ___     #
#     / __| | | / __| __/ _ \| '_ ` _ \   / __| |/ _` / __/ __|/ _ \/ __|    #
#    | (__| |_| \__ \ || (_) | | | | | | | (__| | (_| \__ \__ \  __/\__ \    #
#     \___|\__,_|___/\__\___/|_| |_| |_|  \___|_|\__,_|___/___/\___||___/    #
#                                                                            #
#                                                                            #
##############################################################################

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

def get_params_part(code: str, versbose=True) -> dict:
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
    if code == None or code == '' or ':param' not in code:
        return {}
    elif ':return' in code: # strip ':return:'
        new_code = code[:code.index(':return:')]
        
        regg_ = re.compile(r':return[\d\D]*?:param', flags=re.MULTILINE)
        if len(list(regg_.finditer(new_code))) > 0:
            if versbose:
                print(f'warning-> ":return" MUST BY AT THE END. FIX IT NOW in "{code}"!!!\nBut i will try to parse it...')
            code = re.sub(regg_, r':param', code)
        else:
            code = new_code

    try:
        only_params = code[code.index(':param'):]  # get_only_params_string(code)
    except Exception as e:
        if versbose:
            print(f'SORRY, fail at parsing that stuff in "{code}"')
        return {}

    # making dict
    param_lines = only_params.split(':param ')
    param_lines = [re.sub(r'[ ]{2,}', ' ', i.strip(' ').strip('\t').replace('\n', '  '), flags=re.MULTILINE)
                   for i in param_lines if i.strip()]  # filter empty lines

    args_kwargs_pairs = {}
    for i in param_lines:

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


def special_cases(function_name, function_obj, sig, doc_string, line_break=None):

    doca, params_names = doc_string.strip(), list(dict(sig).keys())
    only_self = 'self' in params_names and len(params_names) == 1

    ############################################################################
    #          _                                                 _             #
    #         | |                                               | |            #
    #      ___| | __ _ ___ ___   _ __  _ __ ___  _ __   ___ _ __| |_ _   _     #
    #     / __| |/ _` / __/ __| | '_ \| '__/ _ \| '_ \ / _ \ '__| __| | | |    #
    #    | (__| | (_| \__ \__ \ | |_) | | | (_) | |_) |  __/ |  | |_| |_| |    #
    #     \___|_|\__,_|___/___/ | .__/|_|  \___/| .__/ \___|_|   \__|\__, |    #
    #                           | |             | |                   __/ |    #
    #                           |_|             |_|                  |___/     #
    ############################################################################

    """
    # TEMPLATE1

        def Get(self):
           ''' '''
    # TEMPLATE2 -return -param
        def Get(self):
            '''
            blah blah blah
            '''
    # TEMPLATE3  +return -param
        def Get(self):
            ''' 
            blah blah blah
            :return: blah-blah
            '''
    """
    
    if is_propery(function_obj):
        # TEMPLATE1
        if only_self and not doca:
            return special_case(ok=True, just_text=f'\n\n#### property: {function_name}\n\n',              sig='', table='')
        # TEMPLATE2
        elif only_self and doca and ':param' not in doca and ':return:' not in doca:
            return special_case(ok=True, just_text=f'\n\n#### property: {function_name}\n{get_doc_desc(doca, function_obj)}\n\n',              sig='', table='')
        # TEMPLATE3
        elif only_self and doca and ':param' not in doca and ':return:' in doca:
            return_part, desc = get_return_part(doca, line_break=line_break), get_doc_desc(doca, function_obj)
            return special_case(ok=True, just_text='', 
                                         sig=f'\n\n#### property: {function_name}\n{desc}\n\n',
                                         table=TABLE_Only_table_RETURN_TEMPLATE.replace('$', return_part) + '\n\n')

    ################################################################################################################
    #                                      _        _                                _   _               _         #
    #                                     | |      | |                              | | | |             | |        #
    #     _ __   ___  _ __ _ __ ___   __ _| |   ___| | __ _ ___ ___   _ __ ___   ___| |_| |__   ___   __| |___     #
    #    | '_ \ / _ \| '__| '_ ` _ \ / _` | |  / __| |/ _` / __/ __| | '_ ` _ \ / _ \ __| '_ \ / _ \ / _` / __|    #
    #    | | | | (_) | |  | | | | | | (_| | | | (__| | (_| \__ \__ \ | | | | | |  __/ |_| | | | (_) | (_| \__ \    #
    #    |_| |_|\___/|_|  |_| |_| |_|\__,_|_|  \___|_|\__,_|___/___/ |_| |_| |_|\___|\__|_| |_|\___/ \__,_|___/    #
    #                                                                                                              #
    #                                                                                                              #
    ################################################################################################################

    """
    # TEMPLATE1

        def Get(self):
           ''' '''
    # TEMPLATE2 -return -param
        def Get(self):
            '''
            blah blah blah
            '''
    # TEMPLATE3  +return -param
        def Get(self):
            ''' 
            blah blah blah
            :return: blah-blah
            '''
    # TEMPLATE4  -return +param
        def SetFocus(self, elem):
            ''' 
            blah blah blah
            :param elem: qwerty
            '''
    """

    # TEMPLATE1
    if only_self and not doca:
        return special_case(ok=True, just_text=f'\n\n```python\n{function_name}()\n```\n\n', sig='', table='')
    # TEMPLATE2
    elif only_self and doca and ':param' not in doca and ':return:' not in doca:
        return special_case(ok=True, just_text=f'\n\n{doca}\n\n```python\n{function_name}()\n```\n\n', sig='', table='')
    # TEMPLATE3
    elif only_self and doca and ':param' not in doca and ':return:' in doca:
        return_part, desc = get_return_part(doca, line_break=line_break), get_doc_desc(doca, function_obj)
        return special_case(ok=True, just_text='',  sig=f'\n\n{desc}\n\n`{function_name}()`\n\n',
                                     table=TABLE_Only_table_RETURN_TEMPLATE.replace('$', return_part) + '\n\n')
    # TEMPLATE4
    elif only_self and doca and ':param' not in doca and ':return:' in doca:
        return special_case(ok=False, just_text='', sig='', table='')


    return special_case(ok=False, just_text='', sig='', table='')


def get_doc_desc(doc, original_obj):

    return_in = ':return' in doc
    param_in = ':param' in doc
    
    if return_in and param_in and doc.index(':return') < doc.index(':param'):
        logging.error(f'BS. You need to FIX IT. PROBLEM ":return:" BEFORE ":param:" in "{original_obj.__name__}"')

    if ':param'  in doc: doc = doc[:doc.index(':param')]
    if ':return' in doc: doc = doc[:doc.index(':return:')]
    if ':param'  in doc: doc = doc[:doc.index(':param')]
    if ':return' in doc: doc = doc[:doc.index(':return:')]

    desc = doc.strip().replace('    ', '')

    return f'\n{desc}' if desc else ''

def is_propery(func):
    return isdatadescriptor(func) and not isfunction(func)

def get_sig_table_parts(function_obj, function_name, doc_string, logger=None, is_method=False, line_break=None, insert_md_section_for__class_methods=False):
    """ Convert "function + __doc__" tp "method call + params table" in MARKDOWN """
    doc_string = doc_string.strip()
    # qpqpqpqpqpqpqpqpqpqpqpqpqpqpqpqpqpqpqpqpqpqpqpqpqp
    # 0   0            Making INIT_CALL          0   0 #
    # qpqpqpqpqpqpqpqpqpqpqpqpqpqpqpqpqpqpqpqpqpqpqpqpqp

    try:
        rows = []
        sig = {'self': None} if is_propery(function_obj) else signature(function_obj).parameters
    except Exception as e:
        if logger: logger.error(f'PROBLEM WITH "{function_obj}" "{function_name}":\nit\'s signature is BS. Ok, I will just return \'\' for \'signature\' and \'param_table\'\nOR BETTER - delete it from the 2_readme.md.\n======')
        return '', ''
    if not is_propery(function_obj):
        for key in sig:
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


    sig_content = f',\n{TAB_char}'.join(rows) if len(rows) > 2 else f', '.join(rows) if rows else ''
    # # # make 2 line signature into 1-line
    # # # sig_content = f',\n{TAB_char}'.join(rows)
    # # # if sig_content.count('\n') < 3: sig_content = re.sub(r'\n[ \t]{,8}', ' ', sig_content, flags=re.MULTILINE)

    sign = "\n\n{0}\n\n```\n{1}({2})\n```".format(get_doc_desc(doc_string, function_obj), function_name, sig_content)

    if is_method:
        if insert_md_section_for__class_methods:
            # sign = "#### {1}\n\n{0}\n\n```\n{1}({2})\n```".format(get_doc_desc(doc_string, function_obj), function_name, sig_content)
            sign = "\n\n{0}\n\n```\n{1}({2})\n```".format(get_doc_desc(doc_string, function_obj), function_name, sig_content)
        else:
            sign = "{0}\n\n```\n{1}({2})\n```".format(get_doc_desc(doc_string, function_obj), function_name, sig_content)
    # --------------
    # SPECIAL CASES
    # --------------
    result = special_cases(function_name, function_obj, sig, doc_string, line_break=line_break)
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
    
    try:
        if 'skip readme' in injection['function_object'].__doc__:
            return ''
    except Exception as e:
        return ''

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


def main(do_full_readme=False, files_to_include: list = [], logger:object=None, output_name:str=None, delete_html_comments:bool=True, delete_x3_newlines:bool=True, allow_multiple_tags:bool=True, line_break:str=None, insert_md_section_for__class_methods:bool=True, remove_repeated_sections_classmethods:bool=False, output_repeated_tags:bool=False, skip_dunder_method:bool=True):
    """
    Goal is:
    1) load 1_.md 2_.md 3_.md 4_.md
    2) get memes - classes and functions in PSG
    3) find all tags in 2_
    4) structure tags and REAL objects
    5) replaces classes, functions.
    6) join 1 big readme file

    :param do_full_readme: (bool=True) if False - use only 2_readme.md
    :param files_to_include: (list=[]) list of markdown files to include in output markdown
    :param logger: (object=None) logger object from logging module
    :param output_name: (str=None) base filename of output markdown file
    :param delete_html_comments: (bool=True) flag for preprocessing input markwon text e.g. deleting every html tag, that is injection_point
    :param delete_x3_newlines: (bool=True) flag for deleting '\\n\\n\\n' in final output makrdown text
    :param allow_multiple_tags: (bool=True) flag for replacing every tag in "input markdown text"
    :param line_break: (str=None) linebreak_character in "return part"
    :param insert_md_section_for__class_methods: (bool=True) insert '###' sign to class_methods when outputing in markdown
    :param remove_repeated_sections_classmethods: (bool=True)
    :param output_repeated_tags: (bool=True) log REPEATED tags in file
    :param skip_dunder_method: (bool=True) skip __something__ methods in classes
    """

    if logger: logger.info(f'STARTING')

    # 888888888888888888888888888888888888888888
    # ===========  1 loading files =========== #
    # 888888888888888888888888888888888888888888
    readme  = readfile('2_readme.md')
    # 8888888888888888888888888888888888888888888888888888888888888888888888888
    # ===========  2 GET classes, funcions, varialbe a.k.a. memes =========== #
    # 8888888888888888888888888888888888888888888888888888888888888888888888888
    psg_members = getmembers(PySimpleGUIlib) # variables, functions, classes

    psg_funcs = [o for o in psg_members if isfunction(o[1])] # only functions
    psg_classes = [o for o in psg_members if isclass(o[1])]  # only classes
    psg_classes_ = list(set([i[1] for i in psg_classes]))    # boildown B,Btn,Butt -into-> Button
    psg_classes = list(zip([i.__name__ for i in psg_classes_], psg_classes_))

    # 8888888888888888888888888888888888888888888888888888888
    # ===========  3 find all tags in 2_readme  =========== #
    # 8888888888888888888888888888888888888888888888888888888
    # PLAN:
    # (1) REMOVE HEADER

    # (2) find good tags e.g.   <!-- <+func.PopupScrolled+> -->

    # (3) (optional) find '_' tags e.g.
    #     '_' tag - is a tag, that has '_' after '.'
    #                                               
    #     Example:  <!-- <+func._PopupScrolled+> -->
    #                          /\                   
    #                          |---that's sign of a bad tags

    # (4) (optional) log repeated tags.
    #      like <!-- <+class.B+> -->
    #                  and
    #           <!-- <+class.Button+> -->
    # 8888888888888888888888888888888888888888888888888888888

    # >1 REMOVE HEADER
    started_mark = '<!-- Start from here -->'
    if started_mark in readme:
        readme = readme[readme.index(started_mark)+len(started_mark):]

    # 2> find good tags
    re_tags     = re.compile(r'<!-- <\+[a-zA-Z_]+[\d\w_]*\.([a-zA-Z_]+[\d\w_]*)\+> -->')
    mark_points = [i for i in readme.split('\n') if re_tags.match(i)]
    
    special_dunder_methods = ['init', 'repr', 'str', 'next']
    # 3> find '_' tags OPTION
    if skip_dunder_method:
        re_bad_tags = re.compile(r'<!-- <\+[a-zA-Z_]+[\d\w_]*\.([_]+[\d\w_]*)\+> -->')
        for i in readme.split('\n'):
            if re_bad_tags.match(i.strip()):
                if not [s_tag for s_tag in special_dunder_methods if s_tag in i.strip()]:
                    readme = readme.replace(i, '\n')

    # 4> log repeated tags
    if output_repeated_tags:
        if not allow_multiple_tags and len(list(set(mark_points))) != len(mark_points):
            mark_points_copy = mark_points[:]
            [mark_points_copy.remove(x) for x in set(mark_points)]
            if logger:
                logger.error("You have repeated tags! \n {0}".format(
                    ','.join(mark_points_copy)))
            return ''

    # 8888888888888888888888888888888888888888888888888888888888888
    # ===========  4 structure tags and REAL objects  =========== #
    # 8888888888888888888888888888888888888888888888888888888888888

    injection_points = []
    classes_method_tags = [j for j in mark_points if 'func.' not in j]
    func_tags = [j for j in mark_points if 'func.' in j]

    # 0===0 functions 0===0
    for tag in func_tags:

        try:
            function_name = part2 = tag.split('.')[1].split('+')[0]

            # {{{{{{{{{ filter number }}}}}}}}}
            number = ''
            if part2[0] in ['1', '2']:
                number, part2 = part2[0], part2[1:]

            # {{{{{{{{{ find function }}}}}}}}}
            founded_function = [func for func_name,
                                func in psg_funcs if func_name == function_name]
            if not founded_function:
                if logger:
                    logger.error(f'function "{function_name}" not found in PySimpleGUI')
                continue
            if len(founded_function) > 1:
                if logger:
                    logger.error(f'more than 1 function named "{function_name}" found in PySimpleGUI')
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
                logger.error(f' General error in parsing function tag: tag = "{tag}"; error="{str(e)}"')
            continue

    # 0===0 classes 0===0
    for tag in classes_method_tags:
        try:
            class_name, method_name = tag.split('.')
            class_name, method_name = part1, part2 = class_name.split('+')[-1], method_name.split('+')[0]

            # {{{{{{{{{ filter number }}}}}}}}}
            number = ''
            if part2[0] in ['1', '2']:
                number, method_name = part2[0], part2[1:]

            # {{{{{{{{{ find class }}}}}}}}}
            founded_class = [a_class_obj
                            for a_class_name, a_class_obj in psg_classes
                            if a_class_name == class_name]
            if not founded_class:
                if logger: logger.error(f'skipping tag "{tag}", WHY: not found in PySimpleGUI')
                continue
            if len(founded_class) > 1:
                if logger: logger.error(f'skipping tag "{tag}", WHY: found more than 1 class in PySimpleGUI')
                continue

            # {{{{{{{{{ find method }}}}}}}}}
            try:
                if method_name != 'doc':
                    founded_method = getattr(founded_class[0], method_name)
                else:
                    founded_method = None
            except AttributeError as e:
                if logger:
                    logger.error(f'METHOD not found!: {str(e)}')
                continue
            except Exception as e:
                if logger:
                    logger.error(f'Error in finding the METHOD: {str(e)}')
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
                logger.error(f' General error in parsing class_method tag: tag = "{tag}"; error="{str(e)}"')
            continue

    # 888888888888888888888888888888888888888
    # ===========  5 injecting  =========== #
    # 888888888888888888888888888888888888888
    # PLAN:
    # (1) replace tags in 2_readme
    #      with properly formateed text
    # (2) log some data
    # 8888888888888888888888888888888888888888888888888888888


    # 1> log some data
    success_tags = []
    bad_tags = []
    for injection in injection_points:
        
        # SPECIAL CASE: X.doc tag
        if injection['part2'] == 'doc':
            readme = readme.replace(injection['tag'], injection['parent_class'].__doc__)
        
        else:
            content = render(injection, logger=logger, line_break=line_break,
                insert_md_section_for__class_methods=insert_md_section_for__class_methods,)
        
            tag = injection["tag"]
            if content:
                success_tags.append(f'{tag} - COMPLETE')
            else:
                bad_tags.append(f'{tag} - FAIL')

            readme = readme.replace(tag, content)

    # 2> log some data
    if logger:
        success_tags_str    = '\n'.join(success_tags).strip()
        bad_tags_str        = '\n'.join(bad_tags).strip()
        
        # good message
        good_message        = f'DONE {len(success_tags)} TAGS:\n' + '\n'.join(success_tags) if success_tags_str else 'All tags are wrong//'
        # bad  message
        bad_message         = f'FAIL WITH {len(bad_tags)} TAGS:\n' + '\n'.join(bad_tags) if bad_tags_str else 'No bad tags, YES!'

        logger.info(good_message)
        logger.info(bad_message)


    # 8888888888888888888888888888888888
    # ===========  6 join  =========== #
    # 8888888888888888888888888888888888

    files = []
    if 0 in files_to_include: files.append(readfile('1_HEADER_top_part.md'))
    if 1 in files_to_include: files.append(readme)
    if 2 in files_to_include: files.append(readfile('3_FOOTER.md'))
    if 3 in files_to_include: files.append(readfile('4_Release_notes.md'))

    Joined_MARKDOWN = '\n\n'.join(files) if do_full_readme or files else readme

    if output_name:
        with open(output_name, 'w', encoding='utf-8') as ff:
            CURR_DT = datetime.today().strftime('<!-- CREATED: %Y-%m-%d %H.%M.%S -->\n')
            content = CURR_DT + Joined_MARKDOWN

            # {{{{{{{{{ html removing }}}}}}}}}
            if delete_html_comments:
                if logger:
                    logger.info('Deleting html comments')

                # remove html comments
                filt_readme = re.sub(r'<!--([\s\S]*?)-->', '\n', content, flags=re.MULTILINE)

                for i in range(5):
                    filt_readme = filt_readme.replace('\n\n\n', '\n\n')

                # add staked_edit
                if '<!--stackedit_data:' in content:
                    stackedit_text = content[content.index('<!--stackedit_data:'):]
                    filt_readme += stackedit_text

                content = filt_readme

            # {{{{{{{{{ filter multiple multilines EVERYWHERE }}}}}}}}}
            if delete_x3_newlines:

                # removing spaces
                content = re.sub(r'^[ ]+$', '', content, flags=re.MULTILINE)
                # removing \n
                content = re.sub(r'\n{3,}', '\n\n', content, flags=re.MULTILINE)

            # {{{{{{{{{ remove repeated sections classmethods }}}}}}}}}
            if remove_repeated_sections_classmethods:
                rega = re.compile(r'((\#+\s\w+)\n\s){2}', flags=re.MULTILINE)
                for index, i in enumerate(re.finditer(rega, content)):
                    print(f'{index} - > {i.group(0)}')
                    print(f'{index} - > {i.group(1)}')
                    content = content.replace(i.group(0), i.group(1))
                # re
                # content = re.sub(rega, r'\1', content, flags=re.MULTILINE)

            # Write into a file
            ff.write(content.strip())

        if logger:
            logger.info(f'ending. writing to a file///////////////')

        return content

    if logger:
        logger.error(f'Error in main')


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
             output_name='OUTPUT.txt',
             delete_html_comments=True)
    elif my_mode == 'debug-mode2':
        log_file_name = 'usage.log.txt'
        import logging
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)

        my_file = logging.FileHandler(log_file_name, mode='w')
        my_file.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s>%(levelname)s: %(message)s')
        my_file.setFormatter(formatter); logger.addHandler(my_file)

        main(logger=logger, files_to_include=[1],
             output_name='OUTPUT.txt',
             delete_html_comments=True)

'''
notes:

Как оказалось, декоратор @property делает из метода вот что:
- isdatadescriptor(class.method_as_property) вернет True
'''