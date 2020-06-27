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

def LED(color, key):
    """
    A "user defined element".  In this case our LED is based on a Text element. This gives up 1 location to change how they look, size, etc.
    :param color: (str) The color of the LED
    :param key: (Any) The key used to look up the element
    :return: (sg.Text) Returns a Text element that displays the circle
    """
    return sg.Text(CIRCLE_OUTLINE, text_color=color, key=key)

layout = [  [sg.Text('Status 1  '), LED('Green', '-LED0-') ],
            [sg.Text('Status 2  '), LED('blue', '-LED1-')],
            [sg.Text('Status 3  '), LED('red', '-LED2-')],
            [sg.Button('Exit')]]

window = sg.Window('Window Title', layout, font='Any 16')

while True:
    event, values = window.read(timeout=200)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    # Loop through all of the LEDs and update. 25% of the time turn it off.
    for i in range(3):
        window[f'-LED{i}-'].update(CIRCLE if randint(1, 100) < 25 else CIRCLE_OUTLINE)

window.close()
