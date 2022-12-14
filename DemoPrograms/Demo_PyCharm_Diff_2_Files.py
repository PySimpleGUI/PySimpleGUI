import PySimpleGUI as sg
import sys
"""
    Compare 2 .py files using PyCharm's compare utility
    If you use PyCharm, then you've likely used their awesome

    Copyright 2021 PySimpleGUI
"""


def main():

    layout = [[sg.T('Choose 2 files to compare using PyCharm\'s compare utility', font='_ 18')],
                [sg.Text('Filename:'), sg.Combo(values=sorted(sg.user_settings_get_entry('-filenames1-', [])),
                        default_value=sg.user_settings_get_entry('-last filename chosen1-', None),
                        size=(90,30), auto_size_text=False, k='-COMBO1-'), sg.FileBrowse(), sg.B('Clear History', k='-CLEAR1-')],
                [sg.Text('Filename:'),sg.Combo(values=sorted(sg.user_settings_get_entry('-filenames2-', [])),
                       default_value=sg.user_settings_get_entry('-last filename chosen2-', None),
                       size=(90,30),  auto_size_text=False, k='-COMBO2-'), sg.FileBrowse(), sg.B('Clear History', k='-CLEAR2-')],
              [sg.Button('Compare'), sg.Button('Exit'), sg.T('PySimpleGUI ver ' + sg.version.split(' ')[0] + '  tkinter ver ' + sg.tclversion_detailed + 'Python ver ' + sys.version, font='Default 8', pad=(0,0))],
              [sg.Text('Note - You must setup the PyCharm information using PySimpleGUI global settings')],
              [sg.Button('Global Settings')]
                ]

    window = sg.Window('Compare 2 files using PyCharm', layout, right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_VER_EXIT)
    while True:
        event, values = window.read()
        print(event, values)
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        if event == 'Compare':
            sg.user_settings_set_entry('-filenames1-', list(set(sg.user_settings_get_entry('-filenames1-', []) + [values['-COMBO1-'],])))
            sg.user_settings_set_entry('-last filename chosen1-',  values['-COMBO1-'])
            sg.user_settings_set_entry('-filenames2-', list(set(sg.user_settings_get_entry('-filenames2-', []) + [values['-COMBO2-'],])))
            sg.user_settings_set_entry('-last filename chosen2-',  values['-COMBO2-'])
            sg.execute_command_subprocess(sg.pysimplegui_user_settings.get('-editor program-', None),  'diff', '"' +values['-COMBO1-']+'"' , '"' +values['-COMBO2-']+'"' )
            # sg.popup(f"You chose {values['-COMBO1-']} and {values['-COMBO2-']}")
        elif event == '-CLEAR1-':
            sg.user_settings_set_entry('-filenames1-', [])
            sg.user_settings_set_entry('-last filename chosen1-', '')
            window['-COMBO1-'].update(values=[], value='')
        elif event == '-CLEAR2-':
            sg.user_settings_set_entry('-filenames2-', [])
            sg.user_settings_set_entry('-last filename chosen2-', '')
            window['-COMBO2-'].update(values=[], value='')
        elif event == 'Global Settings':
            sg.main_global_pysimplegui_settings()
        if event == 'Edit Me':
            sg.execute_editor(__file__)
        elif event == 'Version':
            sg.popup_scrolled(__file__, sg.get_versions(), non_blocking=True, keep_on_top=True)
    window.close()

if __name__ == '__main__':
    main()