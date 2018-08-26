import PySimpleGUI as g

# g.SetOptions(button_color=g.COLOR_SYSTEM_DEFAULT)   # because some people like gray buttons

# Demonstrates a number of PySimpleGUI features including:
#   Default element size
#   auto_size_buttons
#   ReadFormButton
#   Dictionary return values
#   Update of elements in form (Text, Input)
#   do_not_clear of Input elements


# create the 2 Elements we want to control outside the form
out_elem = g.Text('', size=(15, 1), font=('Helvetica', 18), text_color='red')
in_elem = g.Input(size=(10,1), do_not_clear=True, key='input')

layout = [[g.Text('Choose Test'), g.DropDown(values=['Input', 'Output', 'Some option']), g.ReadFormButton('Input Option', auto_size_button=True)],
          [in_elem],
          [g.ReadFormButton('1'), g.ReadFormButton('2'), g.ReadFormButton('3')],
          [g.ReadFormButton('4'), g.ReadFormButton('5'), g.ReadFormButton('6')],
          [g.ReadFormButton('7'), g.ReadFormButton('8'), g.ReadFormButton('9')],
          [g.ReadFormButton('Submit'),g.ReadFormButton('0'), g.ReadFormButton('Clear')],
          [out_elem],
          ]

form = g.FlexForm('Keypad', default_element_size=(5,2), auto_size_buttons=False)
form.Layout(layout)

# Loop forever reading the form's values, updating the Input field
keys_entered = ''
while True:
    button, values = form.Read()                # read the form
    if button is None:                          # if the X button clicked, just exit
        break
    if button == 'Clear':                       # clear keys if clear button
        keys_entered = ''
    elif button in '1234567890':
        keys_entered = values['input']          # get what's been entered so far
        keys_entered += button                  # add the new digit
    elif button == 'Submit':
        keys_entered = values['input']
        out_elem.Update(keys_entered)           # output the final string

    in_elem.Update(keys_entered)                # change the form to reflect current key string

