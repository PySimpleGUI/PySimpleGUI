#!/usr/bin/env python
import sys
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg

layout = [[ sg.Text('My Window') ],
          [ sg.RButton('Disappear')]]

window = sg.Window('My window').Layout(layout)

while True:
    button, value = window.Read()
    if button is None:
        break
    if button == 'Disappear':
        window.Disapper()
        sg.Popup('Click OK to make window reappear')
        window.Reappear()

