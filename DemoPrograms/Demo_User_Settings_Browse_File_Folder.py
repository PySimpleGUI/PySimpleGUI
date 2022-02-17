import PySimpleGUI as sg

"""
    Demo of a Better File / Folder Input Window

    This construct is very common in PySimpleGUI.
        [sg.InputText(size=(50,1), key='-FILENAME-'), sg.FileBrowse()],

    The new user settings APIs can significantly improve the experience.  Now instead of being
    shown a blank input element, the user is shown their previous entry and a history of their
    prior entries to choose from.

    Two new capabilities are presented in this demo
    1. Recalling the last entry
    2. Recalling a history of all of the previous entries as a Combo instead of Input Element

    The previous operations you're used to remain.  You can paste a filename/full path into the combo.
    You can also use the browse button as before.

    But, you also get the 2 history features - last entry used, list of previous choices.

    If your window is not a 1-shot, add an event loop instead of a read with close paramter

    Copyright 2020 PySimpleGUI.org
"""

# ------------------- The Old Way -------------------
import PySimpleGUI as sg

layout = [[sg.Text('My Window')],
          [sg.InputText(size=(50, 1), key='-FILENAME-'), sg.FileBrowse()],
          [sg.Button('Go'), sg.Button('Exit')]]

event1, values1 = sg.Window('Normal Filename', layout).read(close=True)

# ------------------- The New Way with history -------------------
import PySimpleGUI as sg

layout = [[sg.Text('My Window')],
          [sg.Combo(sg.user_settings_get_entry('-filenames-', []), default_value=sg.user_settings_get_entry('-last filename-', ''), size=(50, 1), key='-FILENAME-'),
           sg.FileBrowse()],
          [sg.Button('Go'), sg.Button('Exit')]]

event, values = sg.Window('Filename with History', layout).read(close=True)

if event == 'Go':
    sg.user_settings_set_entry('-filenames-', list(set(sg.user_settings_get_entry('-filenames-', []) + [values['-FILENAME-'], ])))
    sg.user_settings_set_entry('-last filename-', values['-FILENAME-'])


# ------------------- The New Way with history and clear -------------------
import PySimpleGUI as sg

layout = [[sg.Text('My Window')],
          [sg.Combo(sg.user_settings_get_entry('-filenames-', []), default_value=sg.user_settings_get_entry('-last filename-', ''), size=(50, 1), key='-FILENAME-'),
           sg.FileBrowse()],
          [sg.Button('Go'), sg.B('Clear'), sg.Button('Exit')]]

window = sg.Window('Filename History Clearable', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Go':
        sg.user_settings_set_entry('-filenames-', list(set(sg.user_settings_get_entry('-filenames-', []) + [values['-FILENAME-'], ])))
        sg.user_settings_set_entry('-last filename-', values['-FILENAME-'])
        window['-FILENAME-'].update(values=list(set(sg.user_settings_get_entry('-filenames-', []))))
    elif event == 'Clear':
        sg.user_settings_set_entry('-filenames-', [])
        sg.user_settings_set_entry('-last filename-', '')
        window['-FILENAME-'].update(values=[], value='')
