import PySimpleGUI as sg

layout = [[sg.Text('What is your name?')],
          [sg.InputText()],
          [sg.Button('Ok')]]

window = sg.Window('Title of Window').Layout(layout)

button, values = window.Read()

sg.Popup('Hello {}'.format(values[0]))