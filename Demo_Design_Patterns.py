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
import sys
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg

layout = [[ sg.Text('My layout') ]]

window = sg.Window('My window').Layout(layout)
event, values = window.Read()


# -------------------------------------#
# DESIGN PATTERN 2 - Persistent Window #
# -------------------------------------#
import sys
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg

layout = [[ sg.Text('My layout') ]]

window = sg.Window('My new window').Layout(layout)

while True:     # Event Loop
    event, values = window.Read()
    if event is None:
        break

# ------------------------------------------------------------------#
# DESIGN PATTERN 3 - Persistent Window with "early update" required #
# ------------------------------------------------------------------#
import sys
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg

layout = [[ sg.Text('My layout') ]]

window = sg.Window('My new window').Layout(layout).Finalize()

# if you have operations on elements that must take place before the event loop, do them here

while True:     # Event Loop
    event, values = window.Read()
    if event is None:
        break