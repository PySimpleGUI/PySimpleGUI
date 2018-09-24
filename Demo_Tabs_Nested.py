import PySimpleGUI as sg

tab1_layout = [[sg.T('This is inside tab 1')],
               [sg.T('Tabs can be anywhere now!')]
               ]

tab2_layout = [[sg.T('This is inside tab 2'), sg.In(key='in')]]

tab3_layout = [[sg.T('This is inside tab 3')]]
tab4_layout = [[sg.T('This is inside tab 4')]]

tab5_layout = [[sg.T('This is inside tab 5')]]
tab6_layout = [[sg.T('This is inside tab 6')],
               [sg.T('How about a second row of stuff in tab 6?')]]

layout = [[sg.T('My Window!')], [sg.Frame('A Frame', layout=
    [[sg.TabGroup([[sg.Tab('Tab 1', tab1_layout), sg.Tab('Tab 2', tab2_layout)]]), sg.TabGroup([[sg.Tab('Inside of a frame?', tab3_layout), sg.Tab('Tab 4', tab4_layout)]])]])],
    [sg.T('This text is on a row with a column'),sg.Column(layout=[[sg.T('In a column')],
    [sg.TabGroup([[sg.Tab('Tab 5', tab5_layout), sg.Tab('Tab 6', tab6_layout)]])],
          [sg.RButton('Read')]])],
          ]

window = sg.Window('My window with tabs', default_element_size=(12,1)).Layout(layout)

while True:
    b, v = window.Read()
    print(b,v)
    if b is None:           # always,  always give a way out!
        break