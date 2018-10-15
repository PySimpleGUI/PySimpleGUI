#choose one of these are your starting point.  Copy, paste, have fun

# ---------------------------------#
# DESIGN PATTERN 1 - Simple Window #
# ---------------------------------#
#!/usr/bin/env python
import sys
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg

layout = [[ sg.Text('My layout') ],
          [ sg.Button('Next Window')]]

window = sg.Window('My window').Layout(layout)
event, values = window.Read()


# -------------------------------------#
# DESIGN PATTERN 2 - Persistent Window #
# -------------------------------------#
#!/usr/bin/env python
import sys
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg

layout = [[ sg.Text('My layout') ],
          [ sg.RButton('Read The Window')]]

window = sg.Window('My new window').Layout(layout)

while True:     # Event Loop
    event, values = window.Read()
    if event is None:
        break
    print(event, values)