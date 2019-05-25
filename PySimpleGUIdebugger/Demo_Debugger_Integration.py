import PySimpleGUI as sg
import PySimpleGUIdebugger
"""
    Demo program that shows you how to integrate the PySimpleGUI Debugger
    into your program.
    There are THREE steps, and they are copy and pastes.
    1. At the top of your app to debug add
            import PySimpleGUIdebugger
    2. Initialize the debugger by calling:
            PySimpleGUIdebugger.initialize()
    2. At the top of your app's event loop add
            PySimpleGUIdebugger.refresh(locals(), globals())
"""


layout = [
            [sg.T('A typical PSG application')],
            [sg.In(key='_IN_')],
            [sg.T('        ', key='_OUT_')],
            [sg.Radio('a',1, key='_R1_'), sg.Radio('b',1, key='_R2_'), sg.Radio('c',1, key='_R3_')],
            [sg.Combo(['c1', 'c2', 'c3'], size=(6,3), key='_COMBO_')],
            [sg.Output(size=(50,6))],
            [sg.Ok(), sg.Exit()],
        ]


window = sg.Window('This is your Application Window', layout)
# Variables that we'll use to demonstrate the debugger's features
counter = 0
timeout = 100
PySimpleGUIdebugger.initialize()

while True:             # Event Loop
    PySimpleGUIdebugger.refresh(locals(), globals())            # call the debugger to refresh the items being shown
    event, values = window.Read(timeout=timeout)
    if event in (None, 'Exit'):
        break
    elif event == 'Ok':
        print('You clicked Ok.... this is where print output goes')
    counter += 1
    window.Element('_OUT_').Update(values['_IN_'])
