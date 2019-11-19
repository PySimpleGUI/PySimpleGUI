import PySimpleGUIQt as sg
import imwatchingyou

"""
    Combining the imwatchingyou debugger package with PySimpleGUIQt
    This enables you to have a live debugger / REPL in a running PySimpleGUIQt program
"""
layout = [[sg.Text('My PySimpleGUIQt layout')],
          [sg.Button('OK'), sg.Button('Debugger'), sg.B('Popout')]]

window = sg.Window('My window', layout)

counter = 0  # something to see updating in the popout window
while True:
    event, values = window.Read(timeout=100)
    if event is None:
        break
    if event == 'Debugger':
        imwatchingyou.show_debugger_window()
    elif event == 'Popout':
        imwatchingyou.show_debugger_popout_window()
    imwatchingyou.refresh_debugger()
    counter += 1
