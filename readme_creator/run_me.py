import re,datetime,time,os,platform,json,PySimpleGUI as sg; from subprocess import Popen; from make_real_readme import main
cd = os.path.dirname(os.path.abspath(__file__))

def readfile(filename):
    with open(filename, 'r', encoding='utf-8') as ff: return ff.read()
def writefile(fpath, content):
    with open(fpath, 'w', encoding='utf-8') as ff: ff.write(content)
def writejson(a_path:str, a_dict:dict) -> None:
    with open(a_path, 'w', encoding='utf-8') as output_file: json.dump(a_dict, output_file, ensure_ascii=False, indent=2)
def readjson(a_path:str) -> dict:
    with open(a_path, 'r', encoding='utf-8') as f: return json.load(f)


def openfile(a_path):
    # File exists?
    if not os.path.exists(a_path): return sg.Popup(f"Error! This file doesn't exists: {a_path}")

    # check: OS
    if 'Windows' in platform.system():
        os.startfile(a_path)

    elif 'Linux' in platform.system():
        Popen(f'exo-open "{a_path}"', shell=True)

def opendir(a_path):
    # Folder exists?
    if not os.path.exists(a_path): return sg.Popup(f"Error! This directory doesn't exists: {a_path}")

    # check: OS
    if 'Windows' in platform.system():
        os.startfile(a_path)

    elif 'Linux' in platform.system():
        Popen(f'exo-open --launch FileManager --working-directory "{a_path}"', shell=True)


########################################################################
#                              __ _            _                       #
#                             / _(_)          | |                      #
#    __   __   ___ ___  _ __ | |_ _  __ _     | |__   ___ _ __ ___     #
#    \ \ / /  / __/ _ \| '_ \|  _| |/ _` |    | '_ \ / _ \ '__/ _ \    #
#     \ V /  | (_| (_) | | | | | | | (_| |    | | | |  __/ | |  __/    #
#      \_/    \___\___/|_| |_|_| |_|\__, |    |_| |_|\___|_|  \___|    #
#                                    __/ |                             #
#                                   |___/                              #
########################################################################
def load_configs(): return readjson(os.path.join(cd, 'app_configs.json'))
def save_configs(a_config:dict): writejson(os.path.join(cd, 'app_configs.json'), a_config)



APP_CONFIGS = load_configs()
README_OFILENAME = APP_CONFIGS['README_FILENAME']
CALL_REFERENCE_OFILENAME = APP_CONFIGS['CALL_REFERENCE_FILENAME']


##-#-#-# ##-#-#-#
# Post-process logic
##-#-#-# ##-#-#-#
insert_md_section_for__class_methods = False
remove_repeated_sections_classmethods = False

