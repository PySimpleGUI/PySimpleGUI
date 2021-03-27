import PySimpleGUI as sg
"""
    Demo Hotkey

    Want a keyboard hotkey to cause your program to take some action
    that's identical to a button being clicked?

    Well... that's 1 line of code that's needed.

    This line binds the F10 keybaord key to the window. It produces a "Go" event:
        window.bind('<F10>', 'Go')
    
    Copyright 2021 PySimpleGUI
"""

layout = [  [sg.Text('Press F10 to get same result as clicking "Go" button')],
            [sg.Input(key='-IN-')],
            [sg.Output(size=(30,8))],
            [sg.Button('Go'), sg.Button('Exit')] ]

window = sg.Window('Window Title', layout, finalize=True)

window.bind('<F10>', 'Go')      # Make sure your window is finalized first

while True:             # Event Loop
    event, values = window.read()
    print(event, values)
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
window.close()