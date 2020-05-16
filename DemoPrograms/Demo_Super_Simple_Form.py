import PySimpleGUI as sg

"""
    Simple Form (a one-shot data entry window)
    Use this design pattern to show a form one time to a user that is "submitted"
"""

layout = [[sg.Text('Please enter your Name, Address, Phone')],
          [sg.Text('Name', size=(10, 1)), sg.InputText(key='-NAME-')],
          [sg.Text('Address', size=(10, 1)), sg.InputText(key='-ADDRESS-')],
          [sg.Text('Phone', size=(10, 1)), sg.InputText(key='-PHONE-')],
          [sg.Button('Submit'), sg.Button('Cancel')]]

window = sg.Window('Simple Data Entry Window', layout)
event, values = window.read(close=True)

if event == 'Submit':
    print('The events was ', event, 'You input', values['-NAME-'], values['-ADDRESS-'], values['-PHONE-'])
else:
    print('User cancelled')
