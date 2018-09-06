import PySimpleGUI as sg

# g.SetOptions(button_color=g.COLOR_SYSTEM_DEFAULT)   # because some people like gray buttons

# Demonstrates a number of PySimpleGUI features including:
#   Default element size
#   auto_size_buttons
#   ReadFormButton
#   Dictionary return values
#   Update of elements in form (Text, Input)
#   do_not_clear of Input elements


# create the 2 Elements we want to control outside the form

layout = [[sg.Text('Enter Your Passcode')],
          [sg.Input(size=(10, 1), do_not_clear=True, key='input')],
          [sg.ReadFormButton('1'), sg.ReadFormButton('2'), sg.ReadFormButton('3')],
          [sg.ReadFormButton('4'), sg.ReadFormButton('5'), sg.ReadFormButton('6')],
          [sg.ReadFormButton('7'), sg.ReadFormButton('8'), sg.ReadFormButton('9')],
          [sg.ReadFormButton('Submit'), sg.ReadFormButton('0'), sg.ReadFormButton('Clear')],
          [sg.Text('', size=(15, 1), font=('Helvetica', 18), text_color='red', key='out')],
          ]

form = sg.FlexForm('Keypad', default_button_element_size=(5, 2), auto_size_buttons=False)
form.Layout(layout)

# Loop forever reading the form's values, updating the Input field
keys_entered = ''
while True:
    button, values = form.Read()  # read the form
    if button is None:  # if the X button clicked, just exit
        break
    if button is 'Clear':  # clear keys if clear button
        keys_entered = ''
    elif button in '1234567890':
        keys_entered = values['input']  # get what's been entered so far
        keys_entered += button  # add the new digit
    elif button is 'Submit':
        keys_entered = values['input']
        form.FindElement('out').Update(keys_entered)  # output the final string

    form.FindElement('input').Update(keys_entered)  # change the form to reflect current key string