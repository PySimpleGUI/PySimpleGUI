import PySimpleGUI as sg

"""
    Compare 2 .py files using PyCharm's compare utility
    If you use PyCharm, then you've likely used their awesome

    Copyright 2021 PySimpleGUI
"""


def main():

    layout = [[sg.T('This is your layout')],
                [sg.Text('Filename:'), sg.Combo(values=sorted(sg.user_settings_get_entry('-filenames1-', [])),
                        default_value=sg.user_settings_get_entry('-last filename chosen1-', None),
                        size=(40,1), auto_size_text=False, k='-COMBO1-'), sg.FileBrowse(), sg.B('Clear History', k='-CLEAR1-')],
                [sg.Text('Filename:'),sg.Combo(values=sorted(sg.user_settings_get_entry('-filenames2-', [])),
                       default_value=sg.user_settings_get_entry('-last filename chosen2-', None),
                       size=(40,1),  auto_size_text=False, k='-COMBO2-'), sg.FileBrowse(), sg.B('Clear History', k='-CLEAR2-')],
              [sg.Button('Compare'), sg.Button('Exit')]]

    window = sg.Window('Compare 2 files using PyCharm', layout)
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
            sg.execute_command_subprocess(sg.pysimplegui_user_settings.get('-editor program-', None),  'diff',values['-COMBO1-'], values['-COMBO2-'])
            # sg.popup(f"You chose {values['-COMBO1-']} and {values['-COMBO2-']}")
        elif event == '-CLEAR1-':
            sg.user_settings_set_entry('-filenames1-', [])
            sg.user_settings_set_entry('-last filename chosen1-', '')
            window['-COMBO1-'].update(values=[], value='')
        elif event == '-CLEAR2-':
            sg.user_settings_set_entry('-filenames2-', [])
            sg.user_settings_set_entry('-last filename chosen2-', '')
            window['-COMBO2-'].update(values=[], value='')
    window.close()

if __name__ == '__main__':
    main()