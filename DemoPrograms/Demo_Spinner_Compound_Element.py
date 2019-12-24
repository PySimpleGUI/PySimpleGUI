#!/usr/bin/env python
import PySimpleGUI as sg

"""
    Demo of how to combine elements into your own custom element
"""

sg.set_options(element_padding=(0, 0))
# sg.theme('Dark')
# --- Define our "Big-Button-Spinner" compound element. Has 2 buttons and an input field --- #
NewSpinner = [sg.Button('-', size=(2, 1), font='Any 12'),
              sg.Input('0', size=(2, 1), font='Any 14',
                   justification='r', key='spin'),
              sg.Button('+', size=(2, 1), font='Any 12')]
# --- Define Window --- #
layout = [
    [sg.Text('Spinner simulation')],
    NewSpinner,
    [sg.Text('')],
    [sg.Ok()]
]

window = sg.Window('Spinner simulation', layout)


# --- Event Loop --- #
counter = 0
while True:
    event, values = window.read()

    if event == 'Ok' or event is None:    # be nice to your user, always have an exit from your form
        break

    # --- do spinner stuff --- #
    counter += 1 if event == '+' else -1 if event == '-' else 0
    window['spin'].update(counter)

window.close()
