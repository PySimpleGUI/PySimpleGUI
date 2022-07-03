#!/usr/bin/env python

"""
    Demo - Simple Tabs

    How to use the Tab Element and the TabGroup Element

    Copyright 2021 PySimpleGUI
"""

import PySimpleGUI as sg
# Simple example of TabGroup element and the options available to it
sg.theme('Dark Red')     # Please always add color to your window
# The tab 1, 2, 3 layouts - what goes inside the tab
tab1_layout = [[sg.Text('Tab 1')],
               [sg.Text('Put your layout in here')],
               [sg.Text('Input something'), sg.Input(size=(12,1), key='-IN-TAB1-')]]

tab2_layout = [[sg.Text('Tab 2')]]
tab3_layout = [[sg.Text('Tab 3')]]
tab4_layout = [[sg.Text('Tab 3')]]

# The TabgGroup layout - it must contain only Tabs
tab_group_layout = [[sg.Tab('Tab 1', tab1_layout, key='-TAB1-'),
                     sg.Tab('Tab 2', tab2_layout, visible=False, key='-TAB2-'),
                     sg.Tab('Tab 3', tab3_layout, key='-TAB3-'),
                     sg.Tab('Tab 4', tab4_layout, visible=False, key='-TAB4-')]]

# The window layout - defines the entire window
layout = [[sg.TabGroup(tab_group_layout,
                       enable_events=True,
                       key='-TABGROUP-')],
          [sg.Text('Make tab number'), sg.Input(key='-IN-', size=(3,1)), sg.Button('Invisible'), sg.Button('Visible'), sg.Button('Select'), sg.Button('Disable')]]

window = sg.Window('My window with tabs', layout, no_titlebar=False)

tab_keys = ('-TAB1-','-TAB2-','-TAB3-', '-TAB4-')         # map from an input value to a key
while True:
    event, values = window.read()       # type: str, dict
    print(event, values)
    if event == sg.WIN_CLOSED:
        break
    # handle button clicks
    if event == 'Invisible':
        window[tab_keys[int(values['-IN-'])-1]].update(visible=False)
    if event == 'Visible':
        window[tab_keys[int(values['-IN-'])-1]].update(visible=True)
    if event == 'Select':
        window[tab_keys[int(values['-IN-'])-1]].select()
    if event == 'Disable':
        window[tab_keys[int(values['-IN-']) - 1]].update(disabled=True)
window.close()
