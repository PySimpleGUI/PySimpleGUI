import PySimpleGUI as sg

"""
    Demonstrates how to use the Window.layout_extend method.
    Layouts can be extended at the Window level or within any container element such as a Column.
    This demo shows how to extend both.
    Note that while you can extend, add to, a layout, you cannot delete items from a layout.  Of course you
    can make them invisible after adding them.
    
    Copyright 2020 PySimpleGUI
"""

layout = [  [sg.Text('My Window')],
            [sg.Text('Click to add a row inside the frame'), sg.B('+', key='-B1-')],
            [sg.Text('Click to add a row inside the Window'), sg.B('+', key='-B2-')],
            [sg.Frame('Frame',[[sg.T('Frame')]], key='-COL1-')],
            [sg.Input(key='-IN-'), sg.Text(size=(12,1), key='-OUT-')],
            [sg.Button('Button'), sg.Button('Exit')]  ]

window = sg.Window('Window Title', layout)
i = 0
while True:             # Event Loop
    event, values = window.read()
    print(event, values)
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    if event == '-B1-':
        window.extend_layout(window['-COL1-'], [[sg.T('A New Input Line'), sg.I(key=f'-IN-{i}-')]])
        i += 1
    if event == '-B2-':
        window.extend_layout(window, [[sg.T('A New Input Line'), sg.I(key=f'-IN-{i}-')]])
        i += 1
window.close()