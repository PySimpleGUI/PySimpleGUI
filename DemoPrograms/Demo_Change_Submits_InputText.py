#!/usr/bin/env python
import PySimpleGUI as sg
"""
    Demonstrates the new change_submits parameter for inputtext elements
    It ONLY submits when a button changes the field, not normal user input
    Be careful on persistent forms to not clear the input
"""
layout = [[sg.Text('Test of reading input field')],
          [sg.Text('This input is normal'), sg.Input()],
          [sg.Text('This input change submits'),
           sg.Input(change_submits=True)],
          [sg.Text('This multiline input change submits'),
           sg.ML('', change_submits=True)],
          [sg.Text('This input is normal'),
           sg.Input(), sg.FileBrowse()],
          [sg.Text('File Browse submits'),
           sg.Input(change_submits=True,
                key='-in1-'), sg.FileBrowse()],
          [sg.Text('Color Chooser submits'),
           sg.Input(change_submits=True,
                key='-in2-'), sg.ColorChooserButton('Color...', target=(sg.ThisRow, -1))],
          [sg.Text('Folder Browse submits'),
           sg.Input(change_submits=True,
                key='-in3-'), sg.FolderBrowse()],
          [sg.Text('Calendar Chooser submits'),
           sg.Input(change_submits=True,
                key='-in4-'), sg.CalendarButton('Date...', target=(sg.ThisRow, -1))],
          [sg.Text('Disabled input submits'),
           sg.Input(change_submits=True,
                disabled=True,
                key='_in5'), sg.FileBrowse()],
          [sg.Text('This input clears after submit'),
           sg.Input(change_submits=True, key='-in6-'), sg.FileBrowse()],
          [sg.Button('Read')]]

window = sg.Window('Demonstration of InputText with change_submits',
           layout, auto_size_text=False, default_element_size=(22, 1),
                   text_justification='right')

while True:     # Event Loop
    event, values = window.read()
    print(event, values)
    if event is None:
        break

window.close()
