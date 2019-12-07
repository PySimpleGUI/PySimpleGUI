#!/usr/bin/env python
import PySimpleGUI as sg

# Simple example of TabGroup element

sg.change_look_and_feel('Dark Brown 1')

tab1_layout = [[sg.Text('Tab 1')],
               [sg.Text('Put your layout in here')],
               [sg.Text('Input something'), sg.Input(size=(12,1), key='-IN0-')]]

tab2_layout = [[sg.Text('Tab 2')]]
tab3_layout = [[sg.Text('Tab 3')]]


tab_group_layout = [[sg.Tab('Tab 1', tab1_layout, key='-TAB1-'),
                     sg.Tab('Tab 2', tab2_layout, visible=False, key='-TAB2-'),
                     sg.Tab('Tab 3', tab3_layout, key='-TAB3-')]]

layout = [[sg.TabGroup(tab_group_layout,
                       selected_title_color='blue',
                       selected_background_color='red',
                       tab_background_color='green',
                       enable_events=True,
                       key='-TABGROUP-')],
          [sg.Text('Make tab number'), sg.Input(key='-IN-', size=(3,1)), sg.Button('Invisible'), sg.Button('Visible')]]

window = sg.Window('My window with tabs', layout)

tab_keys = ('-TAB1-','-TAB2-','-TAB3-')
while True:
    event, values = window.read()               # type: str, dict
    print(event, values)
    if event is None:
        break
    if event == 'Invisible':
        window[tab_keys[int(values['-IN-'])-1]].update(visible=False)
    if event == 'Visible':
        window[tab_keys[int(values['-IN-'])-1]].update(visible=True)
window.close()
