import PySimpleGUI as sg

"""
    Demo - Fill a listbox with list of files FilesBrowse button

    This technique can be used to generate events from "Chooser Buttons" like FileBrowse, FilesBrowse
    FolderBrowser, ColorChooserButton, Calendar Button

    Any button that uses a "Target" can be used with an invisible Input Element to generate an
    event when the user has made a choice.  Enable events for the invisible element and an event will
    be generated when the Chooser Button fills in the element

    This particular demo users a list of chosen files to populate a listbox
    
    Copyright 2023 PySimpleSoft, Inc. and/or its licensors. All rights reserved.
    
    Redistribution, modification, or any other use of PySimpleGUI or any portion thereof is subject to the terms of the PySimpleGUI License Agreement available at https://eula.pysimplegui.com.
    
    You may not redistribute, modify or otherwise use PySimpleGUI or its contents except pursuant to the PySimpleGUI License Agreement.
"""


layout = [  [sg.LBox([], size=(20,10), key='-FILESLB-')],
            [sg.Input(visible=False, enable_events=True, key='-IN-'), sg.FilesBrowse()],
            [sg.Button('Go'), sg.Button('Exit')]  ]

window = sg.Window('Window Title', layout)

while True:             # Event Loop
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    # When choice has been made, then fill in the listbox with the choices
    if event == '-IN-':
        window['-FILESLB-'].Update(values['-IN-'].split(';'))
window.close()
