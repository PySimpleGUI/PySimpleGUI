import PySimpleGUI as sg

form = sg.FlexForm('Simple data entry form')  # begin with a blank form

layout = [[sg.Text('Please enter your Name, Address, Phone')],
          [sg.Text('Name', size=(15, 1)), sg.InputText()],
          [sg.Text('Address', size=(15, 1)), sg.InputText()],
          [sg.Text('Phone', size=(15, 1)), sg.InputText()],
          [sg.Submit(), sg.Cancel()]]

button, (name, address, phone) = form.LayoutAndRead(layout)

print(name, address, phone)