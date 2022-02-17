import PySimpleGUI as sg
import winsound

"""
    Another simple Desktop Widget using PySimpleGUI
    This one is a manual counter.  Click +/- to add and subtract to the counter
    Dedicated to @SuperScienceGirl for having the original analog clicker that spawned this digital one.
    
    Copyright 2021 PySimpleGUI
"""

ALPHA = 0.9  # Initial alpha until user changes
THEME = 'Dark green 3'  # Initial theme until user changes
title_font = sg.user_settings_get_entry('-title font-', 'Courier 8')
main_number_font = sg.user_settings_get_entry('-main number font-', 'Courier 70')
main_info_size = (None, None)
# May add ability to change theme from the user interface.  For now forcing to constant

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
    button_font = sg.user_settings_get_entry('-button font-', 'Courier 20')
    sg.user_settings_set_entry('-button font-', button_font)
    title = sg.user_settings_get_entry('-title-', '')
    main_number_font = sg.user_settings_get_entry('-main number font-', 'Courier 70')
    sg.user_settings_set_entry('-main number font-', main_number_font)

    if not test_window:
        theme = sg.user_settings_get_entry('-theme-', THEME)
        sg.theme(theme)

    alpha = sg.user_settings_get_entry('-alpha-', ALPHA)

    # ------------------- Window Layout -------------------
    # If this is a test window (for choosing theme), then uses some extra Text Elements to display theme info
    # and also enables events for the elements to make the window easy to close
    if test_window:
        top_elements = [[sg.Text(title, font=title_font,  k='-TITLE-', enable_events=True)],
                        [sg.Text('Click to close', font=title_font, enable_events=True)],
                        [sg.Text('This is theme', font=title_font, enable_events=True)],
                        [sg.Text(sg.theme(), font=title_font, enable_events=True)]]
        right_click_menu = [[''], ['Exit', ]]
    else:
        top_elements = [[sg.Stretch(), sg.Text(title, font=title_font, k='-TITLE-'), sg.Stretch()]]

        right_click_menu = [[''],
                            ['Set Counter', 'Choose Title', 'Edit Me', 'Change Theme', 'Set Button Font',
                             'Set Title Font', 'Set Main Font', 'Set Click Sound', 'Show Settings', 'Alpha', [str(x) for x in range(1, 11)], 'Exit', ]]

    layout = top_elements + \
             [[sg.Column([[sg.pin(sg.Text('0', font=main_number_font, k='-MAIN INFO NUM-', justification='c', enable_events=test_window, pad=(0, 0)))]],justification='c', element_justification='c', pad=0)]] + \
            [[sg.T('+', font=button_font, enable_events=True, pad=0), sg.Stretch(), sg.T('-', font=button_font, enable_events=True, pad=0)]]

    try:
        window = sg.Window('Clicky Counter', layout, location=location, no_titlebar=True, grab_anywhere=True, margins=(0, 0), element_padding=0, alpha_channel=alpha, finalize=True, right_click_menu=right_click_menu, right_click_menu_tearoff=False,
                           enable_close_attempted_event=True, keep_on_top=True)
    except Exception as e:
        if sg.popup_yes_no('Error creating your window', e, 'These are your current settings:', sg.user_settings(),
                           'Do you want to delete your settings file?') == 'Yes':
            sg.user_settings_delete_filename()
            sg.popup('Settings deleted.', 'Please restart your program')
            exit()
        window = None

    return window


def main():
    loc = sg.user_settings_get_entry('-location-', (None, None))
    window = make_window(loc)

    counter = sg.user_settings_get_entry('-counter-', 0)
    sound_file = sg.user_settings_get_entry('-sound file-', None)

    while True:  # Event Loop
        # First update the status information
        window['-MAIN INFO NUM-'].update(counter)
        # for debugging show the last update date time

        # -------------- Start of normal event loop --------------
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED:
            break
        elif event in (sg.WIN_CLOSE_ATTEMPTED_EVENT, 'Exit'):
            sg.user_settings_set_entry('-location-', window.current_location())
            break
        if event == 'Edit Me':
            sg.execute_editor(__file__)
        elif event == 'Set Counter':
            new_count = sg.popup_get_text('What value do you want to set the counter to?', location=window.current_location(), keep_on_top=True)
            try:
                new_count = int(new_count)
            except Exception as e:
                sg.popup_error('Counter must be a valid int')
                continue
            if new_count is not None:
                counter = int(new_count)
        elif event == 'Choose Title':
            new_title = sg.popup_get_text('Choose a title for your counter', default_text=sg.user_settings_get_entry('-title-', ''), location=window.current_location(), )
            if new_title is not None:
                window['-TITLE-'].update(new_title)
                sg.user_settings_set_entry('-title-', new_title)
        elif event in [str(x) for x in range(1, 11)]:
            window.set_alpha(int(event) / 10)
            sg.user_settings_set_entry('-alpha-', int(event) / 10)
        elif event == 'Change Theme':
            loc = window.current_location()
            if choose_theme(loc) is not None:
                # this is result of hacking code down to 99 lines in total. Not tried it before. Interesting test.
                _, window = window.close(), make_window(loc)
        elif event == 'Set Main Font':
            font = sg.popup_get_text('Main Information Font and Size (e.g. courier 70)', default_text=sg.user_settings_get_entry('-main number font-'), keep_on_top=False, location=window.current_location())
            if font:
                sg.user_settings_set_entry('-main number font-', font)
                _, window = window.close(), make_window(loc)
        elif event == 'Set Button Font':
            font = sg.popup_get_text('Font for the +/- symbols (e.g. courier 70)', default_text=sg.user_settings_get_entry('-button font-'), keep_on_top=True, location=window.current_location())
            if font:
                sg.user_settings_set_entry('-button font-', font)
                _, window = window.close(), make_window(loc)
        elif event == 'Set Title Font':
            font = sg.popup_get_text('Title Font and Size (e.g. courier 8)', default_text=sg.user_settings_get_entry('-title font-'), keep_on_top=True, location=window.current_location())
            if font:
                sg.user_settings_set_entry('-title font-', font)
                _, window = window.close(), make_window(loc)
        elif event == '+':
            counter += 1
            if sound_file:
                winsound.PlaySound(sound_file, 1)
        elif event == '-':
            counter -= 1
            if sound_file:
                winsound.PlaySound(sound_file, 1)
        elif event == 'Set Click Sound':
            if not sg.running_windows():
                sg.popup_error('I am terribly sorry to inform you that you are not running Windows and thus, no clicky sound for you.', keep_on_top=True, location=window.current_location())
            else:
                sound_file = sg.popup_get_file('Choose the file to play when changing counter', file_types=(('WAV', '*.wav'),), keep_on_top=True, location=window.current_location(), default_path=sg.user_settings_get_entry('-sound file-', ''))
                if sound_file is not None:
                    sg.user_settings_set_entry('-sound file-', sound_file)
        elif event =='Show Settings':
            sg.popup_scrolled(sg.UserSettings._default_for_function_interface, location=window.current_location())

        sg.user_settings_set_entry('-counter-', counter)

    window.close()


if __name__ == '__main__':
    sg.set_options(keep_on_top=True)
    main()