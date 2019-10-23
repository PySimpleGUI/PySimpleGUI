import PySimpleGUI as sg
"""
    PySimpleGUI The Complete Course
    Lesson 7 - Multiple Windows
    1-lvl nested window
"""

# Design pattern 1 - First window does not remain active

layout = [[ sg.Text('Window 1'),],
          [sg.Input()],
          [sg.Text('', size=(20,1), key='-OUTPUT-')],
          [sg.Button('Launch 2')]]

window1 = sg.Window('Window 1', layout)
window2_active=False

while True:
    event1, values1 = window1.read(timeout=100)
    if event1 is None:
        break
    window1['-OUTPUT-'].update(values1[0])

    if event1 == 'Launch 2' and not window2_active:
        window2_active = True
        window1.hide()
        layout2 = [[sg.Text('Window 2')],
                   [sg.Button('Exit')]]

        window2 = sg.Window('Window 2', layout2)
        while True:
            ev2, vals2 = window2.read()
            if ev2 is None or ev2 == 'Exit':
                window2.close()
                window2_active = False
                window1.un_hide()
                break
window1.close()

