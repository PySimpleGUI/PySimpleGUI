#!/usr/bin/env python
import PySimpleGUI as sg

"""
    Demo of how to combine elements into your own custom element
"""

sg.set_options(element_padding=(0, 0))
# --- Define the Compound Element. Has 2 buttons and an input field --- #
NewSpinner = [sg.Input('0', size=(3, 1), font='Any 12', justification='r', key='-SPIN-'),
             sg.Column([[sg.Button('▲', size=(1, 1), font='Any 7', border_width=0, button_color=(sg.theme_text_color(), sg.theme_background_color()), key='-UP-')],
            [sg.Button('▼', size=(1, 1), font='Any 7', border_width=0, button_color=(sg.theme_text_color(), sg.theme_background_color()), key='-DOWN-')]])]
# --- Define Window --- #
layout = [[sg.Text('Spinner simulation')],
            NewSpinner,
            [sg.Text('')],
            [sg.Ok()]]

window = sg.Window('Spinner simulation', layout, use_default_focus=False)

# --- Event Loop --- #
while True:
    event, values = window.read()

    if event == 'Ok' or event == sg.WIN_CLOSED:    # be nice to your user, always have an exit from your form
        break
    counter = int(values['-SPIN-'])
    # --- do spinner stuff --- #
    counter += 1 if event == '-UP-' else -1 if event == '-DOWN-' else 0
    window['-SPIN-'].update(counter)
window.close()
