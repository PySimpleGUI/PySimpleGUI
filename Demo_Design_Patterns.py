# DESIGN PATTERN 1 - Simple Window
import PySimpleGUI as sg

layout = [[ sg.Text('My layout') ]]

window = sg.Window('My window').Layout(layout)
button, value = window.Read()

# DESIGN PATTERN 2 - Persistent Window
import PySimpleGUI as sg

layout = [[ sg.Text('My layout') ]]

window = sg.Window('My new window').Layout(layout)

while True:     # Event Loop
    button, value = window.Read()
    if button is None:
        break

# DESIGN PATTERN 3 - Persistent Window with "early update" required
import PySimpleGUI as sg

layout = [[ sg.Text('My layout') ]]

window = sg.Window('My new window').Layout(layout).Finalize()

while True:     # Event Loop
    button, value = window.Read()
    if button is None:
        break