import PySimpleGUI as sg

"""
    Demo Desktop Widget Postit

    This is the longer version as it adds a lot to the right click menu to make it like
    the other more complete desktop widgets.

    Note that while the window has no scrollbar, you can still use the mousewheel to scroll

    Copyright 2021 PySimpleGUI
"""

# ----- Make the window -----
def make_window(loc):
    text_font = sg.user_settings_get_entry('-font-', '_ 20')
    text = sg.user_settings_get_entry('-text-', '')
    alpha = sg.user_settings_get_entry('-alpha-', 1.0)
    title = sg.user_settings_get_entry('-title-', 'Postit')

    layout =  [[sg.T(title, text_color='black', background_color='#FFFF88', k='-TITLE-')],
                              [sg.ML(text, size=(30, 5), background_color='#FFFF88', no_scrollbar=True, k='-ML-', border_width=0, expand_y=True, expand_x=True, font=text_font),
                               sg.Sizegrip(background_color='#FFFF88')]]
    window = sg.Window('Postit',layout,
                   no_titlebar=True, grab_anywhere=True, margins=(0, 0), background_color='#FFFF88', element_padding=(0, 0), location=loc,
                   right_click_menu=[[''], ['Edit Me', 'Change Font', 'Alpha', [str(x) for x in range(1, 11)], 'Choose Title', 'Exit', ]], keep_on_top=True,
                   font='_ 20', right_click_menu_font=text_font, resizable=True, finalize=True, alpha_channel=alpha)
    window.set_min_size(window.size)

    return window

# ----- Make sure it doesn't get any smaller than it is initially -----

def main():
    loc =  sg.user_settings_get_entry('-location-', (None, None))
    window = make_window(loc)

    while True:             # Event Loop
        event, values = window.read()
        print(event, values)
        if event in (sg.WIN_CLOSED, 'Exit'):
            if event == 'Exit':
                sg.user_settings_set_entry('-location-', window.current_location())
            break
        if event == 'Edit Me':
            sg.execute_editor(__file__)
        elif event == 'Change Font':
            font = sg.popup_get_text('Main Information Font and Size (e.g. courier 70)', default_text=sg.user_settings_get_entry('-font-'), keep_on_top=True, location=window.current_location())
            if font:
                sg.user_settings_set_entry('-font-', font)
                loc = window.current_location()
                window.close()
                window = make_window(loc)
        elif event in [str(x) for x in range(1,11)]:
            window.set_alpha(int(event)/10)
            sg.user_settings_set_entry('-alpha-', int(event)/10)
        elif event == 'Choose Title':
            new_title = sg.popup_get_text('Choose a title for your date', default_text=sg.user_settings_get_entry('-title-', 'Postit'), location=window.current_location(), keep_on_top=True)
            if new_title is not None:
                window['-TITLE-'].update(new_title)
                sg.user_settings_set_entry('-title-', new_title)
    sg.user_settings_set_entry('-text-', window['-ML-'].get().rstrip())

    window.close()


if __name__ == '__main__':
    # To start the window at a specific location, get this location on the command line
    # The location should be in form x,y with no spaces

    main()