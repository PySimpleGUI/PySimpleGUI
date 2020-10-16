import PySimpleGUI as sg

"""
    Demo - Save previously entered strings as a Combobox entry by using user_settings calls

    It's literally 1 parameter in the layout to get the list of previously used entries shown.
    Then, when the OK button is clicked, it's 4 more lines of code to save the newly added
    name into the saved list.

    Copyright 2020 PySimpleGUI.org
"""

def main():

    layout = [[sg.T('This is your layout')],
              [sg.T('Enter or choose name'), sg.Combo(sorted(sg.user_settings_get_entry('names', [])), size=(20,1), k='-COMBO-')],
              [sg.OK(), sg.Button('Exit')]]

    event, values = sg.Window('Pattern for saving with Combobox', layout).read(close=True)

    if event == 'OK':
        sg.user_settings_set_entry('names', list(set(sg.user_settings_get_entry('names', []) + [values['-COMBO-'],])))
        print(f"You chose {values['-COMBO-']}")

if __name__ == '__main__':
    main()

