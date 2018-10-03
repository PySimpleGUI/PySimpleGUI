#!/usr/bin/env python
import sys
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg

tab1_layout =  [[sg.T('This is inside tab 1')]]

tab2_layout = [[sg.T('This is inside tab 2')],
               [sg.In(key='_in2_')]]

tab3_layout = [[sg.T('This is inside tab 3')],
               [sg.In(key='_in3_')]]

tab4_layout = [[sg.T('This is inside tab 4')],
               [sg.In(key='_in4_')]]


layout = [[sg.TabGroup([[sg.Tab('Tab 1', tab1_layout, key='_mykey_'), sg.Tab('Tab 2', tab2_layout)]], key='_group2_', background_color='green', tab_location='top')],
[sg.TabGroup([[sg.Tab('Tab 3', tab3_layout, key='_mykey_'), sg.Tab('Tab 4', tab4_layout)]], key='_group1_', tab_location='right')],
          [sg.RButton('Read')]]

window = sg.Window('My window with tabs', default_element_size=(12,1)).Layout(layout)

while True:
    b, v = window.Read()
    print(b,v)
    if b is None:           # always,  always give a way out!
        break