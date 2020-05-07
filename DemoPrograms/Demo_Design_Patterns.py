"""
When creating a new PySimpleGUI program from scratch, start here.
These are the accepted design patterns that cover the two primary use cases

1. A "One Shot" window
2. A "One Shot" window in 1 line of code
3. A persistent window that stays open after button clicks (uses an event loop)
4. A persistent window that need to perform update of an element before the window.read
"""
# -----------------------------------#
# DESIGN PATTERN 1 - One-shot Window #
# -----------------------------------#
import PySimpleGUI as sg

layout = [[ sg.Text('My Oneshot') ],
          [ sg.Input(key='-IN-') ],
          [ sg.Button('OK') ]]

window = sg.Window('Design Pattern 1', layout)
event, values = window.read()
window.close()


# ---------------------------------------------#
# DESIGN PATTERN 2 - One-shot Window in 1 line #
# ---------------------------------------------#
import PySimpleGUI as sg

event, values = sg.Window('Design Pattern 2', [[sg.Text('My Oneshot')],[sg.Input(key='-IN-')], [ sg.Button('OK') ]]).read(close=True)



# -------------------------------------#
# DESIGN PATTERN 3 - Persistent Window #
# -------------------------------------#
import PySimpleGUI as sg

layout = [[sg.Text('My layout')],
          [sg.Input(key='-INPUT-')],
          [sg.Button('OK'), sg.Button('Cancel')] ]

window = sg.Window('Design Pattern 3 - Persistent Window', layout)

while True:     # Event Loop
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
window.close()

# ------------------------------------------------------------------#
# DESIGN PATTERN 4 - Persistent Window with "early update" required #
# ------------------------------------------------------------------#
import PySimpleGUI as sg

layout = [[ sg.Text('My layout') ],
          [sg.Input(key='-INPUT-')],
          [sg.Text('Some text will be output here', key='-TEXT-KEY-')],
          [ sg.Button('OK'), sg.Button('Cancel') ]]

window = sg.Window('Design Pattern 4', layout, finalize=True)

# Change the text field. Finalize allows us to do this
window['-TEXT-KEY-'].update('Modified before event loop')

while True:     # Event Loop
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    if event == 'OK':
        window['-TEXT-KEY-'].update(values['-INPUT-'])
window.close()
