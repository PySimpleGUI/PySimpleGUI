#!/usr/bin/env python
import sys
if sys.version_info[0] < 3:
    import PySimpleGUI27 as sg
else:
    import PySimpleGUI as sg

layout = [[sg.Text("Hold down a key")],
          [sg.Button("OK")]]

window = sg.Window("Realtime Keyboard Test", return_keyboard_events=True, use_default_focus=False).Layout(layout)

while True:
    button, value = window.ReadNonBlocking()

    if button == "OK":
        print(button, value, "exiting")
        break
    if button is not None:
        if len(button) == 1:
            print('%s - %s'%(button, ord(button)))
        else:
            print(button)
    elif value is None:
        break
