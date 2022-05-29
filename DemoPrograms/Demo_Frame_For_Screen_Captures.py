import PySimpleGUI as sg

"""
    Demo Frame For Screen Captures

    This program can be used to help you record videos.

    Because it relies on the "transparent color" feature that's only available on Windows, this Demo is only going
    to work the indended way on Windows.

    Some video recorders that record a portion of the screen do not show you, at all times, what portion of the screen
    is being recorded.  This can make it difficult for you to stay within the bounds being recorded.
    This demo program is meant to help the situation by showing a thin line that is 20 pixels larger than the area
    being recorded.  

    The top edge of the window has the controls.  There's an exit button, a solid "bar" for you to grab with your mouse to move
    the frame around your window, and 2 inputs with a "resize" button that enables you to set the frame to the size you want to stay
    within.


    Copyright 2022 PySimpleGUI.org
"""


def main():
    offset = (20, 20)  # Number of extra pixels to add to the recording area
    default_size = (1920, 1080)  # The default size of the recording
    location = (None, None)  # A specific location to place the window if you want a specific spot

    window = sg.Window('Window Title',
                       [[sg.Button('Exit'), sg.T(sg.SYMBOL_SQUARE * 10, grab=True), sg.I(default_size[0], s=4, k='-W-'), sg.I(default_size[1], s=4, k='-H-'), sg.B('Resize')],
                        [sg.Frame('', [[]], s=(default_size[0] + offset[0], default_size[1] + offset[1]), k='-FRAME-')]], transparent_color=sg.theme_background_color(),
                       right_click_menu=['', ['Edit Me', 'Exit']], location=location, no_titlebar=True, keep_on_top=True)

    while True:  # Event Loop
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == 'Edit Me':
            sg.execute_editor(__file__)
        elif event == 'Resize':
            window['-FRAME-'].set_size((int(values['-W-']) + offset[0], int(values['-H-']) + offset[1]))
    window.close()


if __name__ == '__main__':
    main()
