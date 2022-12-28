import PySimpleGUI as sg

"""
    Demo Program - Window Timers

    Uses the PySimpleGUI Window Timers to generate single or periodic timer events.
    Requires version 4.60.4.133 or greater of PySimpleGUI.

    Copyright 2022 PySimpleGUI
"""


def main():
    layout = [  [sg.Text('Demonatrataion of Window Timers', font='_ 15')],
                [sg.T('Timer duration in ms:'), sg.Input(1000, key='-DURATION-', s=4), sg.Checkbox('Repeats', True, key='-REPEATS-'), sg.Button('Start')],
                [sg.T('Timer ID to stop:'), sg.Input(key='-STOP-', s=4), sg.Button('Stop'), sg.B('Stop All'), sg.B('List Active')],
                [sg.Output(size=(90, 10))],
                [sg.Button('Does nothing'), sg.Button('Exit')]  ]

    window = sg.Window('Window Title', layout)

    while True:
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == 'Start':
            try:
                duration = int(values['-DURATION-'])
            except:
                continue
            window.timer_start(duration, repeating=values['-REPEATS-'])
        elif event == 'Stop':
            try:
                id = int(values['-STOP-'])
            except:
                continue
            window.timer_stop(id)
        elif event == 'Stop All':
            window.timer_stop_all()
        elif event == 'List Active':
            sg.cprint('Active Timers:', end='', c='white on red')
            sg.cprint(window.timer_get_active_timers(), c='white on green')
    window.close()

if __name__ == '__main__':
    main()

