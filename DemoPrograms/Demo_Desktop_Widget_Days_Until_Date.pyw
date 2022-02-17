import PySimpleGUI as sg
import sys
import datetime

"""
    Another simple Desktop Widget using PySimpleGUI
    The "Days UNTIL _______" Desktop Widget (Like Rainmeter)

    This widget counts the number of days UNTIL some date of your choosing.  
    Maybe you want to track the number of days until an anniversary?
    
    Unlike other demos, this one is being released as a .pyw file.  If launched on Windows, open with Pythonw.exe so 
        that you don't get a console Window.  That's how these desktop widgets are supposed to be launched, with no
        console.  I usually launch them from another Python program that starts them all at once using the Exec APIs
        built into PySimpleGUI.

    Copyright 2021 PySimpleGUI Project
"""

ALPHA = 0.9  # Initial alpha until user changes
THEME = 'Dark green 3'  # Initial theme until user changes
sg.user_settings_filename(filename='DaysUntil.json')
refresh_font = sg.user_settings_get_entry('-refresh font-', 'Courier 8')
title_font = sg.user_settings_get_entry('-title font-', 'Courier 8')
main_number_font = sg.user_settings_get_entry('-main number font-', 'Courier 70')
main_info_size = (None, 1)
# May add ability to change theme from the user interface.  For now forcing to constant

UPDATE_FREQUENCY_MILLISECONDS = 1000 * 60 * 60  # update every hour


def choose_theme(location):
    layout = [[sg.Text(f'Current theme {sg.theme()}')],
              [sg.Listbox(values=sg.theme_list(), size=(20, 20), key='-LIST-', enable_events=True)],
              [sg.OK(), sg.Cancel()]]

    window = sg.Window('Look and Feel Browser', layout, location=location, keep_on_top=True)
    old_theme = sg.theme()
    while True:  # Event Loop
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit', 'OK', 'Cancel'):
            break
        sg.theme(values['-LIST-'][0])
        test_window = make_window(location=(location[0] - 200, location[1]), test_window=True)
        test_window.read(close=True)
    window.close()

    if event == 'OK' and values['-LIST-']:
        sg.theme(values['-LIST-'][0])
        sg.user_settings_set_entry('-theme-', values['-LIST-'][0])
        return values['-LIST-'][0]
    else:
        sg.theme(old_theme)
    return None


def make_window(location, test_window=False):
    title_font = sg.user_settings_get_entry('-title font-', 'Courier 8')
    title = sg.user_settings_get_entry('-title-', '')
    main_number_font = sg.user_settings_get_entry('-main number font-', 'Courier 70')

    if not test_window:
        theme = sg.user_settings_get_entry('-theme-', THEME)
        sg.theme(theme)

    alpha = sg.user_settings_get_entry('-alpha-', ALPHA)

    # ------------------- Window Layout -------------------
    # If this is a test window (for choosing theme), then uses some extra Text Elements to display theme info
    # and also enables events for the elements to make the window easy to close
    if test_window:
        top_elements = [[sg.Text(title, font=title_font, justification='c', k='-TITLE-', enable_events=True)],
                        [sg.Text('Click to close', font=title_font, enable_events=True)],
                        [sg.Text('This is theme', font=title_font, enable_events=True)],
                        [sg.Text(sg.theme(), font=title_font, enable_events=True)]]
        right_click_menu = [[''], ['Exit', ]]
    else:
        top_elements = [[sg.Text(title, size=(20, 1), font=title_font, justification='c', k='-TITLE-')]]
        right_click_menu = [[''],
                            ['Choose Date', 'Choose Title', '---', 'Set Title Font', 'Set Main Font',  'Edit Me', 'Change Theme', '---', 'Refresh', 'Show Refresh Info', 'Hide Refresh Info', '---', 'Alpha', [str(x) for x in range(1, 11)], '---', 'Show Debug Info', 'Route Print To Screen', 'Stop print to screen', 'Exit', ]]

    layout = top_elements + \
             [[sg.pin(sg.Text('0', size=main_info_size, font=main_number_font, k='-MAIN INFO NUM-', justification='c', enable_events=test_window, pad=(0, 0)))],
              [sg.pin(sg.Text(size=(15, None), font=refresh_font, k='-REFRESHED-', justification='c', visible=sg.user_settings_get_entry('-show refresh-', False)))]]

    try:
        window = sg.Window('Day Number', layout, location=location, no_titlebar=True, grab_anywhere=True, margins=(0, 0), element_justification='c',
                           element_padding=(0, 0), alpha_channel=alpha, finalize=True, right_click_menu=right_click_menu, right_click_menu_tearoff=False,
                           keep_on_top=True, enable_close_attempted_event=True)
    except Exception as e:
        if sg.popup_yes_no('Error creating your window', e, 'These are your current settings:', sg.user_settings(),
                           'Do you want to delete your settings file?') == 'Yes':
            sg.user_settings_delete_filename()
            sg.popup('Settings deleted.', 'Please restart your program')
            exit()
        window = None

    return window


