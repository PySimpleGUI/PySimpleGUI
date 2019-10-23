import PySimpleGUI as sg

layout = [[sg.Text('What is your name?')],
          [sg.InputText()],
          [sg.Button('Ok')]]

window = sg.Window('Title of Window').Layout(layout)

event, values = window.Read()

sg.Popup('Hello {}'.format(values[0]))