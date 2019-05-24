import PySimpleGUI as sg
import PSGdebugger

"""
    Demo program that shows you how to integrate the PySimpleGUI Debugger
    into your program.
    There are TWO steps, and they are copy and pastes.
    1. At the top of your app to debug add
            import PSGdebugger
    2. At the end of your app's event loop add
            PSGdebugger.refresh(locals(), globals())
"""


layout = [
            [sg.T('A typical PSG application')],
            [sg.In(key='_IN_')],
            [sg.T('        ', key='_OUT_')],
            [sg.Radio('a',1, key='_R1_'), sg.Radio('b',1, key='_R2_'), sg.Radio('c',1, key='_R3_')],
            [sg.Combo(['c1', 'c2', 'c3'], size=(6,3), key='_COMBO_')],
            [sg.Output(size=(40,6))],
            [sg.Ok(), sg.Exit()],
        ]


window = sg.Window('This is your Application Window', layout)

# Variables that we'll use to demonstrate the debugger's features
counter = 0
timeout = 100

while True:             # Event Loop
    event, values = window.Read(timeout=timeout)
    if event in (None, 'Exit'):
        break
    counter += 1
    window.Element('_OUT_').Update(values['_IN_'])
    PSGdebugger.refresh(locals(), globals())
