#choose one of these are your starting point

# ---------------------------------#
# DESIGN PATTERN 1 - Simple Window #
# ---------------------------------#
#!/usr/bin/env python
import sys
if sys.version_info[0] < 3:
    import PySimpleGUI27 as sg
else:
    import PySimpleGUI as sg

layout = [[ sg.Text('My layout') ]]

window = sg.Window('My window').Layout(layout)
button, value = window.Read()


# -------------------------------------#
# DESIGN PATTERN 2 - Persistent Window #
# -------------------------------------#
#!/usr/bin/env python
import sys
if sys.version_info[0] < 3:
    import PySimpleGUI27 as sg
else:
    import PySimpleGUI as sg

layout = [[ sg.Text('My layout') ]]

window = sg.Window('My new window').Layout(layout)

while True:     # Event Loop
    button, value = window.Read()
    if button is None:
        break