import PySimpleGUI as sg

"""
    Demo - "Collapsible" sections of windows

    This demo shows one techinique for creating a collapsible section (Column) within your window.

    It uses the "pin" function so you'll need version 4.28.0+

    Copyright 2020 PySimpleGUI.org
"""

SYMBOL_UP =    '▲'
SYMBOL_DOWN =  '▼'

def collapse(layout, key):
    """
    Helper function that creates a Column that can be later made hidden, thus appearing "collapsed"
    :param layout: The layout for the section
    :param key: Key used to make this seciton visible / invisible
    :return: A pinned column that can be placed directly into your layout
    :rtype: sg.pin
    """
    return sg.pin(sg.Column(layout, key=key))


section1 = [[sg.pin(sg.Input('Input sec 1', key='-IN1-'))],
            [sg.Input(key='-IN11-')],
            [sg.pin(sg.Button('Button section 1', button_color='yellow on green')), sg.pin(sg.Button('Button2 section 1', button_color='yellow on green')), sg.B('Button3 section 1', button_color='yellow on green')]]

section2 = [[sg.pin(sg.Input('Input sec 2', key='-IN2-'))],
            [sg.Input(key='-IN21-')],
            [sg.pin(sg.Button('Button section 2', button_color='yellow on purple')),sg.Button('Button2 section 2', button_color='yellow on purple'), sg.B('Button3 section 2', button_color='yellow on purple')]]


layout = [  [sg.Text('Window with 2 collapsible sections')],
            [sg.pin(sg.Input('Input 1', key='-IN0-'))],
            [sg.T(SYMBOL_DOWN, enable_events=True, k='-OPEN SEC1-', text_color='yellow'), sg.T('Section 1', enable_events=True, text_color='yellow', k='-OPEN SEC1-0')],
            [collapse(section1, '-SEC1-')],
            [sg.T(SYMBOL_DOWN, enable_events=True, k='-OPEN SEC2-', text_color='purple'),
             sg.T('Section 2', enable_events=True, text_color='purple', k='-OPEN SEC2-0')],
            [collapse(section2, '-SEC2-')],
            [sg.pin(sg.Button('Button1')), sg.pin(sg.Button('Button2')), sg.B('Hide/Unhide Input 1', k='-HIDE-IN1-')]]

window = sg.Window('Visible / Invisible Element Demo', layout, finalize=True)

toggle_in, opened1, opened2 = False, True, True

while True:             # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    if event.startswith('-OPEN SEC1-'):
        opened1 = not opened1
        window['-OPEN SEC1-'].update(SYMBOL_DOWN if opened1 else SYMBOL_UP)
        window['-SEC1-'].update(visible=opened1)

    if event.startswith('-OPEN SEC2-'):
        opened2 = not opened2
        window['-OPEN SEC2-'].update(SYMBOL_DOWN if opened2 else SYMBOL_UP)
        window['-SEC2-'].update(visible=opened2)

    if event == '-HIDE-IN1-':
        window['-IN0-'].update(visible=toggle_in)
        toggle_in = not toggle_in
window.close()
