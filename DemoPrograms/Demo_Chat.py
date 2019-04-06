#!/usr/bin/env python
import sys
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg

'''
A chat window.  Add call to your send-routine, print the response and you're done

To see this program RUN on the web go here:
https://repl.it/@PySimpleGUI/Chat-Application-Demo

Note that the size of the display on repl.it is smaller than most, so the sizes of the 
Multiline and Output text areas were reduced in the online version.  Nothing else was changed
'''

sg.ChangeLookAndFeel('GreenTan')            # give our window a spiffy set of colors

layout =  [ [sg.Text('Your output will go here', size=(40, 1))],
            [sg.Output(size=(127, 30), font=('Helvetica 10'))],
            [sg.Multiline(size=(85, 5), enter_submits=True, key='query'),
            sg.Button('SEND', button_color=(sg.YELLOWS[0], sg.BLUES[0]), bind_return_key=True),
            sg.Button('EXIT', button_color=(sg.YELLOWS[0], sg.GREENS[0]))]]

window = sg.Window('Chat window',
                   default_element_size=(30, 2),
                   font=('Helvetica',' 13'),
                   default_button_element_size=(8,2)).Layout(layout)

# ---===--- Loop taking in user input and using it  --- #
while True:
    event, value = window.Read()
    if event is 'SEND':
        query = value['query'].rstrip()
        # EXECUTE YOUR COMMAND HERE
        print('The command you entered was {}'.format(query))
    elif event in (None, 'EXIT'):            # quit if exit button or X
        break
sys.exit(69)

