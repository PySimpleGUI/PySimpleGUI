import PySimpleGUI as sg

"""
    Demo - Save previously entered strings for Input and Combo elements by using user_settings calls

    This demo is the same as the Demo_User_Settings_Remember_Input_and_Combo.py
    The difference between the 2 files is that this one users the UserSettings class syntax while the other uses the function calls.

    Copyright 2020 PySimpleGUI.org
"""

def main():
    settings = sg.UserSettings(path='.')            # The settings file will be in the same folder as this program

    layout = [[sg.T('This is your layout')],
              [sg.T('Enter or choose name'),
               sg.Combo(values=sorted(settings.get('-names-', [])),
                        default_value=settings['-last name chosen-'],
                        size=(20,1), k='-COMBO-')],
              [sg.T('Remembers last value'), sg.In(settings.get('-input-', ''), k='-INPUT-')],
              [sg.OK(), sg.Button('Exit')]]

    event, values = sg.Window('Pattern for saving with Combobox', layout).read(close=True)

    if event == 'OK':
        settings['-names-'] = list(set(settings.get('-names-', []) + [values['-COMBO-'],]))
        settings['-last name chosen-'] =  values['-COMBO-']
        settings['-input-'] = values['-INPUT-']
        sg.popup(f"You chose {values['-COMBO-']} and input {values['-INPUT-']}",
                 'The settions dictionary:', settings)

if __name__ == '__main__':
    main()

