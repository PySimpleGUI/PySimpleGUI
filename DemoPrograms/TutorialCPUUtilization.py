import PySimpleGUI as sg
import psutil

layout = [ [sg.Text('CPU Utilization')] ,
           [sg.Text('', size=(8,2), font='Helvetica 20', justification='center', key='_text_')],
           [sg.Exit()]]

window = sg.Window('CPU Meter').Layout(layout)

while True:
    button, values = window.ReadNonBlocking()

    if button == 'Exit' or values is None:
        break

    cpu_percent = psutil.cpu_percent(interval=1)

    window.FindElement('_text_').Update(f'CPU {cpu_percent:02.0f}%')
