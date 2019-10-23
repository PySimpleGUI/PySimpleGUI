#!/usr/bin/env python
import sys
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg

layout = [[ sg.Text('My Window') ],
          [ sg.Button('Disappear')]]

window = sg.Window('My window').Layout(layout)

while True:
    event, values = window.Read()
    if event is None:
        break
    if event == 'Disappear':
        window.Disappear()
        sg.Popup('Click OK to make window reappear')
        window.Reappear()

