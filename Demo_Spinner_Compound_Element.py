#!/usr/bin/env python
import sys
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg
"""
    Demo of how to combine elements into your own custom element
"""

sg.SetOptions(element_padding=(0,0))
# sg.ChangeLookAndFeel('Dark')
# --- Define our "Big-Button-Spinner" compound element. Has 2 buttons and an input field --- #
NewSpinner =  [sg.Button('-', size=(2,1), font='Any 12'),
               sg.In('0', size=(2,1), font='Any 14', justification='r', key='spin'),
               sg.Button('+', size=(2,1), font='Any 12')]
# --- Define Window --- #
layout = [
          [sg.Text('Spinner simulation')],
            NewSpinner,
            [sg.T('')],
          [sg.Ok()]
         ]

window = sg.Window('Spinner simulation').Layout(layout)

# --- Event Loop --- #
counter = 0
while True:
    event, values = window.Read()

    if event == 'Ok' or event is None:    # be nice to your user, always have an exit from your form
        break

    # --- do spinner stuff --- #
    counter += 1 if event == '+' else -1 if event == '-' else 0
    window.FindElement('spin').Update(counter)
