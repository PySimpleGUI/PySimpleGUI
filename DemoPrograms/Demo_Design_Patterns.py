"""
When creating a new PySimpleGUI program from scratch, start here.
These are the accepted design patterns that cover the two primary use cases

1. A "One Shot" window
2. A persistent window that stays open after button clicks (uses an event loop)
3. A persistent window that need to perform update of an element before the window.read
"""
# ---------------------------------#
# DESIGN PATTERN 1 - Simple Window #
# ---------------------------------#
import PySimpleGUI as sg

sg.change_look_and_feel('Dark Blue 3')

layout = [[ sg.Text('My Oneshot') ],
          [ sg.Button('OK') ]]

window = sg.Window('My Oneshot', layout)
event, values = window.read()
window.close()


# -------------------------------------#
# DESIGN PATTERN 2 - Persistent Window #
# -------------------------------------#
import PySimpleGUI as sg

sg.change_look_and_feel('Dark Blue 3')

layout = [[ sg.Text('My layout', text_color='red') ],
          [ sg.Input(key='-INPUT-')],
          [ sg.Button('OK'), sg.Button('Cancel') ]]

window = sg.Window('Design Pattern 2 - Persistent Window', layout)

while True:     # Event Loop
    event, values = window.read()
    if event in (None, 'Cancel'):
        break
window.close()

# ------------------------------------------------------------------#
# DESIGN PATTERN 3 - Persistent Window with "early update" required #
# ------------------------------------------------------------------#
import PySimpleGUI as sg

sg.change_look_and_feel('Dark Blue 3')

layout = [[ sg.Text('My layout', key='-TEXT-KEY-') ],
          [ sg.Button('OK'), sg.Button('Cancel') ]]

window = sg.Window('Design Pattern 3', layout, finalize=True)

window['-TEXT-KEY-'].update('NEW Text')     # Change the text field. Finalize allows us to do this

while True:     # Event Loop
    event, values = window.read()
    if event in (None, 'Cancel'):
        break
window.close()
