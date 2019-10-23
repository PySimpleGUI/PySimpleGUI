import PySimpleGUI as sg
import psutil

# Usage of PSG and cpu data

layout = [[sg.Text('CPU Utilization')],
          [sg.Text('', size=(8, 2), font='Helvetica 20',
                justification='center', key='-text-')],
          [sg.Exit()]]

window = sg.Window('CPU Meter', layout)

while True:
    event, values = window.ReadNonBlocking()

    if event == 'Exit' or values is None:
        break

    cpu_percent = psutil.cpu_percent(interval=1)

    window['-text-'].update(f'CPU {cpu_percent:02.0f}%')

window.close()
