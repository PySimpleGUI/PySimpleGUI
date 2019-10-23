import PySimpleGUI as sg

"""
    PySimpleGUI The Complete Course
    Lesson 7
    Multiple Independent Windows
"""
# Design pattern 2 - First window remains active

layout = [[ sg.Text('Window 1'),],
          [sg.Input('')],
          [sg.Text('', size=(20,1), key='-OUTPUT-')],
          [sg.Button('Launch 2'), sg.Button('Exit')]]

window1 = sg.Window('Window 1', layout)

window2_active = False
while True:
    event1, values1 = window1.read(timeout=100)
    window1['-OUTPUT-'].update(values1[0])
    if event1 is None or event1 == 'Exit':
        break

    if not window2_active and event1 == 'Launch 2':
        window2_active = True
        layout2 = [[sg.Text('Window 2')],
                   [sg.Button('Exit')]]

        window2 = sg.Window('Window 2', layout2)

    if window2_active:
        ev2, vals2 = window2.read(timeout=100)
        if ev2 is None or ev2 == 'Exit':
            window2_active  = False
            window2.close()

window1.close()
