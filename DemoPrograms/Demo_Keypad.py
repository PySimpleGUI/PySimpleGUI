#!/usr/bin/env python
import PySimpleGUI as sg


# Demonstrates a number of PySimpleGUI features including:
#   Default element size
#   auto_size_buttons
#   Button
#   Dictionary return values
#   update of elements in form (Text, Input)


layout = [[sg.Text('Enter Your Passcode')],
          [sg.Input('', size=(10, 1), key='input')],
          [sg.Button('1'), sg.Button('2'), sg.Button('3')],
          [sg.Button('4'), sg.Button('5'), sg.Button('6')],
          [sg.Button('7'), sg.Button('8'), sg.Button('9')],
          [sg.Button('Submit'), sg.Button('0'), sg.Button('Clear')],
          [sg.Text('', size=(15, 1), font=('Helvetica', 18),
                text_color='red', key='out')],
          ]

window = sg.Window('Keypad', layout,
                   default_button_element_size=(5, 2),
                   auto_size_buttons=False,
                   grab_anywhere=False)

# Loop forever reading the form's values, updating the Input field
keys_entered = ''
while True:
    event, values = window.read()  # read the form
    if event == sg.WIN_CLOSED:  # if the X button clicked, just exit
        break
    if event == 'Clear':  # clear keys if clear button
        keys_entered = ''
    elif event in '1234567890':
        keys_entered = values['input']  # get what's been entered so far
        keys_entered += event  # add the new digit
    elif event == 'Submit':
        keys_entered = values['input']
        window['out'].update(keys_entered)  # output the final string

    # change the form to reflect current key string
    window['input'].update(keys_entered)
window.close()
