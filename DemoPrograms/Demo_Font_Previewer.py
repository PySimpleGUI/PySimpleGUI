#!/usr/bin/env python
import sys
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg

from tkinter import font
import tkinter
root = tkinter.Tk()
fonts = list(font.families())
fonts.sort()
root.destroy()

sg.ChangeLookAndFeel('Black')

layout = [[ sg.Text('My Text Element',
                    size=(20,1),
                    auto_size_text=False,
                    click_submits=True,
                    relief=sg.RELIEF_GROOVE,
                    font = 'Courier` 25',
                    text_color='#FF0000',
                    background_color='white',
                    justification='center',
                    pad=(5,3),
                    key='_text_',
                    tooltip='This is a text element',
                    ) ],
            [sg.Listbox(fonts, size=(30,20), change_submits=True, key='_list_')],
            [sg.Input(key='_in_')],
          [ sg.Button('Read', bind_return_key=True), sg.Exit()]]

window = sg.Window('My new window',
                   # grab_anywhere=True,
                   # force_toplevel=True,
                   ).Layout(layout)


while True:     # Event Loop
    event, values = window.Read()
    if event is None or event == 'Exit':
        break
    text_elem = window.FindElement('_text_')
    print(event, values)
    if values['_in_'] != '':
        text_elem.Update(font=values['_in_'])
    else:
        text_elem.Update(font=(values['_list_'][0], 25))