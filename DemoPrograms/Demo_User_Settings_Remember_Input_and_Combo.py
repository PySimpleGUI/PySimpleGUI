import PySimpleGUI as sg

"""
    Demo - Save previously entered strings for Input and Combo elements by using user_settings calls

    It's literally 1 parameter in the layout to get the list of previously used entries shown.
    Then, when the OK button is clicked, it's one line of code to save the newly added
    name into the saved list.

    Copyright 2020-2023 PySimpleSoft, Inc. and/or its licensors. All rights reserved.
    
    Redistribution, modification, or any other use of PySimpleGUI or any portion thereof is subject to the terms of the PySimpleGUI License Agreement available at https://eula.pysimplegui.com.
    
    You may not redistribute, modify or otherwise use PySimpleGUI or its contents except pursuant to the PySimpleGUI License Agreement.
"""

def main():
    sg.user_settings_filename(path='.')         # The settings file will be in the same folder as this program

    layout = [[sg.T('This is your layout')],
              [sg.T('Enter or choose name'),
               sg.Combo(values=sorted(sg.user_settings_get_entry('-names-', [])),
                        default_value=sg.user_settings_get_entry('-last name chosen-', None),
                        size=(20,1), k='-COMBO-')],
              [sg.T('Remembers last value'), sg.In(sg.user_settings_get_entry('-input-', ''), k='-INPUT-')],
              [sg.OK(), sg.Button('Exit')]]

    event, values = sg.Window('Pattern for saving with Combobox', layout).read(close=True)

    if event == 'OK':
        sg.user_settings_set_entry('-names-', list(set(sg.user_settings_get_entry('-names-', []) + [values['-COMBO-'],])))
        sg.user_settings_set_entry('-last name chosen-',  values['-COMBO-'])
        sg.user_settings_set_entry('-input-', values['-INPUT-'])
        sg.popup(f"You chose {values['-COMBO-']} and input {values['-INPUT-']}",
                 'The settions dictionary:', sg.user_settings())


if __name__ == '__main__':
    main()

