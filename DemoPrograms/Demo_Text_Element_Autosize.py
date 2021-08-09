import PySimpleGUI as sg

"""
    Demo of autosize of Text Element

    Beginning in version 4.46.0 the Text element will fully autosize if:
        * auto_size_text is True (default)
        * No size is supplied or (None, None) is supplied

    "Fully autosize" means that both the element and the window will grow/shrink 
        as the contents of the Text element changes.

    Prior versions autosized in 1 direction, either horizontally or vertically
        * Set size = (None, int) to autosize horizontally
        * Set size = (int, None) to autosize vertically

    By default autosize is enabled, but setting a size parameter will disable unless None is specified
        in one of the directions.
        
    Copyright 2021 PySimpleGUI
"""

layout = [[sg.Text('Starting string', size=(None, None), k='-T-'), sg.Text('Also on first row')],
          # THIS is the newly added combination. Note (None, None) is default and not really needed
          [sg.Text('None, 1', size=(None, 1), k='-T1-'), sg.Text('rest of the row')],
          [sg.Text('30, None', size=(30, None), k='-T2-'), sg.Text('rest of the row')],
          [sg.Text('Explicit size', size=(15, 1)), sg.Text('Second Text Element on second row')],
          [sg.Button('Go'), sg.B('Clear'), sg.Button('Exit')]]

window = sg.Window('Autosize Text', layout)

while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Go':
        window['-T-'].update('This is the new string\nThat is multiple\nlines')
        window['-T1-'].update('This is the new string\nThat is multiple\nlines')
        window['-T2-'].update('This is the new string\nThat is multiple\nlines')
    elif event == 'Clear':
        window['-T-'].update('')
        window['-T1-'].update('')
        window['-T2-'].update('')

window.close()
