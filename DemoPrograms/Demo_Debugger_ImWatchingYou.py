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
    [sg.T('A typical PSG application')],
    [sg.In(key='_IN_')],
    [sg.T('        ', key='_OUT_', size=(30, 1))],
    [sg.Radio('a', 1, key='_R1_'),
     sg.Radio('b', 1, key='_R2_'),
     sg.Radio('c', 1, key='_R3_')],
    [sg.Combo(['c1', 'c2', 'c3'], size=(6, 3), key='_COMBO_')],
    [sg.Output(size=(50, 6))],
    [sg.Ok(), sg.Exit(), sg.Button('Debug'), sg.Button('Popout')],
]

window = sg.Window('This is your Application Window', layout)

counter = 0
timeout = 100

# Start the program with the popout window showing so you can immediately start debugging!
imwatchingyou.show_debugger_popout_window()

while True:  # Your Event Loop
    event, values = window.Read(timeout=timeout)
    if event in (None, 'Exit'):
        break
    elif event == 'Ok':
        print('You clicked Ok.... this is where print output goes')
        imwatchingyou.show_debugger_popout_window()  # STEP 2 also
    elif event == 'Debug':
        imwatchingyou.show_debugger_window()  # STEP 2
    elif event == 'Popout':
        imwatchingyou.show_debugger_popout_window()  # STEP 2
    counter += 1
    # to prove window is operating, show the input in another area in the window.
    window.Element('_OUT_').Update(values['_IN_'])

    # don't worry about the "state" of things, just call this function "frequently"
    imwatchingyou.refresh_debugger()  # STEP 3 - refresh debugger

window.Close()
