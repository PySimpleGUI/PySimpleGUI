#!/usr/bin/env python
import PySimpleGUI as sg
from random import randint as randint

"""
    Demo - LEDS using Text

    A simple example of how you can use UNICODE characters as LED indicators in a window

    Copyright 2020 PySimpleGUI.org
"""

sg.theme('Light Brown 4')

CIRCLE = '⚫'
CIRCLE_OUTLINE = '⚪'

layout = [  [sg.Text('Status 1', size=(12,1)), sg.Text(CIRCLE_OUTLINE, size=(10,1), text_color='green', key='-LED0-')],
            [sg.Text('Status 2', size=(12,1)), sg.Text(CIRCLE_OUTLINE, size=(10,1), text_color='red', key='-LED1-')],
            [sg.Text('Status 3', size=(12,1)), sg.Text(CIRCLE_OUTLINE, size=(10,1), text_color='blue', key='-LED2-')]]

window = sg.Window('Window Title', layout, font='Any 16')

while True:
    event, values = window.read(timeout=200)
    if event == sg.WIN_CLOSED:
        break
    for i in range(3):
        if randint(1,100) < 25:
            window[f'-LED{i}-'].update(CIRCLE)
        else:
            window[f'-LED{i}-'].update(CIRCLE_OUTLINE)

window.close()
