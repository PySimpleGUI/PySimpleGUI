import PySimpleGUI as sg

"""
    Demo Titlebar Multiple Combintions - how to make a custom titlebar with different color options
    
    Demo showing how to remove the titlebar and replace with your own
    Unlike previous demos that lacked a titlebar, this one provides a way for you
    to "minimize" your window that does not have a titlebar.  This is done by faking
    the window using a hidden window that is minimized.

    Use the "theme" calls to experiment with the color combinations to get to the colors you like.  With themes, there
    are pairs of colors that usually match well.  You're shown each of these combinations to help you decide which you
    like the best.  These color combinations are shown to you one by one as you click the "next" button:

        ['1 - Button Colors', sg.theme_button_color()[0], sg.theme_button_color()[1]],
        ['2 - Reversed Button Colors', sg.theme_button_color()[1], sg.theme_button_color()[0]],
        ['3 - Input Colors', sg.theme_input_text_color(), sg.theme_input_background_color()],
        ['4 - Reversed Input Colors', sg.theme_input_background_color(), sg.theme_input_text_color()],
        ['5 - Reversed background & Text', sg.theme_background_color(), sg.theme_text_color()],
        ['6 - Button Background & Slider', sg.theme_button_color()[1], sg.theme_slider_color()],
        ['7 - Slider & Button Text', sg.theme_slider_color(), sg.theme_button_color()[0]],

    Copyright 2020 PySimpleGUI.org
"""


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
    :param text_color: Text color for titlebar
    :type text_color: str
    :param background_color: Background color for titlebar
    :type background_color: str
    :return: A list of elements (i.e. a "row" for a layout)
    :rtype: List[sg.Element]
    """
    bc = background_color
    tc = text_color
    font = 'Helvetica 12'

    return [sg.Col([[sg.T(title, text_color=tc, background_color=bc, font=font, grab=True)]], pad=(0, 0), background_color=bc),
            sg.Col([[sg.T('_', text_color=tc, background_color=bc, enable_events=True, font=font, key='-MINIMIZE-'),
                     sg.Text('❎', text_color=tc, background_color=bc, font=font, enable_events=True, key='Exit')]], element_justification='r', key='-C-', expand_x=True, grab=True,
                   pad=(0, 0), background_color=bc)]


def create_window(title, bar_text_color, bar_background_color):
    """
    Creates a window using the title and colors provided to make the titlebar
    :return: A window with a custom titlebar using specificied colors
    :rtype:  sg.Window
    """

    layout = [
        title_bar(title, bar_text_color, bar_background_color),

        [sg.T('This is normal window text.   The above is the fake "titlebar"')],
        [sg.T('Input something:')],
        [sg.Input('Color of input text', focus=True, key='-IN-'), sg.Text(size=(12, 1), key='-OUT-')],
        [sg.Button('Go'), sg.Button('Next'), sg.B('New Theme'), sg.Button('Exit')]]

    window = sg.Window(title, layout, resizable=True, no_titlebar=True, grab_anywhere=False, keep_on_top=True, margins=(0, 0), finalize=True)

    # window['-C-'].expand(True, False, False)  # expand the titlebar's rightmost column so that it resizes correctly

    return window


def choose_theme():
    layout = [[sg.Text('Custom Titlebar Demo', font='Any 14')],
              [sg.Text('This program requires version 4.28.0.20 and later')],
              [sg.Text('Click a look and feel color to see demo window')],
              [sg.Listbox(values=sg.theme_list(),
                          size=(20, 20), key='-LIST-', enable_events=True)],
              [sg.Button('Choose')]]

    window = sg.Window('Look and Feel Browser', layout)

    while True:  # Event Loop
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Choose'):
            break

    window.close()
    if event is None:
        theme = sg.theme()
    else:
        theme = values['-LIST-'][0]

    sg.theme(theme)
    color_pairs = [['1 - Button Colors', sg.theme_button_color()[0], sg.theme_button_color()[1]],
                   ['2 - Reversed Button Colors', sg.theme_button_color()[1], sg.theme_button_color()[0]],
                   ['3 - Input Colors', sg.theme_input_text_color(), sg.theme_input_background_color()],
                   ['4 - Reversed Input Colors', sg.theme_input_background_color(), sg.theme_input_text_color()],
                   ['5 - Reversed background & Text', sg.theme_background_color(), sg.theme_text_color()],
                   ['6 - Button Background & Slider', sg.theme_button_color()[1], sg.theme_slider_color()],
                   ['7 - Slider & Button Text', sg.theme_slider_color(), sg.theme_button_color()[0]], ]

    return theme, color_pairs


def main():
    theme, color_pairs = choose_theme()

    index = 0
    window = create_window('{} - {}'.format(color_pairs[index][0],theme), color_pairs[index][1], color_pairs[index][2])

    while True:  # Event Loop
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED or event.startswith('Exit'):
            break
        if event == '-MINIMIZE-':
            window.hide()
            dummy_minimized_window(window.Title)
            window.un_hide()
            window.force_focus()
        elif event == 'Go':
            window['-OUT-'].update(values['-IN-'])
        elif event == 'Next':
            window.close()
            index = (index + 1) % len(color_pairs)
            window = create_window('{} - {}'.format(color_pairs[index][0],theme), color_pairs[index][1], color_pairs[index][2])
        elif event == 'New Theme':
            window.close()
            theme, color_pairs = choose_theme()
            index = 0
            window = create_window('{} - {}'.format(color_pairs[index][0],theme), color_pairs[index][1], color_pairs[index][2])

    window.close()


if __name__ == '__main__':
    main()
