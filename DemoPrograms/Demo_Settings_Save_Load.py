import PySimpleGUI as sg
from json import (load as jsonload, dump as jsondump)
from os import path

"""
    A simple "settings" implementation.  Load/Edit/Save settings for your programs
    Uses json file format which makes it trivial to integrate into a Python program.  If you can
    put your data into a dictionary, you can save it as a settings file.
    
    Note that it attempts to use a lookup dictionary to convert from the settings file to keys used in 
    your settings window.  Some element's "update" methods may not work correctly for some elements.
    
    Copyright 2020 PySimpleGUI.com
    Licensed under LGPL-3
"""

SETTINGS_FILE = path.join(path.dirname(__file__), r'settings_file.cfg')
DEFAULT_SETTINGS = {'max_users': 10, 'user_data_folder': None , 'theme': sg.theme(), 'zipcode' : '94102'}
# "Map" from the settings dictionary keys to the window's element keys
SETTINGS_KEYS_TO_ELEMENT_KEYS = {'max_users': '-MAX USERS-', 'user_data_folder': '-USER FOLDER-' , 'theme': '-THEME-', 'zipcode' : '-ZIPCODE-'}

########################################## Load/Save Settings File ##########################################
def load_settings(settings_file, default_settings):
    try:
        with open(settings_file, 'r') as f:
            settings = jsonload(f)
    except Exception as e:
        sg.popup_quick_message(f'exception {e}', 'No settings file found... will create one for you', keep_on_top=True, background_color='red', text_color='white')
        settings = default_settings
        save_settings(settings_file, settings, None)
    return settings


def save_settings(settings_file, settings, values):
    if values:      # if there are stuff specified by another window, fill in those values
        for key in SETTINGS_KEYS_TO_ELEMENT_KEYS:  # update window with the values read from settings file
            try:
                settings[key] = values[SETTINGS_KEYS_TO_ELEMENT_KEYS[key]]
            except Exception as e:
                print(f'Problem updating settings from window values. Key = {key}')

    with open(settings_file, 'w') as f:
        jsondump(settings, f)

    sg.popup('Settings saved')

########################################## Make a settings window ##########################################
def create_settings_window(settings):
    sg.theme(settings['theme'])

    def TextLabel(text): return sg.Text(text+':', justification='r', size=(15,1))

    layout = [  [sg.Text('Settings', font='Any 15')],
                [TextLabel('Max Users'), sg.Input(key='-MAX USERS-')],
                [TextLabel('User Folder'),sg.Input(key='-USER FOLDER-'), sg.FolderBrowse(target='-USER FOLDER-')],
                [TextLabel('Zipcode'),sg.Input(key='-ZIPCODE-')],
                [TextLabel('Theme'),sg.Combo(sg.theme_list(), size=(20, 20), key='-THEME-')],
                [sg.Button('Save'), sg.Button('Exit')]  ]

    window = sg.Window('Settings', layout, keep_on_top=True, finalize=True)

    for key in SETTINGS_KEYS_TO_ELEMENT_KEYS:   # update window with the values read from settings file
        try:
            window[SETTINGS_KEYS_TO_ELEMENT_KEYS[key]].update(value=settings[key])
        except Exception as e:
            print(f'Problem updating PySimpleGUI window from settings. Key = {key}')

    return window

########################################## Main Program Window & Event Loop ##########################################
def create_main_window(settings):
    sg.theme(settings['theme'])

    layout = [[sg.Menu([['&File', []], ['&Edit', ['&Settings'], ],['&Help', '&About...'],])],
              [sg.T('This is my main application')],
              [sg.T('Add your primary window stuff in here')],
              [sg.B('Ok'), sg.B('Exit'), sg.B('Change Settings')]]

    return sg.Window('Main Application', layout)


def main():
    window, settings = None, load_settings(SETTINGS_FILE, DEFAULT_SETTINGS )

    while True:             # Event Loop
        if window is None:
            window = create_main_window(settings)

        event, values = window.read()

        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        if event in ('Change Settings', 'Settings'):
            event, values = create_settings_window(settings).read(close=True)
            if event == 'Save':
                window.close()
                window = None
                save_settings(SETTINGS_FILE, settings, values)
    window.close()


main()