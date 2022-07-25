import PySimpleGUI as sg

"""
    Read all windows example
    The input elements are shown as output on the other window when "Go" is pressed
    The checkboxes on window 1 are mirrored on window 2 if "mirror" checkbox is set
    
    Copyright 2022 PySimpleGUI
"""
layout1 = [  [sg.Text('My Window')],
            [sg.Input(k='-IN-'), sg.Text(k='-OUT-')],
             [sg.CB('Check 1', k='-CB1-', enable_events=True), sg.CB('Check 2', k='-CB2-', enable_events=True), sg.CB('Mirror on Window 2', enable_events=True, k='-CB3-')],
            [sg.Button('Go'), sg.Button('Exit')]  ]

window1 = sg.Window('Window 1 Title', layout1, finalize=True, grab_anywhere=True, relative_location=(-600, 0))

layout2 = [  [sg.Text('My Window')],
            [sg.Input(k='-IN-'), sg.Text(k='-OUT-')],
             [sg.CB('Check 1', k='-CB1-'), sg.CB('Check 2', k='-CB2-')],
             [sg.Button('Go'),  sg.Button('Exit')]  ]

window2 = sg.Window('Window 2 Title', layout2, finalize=True,  grab_anywhere=True)

while True:             # Event Loop
    window, event, values = sg.read_all_windows()
    if window is None:
        print('exiting because no windows are left')
        break
    print(window.Title, event, values) if window is not None else None
    if event == sg.WIN_CLOSED or event == 'Exit':
        window.close()
    if event == 'Go':
        # Output the input element to the other windwow
        try:        # try to update the other window
            if window == window1:
                window2['-OUT-'].update(values['-IN-'])
            else:
                window1['-OUT-'].update(values['-IN-'])
        except:
            pass
    try:
        if window == window1 and values['-CB3-']:
            window2['-CB1-'].update(values['-CB1-'])
            window2['-CB2-'].update(values['-CB2-'])
    except:
        pass
