import PySimpleGUI as sg

"""
    Copyright 2023 PySimpleSoft, Inc. and/or its licensors. All rights reserved.

    Redistribution, modification, or any other use of PySimpleGUI or any portion thereof is subject to the terms of the PySimpleGUI License Agreement available at https://eula.pysimplegui.com.

    You may not redistribute, modify or otherwise use PySimpleGUI or its contents except pursuant to the PySimpleGUI License Agreement.
"""

names = ['Roberta', 'Kylie', 'Jenny', 'Helen',
         'Andrea', 'Meredith', 'Deborah', 'Pauline',
         'Belinda', 'Wendy']

layout = [[sg.Text('Listbox with search')],
          [sg.Input(size=(20, 1), enable_events=True, key='-INPUT-')],
          [sg.Listbox(names, size=(20, 4), enable_events=True, key='-LIST-')],
          [sg.Button('Chrome'), sg.Button('Exit')]]

window = sg.Window('Listbox with Search', layout)
# Event Loop
while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):                # always check for closed window
        break
    if values['-INPUT-'] != '':                         # if a keystroke entered in search field
        search = values['-INPUT-']
        new_values = [x for x in names if search in x]  # do the filtering
        window['-LIST-'].update(new_values)     # display in the listbox
    else:
        # display original unfiltered list
        window['-LIST-'].update(names)
    # if a list item is chosen
    if event == '-LIST-' and len(values['-LIST-']):
        sg.popup('Selected ', values['-LIST-'])

window.close()
