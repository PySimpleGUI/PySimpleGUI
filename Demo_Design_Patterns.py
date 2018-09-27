"""
When creating a new PySimpleGUI program from scratch, start here.
These are the accepted design patterns that cover the two primary use cases

1. A window that closes when a "submit" type button is clicked
2. A persistent window that stays open after button clicks (uses an event loop)
3. A persistent window that needs access to the elements' interface variables
"""
# ---------------------------------#
# DESIGN PATTERN 1 - Simple Window #
# ---------------------------------#
import PySimpleGUI as sg

layout = [[ sg.Text('My layout') ]]

window = sg.Window('My window').Layout(layout)
button, value = window.Read()


# -------------------------------------#
# DESIGN PATTERN 2 - Persistent Window #
# -------------------------------------#
import PySimpleGUI as sg

layout = [[ sg.Text('My layout') ]]

window = sg.Window('My new window').Layout(layout)

while True:     # Event Loop
    button, value = window.Read()
    if button is None:
        break

# ------------------------------------------------------------------#
# DESIGN PATTERN 3 - Persistent Window with "early update" required #
# ------------------------------------------------------------------#
import PySimpleGUI as sg

layout = [[ sg.Text('My layout') ]]

window = sg.Window('My new window').Layout(layout).Finalize()

while True:     # Event Loop
    button, value = window.Read()
    if button is None:
        break