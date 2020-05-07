import PySimpleGUI as sg

sg.theme('GreenTan')

col1 = sg.Col([[sg.Text('in pane1', text_color='blue')],
               [sg.Text('Pane1')],
               [sg.Text('Pane1')],
               ])
col2 = sg.Col([[sg.Text('in pane2', text_color='red')],
               [sg.Text('Pane2')],
               [sg.Input('', key='-IN2-')],
               [sg.Text('Pane2')],
               [sg.Text('Pane2')],
               ], key='-COL2-', visible=False)
col3 = sg.Col([[sg.Text('in pane 4', text_color='green')],
               [sg.Input(key='-IN3-', enable_events=True)],
               ], key='-COL3-', visible=False)
col4 = sg.Col([[sg.Text('Column 4', text_color='firebrick')],
               [sg.Input()],
               ], key='-COL4-')
col5 = sg.Col([[sg.Frame('Frame', [[sg.Text('Column 5', text_color='purple')],
                                   [sg.Input()],
                                   ])]])

layout = [[sg.Text('Click'), sg.Text('', key='-OUTPUT-')],
          [sg.Button('Remove'), sg.Button('Add')],
          [sg.Pane([col5,
                    sg.Col([[sg.Pane([col1, col2, col4], handle_size=15,
                                     orientation='v', background_color='red', show_handle=True,
                                     visible=True, key='-PANE-', border_width=0,
                                     relief=sg.RELIEF_GROOVE), ]]), col3],
                   orientation='h', background_color=None, size=(160, 160),
                   relief=sg.RELIEF_RAISED, border_width=0)]
          ]

window = sg.Window('Window Title', layout, border_depth=5,
  default_element_size=(15, 1), resizable=True)

while True:             # Event Loop
    event, values = window.read()
    print(event, values)
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    if event == 'Remove':
        window['-COL2-'].update(visible=False)
        window['-COL3-'].update(visible=False)
    elif event == 'Add':
        window['-COL2-'].update(visible=True)
        window['-COL3-'].update(visible=True)
    window['-IN2-'].update(values['-IN3-'])

window.close()
