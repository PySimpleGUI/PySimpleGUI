#!/usr/bin/env python
import PySimpleGUI as sg

#
# Choose one of these are your starting point.  Copy, paste, have fun
#


# ---------------------------------#
# DESIGN PATTERN 1 - Simple Window #
# ---------------------------------#
layout = [[ sg.Text('My layout') ],
          [ sg.CloseButton('Next Window')]]

window = sg.Window('My window', layout)
event, values = window.read()


# --------------------------------------------------#
# DESIGN PATTERN 2 - Persistent Window (stays open) #
# --------------------------------------------------#

layout = [[ sg.Text('My Window') ],
          [ sg.Button('Read The Window')]]

window = sg.Window('My Window Title', layout)

while True:                         # Event Loop
    event, values = window.read()
    if event is None:               # if window closed with X
        break
    print(event, values)

window.close()
