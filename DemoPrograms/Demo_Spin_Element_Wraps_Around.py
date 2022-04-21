#!/usr/bin/env python
import PySimpleGUI as sg

"""

    Demo Spin Element - Wraps around

    This is a nice touch for the Spin Element that is yet another jason990420 creation

    This Spin element will wrap around going in either direction. When getting to the end then
        it will go back to the beginning.

    Copyright 2022 PySimpleGUI
"""


lower, upper = 0, 10
data = [i for i in range(lower - 1, upper + 2)]

layout = [[sg.Text('This Spin element wraps around in both directions')],
          [sg.Spin(data, initial_value=lower, readonly=True, size=3, enable_events=True, key='-SPIN-')]]

window = sg.Window('Wrapping Spin Element', layout, font='_ 18', keep_on_top=True)

while True:

    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    # code to make the Spin do the wrap around. Do this prior to using the Spin's value in your code
    if event == '-SPIN-':
        value = values['-SPIN-']
        if value == lower - 1:
            window['-SPIN-'].update(value=upper)
            values['-SPIN-'] = upper        # Change the values dictionary too so it'll be correct if used
        elif value == upper + 1:
            window['-SPIN-'].update(value=lower)
            values['-SPIN-'] = lower        # Change the values dictionary too so it'll be correct if used

    sg.Print('Spin Value:', values['-SPIN-'], relative_location=(-400, 0))

window.close()