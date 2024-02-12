#!/usr/bin/env python
import PySimpleGUI as sg

'''
   Use this code as a starting point for creating your own Popup functions.  
   Rather than creating a long list of Popup high-level API calls, PySimpleGUI provides
   you with the tools to easily create your own.  If you need more than what the standard popup_get_text and
   other calls provide, then it's time for you to graduate into making your own windows.  Or, maybe you need
   another window that pops-up over your primary window.  Whatever the need, don't hesitate to dive in
   and create your own Popup call.
   
   This example is for a DropDown / Combobox Popup.  You provide it with a title, a message and the list
   of values to choose from. It mimics the return values of existing Popup calls (None if nothing was input)
   
   Copyright 2023 PySimpleSoft, Inc. and/or its licensors. All rights reserved.
   
   Redistribution, modification, or any other use of PySimpleGUI or any portion thereof is subject to the terms of the PySimpleGUI License Agreement available at https://eula.pysimplegui.com.
   
   You may not redistribute, modify or otherwise use PySimpleGUI or its contents except pursuant to the PySimpleGUI License Agreement.
'''


def PopupDropDown(title, text, values):
    window = sg.Window(title,
        [[sg.Text(text)],
        [sg.DropDown(values, key='-DROP-')],
        [sg.OK(), sg.Cancel()]
    ])
    event, values = window.read()
    return None if event != 'OK' else values['-DROP-']

# -----------------------  Calling your PopupDropDown function -----------------------

values = ['choice {}'.format(x) for x in range(30)]
print(PopupDropDown('My Title', 'Please make a selection', values))
