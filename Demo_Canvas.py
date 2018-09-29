#!/usr/bin/env python
import sys
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg

layout = [
           [sg.Canvas(size=(150, 150), background_color='red', key='canvas')],
           [sg.T('Change circle color to:'), sg.ReadButton('Red'), sg.ReadButton('Blue')]
           ]

window = sg.Window('Canvas test').Layout(layout).Finalize()

cir = window.FindElement('canvas').TKCanvas.create_oval(50, 50, 100, 100)

while True:
    button, values = window.Read()
    if button is None:
        break
    if button is 'Blue':
        window.FindElement('canvas').TKCanvas.itemconfig(cir, fill = "Blue")
    elif button is 'Red':
        window.FindElement('canvas').TKCanvas.itemconfig(cir, fill = "Red")
