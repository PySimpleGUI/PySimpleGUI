#!/usr/bin/env python
import PySimpleGUIWeb as sg
import time

# ----------------  Create Form  ----------------
layout = [
    [sg.Text('', background_color='black')],
    [sg.Text('00:00', size=(30, 1), font=('Helvetica', 30), justification='center',
          text_color='white', key='text', background_color='black')],
    [sg.Text('', background_color='black')],
    [sg.Button('Pause', key='button', button_color=('white', '#001480')),
     sg.Button('Reset', button_color=('white', '#007339'), key='Reset'),
     sg.Exit(button_color=('white', '#8B1A1A'), key='Exit', )],
]

window = sg.Window('Running Timer', layout,
            background_color='black', font='Helvetica 18')

# ----------------  main loop  ----------------
current_time = 0
paused = False
start_time = int(round(time.time() * 100))
while True:
    # --------- read and update window --------
    if not paused:
        event, values = window.read(timeout=0)
        current_time = int(round(time.time() * 100)) - start_time
    else:
        event, values = window.read()
    print(event, values) if event != sg.TIMEOUT_KEY else None

    if event == 'button':
        event = window[event].GetText()
    # --------- Do Button Operations --------
    
    if event in (None, 'Exit'):        # ALWAYS give a way out of program
        break
    
    if event == 'Reset':
        start_time = int(round(time.time() * 100))
        current_time = 0
        paused_time = start_time
    
    elif event == 'Pause':
        paused = True
        paused_time = int(round(time.time() * 100))
        element = window['button']
        element.update(text='Run')
    
    elif event == 'Run':
        paused = False
        start_time = start_time + int(round(time.time() * 100)) - paused_time
        element = window['button']
        element.update(text='Pause')

    # --------- Display timer in window --------
    window['text'].update('{:02d}:{:02d}.{:02d}'.format((current_time // 100) // 60,
                                                                    (current_time //
                                                                     100) % 60,
                                                                    current_time % 100))
# --------- After loop --------
window.close()
