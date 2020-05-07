#!/usr/bin/env python
import PySimpleGUI as sg

layout = [[sg.Text("Hold down a key")],
          [sg.Button("OK")]]

window = sg.Window("Realtime Keyboard Test", layout, return_keyboard_events=True,
                   use_default_focus=False)

while True:
    event, values = window.read(timeout=0)

    if event == "OK":
        print(event, values, "exiting")
        break
    if event is not sg.TIMEOUT_KEY:
        if len(event) == 1:
            print('%s - %s' % (event, ord(event)))
        else:
            print(event)
    elif event == sg.WIN_CLOSED:
        break

window.close()
