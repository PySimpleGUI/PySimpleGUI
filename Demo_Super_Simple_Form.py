import PySimpleGUI as sg

form = sg.FlexForm('Simple data entry form')  # begin with a blank form

layout = [
          [sg.Text('Please enter your Name, Address, Phone')],
          [sg.Text('Name', size=(15, 1)), sg.InputText('1', key='name')],
          [sg.Text('Address', size=(15, 1)), sg.InputText('2', key='address')],
          [sg.Text('Phone', size=(15, 1)), sg.InputText('3', key='phone')],
          [sg.Submit(), sg.Cancel()]
         ]

button, values = form.LayoutAndRead(layout)

sg.MsgBox(button, values['name'], values['address'], values['phone'])

print(values)
