import PySimpleGUI as sg

"""
    Copyright 2018-2026 PySimpleGUI. All rights reserved.


"""

layout = [[sg.Text('What is your name?')],
          [sg.InputText()],
          [sg.Button('Ok')]]

window = sg.Window('Title of Window', layout)
event, values = window.read()
window.close()

sg.popup('Hello {}'.format(values[0]))