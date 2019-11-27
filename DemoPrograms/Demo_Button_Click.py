#!/usr/bin/env python
import winsound
import sys
import PySimpleGUI as sg

if not sys.platform.startswith('win'):
    sg.popup_error('Sorry, you gotta be on Windows')
    sys.exit(0)

# .WAV files that contain your click sounds. Put full path if not in your application's folder
click_sound = r'ButtonClick.wav'
click_sound1 = r'ButtonClick1.wav'

sg.change_look_and_feel('Dark Blue 3')      # because gray windows are boring

# Your window's layout
layout = [  [sg.Text('Click a button to hear a click')],
            [sg.Button('Click'), sg.Button('Another Click')]]
# Create your Window
window = sg.Window("Button Click", layout)

while True:             # The Event Loops
    event, values = window.read()
    if event is None:
        break
    if event == 'Click':
        winsound.PlaySound(click_sound, 1)
    elif event == 'Another Click':
        winsound.PlaySound(click_sound1, 1)
window.close()