def main(location):
    if sg.user_settings_get_entry('-end date-', None) is None:
        sg.popup('You have no yet set up an end date - set an end date to begin.',
                 'When you close this Window you will be shown a calendar to choose an ending date.')
        new_end = sg.popup_get_date( keep_on_top=True)
        if new_end is not None:
            sg.user_settings_set_entry('-end date-', new_end)
        else:
            sg.popup_error('You have to set an end date to use this program. Try again later when you are ready to begin for real....')
            exit()
    loc = sg.user_settings_get_entry('-location-', location)
    if sg.user_settings_get_entry('-print to debug-', False) is True:
        mprint = sg.Print
    else:
        mprint = print
    window = make_window(loc)

    saved_date = sg.user_settings_get_entry('-end date-', (1, 1, 2021))
    end_date = datetime.datetime(saved_date[2], saved_date[0], saved_date[1])

    while True:  # Event Loop
        # First update the status information
        delta = end_date - datetime.datetime.now()
        title_data = delta.days + 1
        msg_num = f'{title_data}'
        window['-MAIN INFO NUM-'].update(msg_num)
        # for debugging show the last update date time
        window['-REFRESHED-'].update(datetime.datetime.now().strftime("%m/%d/%Y\n%I:%M:%S %p") + \
                                     f'\nEnd date '+ end_date.strftime("%m/%d/%Y"))
        # -------------- Start of normal event loop --------------
        event, values = window.read(timeout=UPDATE_FREQUENCY_MILLISECONDS)
        mprint(event, values)
        if event == sg.WIN_CLOSE_ATTEMPTED_EVENT or event == 'Exit':
            sg.user_settings_set_entry('-location-', window.current_location())  # The line of code to save the position before exiting
            break
        if event == 'Edit Me':
            sg.execute_editor(__file__)
        elif event == 'Choose Date':
            new_end = sg.popup_get_date(location=window.current_location(), keep_on_top=True)
            if new_end is not None:
                end_date = datetime.datetime(new_end[2], new_end[0], new_end[1])
                sg.user_settings_set_entry('-end date-', new_end)
        elif event == 'Choose Title':
            new_title = sg.popup_get_text('Choose a title for your date',  default_text=sg.user_settings_get_entry('-title-', ''), location=window.current_location(), keep_on_top=True)
            if new_title is not None:
                window['-TITLE-'].update(new_title)
                sg.user_settings_set_entry('-title-', new_title)
        elif event == 'Show Refresh Info':
            window['-REFRESHED-'].update(visible=True)
            sg.user_settings_set_entry('-show refresh-', True)
        elif event == 'Hide Refresh Info':
            window['-REFRESHED-'].update(visible=False)
            sg.user_settings_set_entry('-show refresh-', False)
        elif event in [str(x) for x in range(1, 11)]:
            window.set_alpha(int(event) / 10)
            sg.user_settings_set_entry('-alpha-', int(event) / 10)
        elif event == 'Change Theme':
            loc = window.current_location()
            if choose_theme(loc) is not None:
                # this is result of hacking code down to 99 lines in total. Not tried it before. Interesting test.
                _, window = window.close(), make_window(loc)
        elif event == 'Set Main Font':
            font = sg.popup_get_text('Main Information Font and Size (e.g. courier 70)', default_text=sg.user_settings_get_entry('-main number font-'), keep_on_top=True, location=window.current_location())
            if font:
                sg.user_settings_set_entry('-main number font-', font)
                _, window = window.close(), make_window(loc)
        elif event == 'Set Title Font':
            font = sg.popup_get_text('Title Font and Size (e.g. courier 8)', default_text=sg.user_settings_get_entry('-title font-'), keep_on_top=True, location=window.current_location())
            if font:
                sg.user_settings_set_entry('-title font-', font)
                _, window = window.close(), make_window(loc)
        elif event == 'Show Debug Info':
            mprint(sg.get_versions())
        elif event == 'Route Print To Screen':
            mprint = sg.Print
        elif event == 'Stop print to screen':
            mprint = print

    window.close()


if __name__ == '__main__':
    # To start the window at a specific location, get this location on the command line
    # The location should be in form x,y with no spaces
    if len(sys.argv) > 1:
        location = sys.argv[1].split(',')
        location = (int(location[0]), int(location[1]))
    else:
        location = (None, None)
    main(location)