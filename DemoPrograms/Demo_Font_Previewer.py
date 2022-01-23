#!/usr/bin/env python
import PySimpleGUI as sg

'''
    Demo Font Previewer
    
    Gets a list of the installed fonts according to tkinter.
    Requires PySimpleGUI version 4.57.0 and newer (that's when sg.Text.fonts_installed_list was added)
    
    Uses the Text element's class method to get the fonts reported by tkinter.
    
    Copyright 2020, 2021, 2022 PySimpleGUI
'''

fonts = sg.Text.fonts_installed_list()


sg.theme('Black')

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
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    text_elem = window['-text-']
    print(event, values)
    if values['-in-'] != '':
        text_elem.update(font=values['-in-'])
    else:
        text_elem.update(font=(values['-list-'][0], 25))
window.close()
