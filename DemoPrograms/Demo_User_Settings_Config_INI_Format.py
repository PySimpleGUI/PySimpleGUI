import PySimpleGUI as sg

"""
    Demo - User Settings - Config.ini format
    
    There are now 2 types of settings files available through the UserSettings APIs
        1. JSON - .json files
        2. INI - Config.ini files

    The default is JSON files.
    
    If you wish to use .ini files, then you can do so using the UserSettings object.  The function interface
    for the UserSettings API does not support .ini files, only the object interface at this time.  You'll see
    why by looking at this demo.
    
    JSON settings:
        settings['key']
        
    CONFIG.INI settings:
        settings['section']['key']
    
    NOTE - There is a setting (default is ON) that converts True", "False, "None" into Python values of True, False, None
     
    Copyright 2021 PySimpleGUI
"""


def show_settings_file(filename):
    """
    Display the contents of any .INI file you wish to display
    :param filename: full path and filename
    """
    settings_obj = sg.UserSettings(filename, use_config_file=True)
    sg.popup_scrolled(settings_obj, title=f'INI File: {filename}')


def save_previous_filename_demo():
    """
    Saving the previously selected filename....
    A demo of one of the likely most popular use of user settings
    * Use previous input as default for Input
    * When a new filename is chosen, write the filename to user settings
    """

    layout = [[sg.Text('The filename value below will be auto-filled with previously saved entry')],
              [sg.T('The format for this entry is:')],
              [sg.T('settings["My Section"]["filename"]', background_color=sg.theme_text_color(), text_color=sg.theme_background_color())],
              [sg.Input(settings['My Section'].get('filename', ''), key='-IN-'), sg.FileBrowse()],
              [sg.B('Save')],
              [sg.B('Display Settings'), sg.B('Display Section'), sg.B('Display filename setting')],
              [sg.B('Dump an INI File')],
               [sg.B('Exit Without Saving', key='Exit')]]

    window = sg.Window('Filename Example', layout)

    while True:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, 'Exit'):
            break
        elif event == 'Save':
            settings['My Section']['filename'] = values['-IN-']
        elif event == 'Display Settings':
            sg.popup_scrolled(settings, title='All settings')
        elif event == 'Display Section':
            sect = settings['My Section']
            sg.popup_scrolled(sect, title='Section Contents')
        elif event == 'Display filename setting':
            sg.popup_scrolled(f'filename = {settings["My Section"]["filename"]}', title='Filename Setting')
        elif event.startswith('Dump'):
            filename = sg.popup_get_file('What INI file would you like to display?', file_types= (("INI Files", "*.ini"),))
            if filename:
                show_settings_file(filename)

    window.close()


if __name__ == '__main__':
    sg.theme('dark green 7')
    SETTINGS_PATH = '.'
    # create the settings object and use ini format
    settings = sg.UserSettings(path=SETTINGS_PATH, use_config_file=True, convert_bools_and_none=True)
    # sg.popup(settings)
    # settings['My Section1'].delete_entry(key='test')
    # settings.delete_entry(section='My Section1', key='test')
    # settings['My Section1'].delete_section()
    # del settings['My Section1']
    # settings.delete_section(section='My Section1')
    settings['Section 2'].set('var1', 'Default')
    settings['Section 2']['var'] = 'New Value'
    settings['NEW SECTION']['a'] = 'brand new section'
    save_previous_filename_demo()
