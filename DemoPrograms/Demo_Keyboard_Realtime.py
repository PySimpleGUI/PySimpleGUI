#!/usr/bin/env python
import PySimpleGUI as sg

"""
    Copyright 2023 PySimpleSoft, Inc. and/or its licensors. All rights reserved.

    Redistribution, modification, or any other use of PySimpleGUI or any portion thereof is subject to the terms of the PySimpleGUI License Agreement available at https://eula.pysimplegui.com.

    You may not redistribute, modify or otherwise use PySimpleGUI or its contents except pursuant to the PySimpleGUI License Agreement.
"""

layout = [[sg.Text("Hold down a key")],
          [sg.Button("OK")]]

window = sg.Window("Realtime Keyboard Test", layout, return_keyboard_events=True,
                   use_default_focus=False)

while True:
    event, values = window.read(timeout=0)

    if event == "OK":
        print(event, values, "exiting")
        break
    if event is not sg.TIMEOUT_KEY:
        if len(event) == 1:
            print('%s - %s' % (event, ord(event)))
        else:
            print(event)
    elif event == sg.WIN_CLOSED:
        break

window.close()