class BESTLOG(object):
    def __init__(self, filename):
        # my_file = logging.FileHandler(filename, mode='w')
        # my_file.setLevel(logging.DEBUG)
        # my_file.setFormatter(logging.Formatter('%(asctime)s>%(levelname)s: %(message)s'))
        # logger = logging.getLogger(__name__)
        # logger.setLevel(logging.DEBUG)
        # logger.addHandler(my_file)
        self.filename = filename
        self.json_name = filename + '.json'
        self.error_list = []
        self.warning_list = []
        self.info_list = []
        self.debug_list = []
        self.tick_amount=1
        self.names = self.messages_names = 'error warning info debug'.split(' ')

    def tick(self):
        self.tick_amount+=1
        return self.tick_amount

    #######################################################################
    #      __             _                             _ _               #
    #     / _|           | |                           (_) |              #
    #    | |_ ___  _ __  | |_ _ __ __ _ _ __  ___ _ __  _| | ___ _ __     #
    #    |  _/ _ \| '__| | __| '__/ _` | '_ \/ __| '_ \| | |/ _ \ '__|    #
    #    | || (_) | |    | |_| | | (_| | | | \__ \ |_) | | |  __/ |       #
    #    |_| \___/|_|     \__|_|  \__,_|_| |_|___/ .__/|_|_|\___|_|       #
    #                                            | |                      #
    #                                            |_|                      #
    #######################################################################
    def error(self, m):     self.error_list.append([self.tick(), m])
    def warning(self, m):   self.warning_list.append([self.tick(), m])
    def info(self, m):      self.info_list.append([self.tick(), m])
    def debug(self, m):     self.debug_list.append([self.tick(), m])

    ##########################################
    #      __                                #
    #     / _|                               #
    #    | |_ ___  _ __   _ __ ___   ___     #
    #    |  _/ _ \| '__| | '_ ` _ \ / _ \    #
    #    | || (_) | |    | | | | | |  __/    #
    #    |_| \___/|_|    |_| |_| |_|\___|    #
    #                                        #
    #                                        #
    ##########################################
    def tolist(self):    return zip([self.error_list, self.warning_list, self.info_list, self.debug_list], self.names)
    def todict(self):    return {'error' : self.error_list, 'warning' : self.warning_list, 'info' : self.info_list, 'debug' : self.debug_list}
    
    def save(self):
        all_messages_list = []
        for messages, message_type in self.tolist():
            all_messages_list.extend([{'message_type' : message_type, 'message_text' : m_text, 'message_time' : m_time} for m_time, m_text in messages])

        # sort messages on time
        all_messages_list = sorted(all_messages_list, key=lambda x: x['message_time'])
        
        # convert time
        # for i in all_messages_list: i['message_time'] = i['message_time'].strftime('%Y-%m-%d %H:%M:%S.%f')

        writejson(self.json_name, all_messages_list)
    def load(self, **kw):
        '''
            return dict with messages
            
            kw = {
                use_psg_color : bool
                show_time : bool
            }
        '''

        # plan:
        # read json, convert time

        # read
        all_messages_list = readjson(self.json_name)
        # convert time
        # for i in all_messages_list: i['message_time'] = datetime.datetime.strptime(i['message_time'], '%Y-%m-%d %H:%M:%S.%f')

        def format_message(message):
            if kw['show_time']:
                return str(message['message_time']) + ':' + message['message_text'] 
            else:
                return message['message_text']


        #=========#
        # 4 lists #
        #=========#
        error_list =   [i for i in all_messages_list if i['message_type'] == 'error']
        warning_list = [i for i in all_messages_list if i['message_type'] == 'warning']
        info_list =    [i for i in all_messages_list if i['message_type'] == 'info']
        debug_list =   [i for i in all_messages_list if i['message_type'] == 'debug']


        #=================#
        # and 1 more list #
        #=================#
        colors = {'warning' : 'magenta', 'info' : 'black'}
        warning_info_ = []
        for message in sorted(warning_list + info_list, key=lambda x: x['message_time']):
            if kw['use_psg_color']:
                warning_info_.append([   format_message(message),
                                        colors.get(message['message_type'])    ])
            else:
                warning_info_.append(format_message(message))

        error_list = map(format_message, error_list)
        warning_list = map(format_message, warning_list)
        info_list = map(format_message, info_list)
        debug_list = map(format_message, debug_list)

        return error_list, warning_list, info_list, debug_list, warning_info_

def compile_call_ref(output_filename='output/LoG_call_ref', **kw):
    ''' Compile a "5_call_reference.md" file'''

    log_obj = BESTLOG(os.path.join(cd, output_filename))
    
    main(logger=log_obj,
         main_md_file='markdown input files/5_call_reference.md',
         insert_md_section_for__class_methods=insert_md_section_for__class_methods,
         remove_repeated_sections_classmethods=remove_repeated_sections_classmethods,
         files_to_include=[],
         output_name=CALL_REFERENCE_OFILENAME,
         delete_html_comments=True)
    log_obj.save()
    return log_obj.load(**kw)

def compile_readme(output_filename='output/LoG', **kw):
    ''' Compile a "2_readme.md" file'''
    log_obj = BESTLOG(os.path.join(cd, output_filename))
    main(logger=log_obj,
         insert_md_section_for__class_methods=insert_md_section_for__class_methods,
         remove_repeated_sections_classmethods=remove_repeated_sections_classmethods,
         files_to_include=[0, 1, 2, 3],
         output_name=README_OFILENAME,
         delete_html_comments=True)
    log_obj.save()
    return log_obj.load(**kw)

