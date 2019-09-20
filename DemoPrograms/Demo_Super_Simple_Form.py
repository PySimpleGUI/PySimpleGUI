import PySimpleGUI as sg

layout =   [[sg.Text('Please enter your Name, Address, Phone')],
            [sg.Text('Name', size=(10,1)), sg.InputText(key='-NAME-')],
            [sg.Text('Address', size=(10,1)), sg.InputText(key='-ADDRESS-')],
            [sg.Text('Phone', size=(10,1)), sg.InputText(key='-PHONE-')],
            [sg.Button('Submit'), sg.Button('Cancel')]]

window = sg.Window('Simple Data Entry Window', layout)
event, values = window.read()
print(event, values['-NAME-'], values['-ADDRESS-'], values['-PHONE-'])
