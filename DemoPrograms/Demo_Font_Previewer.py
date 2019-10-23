#!/usr/bin/env python
import sys
import PySimpleGUI as sg
from tkinter import font
import tkinter
root = tkinter.Tk()
fonts = list(font.families())
fonts.sort()
root.destroy()

'''
    Showing fonts in PSG / tk
'''

sg.change_look_and_feel('Black')

layout = [[sg.Text('My Text Element',
                size=(20, 1),
                click_submits=True,
                relief=sg.RELIEF_GROOVE,
                font='Courier` 25',
                text_color='#FF0000',
                background_color='white',
                justification='center',
                pad=(5, 3),
                key='-text-',
                tooltip='This is a text element',
                )],
          [sg.Listbox(fonts, size=(30, 20), change_submits=True, key='-list-')],
          [sg.Input(key='-in-')],
          [sg.Button('Read', bind_return_key=True), sg.Exit()]]

window = sg.Window('My new window', layout)

while True:     # Event Loop
    event, values = window.read()
    if event in (None, 'Exit'):
        break
    text_elem = window['-text-']
    print(event, values)
    if values['-in-'] != '':
        text_elem.update(font=values['-in-'])
    else:
        text_elem.update(font=(values['-list-'][0], 25))
window.close()
