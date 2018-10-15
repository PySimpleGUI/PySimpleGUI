#!/usr/bin/env python
import sys
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg

# Demonstrates a number of PySimpleGUI features including:
#   Default element size
#   auto_size_buttons
#   ReadButton
#   Dictionary return values
#   Update of elements in form (Text, Input)
#   do_not_clear of Input elements



layout = [[sg.Text('Enter Your Passcode')],
          [sg.Input(size=(10, 1), do_not_clear=True, key='input')],
          [sg.ReadButton('1'), sg.ReadButton('2'), sg.ReadButton('3')],
          [sg.ReadButton('4'), sg.ReadButton('5'), sg.ReadButton('6')],
          [sg.ReadButton('7'), sg.ReadButton('8'), sg.ReadButton('9')],
          [sg.ReadButton('Submit'), sg.ReadButton('0'), sg.ReadButton('Clear')],
          [sg.Text('', size=(15, 1), font=('Helvetica', 18), text_color='red', key='out')],
          ]

window = sg.Window('Keypad', default_button_element_size=(5, 2), auto_size_buttons=False, grab_anywhere=False).Layout(layout)

# Loop forever reading the form's values, updating the Input field
keys_entered = ''
while True:
    event, values = window.Read()  # read the form
    if event is None:  # if the X button clicked, just exit
        break
    if event == 'Clear':  # clear keys if clear button
        keys_entered = ''
    elif event in '1234567890':
        keys_entered = values['input']  # get what's been entered so far
        keys_entered += event  # add the new digit
    elif event == 'Submit':
        keys_entered = values['input']
        window.FindElement('out').Update(keys_entered)  # output the final string

    window.FindElement('input').Update(keys_entered)  # change the form to reflect current key string