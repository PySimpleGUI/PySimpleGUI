import PySimpleGUI as sg

# Very basic form.  Return values as a dictionary
form = sg.FlexForm('Simple data entry form')  # begin with a blank form

layout = [
          [sg.Text('Please enter your Name, Address, Phone')],
          [sg.Text('Name', size=(15, 1)), sg.InputText('name', key='name')],
          [sg.Text('Address', size=(15, 1)), sg.InputText('address', key='address')],
          [sg.Text('Phone', size=(15, 1)), sg.InputText('phone', key='phone')],
          [sg.Ok(), sg.Cancel()]
         ]

button, values = form.LayoutAndRead(layout)

print(button, values, values['name'], values['address'], values['phone'])

form = sg.FlexForm('Simple data entry form')  # begin with a blank form

layout = [
          [sg.Text('Please enter your Name, Address, Phone')],
          [sg.Text('Name', size=(15, 1)), sg.InputText('name')],
          [sg.Text('Address', size=(15, 1)), sg.InputText('address')],
          [sg.Text('Phone', size=(15, 1)), sg.InputText('phone')],
          [sg.Ok(), sg.Cancel()]
         ]

button, values = form.LayoutAndRead(layout)
print(values)
name, address, phone = values
sg.MsgBox(button, values[0], values[1], values[2])