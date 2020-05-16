import datetime,time,os
cd = CD = os.path.dirname(os.path.abspath(__file__))

from make_real_readme import main
def readfile(filename):
    with open(filename, 'r', encoding='utf-8') as ff: return ff.read()
def writefile(fpath, content):
    with open(fpath, 'w', encoding='utf-8') as ff: ff.write(content)
import json
def writejson(a_path:str, a_dict:dict) -> None:
    with open(a_path, 'w', encoding='utf-8') as output_file:
        json.dump(a_dict, output_file, ensure_ascii=False, indent=2)
def readjson(a_path:str) -> dict:
    with open(a_path, 'r', encoding='utf-8') as f: return json.load(f)

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
OUTPUT_FILENAME = 'readme.md'

##-#-#-# ##-#-#-#
# Pre-process logic
##-#-#-# ##-#-#-#

line_break = '<br>'
# line_break can be:
# - '<br>'
# - ' \n '

method = 'with logs'
# method can be:
# - 'simple, no log'
# - 'with logs'


##-#-#-# ##-#-#-#
# Post-process logic
##-#-#-# ##-#-#-#
enable_popup = True
insert_md_section_for__class_methods = False
remove_repeated_sections_classmethods = False



##############
#     __     #
#    /_ |    #
#     | |    #
#     | |    #
#     | |    #
#     |_|    #
##############
if method == 'simple, no log':
    main(logger=None,
         insert_md_section_for__class_methods=insert_md_section_for__class_methods,
         remove_repeated_sections_classmethods=remove_repeated_sections_classmethods,
         files_to_include=[0, 1, 2, 3],
         output_name=OUTPUT_FILENAME,
         delete_html_comments=True)

################
#     ___      #
#    |__ \     #
#       ) |    #
#      / /     #
#     / /_     #
#    |____|    #
################
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

def compile_all_stuff(**kw):
    # import logging

    log_file = os.path.join(cd, 'LoG')
    log_obj = BESTLOG(log_file)
    main(logger=log_obj,
         insert_md_section_for__class_methods=insert_md_section_for__class_methods,
         remove_repeated_sections_classmethods=remove_repeated_sections_classmethods,
         files_to_include=[0, 1, 2, 3],
         output_name=OUTPUT_FILENAME,
         delete_html_comments=True)
    log_obj.save()

    # cd = CD = os.path.dirname(os.path.abspath(__file__))
    # log_file = os.path.join(cd, 'usage.log.txt')
    return log_obj.load(**kw)

# if method == 'with logs': compile_all_stuff()

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
def mini_GUI():
    my_font = ("Helvetica", 12)
    my_font2 = ("Helvetica", 12, "bold")
    my_font3 = ("Helvetica", 15, "bold")


    layout = [
       [
           sg.Column(layout=[
                [sg.T('debug', font=my_font, text_color='blue')],
                [sg.ML(size=(70-15,20), key='debug')],
                [sg.T('error', font=my_font, text_color='red')],
                [sg.ML(size=(70-15,20), key='error')],
            ])
           ,sg.T('            ')
           ,sg.Column(layout=[
                [sg.T('warning', font=my_font2)],
                [sg.ML(size=(70-12,20), key='warning')],
                [sg.T('info', font=my_font2)],
                [sg.ML(size=(70-12,20), key='info')],
            ]),
           sg.Column(layout=[
                [sg.T('warning_info', font=my_font3)],
                [sg.ML(size=(110,42), key='warning_info')],
            ]),
           
        ]
    ]
    window = sg.Window('We are live! Again! --- ' + 'Completed making {}'.format(OUTPUT_FILENAME), [
        [sg.T(size=(25,1), font=my_font, key='-compile-time-')]
        ,[  
            sg.B('Run again (F1)', key='-run-')
            ,sg.CB('show time in logs (F2)', False, key='show_time')
            ,sg.CB('Logs with Color (F3)', True, key='use_psg_color')
        ]
        ,*layout
    ], resizable=True, finalize=True, location=(0,0), return_keyboard_events = True)

    def update_compilation_in_psg(values):
        # get results
        results = compile_all_stuff(use_psg_color=values['use_psg_color'], show_time=values['show_time'])

        # UPDATE GUI
        curr_time = lambda : datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S.%f')
        window['-compile-time-'](curr_time())
        for key, txt in zip('error warning info debug'.split(' '), results[:4]):
            window[key]('\n'.join(txt))
        # colors warning_info
        window['warning_info'].update('')
        if values['use_psg_color']:
            for text, color in results[-1]:
                window['warning_info'].print(text, text_color=color)
        else:
            window['warning_info']('\n'.join(results[-1]))

    update_compilation_in_psg({'use_psg_color':not False, 'show_time':False})
    while True:
        event, values = window()
        if event in ('Exit', None): break

        # print(event)
        if event == '-run-' or 'F1' in event: update_compilation_in_psg(values)
        if 'F2' in event: window['show_time'](not values['show_time'])
        if 'F3' in event: window['use_psg_color'](not values['use_psg_color'])

    window.close()


if enable_popup:
    import PySimpleGUI as sg

    mini_GUI()
    # sg.PopupScrolled('Completed making {}'.format(OUTPUT_FILENAME), ''.join(lines), size=(80,50))