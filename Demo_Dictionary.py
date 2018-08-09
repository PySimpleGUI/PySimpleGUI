import PySimpleGUI as sg

# THIS FILE REQIRES THE LATEST PySimpleGUI.py FILE
# IT WILL NOT WORK WITH CURRENT PIP RELEASE (2.7)
#
# If you want to use the return values as Dictionary feature, you need to download the PySimpleGUI.py file
# from GitHub and then place it in your project's folder.  This SHOULD cause it to use this downloaded version
# instead of the pip installed one, if you've pip installed it.  You can always uninstall the pip one :-)


# This design pattern shows how to use return values in dictionary form

form = sg.FlexForm('Simple data entry form')  # begin with a blank form

layout = [
          [sg.Text('Please enter your Name, Address, Phone')],
          [sg.Text('Name', size=(15, 1)), sg.InputText('1')],
          [sg.Text('Address', size=(15, 1)), sg.InputText('2', key='address')],
          [sg.Text('Phone', size=(15, 1)), sg.InputText('3', key='phone')],
          [sg.Submit(), sg.Cancel()]
         ]

button, values = form.LayoutAndRead(layout)

sg.MsgBox(button, values, values[0], values['address'], values['phone'])

print(values)
