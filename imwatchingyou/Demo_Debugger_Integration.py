import PySimpleGUI as sg
import imwatchingyou            # STEP 1

"""
    Demo program that shows you how to integrate the PySimpleGUI Debugger
    into your program.
    In this example, the debugger is not started initiallly. You click the "Debug" button to launch it
    There are THREE steps, and they are copy and pastes.
    1. At the top of your app to debug add
            import imwatchingyou
    2. Initialize the debugger at the start of your program by calling:
            imwatchingyou.initialize()
    3. At the top of your app's Event Loop add:
            imwatchingyou.refresh(locals(), globals())
"""

layout = [
            [sg.T('A typical PSG application')],
            [sg.In(key='_IN_')],
            [sg.T('        ', key='_OUT_')],
            [sg.Radio('a',1, key='_R1_'), sg.Radio('b',1, key='_R2_'), sg.Radio('c',1, key='_R3_')],
            [sg.Combo(['c1', 'c2', 'c3'], size=(6,3), key='_COMBO_')],
            [sg.Output(size=(50,6))],
            [sg.Ok(), sg.Exit(), sg.B('Debug')],
        ]

window = sg.Window('This is your Application Window', layout)

counter = 0
timeout = 100
debug_started = False

while True:             # Your Event Loop
    if debug_started:
        debug_started = imwatchingyou.refresh(locals(), globals())   # STEP 3 - refresh debugger
    event, values = window.Read(timeout=timeout)
    if event in (None, 'Exit'):
        break
    elif event == 'Ok':
        print('You clicked Ok.... this is where print output goes')
    elif event == 'Debug' and not debug_started:
        imwatchingyou.initialize()  # STEP 2
        debug_started = True
    counter += 1
    window.Element('_OUT_').Update(values['_IN_'])
window.Close()
