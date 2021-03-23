import PySimpleGUI as sg
import sys
import datetime

"""
    Desktop Widget - Template to start with
    This "template" is meant to give you a starting point towards making your own Desktop Widget
    Note - the term "Widget" here means a "Desktop Widget", not a GUI Widget
    
    It has many of the features that a Rainmeter-style Desktop Widget would have
        * Save position of window
        * Set Alpha channel
        * "Edit Me" which will launch your editor to edit the code
        * Right click menu to access all setup
        * Theme selection
        * Preview of window using a different theme
        * A command line parm to set the intial position of the window in case one hasn't been saved
        * A status section of the window that can be hidden / restored (currently shows last refresh time)
        * A title
        * A main display area
        
    The contents of your widget may be significantly different than this example.  Change the function
        make_window to create your own custom layout and window.
        
    There are several important design patterns provided including:
        Using a function to define and create your window
        Using User Settings APIs to save program settings
        A Theme Selection window with previewing capability
        
    The standard PySimpleGUI Coding Conventions are used throughout including
        * Naming layout keys in format '-KEY-'
        * Naming User Settings keys in the format '-key-'
        * Using standard layout, window, event, values variable names
        
    Copyright 2021 PySimpleGUI
"""

ALPHA = 0.9  # Initial alpha until user changes
THEME = 'Dark green 3'  # Initial theme until user changes
refresh_font = title_font = 'Courier 8'
main_info_font ='Courier 20'
main_info_size = (10,1)
UPDATE_FREQUENCY_MILLISECONDS = 1000 * 60 * 60  # update every hour by default until set by user

def choose_theme(location, size):
    """
    A window to allow new themes to be tried out.
    Changes the theme to the newly chosen one and returns theme's name
    Automaticallyi switches to new theme and saves the setting in user settings file

    :param location: (x,y) location of the Widget's window
    :type location:  Tuple[int, int]
    :param size: Size in pixels of the Widget's window
    :type size: Tuple[int, int]
    :return: The name of the newly selected theme
    :rtype: None | str
    """
    layout = [[sg.Text('Try a theme')],
              [sg.Listbox(values=sg.theme_list(), size=(20, 20), key='-LIST-', enable_events=True)],
              [sg.OK(), sg.Cancel()]]

    window = sg.Window('Look and Feel Browser', layout, location=location, keep_on_top=True)
    old_theme = sg.theme()
    while True:  # Event Loop
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit', 'OK', 'Cancel'):
            break
        sg.theme(values['-LIST-'][0])
        window.hide()
        # make at test window to the left of the current one
        test_window = make_window(location=((location[0]-size[0]*1.2, location[1])), test_window=True)
        test_window.read(close=True)
        window.un_hide()
    window.close()

    # after choice made, save theme or restore the old one
    if event == 'OK' and values['-LIST-']:
        sg.theme(values['-LIST-'][0])
        sg.user_settings_set_entry('-theme-', values['-LIST-'][0])
        return values['-LIST-'][0]
    else:
        sg.theme(old_theme)
    return None

def make_window(location, test_window=False):
    """
    Defines the layout and creates the window for the main window
    If the parm test_window is True, then a simplified, and EASY to close version is shown

    :param location: (x,y) location to create the window
    :type location: Tuple[int, int]
    :param test_window: If True, then this is a test window & will close by clicking on it
    :type test_window: bool
    :return: newly created window
    :rtype: sg.Window
    """
    title = sg.user_settings_get_entry('-title-', '')
    if not test_window:
        theme = sg.user_settings_get_entry('-theme-', THEME)
        sg.theme(theme)

    # ------------------- Window Layout -------------------
    # If this is a test window (for choosing theme), then uses some extra Text Elements to display theme info
    # and also enables events for the elements to make the window easy to close
    if test_window:
        top_elements = [[sg.Text(title, size=(20, 1), font=title_font, justification='c', k='-TITLE-', enable_events=True)],
                        [sg.Text('Click to close', font=title_font, enable_events=True)],
                        [sg.Text('This is theme', font=title_font, enable_events=True)],
                        [sg.Text(sg.theme(), font=title_font, enable_events=True)]]
        right_click_menu = [[''], ['Exit',]]
    else:
        top_elements = [[sg.Text(title, size=(20, 1), font=title_font, justification='c', k='-TITLE-')]]
        right_click_menu = [[''], ['Choose Title', 'Edit Me', 'New Theme', 'Save Location', 'Refresh', 'Set Refresh Rate', 'Show Refresh Info', 'Hide Refresh Info', 'Alpha', [str(x) for x in range(1, 11)], 'Exit', ]]

    layout = top_elements + \
              [[sg.Text('0', size=main_info_size, font=main_info_font, k='-MAIN INFO-', justification='c', enable_events=test_window)],
              [sg.pin(sg.Text(size=(15, 2), font=refresh_font, k='-REFRESHED-', justification='c', visible=sg.user_settings_get_entry('-show refresh-', True)))]]

    # ------------------- Window Creation -------------------
    return sg.Window('Desktop Widget Template', layout, location=location, no_titlebar=True, grab_anywhere=True, margins=(0, 0), element_justification='c',
                       element_padding=(0, 0), alpha_channel=sg.user_settings_get_entry('-alpha-', ALPHA), finalize=True, right_click_menu=right_click_menu, keep_on_top=True)


