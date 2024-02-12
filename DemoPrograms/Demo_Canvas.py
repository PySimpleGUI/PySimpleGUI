#!/usr/bin/env python
import PySimpleGUI as sg

"""
    Copyright 2023 PySimpleSoft, Inc. and/or its licensors. All rights reserved.

    Redistribution, modification, or any other use of PySimpleGUI or any portion thereof is subject to the terms of the PySimpleGUI License Agreement available at https://eula.pysimplegui.com.

    You may not redistribute, modify or otherwise use PySimpleGUI or its contents except pursuant to the PySimpleGUI License Agreement.
"""

layout = [
    [sg.Canvas(size=(150, 150), background_color='red', key='canvas')],
    [sg.Text('Change circle color to:'), sg.Button('Red'), sg.Button('Blue')]
]

window = sg.Window('Canvas test', layout, finalize=True)

cir = window['canvas'].TKCanvas.create_oval(50, 50, 100, 100)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event in ('Blue', 'Red'):
        window['canvas'].TKCanvas.itemconfig(cir, fill=event)