def compile_all_stuff(**kw):
    '''
        Compile a "2_ and 5_" .md filess
        return output from them
    '''
    result_readme  = compile_readme(**kw)
    result_call_ref = compile_call_ref(**kw)
    return result_readme, result_call_ref


########################################
#     _____                            #
#    |  __ \                           #
#    | |__) |__  _ __  _   _ _ __      #
#    |  ___/ _ \| '_ \| | | | '_ \     #
#    | |  | (_) | |_) | |_| | |_) |    #
#    |_|   \___/| .__/ \__,_| .__/     #
#               | |         | |        #
#               |_|         |_|        #
########################################

def md2psg(target_text):
    # target = 'This is **bold** and *italic* words'
    #              V
    # sg.T('This is '), sg.T('bold', font=...bold), ...'

    # imports
    from collections import namedtuple
    spec = namedtuple('spec', 'char text'.split(' '))

    # START
    # =====
    parts = re.compile(r'([\*]{1,2})([\s\S]*?)([\*]{1,2})', flags=re.M|re.DOTALL).split(target_text)
    chuncks, skip_this = [], 0
    for index, part in enumerate(parts):
        if skip_this != 0:
            skip_this -= 1; continue

        if part not in ['*', '**']: chuncks.append(part)
        else:
            skip_this = 2
            chuncks.append(spec(part, parts[index+1]))

    font_norm = ('Mono 13 ')     # (*sg.DEFAULT_FONT, 'italic')
    font_bold = ('Mono 13 italic')     # (*sg.DEFAULT_FONT, 'italic')
    font_ita  = ('Mono 13 bold')       # (*sg.DEFAULT_FONT, 'bold')
    
    list_of_Ts = []
    for chunck in chuncks:
        if type(chunck) is str:     list_of_Ts.append(sg.T(chunck, font=font_norm, size=(len(chunck), 1), pad=(0,0)))
        elif type(chunck) is spec:
            if chunck.char == '*':  list_of_Ts.append(sg.T(chunck.text, font=font_ita, pad=(0,0), size=(len(chunck.text), 1)))
            if chunck.char == '**': list_of_Ts.append(sg.T(chunck.text, font=font_bold,  pad=(0,0), size=(len(chunck.text), 1)))
    return list_of_Ts


