import PySimpleGUI as sg

"""
    Custom Titlebar - Async Version

    Demo showing how to remove the titlebar and replace with your own
    Unlike previous demos that lacked a titlebar, this one provides a way for you
    to "minimize" your window that does not have a titlebar.  This is done by faking
    the window using a hidden window that is minimized.

    While this demo uses the button colors for the titlebar color, you can use anything you want.
    If possible it could be good to use combinations that are known to match like the input element colors
    or the button colors.

    This version of the demo allows for async execution of your code.  In another demo of this
    custom titlebar idea, the user window would stop when the window is minimized.  This is OK
    for most applications, but if you're running a window with a timeout value (an async window)
    then stopping execution when the window is minimized is not good.

    The way to achieve both async window and the custom titlebar is to use the "read_all_windows"
    function call.  Using this function with a timeout has the same effect as running your
    window.read with a timeout.

    Additionally, if you right click and choose "close" on the minimized window on your
    taskbar, now the program will exist rather than restoring the window like the other demo does.

    Copyright 2020 PySimpleGUI.org
"""


def minimize_main_window(main_window):
    """
    Creates an icon on the taskbar that represents your custom titlebar window.
    The FocusIn event is set so that if the user restores the window from the taskbar.
    If this window is closed by right clicking on the icon and choosing close, then the
    program will exit just as if the "X" was clicked on the main window.
    """
    main_window.hide()
    layout = [[sg.T('This is your window with a customized titlebar... you just cannot see it')]]
    window = sg.Window(main_window.Title, layout, finalize=True, alpha_channel=0)
    window.minimize()
    window.bind('<FocusIn>', '-RESTORE-')
    # store the dummy window as a function property
    minimize_main_window.dummy_window = window


def restore_main_window(main_window):
    """
    Call this function when you want to restore your main window

    :param main_window:
    :return:
    """
    if hasattr(minimize_main_window, 'dummy_window'):
        minimize_main_window.dummy_window.close()
        minimize_main_window.dummy_window = None
    main_window.un_hide()


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

    return [sg.Col([[sg.T(title, text_color=tc, background_color=bc)]], pad=(0, 0), background_color=bc),
            sg.Col([[sg.T('_', text_color=tc, background_color=bc, enable_events=True, key='-MINIMIZE-'),
                     sg.Text('❎', text_color=tc, background_color=bc, enable_events=True, key='Exit')]], element_justification='r', key='-TITLEBAR-',
                   pad=(0, 0), background_color=bc)]


def main():
    # sg.theme('light green 3')
    # sg.theme('dark red')
    # sg.theme('dark green 3')
    sg.theme('light brown 10')

    title = 'Customized Titlebar Window'
    # Here the titlebar colors are based on the theme. A few suggestions are shown. Try each of them
    layout = [title_bar(title, sg.theme_button_color()[0], sg.theme_button_color()[1]),
              # title_bar(title, sg.theme_button_color()[1], sg.theme_slider_color()),
              # title_bar(title, sg.theme_slider_color(), sg.theme_button_color()[0]),
              [sg.T('This is normal window text.   The above is the fake "titlebar"')],
              [sg.T('Input something:')],
              [sg.Input(key='-IN-'), sg.Text(size=(12, 1), key='-OUT-')],
              [sg.Button('Go')]]

    window_main = sg.Window(title, layout, resizable=True, no_titlebar=True, grab_anywhere=True, keep_on_top=True, margins=(0, 0), finalize=True)

    window_main['-TITLEBAR-'].expand(True, False, False)  # expand the titlebar's rightmost column so that it resizes correctly
    counter = 0
    while True:  # Event Loop
        window, event, values = sg.read_all_windows(timeout=100)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break

        # ------ events to handle minimize and restore of window ------
        if event == '-MINIMIZE-':
            minimize_main_window(window_main)
            continue
        elif event == '-RESTORE-' or (event == sg.WINDOW_CLOSED and window != window_main):
            restore_main_window(window_main)
            continue

        # ------ remainder of your "normal" events and window code ------
        window_main['-OUT-'].update(counter)
        counter += 1
    window.close()


if __name__ == '__main__':
    main()
