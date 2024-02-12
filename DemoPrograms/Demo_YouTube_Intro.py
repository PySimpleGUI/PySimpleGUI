import PySimpleGUI as sg

"""
    Copyright 2023 PySimpleSoft, Inc. and/or its licensors. All rights reserved.

    Redistribution, modification, or any other use of PySimpleGUI or any portion thereof is subject to the terms of the PySimpleGUI License Agreement available at https://eula.pysimplegui.com.

    You may not redistribute, modify or otherwise use PySimpleGUI or its contents except pursuant to the PySimpleGUI License Agreement.
"""

layout = [[sg.Text('What is your name?')],
          [sg.InputText()],
          [sg.Button('Ok')]]

window = sg.Window('Title of Window', layout)
event, values = window.read()
window.close()

sg.popup('Hello {}'.format(values[0]))