def mini_GUI():
    my_font = ("Helvetica", 12)
    my_font2 = ("Helvetica", 12, "bold")
    my_font3 = ("Helvetica", 15, "bold")
    my_font4 = ("Mono", 18, "bold")

    def make_tab(word):
        return [[
            sg.Column(layout=[
                [sg.T('debug', font=my_font, text_color='blue')],
                [sg.ML(size=(70-15, 15), key=f'-{word}-debug-')],
                [sg.T('error', font=my_font, text_color='red')],
                [sg.ML(size=(70-15, 15), key=f'-{word}-error-')],
            ]),
            sg.T('            '), sg.Column(layout=[
                [sg.T('warning', font=my_font2)],
                [sg.ML(size=(70-12, 15), key=f'-{word}-warning-')],
                [sg.T('info', font=my_font2)],
                [sg.ML(size=(70-12, 15), key=f'-{word}-info-')],
            ]),
            sg.Column(layout=[
                [sg.T('warning_info', font=my_font3)],
                [sg.ML(size=(110, 42-8), key=f'-{word}-warning_info-')],
            ]),
        ]]
    layout = [
        [ sg.TabGroup(  [[
                            sg.Tab('README', make_tab('README')),
                            sg.Tab('CALL_REF', make_tab('CALL_REF'))
                        ]]
                     )
        ]
    ]

    window = sg.Window('We are live! Again! --- ' + 'Completed making            {}, {}'.format(os.path.basename(README_OFILENAME), os.path.basename(CALL_REFERENCE_OFILENAME)), [
        [sg.T(size=(25,1), font=my_font, key='-compile-time-')],
        [sg.T(f'The PySimpleGUI module being processed is {sg}')],
        [  
            sg.B('Run again (F1)', key='-run-')
            ,sg.CB('show time in logs (F2)', False, key='show_time')
            ,sg.CB('Logs with Color (F3)', True, key='use_psg_color')
            ,sg.B('open call ref', key='-open_call_ref-')
            ,sg.B('open readme.txt', key='-open_readme.txt-')
            ,sg.B('open "db folder"', key='-open_db_folder-')
            ,sg.T(' '*30)
            ,sg.Col([
                    # [sg.T('output name for call_ref markdown file', key=(15,1)), sg.I(key='')],
                    [*md2psg('markdown outputFileName *FOR* **readme  **: '), sg.I(README_OFILENAME, key='md1'), sg.B('open in explorer', key='open in explorer_readme')],
                    [*md2psg('markdown outputFileName *FOR* **call ref**: '), sg.I(CALL_REFERENCE_OFILENAME, key='md2'), sg.B('open in explorer', key='open in explorer_calref')]
                ])
        ]
        ,*layout
    ], resizable=True, finalize=True, location=(0,0), return_keyboard_events = True)
    
    def update_time_in_GUI(): window['-compile-time-'](datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S.%f'))

    def update_compilation_in_psg(values):
        # get results
        result_readme, result_call_ref = compile_all_stuff(use_psg_color=values['use_psg_color'], show_time=values['show_time'])

        # DO 2_readme
        window['-README-error-']('\n'.join(result_readme[0]))
        window['-README-warning-']('\n'.join(result_readme[1]))
        window['-README-info-']('\n'.join(result_readme[2]))
        window['-README-debug-']('\n'.join(result_readme[3]))
        # /// colors warning_info
        window['-README-warning_info-'].update('')
        if values['use_psg_color']:
            for text, color in result_readme[-1]:
                window['-README-warning_info-'].print(text, text_color=color)
        else:
            window['-README-warning_info-']('\n'.join(result_readme[-1]))
        
        # DO 5_cal_ref
        window['-CALL_REF-error-']('\n'.join(result_call_ref[0]))
        window['-CALL_REF-warning-']('\n'.join(result_call_ref[1]))
        window['-CALL_REF-info-']('\n'.join(result_call_ref[2]))
        window['-CALL_REF-debug-']('\n'.join(result_call_ref[3]))
        # /// colors warning_info
        window['-CALL_REF-warning_info-'].update('')
        if values['use_psg_color']:
            for text, color in result_call_ref[-1]:
                window['-CALL_REF-warning_info-'].print(text, text_color=color)
        else:
            window['-CALL_REF-warning_info-']('\n'.join(result_call_ref[-1]))

        # ~~~~~~~~~~~~
        # GUI updating
        # ~~~~~~~~~~~~
        update_time_in_GUI()

    update_compilation_in_psg({'use_psg_color':not False, 'show_time':False})
    while True:
        event, values = window()

        # print(values)
        if event in ('Exit', None):
            APP_CONFIGS['README_FILENAME'], APP_CONFIGS['CALL_REFERENCE_FILENAME'] = window['md1'].get(), window['md2'].get()
            save_configs(APP_CONFIGS)
            break
        
        print('PSG event>', event)

        # buttons
        if event == '-run-':              update_compilation_in_psg(values)
        if event == '-open_readme.txt-':  openfile(README_OFILENAME)
        if event == '-open_call_ref-':    openfile(CALL_REFERENCE_OFILENAME)
        if event == '-open_db_folder-':   opendir(cd)
        if event == '-open_github_gallery-':   opendir(cd)
        if event == 'open in explorer_readme':    opendir(os.path.dirname(os.path.join(cd, values['md1'])))
        if event == 'open in explorer_calref':   opendir(os.path.dirname(os.path.join(cd, values['md2'])))
        # hotkeys
        if 'F1' in event: update_compilation_in_psg(values)
        if 'F2' in event: window['show_time'](not values['show_time'])
        if 'F3' in event: window['use_psg_color'](not values['use_psg_color'])

    window.close()


if __name__ == '__main__':
    mini_GUI()
    # sg.PopupScrolled('Completed making {}'.format(README_OFILENAME), ''.join(lines), size=(80,50))