def main(location):
    """
    Where execution begins
    The Event Loop lives here, but the window creation is done in another function
    This is an important design pattern

    :param location: Location to create the main window if one is not found in the user settings
    :type location: Tuple[int, int]
    """

    window = make_window(sg.user_settings_get_entry('-location-', location))

    refresh_frequency = sg.user_settings_get_entry('-fresh frequency-', UPDATE_FREQUENCY_MILLISECONDS)

    while True:  # Event Loop
        # Normally a window.read goes here, but first we're updating the values in the window, then reading it
        # First update the status information
        window['-MAIN INFO-'].update('Your Info')
        # for debugging show the last update date time
        window['-REFRESHED-'].update(datetime.datetime.now().strftime("%m/%d/%Y\n%I:%M:%S %p"))

        # -------------- Start of normal event loop --------------
        event, values = window.read(timeout=refresh_frequency)
        print(event, values)
        if event in (sg.WIN_CLOSED, 'Exit'):   # standard exit test... ALWAYS do this
            break
        if event == 'Edit Me':
            sg.execute_editor(__file__)
        elif event == 'Choose Title':
            new_title = sg.popup_get_text('Choose a title for your Widget', location=window.current_location(), keep_on_top=True)
            if new_title is not None:
                window['-TITLE-'].update(new_title)
                sg.user_settings_set_entry('-title-', new_title)
        elif event == 'Show Refresh Info':
            window['-REFRESHED-'].update(visible=True)
            sg.user_settings_set_entry('-show refresh-', True)
        elif event == 'Save Location':
            sg.user_settings_set_entry('-location-', window.current_location())
        elif event == 'Hide Refresh Info':
            window['-REFRESHED-'].update(visible=False)
            sg.user_settings_set_entry('-show refresh-', False)
        elif event in [str(x) for x in range(1, 11)]:       # if Alpha Channel was chosen
            window.set_alpha(int(event) / 10)
            sg.user_settings_set_entry('-alpha-', int(event) / 10)
        elif event == 'Set Refresh Rate':
            choice = sg.popup_get_text('How frequently to update window in seconds? (can be a float)', default_text=sg.user_settings_get_entry('-fresh frequency-', UPDATE_FREQUENCY_MILLISECONDS)/1000, location=window.current_location(), keep_on_top=True)
            if choice is not None:
                try:
                    refresh_frequency = float(choice)*1000    # convert to milliseconds
                    sg.user_settings_set_entry('-fresh frequency-', float(refresh_frequency))
                except Exception as e:
                    sg.popup_error(f'You entered an incorrect number of seconds: {choice}', f'Error: {e}', location=window.current_location(), keep_on_top=True)
        elif event == 'New Theme':
            loc = window.current_location()
            if choose_theme(window.current_location(), window.size) is not None:
                window.close()              # out with the old...
                window = make_window(loc)   # in with the new

    window.close()


if __name__ == '__main__':
    # To start the window at a specific location, get this location on the command line
    # The location should be in form x,y with no spaces
    location = (None, None) # assume no location provided
    if len(sys.argv) > 1:
        location = sys.argv[1].split(',')
        location = (int(location[0]), int(location[1]))
    main(location)