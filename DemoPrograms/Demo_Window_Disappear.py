#!/usr/bin/env python
import PySimpleGUI as sg

# Example .disappear() .reappear() methods in window


layout = [[ sg.Text('My Window') ],
          [ sg.Button('Disappear')]]

window = sg.Window('My window', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Disappear':
        window.disappear()
        sg.popup('Click OK to make window reappear')
        window.reappear()

window.close()