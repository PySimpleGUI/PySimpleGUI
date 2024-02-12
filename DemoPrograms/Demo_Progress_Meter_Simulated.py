"""
    Demo Program - Progress Meter using a Text Element

    This program was written by @jason990420

    This is a clever use of a Text Element to create the same look
    and feel of a progress bar in PySimpleGUI using only a Text Element.

    Copyright 2020-2023 PySimpleSoft, Inc. and/or its licensors. All rights reserved.
    
    Redistribution, modification, or any other use of PySimpleGUI or any portion thereof is subject to the terms of the PySimpleGUI License Agreement available at https://eula.pysimplegui.com.
    
    You may not redistribute, modify or otherwise use PySimpleGUI or its contents except pursuant to the PySimpleGUI License Agreement.
"""

import PySimpleGUI as sg

sg.theme('DarkBlue')

layout = [[sg.Text('', size=(50, 1), relief='sunken',
                   text_color='yellow', background_color='black',key='-TEXT-', metadata=0)]]

window = sg.Window('Title', layout, finalize=True)

text = window['-TEXT-']

while True:

    event, values = window.read(timeout=100)

    if event == sg.WINDOW_CLOSED:
        break
    text.metadata = (text.metadata + 1) % 51
    text.update(sg.SYMBOL_SQUARE * text.metadata)

window.close()