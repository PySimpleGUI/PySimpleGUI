#!/usr/bin/env python
import sys
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg

layout = [[sg.Text('Filename', )],
          [sg.Input(), sg.FileBrowse()],
          [sg.OK(), sg.Cancel()]]

button, (number,) = sg.Window('Get filename example').LayoutAndRead(layout)



import PySimpleGUI as sg

button, (filename,) = sg.Window('Get filename example').LayoutAndRead(
    [[sg.Text('Filename')], [sg.Input(), sg.FileBrowse()], [sg.OK(), sg.Cancel()]])