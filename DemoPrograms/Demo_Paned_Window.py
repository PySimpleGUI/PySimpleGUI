import PySimpleGUI as sg

sg.ChangeLookAndFeel('GreenTan')

col1 = sg.Column([[sg.Text('in pane1', text_color='blue')],
                  [sg.T('Pane1')],
                  [sg.T('Pane1')],
                  ])
col2 = sg.Column([[sg.Text('in pane2', text_color='red')],
                  [sg.T('Pane2')],
                  [sg.Input(key='_IN2_', do_not_clear=True)],
                  [sg.T('Pane2')],
                  [sg.T('Pane2')],
                  ], key='_COL2_', visible=False)
col3 = sg.Column([[sg.Text('in pane 4', text_color='green')],
                  [sg.In(key='_IN3_', enable_events=True, do_not_clear=True)],
                  ], key='_COL3_', visible=False)
col4 = sg.Column([[sg.Text('Column 4', text_color='firebrick')],
                  [sg.In()],
                  ], key='_COL4_')
col5 = sg.Column([[sg.Frame('Frame', [[sg.Text('Column 5', text_color='purple')],
                  [sg.In()],
                  ])]])

layout = [ [sg.Text('Click'), sg.Text('', key='_OUTPUT_')],
           [sg.Button('Remove'), sg.Button('Add')],
           [sg.Pane([col5, sg.Column([[sg.Pane([col1, col2, col4], handle_size=15, orientation='v',  background_color='red', show_handle=True, visible=True, key='_PANE_', border_width=0,  relief=sg.RELIEF_GROOVE),]]),col3 ], orientation='h', background_color=None, size=(160,160), relief=sg.RELIEF_RAISED, border_width=0)]
        ]

window = sg.Window('Window Title', default_element_size=(15,1), resizable=True, border_depth=5).Layout(layout)

while True:             # Event Loop
    event, values = window.Read()
    print(event, values)
    if event is None or event == 'Exit':
        break
    if event == 'Remove':
        window.Element('_COL2_').Update(visible=False)
        window.Element('_COL3_').Update(visible=False)
    elif event == 'Add':
        window.Element('_COL2_').Update(visible=True)
        window.Element('_COL3_').Update(visible=True)
    window.Element('_IN2_').Update(values['_IN3_'])

window.Close()
