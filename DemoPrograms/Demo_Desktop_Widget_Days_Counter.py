import PySimpleGUI as sg
import sys
import datetime

"""
    Another simple Desktop Widget using PySimpleGUI
    The "Days Since _______" Widget
    
    This widget counts the number of days since some date of your choosing.  
    Maybe you want to track the number of days since the start of the year.
    Or perhaps when you got married.... or divorced.... or stopped some activity
    Or started some activity.... you get the idea.  It tracks a time delta in days  

    Copyright 2021 PySimpleGUI
"""

ALPHA = 0.9
THEME = 'Dark green 3'
# May add ability to change theme from the user interface.  For now forcing to constant
sg.user_settings_set_entry('-theme-', THEME)

GSIZE = (160, 160)
UPDATE_FREQUENCY_MILLISECONDS = 1000*60*60      # update every hour

def main(location):
    title = sg.user_settings_get_entry('-title-', '')
    # May add ability to change theme from the user interface.  For now use constant
    theme = sg.user_settings_get_entry('-theme-', THEME)
    sg.theme(theme)

    font = 'Courier 70'
    title_font = 'Courier 8'
    refresh_font = 'Courier 8'

    layout = [
        [sg.Text(title, size=(20,1), font=title_font, justification='c', k='-TITLE-')],
        [sg.Text(size=(3,1), font=font, k='-T-', justification='c')],
        [sg.pin(sg.Text(size=(15,2), font=refresh_font, k='-REFRESHED-', justification='c'))],
    ]

    window = sg.Window('Day Number', layout, location=location, no_titlebar=True, grab_anywhere=True, margins=(0, 0), element_justification='c', element_padding=(0, 0), alpha_channel=ALPHA, finalize=True, right_click_menu=[[''], ['Choose Date', 'Choose Title', 'Edit Me', 'Refresh', 'Show Refresh', 'Hide Refresh', 'Exit']])

    saved_date = sg.user_settings_get_entry('-start date-', (1,1,2021))
    start_date = datetime.datetime(saved_date[2], saved_date[0], saved_date[1])
    window['-REFRESHED-'].update(visible=sg.user_settings_get_entry('-show refresh-', True))

    while True:             # Event Loop
        # First update the status information
        now = datetime.datetime.now()
        delta =now-start_date
        window['-T-'].update(f'{delta.days}')

        # for debugging show the last update date time
        date_time = now.strftime("%m/%d/%Y\n%I:%M:%S %p")
        window['-REFRESHED-'].update(f'{date_time}')

        # -------------- Start of normal event loop --------------
        event, values = window.read(timeout=UPDATE_FREQUENCY_MILLISECONDS)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == 'Edit Me':
            sg.execute_editor(__file__)
        elif event == 'Choose Date':
            new_start = sg.popup_get_date()
            if new_start is not None:
                start_date = datetime.datetime(new_start[2], new_start[0], new_start[1])
                sg.user_settings_set_entry('-start date-', new_start)
        elif event == 'Choose Title':
            new_title = sg.popup_get_text('Choose a title for your date')
            if new_title is not None:
                window['-TITLE-'].update(new_title)
                sg.user_settings_set_entry('-title-', new_title)
        elif event == 'Show Refresh':
            window['-REFRESHED-'].update(visible=True)
            sg.user_settings_set_entry('-show refresh-', True)
        elif event == 'Hide Refresh':
            window['-REFRESHED-'].update(visible=False)
            sg.user_settings_set_entry('-show refresh-', False)

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