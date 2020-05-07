#!/usr/bin/env python
import PySimpleGUI as sg

#
# An Async Demonstration of a media player
# Uses button images for a super snazzy look
# See how it looks here:
# https://user-images.githubusercontent.com/13696193/43159403-45c9726e-8f50-11e8-9da0-0d272e20c579.jpg
#


def MediaPlayerGUI():
    background = '#F0F0F0'
    sg.set_options(background_color=background,
                   element_background_color=background)

    def ImageButton(title, key):
        return sg.Button(title, button_color=(background, background),
                    border_width=0, key=key)

    # define layout of the rows
    layout = [[sg.Text('Media File Player', font=("Helvetica", 25))],
              [sg.Text('', size=(15, 2), font=("Helvetica", 14), key='output')],
              [ImageButton('restart', key='Restart Song'), sg.Text(' ' * 2),
               ImageButton('pause', key='Pause'), sg.Text(' ' * 2),
               ImageButton('next', key='Next'), sg.Text(' ' * 2),
               sg.Text(' ' * 2), ImageButton('exit', key='Exit')],
              ]

    window = sg.Window('Media File Player', layout,
                       default_element_size=(20, 1),
                       font=("Helvetica", 25))

    while True:
        event, values = window.read(timeout=100)
        if event == 'Exit' or event == sg.WIN_CLOSED:
            break
        # If a button was pressed, display it on the GUI by updating the text element
        if event != sg.TIMEOUT_KEY:
            window['output'].update(event)

    window.close()


MediaPlayerGUI()
