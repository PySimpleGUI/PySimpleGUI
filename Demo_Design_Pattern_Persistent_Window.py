# -------------------------------------#
# DESIGN PATTERN 2 - Persistent Window #
# Update a text field based on input   #
# -------------------------------------#
import sys
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg

layout = [[sg.Text('Your typed chars appear here:'), sg.Text('', key='_OUTPUT_') ],
          [sg.Input(key='_IN_')],
          [sg.Button('Show'), sg.Button('Exit')],
          ]

window = sg.Window('My new window').Layout(layout)

while True:                 # Event Loop
    event, values = window.Read()
    if event is None or event == 'Exit':
        break
    if event == 'Show':     # change the text "output" element to be the value of "input" element
        window.FindElement('_OUTPUT_').Update(values['_IN_'])
