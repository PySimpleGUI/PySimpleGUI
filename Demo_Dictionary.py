import PySimpleGUI as sg

# THIS FILE REQIRES THE LATEST PySimpleGUI.py FILE
# IT WILL NOT WORK WITH CURRENT PIP RELEASE (2.7)

# Shows how to use return values in dictionary form

form = sg.FlexForm('Simple data entry form', use_dictionary=True)  # begin with a blank form

layout = [
          [sg.Text('Please enter your Name, Address, Phone')],
          [sg.Text('Name', size=(15, 1)), sg.InputText('1', key='name')],
          [sg.Text('Address', size=(15, 1)), sg.InputText('2', key='address')],
          [sg.Text('Phone', size=(15, 1)), sg.InputText('3', key='phone')],
          [sg.Submit(), sg.Cancel()]
         ]

button, values = form.LayoutAndRead(layout)

sg.MsgBox(button, values, values['name'], values['address'], values['phone'])

print(values)
