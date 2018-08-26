import PySimpleGUI as g

# g.SetOptions(button_color=g.COLOR_SYSTEM_DEFAULT)   # because some people like gray buttons

# create the 2 Elements we want to control outside the form
out_elem = g.Text('', size=(15, 1), font=('Helvetica', 18), text_color='red')
in_elem = g.Input(size=(10,1), do_not_clear=True, key='input')

layout = [[g.Text('Choose Test'), g.DropDown(values=['Input', 'Output', 'Some option']), g.ReadFormButton('Input Option', size=(10,1))],
          [in_elem],
          [g.ReadFormButton('1', size=(5,2)), g.ReadFormButton('2', size=(5,2)), g.ReadFormButton('3', size=(5,2))],
          [g.ReadFormButton('4', size=(5,2)), g.ReadFormButton('5', size=(5,2)), g.ReadFormButton('6', size=(5,2))],
          [g.ReadFormButton('7', size=(5,2)), g.ReadFormButton('8', size=(5,2)), g.ReadFormButton('9', size=(5,2))],
          [g.ReadFormButton('Submit', size=(5,2)),g.ReadFormButton('0', size=(5,2)), g.ReadFormButton('Clear', size=(5,2))],
          [out_elem],
          ]

form = g.FlexForm('Keypad', auto_size_buttons=False)
form.Layout(layout)

keys_entered = ''
while True:
    button, values = form.Read()                # read the form
    if button is None:                          # if the X button clicked, just exit
        break
    if button == 'Clear':                       # clear keys if clear button
        keys_entered = ''
    elif button in '1234567890':
        keys_entered = values['input']            # get what's been entered so far
        keys_entered += button                  # add the new digit
    elif button == 'Submit':
        keys_entered = in_elem.Get()
        out_elem.Update(keys_entered)           # output the final string

    in_elem.Update(keys_entered)                # change the form to reflect current key string

