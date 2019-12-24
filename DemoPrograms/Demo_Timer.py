import PySimpleGUI as sg
import time

# Basic timer in PSG

def Timer():
    sg.theme('Dark')
    sg.set_options(element_padding=(0, 0))
    form_rows = [[sg.Text(size=(8, 2), font=('Helvetica', 20),
                       justification='center', key='text')],
                 [sg.Button('Pause', key='-RUN-PAUSE-'),
                 sg.Button('Reset'),
                 sg.Exit(button_color=('white', 'firebrick4'))]]
    window = sg.Window('Running Timer', form_rows,
                       no_titlebar=True, auto_size_buttons=False)
    i = 0
    paused = False
    start_time = int(round(time.time() * 100))

    while True:
        # This is the code that reads and updates your window
        button, values = window.read(timeout=0)
        window['text'].update('{:02d}:{:02d}.{:02d}'.format(
            (i // 100) // 60, (i // 100) % 60, i % 100))

        if values is None or button == 'Exit':
            break

        if button == 'Reset':
            i = 0

        elif button == '-RUN-PAUSE-':
            paused = not paused
            window['-RUN-PAUSE-'].update('Run' if paused else 'Pause')

        if not paused:
            i += 1

    window.close()

Timer()
