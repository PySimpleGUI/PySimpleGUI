#!/usr/bin/env python
import PySimpleGUI as sg

layout = [
    [sg.Canvas(size=(150, 150), background_color='red', key='canvas')],
    [sg.Text('Change circle color to:'), sg.Button('Red'), sg.Button('Blue')]
]

window = sg.Window('Canvas test', layout, finalize=True)

cir = window['canvas'].TKCanvas.create_oval(50, 50, 100, 100)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event in ('Blue', 'Red'):
        window['canvas'].TKCanvas.itemconfig(cir, fill=event)
