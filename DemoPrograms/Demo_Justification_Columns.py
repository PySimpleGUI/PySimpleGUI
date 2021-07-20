import PySimpleGUI as sg

""""
    Demo Justification Columns
    
    Using Column elements to justify one or more elements within a window
    
    Copyright 2021 PySimpleGUI
"""

col1 = [[sg.T('Left side')],[sg.T('Still left')]]
col2 = [[sg.T('Middle')]]
col3 = [[sg.T('Right side')]]

layout = [[sg.T('First row of the layout is left justified', font='Any 14')],
          [sg.HorizontalSeparator()],
          [sg.Column(col1, key='c1', element_justification='l', expand_x=True),
           sg.Column(col2, key='c2', element_justification='c', expand_x=True),
           sg.Column(col3, key='c3', element_justification='r', expand_x=True)],
          [sg.HorizontalSeparator()],
          [sg.Text('The remainder of the window is left justified')],
          [sg.Input(key='-IN-')],
          [sg.Button('Go'), sg.Button('Exit')]]

window = sg.Window('Justifying and resizing window contents', layout, finalize=True, resizable=True)

# If using an older version of PySimpleGUI, you can add the expansion using these expand method calls
# window['c1'].expand(True, False, False)
# window['c2'].expand(True, False, False)
# window['c3'].expand(True, False, False)

while True:             # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
window.close()
