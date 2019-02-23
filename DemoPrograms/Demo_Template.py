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
          [ sg.CloseButton('Next Window')]]

window = sg.Window('My window').Layout(layout)
event, values = window.Read()


# --------------------------------------------------#
# DESIGN PATTERN 2 - Persistent Window (stays open) #
# --------------------------------------------------#
#!/usr/bin/env python
import sys
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg

layout = [[ sg.Text('My Window') ],
          [ sg.Button('Read The Window')]]

window = sg.Window('My Window Title').Layout(layout)

while True:                         # Event Loop
    event, values = window.Read()
    if event is None:               # if window closed with X
        break
    print(event, values)