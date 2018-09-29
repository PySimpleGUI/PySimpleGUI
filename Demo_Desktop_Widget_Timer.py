#!/usr/bin/env python
import sys
import sys
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg
import time

"""
 Timer Desktop Widget Creates a floating timer that is always on top of other windows You move it by grabbing anywhere on the window Good example of how to do a non-blocking, polling program using PySimpleGUI Can be used to poll hardware when running on a Pi     NOTE - you will get a warning message printed when you exit using exit button.
 It will look something like: invalid command name \"1616802625480StopMove\"
"""


# ----------------  Create Form  ----------------
sg.ChangeLookAndFeel('Black')
sg.SetOptions(element_padding=(0, 0))

layout = [[sg.Text('')],
         [sg.Text('', size=(8, 2), font=('Helvetica', 20), justification='center', key='text')],
         [sg.ReadButton('Pause', key='button', button_color=('white', '#001480')),
          sg.ReadButton('Reset', button_color=('white', '#007339'), key='Reset'),
          sg.Exit(button_color=('white', 'firebrick4'), key='Exit')]]

window = sg.Window('Running Timer', no_titlebar=False, auto_size_buttons=False, keep_on_top=True, grab_anywhere=True).Layout(layout)

# ----------------  main loop  ----------------
current_time = 0
paused = False
start_time = int(round(time.time() * 100))
while (True):
    # --------- Read and update window --------
    if not paused:
        button, values = window.ReadNonBlocking()
        current_time = int(round(time.time() * 100)) - start_time
    else:
        button, values = window.Read()
    if button == 'button':
        button = window.FindElement(button).GetText()
    # --------- Do Button Operations --------
    if values is None or button == 'Exit':
        break
    if button is 'Reset':
        start_time = int(round(time.time() * 100))
        current_time = 0
        paused_time = start_time
    elif button == 'Pause':
        paused = True
        paused_time = int(round(time.time() * 100))
        element = window.FindElement('button')
        element.Update(text='Run')
    elif button == 'Run':
        paused = False
        start_time = start_time + int(round(time.time() * 100)) - paused_time
        element = window.FindElement('button')
        element.Update(text='Pause')

    # --------- Display timer in window --------
    window.FindElement('text').Update('{:02d}:{:02d}.{:02d}'.format((current_time // 100) // 60,
                                                                  (current_time // 100) % 60,
                                                                  current_time % 100))
    time.sleep(.01)

# --------- After loop --------

# Broke out of main loop. Close the window.
window.CloseNonBlocking()
