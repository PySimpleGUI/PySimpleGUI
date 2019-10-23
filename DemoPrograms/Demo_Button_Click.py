#!/usr/bin/env python
import winsound
import sys
import PySimpleGUI as sg


if not sys.platform.startswith('win'):
    sg.popup_error('Sorry, you gotta be on Windows')
    sys.exit(0)


# sg.change_look_and_feel('Dark')
# sg.set_options(element_padding=(0,0))

layout = [
    [sg.Button('Start', button_color=('white', 'black'), key='start'),
     sg.Button('Stop', button_color=('white', 'black'), key='stop'),
     sg.Button('Reset', button_color=('white', 'firebrick3'), key='reset'),
     sg.Button('Submit', button_color=('white', 'springgreen4'), key='submit')]
]

window = sg.Window("Button Click", layout, finalize=True,
         default_element_size=(12, 1), text_justification='r',
         auto_size_text=False, auto_size_buttons=False,
         default_button_element_size=(12, 1), use_default_focus=False )

window['submit'].update(disabled=True)

recording = have_data = False
while True:
    event, values = window.read(timeout=100)
    if event is None:
        break
    if event != sg.TIMEOUT_KEY:
      winsound.PlaySound("ButtonClick.wav", 1)

window.close()
