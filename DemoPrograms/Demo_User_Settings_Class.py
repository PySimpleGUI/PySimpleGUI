import PySimpleGUI as sg

"""
    Demo - User Settings Using Class

    There are 2 interfaces for the User Settings APIs in PySimpleGUI. 
    1. Function calls
    2. The UserSettings class
    
    This demo focuses on using the class interface.  The advantage of using the class is that 
    lookups resemble the syntax used for Python dictionaries

    This demo is very basic. The user_settings functions are used directly without a lookup table
    or some other mechanism to map between PySimpleGUI keys and user settings keys. 

    Note that there are 2 coding conventions being used.  The PySimpleGUI Demo Programs all use
    keys on the elements that are strings with the format '-KEY-'.  They are upper case.  The
    coding convention being used in Demo Programs that use User Settings use keys that have
    the same format, but are lower case.  A User Settings key is '-key-'.  The reason for this
    convention is so that you will immediately know what the string you are looking at is.
    By following this convention, someone reading the code that encounters '-filename-' will
    immediately recognize that this is a User Setting.  

    Two windows are shown.  One is a super-simple "save previously entered filename"
    The other is a larger "settings window" where multiple settings are saved/loaded

    Copyright 2020 PySimpleGUI.org
"""

SETTINGS_PATH = '.'

# create the settings object that will be used globally, but not need to change so not declared as global
settings = sg.UserSettings(path=SETTINGS_PATH)

def make_window():
    """
    Creates a new window.  The default values for some elements are pulled directly from the
    "User Settings" without the use of temp variables.

    Some get_entry calls don't have a default value, such as theme, because there was an initial call
    that would have set the default value if the setting wasn't present.  Could still put the default
    value if you wanted but it would be 2 places to change if you wanted a different default value.

    Use of a lookup table to map between element keys and user settings could be aded. This demo
    is intentionally done without one to show how to use the settings APIs in the most basic,
    straightforward way.

    If your application allows changing the theme, then a make_window function is good to have
    so that you can close and re-create a window easily.

    :return: (sg.Window)  The window that was created
    """

    sg.theme(settings.get('-theme-', 'DarkBlue2'))  # set the theme

    layout = [[sg.Text('Settings Window')],
              [sg.Input(settings.get('-input-', ''), k='-IN-')],
              [sg.Listbox(sg.theme_list(), default_values=[settings['-theme-'],], size=(15, 10), k='-LISTBOX-')],
              [sg.CB('Option 1', settings.get('-option1-', True), k='-CB1-')],
              [sg.CB('Option 2', settings.get('-option2-', False), k='-CB2-')],
              [sg.T('Settings file = ' + settings.get_filename())],
              [sg.Button('Save'), sg.Button('Settings Dictionary'), sg.Button('Exit without saving', k='Exit')]]

    window =  sg.Window('A Settings Window', layout)


def settings_window():
    """
    Create and interact with a "settings window". You can a similar pair of functions to your
    code to add a "settings" feature.
    """

    window = make_window()
    current_theme = sg.theme()

    while True:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, 'Exit'):
            break
        if event == 'Save':
            # Save some of the values as user settings
            settings['-input-'] = values['-IN-']
            settings['-theme-'] = values['-LISTBOX-'][0]
            settings['-option1-'] = values['-CB1-']
            settings['-option2-'] = values['-CB2-']
        elif event == 'Settings Dictionary':
            sg.popup(settings)
        # if a listbox item is selected and if the theme was changed, then restart the window
        if values['-LISTBOX-'] and values['-LISTBOX-'][0] != current_theme:
            current_theme = values['-LISTBOX-'][0]
            window.close()
            window = make_window()


def save_previous_filename_demo():
    """
    Saving the previously selected filename....
    A demo of one of the likely most popular use of user settings
    * Use previous input as default for Input
    * When a new filename is chosen, write the filename to user settings
    """

    # Notice that the Input element has a default value given (first parameter) that is read from the user settings
    layout = [[sg.Text('Enter a filename:')],
              [sg.Input(settings.get('-filename-', ''), key='-IN-'), sg.FileBrowse()],
              [sg.B('Save'), sg.B('Exit Without Saving', key='Exit')]]

    window = sg.Window('Filename Example', layout)

    while True:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, 'Exit'):
            break
        elif event == 'Save':
            settings['-filename-'] = values['-IN-']

    window.close()


if __name__ == '__main__':
    # Run a couple of demo windows
    save_previous_filename_demo()
    settings_window()
