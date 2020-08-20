import PySimpleGUI as sg

"""
    Demo showing how to remove the titlebar and replace with your own
    Unlike previous demos that lacked a titlebar, this one provides a way for you
    to "minimize" your window that does not have a titlebar.  This is done by faking
    the window using a hidden window that is minimized.
    
    While this demo uses the button colors for the titlebar color, you can use anything you want.
    If possible it could be good to use combinations that are known to match like the input element colors
    or the button colors.
    
    Copyright 2020 PySimpleGUI.org
"""


# If not running 4.28.0.4+ that has the DarkGrey8 theme, then uncomment to get it added.
DarkGrey8 = {'BACKGROUND': '#19232D',
              'TEXT': '#ffffff',
              'INPUT': '#32414B',
              'TEXT_INPUT': '#ffffff',
              'SCROLL': '#505F69',
              'BUTTON': ('#ffffff', '#32414B'),
              'PROGRESS': ('#505F69', '#32414B'),
              'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
              }

sg.theme_add_new('DarkGrey8', DarkGrey8)

sg.theme('DarkGrey8')

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


def title_bar(title, text_color, background_color):
    """
    Creates a "row" that can be added to a layout. This row looks like a titlebar
    :param title: The "title" to show in the titlebar
    :type title: str
    :return: A list of elements (i.e. a "row" for a layout)
    :type: List[sg.Element]
    """
    bc = background_color
    tc = text_color

    return [sg.Col([[sg.T(title,text_color=tc, background_color=bc )]], pad=(0, 0), background_color=bc),
     sg.Col([[sg.T('_', text_color=tc, background_color=bc, enable_events=True, key='-MINIMIZE-'),sg.Text('❎', text_color=tc, background_color=bc, enable_events=True, key='Exit')]], element_justification='r', key='-C-', pad=(0, 0), background_color=bc)]




def main():
    # sg.theme('light green 3')
    # sg.theme('dark red')
    sg.theme('DarkGrey8')

    title = 'Customized Titlebar Window'
    # Here the titlebar colors are based on the theme. A few suggestions are shown. Try each of them
    layout = [   title_bar(title, sg.theme_button_color()[0], sg.theme_button_color()[1]),
                # title_bar(title, sg.theme_button_color()[1], sg.theme_slider_color()),
                # title_bar(title, sg.theme_slider_color(), sg.theme_button_color()[0]),
                [sg.T('This is normal window text.   The above is the fake "titlebar"')],
                [sg.T('Input something:')],
                [sg.Input(key='-IN-'), sg.Text(size=(12,1), key='-OUT-')],
                [sg.Button('Go')]  ]

    window = sg.Window(title, layout, resizable=True, no_titlebar=True, grab_anywhere=True, keep_on_top=True, margins=(0,0), finalize=True)

    window['-C-'].expand(True, False, False)        # expand the titlebar's rightmost column so that it resizes correctly

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
