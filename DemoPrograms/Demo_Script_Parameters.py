#!/usr/bin/env python
import PySimpleGUI as sg
import sys
'''
Quickly add a GUI to your script!

This simple script shows a 1-line-GUI addition to a typical Python command line script.

Previously this script accepted 1 parameter on the command line.  When executed, that
parameter is read into the variable fname.

The 1-line-GUI shows a form that allows the user to browse to find the filename. The GUI
stores the result in the variable fname, just like the command line parsing did.

Copyright 2023 PySimpleSoft, Inc. and/or its licensors. All rights reserved.

Redistribution, modification, or any other use of PySimpleGUI or any portion thereof is subject to the terms of the PySimpleGUI License Agreement available at https://eula.pysimplegui.com.

You may not redistribute, modify or otherwise use PySimpleGUI or its contents except pursuant to the PySimpleGUI License Agreement.
'''

fname = ''
if len(sys.argv) == 1:
    layout = [
        [sg.Text('Document to open')],
        [sg.Input(), sg.FileBrowse()],
        [sg.CloseButton('Open'), sg.CloseButton('Cancel')]
    ]
    window = sg.Window('My Script', layout)
    event, values = window.read()
    window.close()
    fname = values['-FNAME-']
else:
    fname = sys.argv[1]
if not fname:
    sg.popup("Cancel", "No filename supplied")
    raise SystemExit("Cancelling: no filename supplied")
