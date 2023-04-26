#!/usr/bin/env python
import PySimpleGUI as sg

'''
A simple send/response chat window.  Add call to your send-routine and print the response
If async responses can come in, then will need to use a different design that uses PySimpleGUI async design pattern

Copyright 2023 PySimpleGUI

'''

sg.theme('GreenTan') # give our window a spiffy set of colors

layout = [[sg.Text('Your output will go here', size=(40, 1))],
          [sg.Output(size=(110, 20), font=('Helvetica 10'))],
          [sg.Multiline(size=(70, 5), enter_submits=True, key='-QUERY-', do_not_clear=False),
           sg.Button('SEND', button_color=(sg.YELLOWS[0], sg.BLUES[0]), bind_return_key=True),
           sg.Button('EXIT', button_color=(sg.YELLOWS[0], sg.GREENS[0]))]]

window = sg.Window('Chat window', layout, font=('Helvetica', ' 13'), default_button_element_size=(8,2), use_default_focus=False)

while True:     # The Event Loop
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'EXIT'):            # quit if exit button or X
        break
    if event == 'SEND':
        query = values['-QUERY-'].rstrip()
        # EXECUTE YOUR COMMAND HERE
        print('The command you entered was {}'.format(query), flush=True)

window.close()
