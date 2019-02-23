"""
    PySimpleGUI The Complete Course
    Lesson 7 - Multiple Windows
"""
import PySimpleGUI as sg

# Design pattern 2 - First window remains active

layout = [[ sg.Text('Window 1'),],
          [sg.Input(do_not_clear=True)],
          [sg.Text('', key='_OUTPUT_')],
          [sg.Button('Launch 2'), sg.Button('Exit')]]

win1 = sg.Window('Window 1').Layout(layout)

win2_active = False
while True:
    ev1, vals1 = win1.Read(timeout=100)
    win1.FindElement('_OUTPUT_').Update(vals1[0])
    if ev1 is None or ev1 == 'Exit':
        break

    if not win2_active and ev1 == 'Launch 2':
        win2_active = True
        layout2 = [[sg.Text('Window 2')],
                   [sg.Button('Exit')]]

        win2 = sg.Window('Window 2').Layout(layout2)

    if win2_active:
        ev2, vals2 = win2.Read(timeout=100)
        if ev2 is None or ev2 == 'Exit':
            win2_active  = False
            win2.Close()
