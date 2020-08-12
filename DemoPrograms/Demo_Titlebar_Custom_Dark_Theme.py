import PySimpleGUI as sg

"""
    Demo showing how to remove the titlebar and replace with your own
    Note that you cannot minimize these kinds of windows because they do not
    have an icon representing them on the taskbar
    
    Copyright 2020 PySimpleGUI.org
"""


# If not running 4.28.0.4+ that has the DarkGrey8 theme, then uncomment to get it added.
# DarkGrey8 = {'BACKGROUND': '#19232D',
#               'TEXT': '#ffffff',
#               'INPUT': '#32414B',
#               'TEXT_INPUT': '#ffffff',
#               'SCROLL': '#505F69',
#               'BUTTON': ('#ffffff', '#32414B'),
#               'PROGRESS': ('#505F69', '#32414B'),
#               'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
#               }
#
# sg.theme_add_new('DarkGrey8', DarkGrey8)


def dummy_minimized_window(title):
    """
    Creates an invisible window that is minimized to the taskbar
    As soon as something happens to the window, it is closed and the function
    returns.
    The FocusIn event is set so that if the user restores the window from the taskbar, then the read
    wille return, the window will be closed, and the function will return
    """
    layout = [[sg.T('This is your window with a customized titlebar... you just cannot see it')]]
    window = sg.Window(title, layout, finalize=True, alpha_channel=0)
    window.minimize()
    window.bind('<FocusIn>', '-FOCUS-')
    window.read(close=True)


def title_bar(title):
    """
    Creates a "row" that can be added to a layout. This row looks like a titlebar
    :param title: The "title" to show in the titlebar
    :type title: str
    :return: List[sg.Element]
    """
    bg = sg.theme_input_background_color()

    return [sg.Col([[sg.T(title, background_color=bg )]], pad=(0, 0), background_color=bg),
     sg.Col([[sg.T('_', background_color=bg, enable_events=True, key='-MINIMIZE-'),sg.Text('❎', background_color=bg, enable_events=True, key='Exit')]], element_justification='r', k='-C-', pad=(0, 0), background_color=bg)]


def main():
    sg.theme('DarkGrey8')

    title = 'Customized Titlebar Window'

    layout = [  title_bar(title),
                [sg.T('This is normal window text.   The above is the fake "titlebar"')],
                [sg.T('Input something:')],
                [sg.Input(key='-IN-'), sg.Text(size=(12,1), key='-OUT-')],
                [sg.Button('Go')]  ]

    window = sg.Window(title, layout, resizable=True, no_titlebar=True, grab_anywhere=True, keep_on_top=True, margins=(0,0), finalize=True)

    window['-C-'].expand(True, False, False)

    while True:             # Event Loop
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == '-MINIMIZE-':
            window.hide()
            dummy_minimized_window(window.Title)
            window.un_hide()
        if event == 'Go':
            window['-OUT-'].update(values['-IN-'])
    window.close()

if __name__ == '__main__':
    main()
