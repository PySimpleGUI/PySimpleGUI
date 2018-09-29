#!/usr/bin/env python
import sys
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg

# Recipe for getting keys, one at a time as they are released
# If want to use the space bar, then be sure and disable the "default focus"

layout = [[sg.Text("Press a key or scroll mouse")],
          [sg.Text("", size=(18,1), key='text')],
          [sg.Button("OK", key='OK')]]

window = sg.Window("Keyboard Test", return_keyboard_events=True, use_default_focus=False).Layout(layout)

# ---===--- Loop taking in user input --- #
while True:
    button, value = window.Read()
    text_elem = window.FindElement('text')
    if button in ("OK", None):
        print(button, "exiting")
        break
    if len(button) == 1:
        text_elem.Update(value='%s - %s' % (button, ord(button)))
    if button is not None:
        text_elem.Update(button)


