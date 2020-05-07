import PySimpleGUI as sg
import imwatchingyou  # STEP 1

"""
    Demo program that shows you how to integrate the PySimpleGUI Debugger
    into your program.
    This particular program is a GUI based program simply to make it easier for you to interact and change
    things.

    In this example, the debugger is not started initiallly. You click the "Debug" button to launch it
    There are THREE steps, and they are copy and pastes.
    1. At the top of your app to debug add
            import imwatchingyou
    2. When you want to show a debug window, call one of two functions:
        imwatchingyou.show_debug_window()
        imwatchingyou.show_popout_window()
    3. You must find a location in your code to "refresh" the debugger.  Some loop that's executed often.
        In this loop add this call:
        imwatchingyou.refresh()
"""

layout = [
    [sg.Text('A typical PSG application')],
    [sg.Input(key='-IN-')],
    [sg.Text('        ', key='-OUT-', size=(30, 1))],
    [
     sg.Rad('a', 1, key='-R1-'),
     sg.Rad('b', 1, key='-R2-'),
     sg.Rad('c', 1, key='-R3-')
     ],
    [sg.Combo(['c1', 'c2', 'c3'], size=(6, 3), key='-COMBO-')],
    [sg.Output(size=(50, 6))],
    [sg.Ok(), sg.Exit(), sg.Button('Debug'), sg.Button('Popout')],
]

window = sg.Window('This is your Application Window', layout)

counter = 0

while True:  # Your Event Loop
    event, values = window.read(timeout=100)
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    elif event == 'Ok':
        print('You clicked Ok.... this is where print output goes')
    elif event == 'Debug':
        imwatchingyou.show_debugger_window()  # STEP 2
    elif event == 'Popout':
        imwatchingyou.show_debugger_popout_window()  # STEP 2
    counter += 1
    # to prove window is operating, show the input in another area in the window.
    window['-OUT-'].update(values['-IN-'])

    # don't worry about the "state" of things, just call this function "frequently"
    imwatchingyou.refresh_debugger()  # STEP 3 - refresh debugger

window.close()
