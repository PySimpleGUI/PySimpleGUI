import PySimpleGUI as sg
"""
    Demo - Running 2 windows with both being active at the same time
    Three important things to note about this design patter:
        1. The layout for window 2 is inside of the while loop, just before the call to window2=sg.Window
        2. The read calls have timeout values of 100 and 0.  You can change the 100 to whatever interval you wish
            but must keep the second window's timeout at 0
        3. There is a safeguard to stop from launching multiple copies of window2.  Only 1 window2 is visible at a time
"""

sg.theme('Dark Blue 3')
# Window 1 layout
layout = [
            [sg.Text('This is the FIRST WINDOW'), sg.Text('      ', key='-OUTPUT-')],
            [sg.Text()],
            [sg.Button('Launch 2nd Window'), sg.Button('Popup'), sg.Button('Exit')]
         ]

window = sg.Window('Window Title', layout, location=(800,600))

win2_active = False
i=0
while True:             # Event Loop
    event, values = window.read(timeout=100)
    if event != sg.TIMEOUT_KEY:
        print(i, event, values)
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    elif event == 'Popup':
        sg.popup('This is a BLOCKING popup','all windows remain inactive while popup active')
    i+=1
    if event == 'Launch 2nd Window' and not win2_active:     # only run if not already showing a window2
        win2_active = True
        # window 2 layout - note - must be "new" every time a window is created
        layout2 = [
            [sg.Text('The second window')],
            [sg.Input(key='-IN-')],
            [sg.Button('Show'), sg.Button('Exit')]
                ]
        window2 = sg.Window('Second Window', layout2)
    # Read window 2's events.  Must use timeout of 0
    if win2_active:
        # print("reading 2")
        event, values = window2.read(timeout=100)
        # print("win2 ", event)
        if event != sg.TIMEOUT_KEY:
            print("win2 ", event)
        if event == 'Exit' or event == sg.WIN_CLOSED:
            # print("Closing window 2", event)
            win2_active = False
            window2.close()
        if event == 'Show':
            sg.popup('You entered ', values['-IN-'])

window.close()