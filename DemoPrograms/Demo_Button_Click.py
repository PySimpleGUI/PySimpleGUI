import PySimpleGUI as sg
from random import randint

sg.theme('Dark Blue 3')

layout = [  [sg.Text('Temperature'), sg.T(' '*30), sg.Text(size=(8,1), key='-TEMP OUT-')],
            [sg.Text('Set Temp'), sg.T(' '*8), sg.Input(size=(8,1), key='-IN-'), sg.T(' '*10), sg.Button('Set')],
            [sg.Button('Off'), sg.T(' '*13), sg.Button('Turn relay on', button_color=('white', 'red')),sg.T(' '*5), sg.Button('Quit')]  ]

window = sg.Window('Temperature Manager', layout, font='Default -24', return_keyboard_events=True, no_titlebar=True)

while True:             # Event Loop
    event, values = window.read(timeout=500)    # returns every 500 ms
    print(event, values) if event != sg.TIMEOUT_KEY else None       # a debug print
    if event in (None, 'Quit'):
        break
    if event == 'Set':
        print('setting temperature to ', values['-IN-'])
        window['-TEMP OUT-'].update(values['-IN-'] + ' C')
    elif event.startswith('Turn'):
        print('Turning on the relay')
    elif event == 'Off':
        print('Turning off sensor')
    elif event.startswith('F11'):
        window.maximize()
    elif event.startswith('Escape'):
        window.normal()

    window['-TEMP OUT-'].update(str(randint(2,70)) + ' C')

window.close()
