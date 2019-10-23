import PySimpleGUI as sg
# import imwatchingyou            # Not needed because using the one inside PySimpleGUI.py code itself

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
            [sg.T(' ', key='_OUT_', size=(45,1))],
            [sg.CBox('Checkbox 1'), sg.CBox('Checkbox 2')],
            [sg.Radio('a',1, key='_R1_'), sg.Radio('b',1, key='_R2_'), sg.Radio('c',1, key='_R3_')],
            [sg.Combo(['c1', 'c2', 'c3'], size=(6,3), key='_COMBO_')],
            [sg.Output(size=(50,6))],
            [sg.Ok(), sg.Exit(), sg.Button('Enable'), sg.Button('Popout'), sg.Button('Debugger'), sg.Debug(key='Debug')],
        ]

window = sg.Window('This is your Application Window', layout, debugger_enabled=False)

counter = 0
timeout = 100

# Note that you can launch the debugger windows right away, without waiting for user input
sg.show_debugger_popout_window()

while True:             # Your Event Loop
    event, values = window.Read(timeout=timeout)
    if event in (None, 'Exit'):
        break
    elif event == 'Enable':
        window.EnableDebugger()
    elif event == 'Popout':
        sg.show_debugger_popout_window() # replaces old popout with a new one, possibly with new variables`
    elif event == 'Debugger':
        sg.show_debugger_window()
    counter += 1
    # to prove window is operating, show the input in another area in the window.
    window.Element('_OUT_').Update(values['_IN_'])

window.Close()
