#!/usr/bin/env python
import sys
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg

layout1 = [[ sg.Text('Window 1') ],
           [sg.Input(do_not_clear=True)],
          [ sg.Button('Read')]]

window1 = sg.Window('My new window', location=(800,500)).Layout(layout1)


layout2 = [[ sg.Text('Window 2') ],
           [sg.Input(do_not_clear=True)],
          [ sg.Button('Read')]]

window2 = sg.Window('My new window', location=(800, 625), return_keyboard_events=True).Layout(layout2)


layout3 = [[ sg.Text('Window 3') ],
           [sg.Input(do_not_clear=False)],
          [ sg.Button('Read')]]

window3 = sg.Window('My new window', location=(800,750), return_keyboard_events=True).Layout(layout3)


while True:     # Event Loop
    event, values = window1.Read(timeout=50)
    if event is None:
        break
    elif event != '__timeout__':
        print(event, values)

    event, values = window2.Read(timeout=0)
    if event is None:
        break
    elif event != '__timeout__':
        print(event, values)

    event, values = window3.Read(timeout=0)
    if event is None:
        break
    elif event != '__timeout__':
        print(event, values)
