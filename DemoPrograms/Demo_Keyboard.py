#!/usr/bin/env python
import sys
import PySimpleGUI as sg

"""
    Copyright 2023 PySimpleSoft, Inc. and/or its licensors. All rights reserved.

    Redistribution, modification, or any other use of PySimpleGUI or any portion thereof is subject to the terms of the PySimpleGUI License Agreement available at https://eula.pysimplegui.com.

    You may not redistribute, modify or otherwise use PySimpleGUI or its contents except pursuant to the PySimpleGUI License Agreement.
"""

# Recipe for getting keys, one at a time as they are released
# If want to use the space bar, then be sure and disable the "default focus"

layout = [[sg.Text("Press a key or scroll mouse")],
          [sg.Text("", size=(18, 1), key='text')],
          [sg.Button("OK", key='OK')]]

window = sg.Window("Keyboard Test", layout,
                   return_keyboard_events=True, use_default_focus=False)

# ---===--- Loop taking in user input --- #
while True:
    event, values = window.read()
    text_elem = window['text']
    if event in ("OK", None):
        print(event, "exiting")
        break
    if len(event) == 1:
        text_elem.update(value='%s - %s' % (event, ord(event)))
    if event is not None:
        text_elem.update(event)


window.close()
