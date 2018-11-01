#!/usr/bin/env python
import sys
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg

tab1_layout =  [[sg.T('Tab 1')],
                [sg.T('Put your layout in here')],
                [sg.T('Input something'),sg.In(key='_IN0_')]]

tab2_layout = [[sg.T('Tab2')]]


layout = [[sg.TabGroup([[sg.Tab('Tab 1', tab1_layout), sg.Tab('Tab 2', tab2_layout)]], key='_TABGROUP_')],
                         [sg.Button('Read')]]

window = sg.Window('My window with tabs', default_element_size=(12,1)).Layout(layout)


while True:
    event, values = window.Read()
    sg.PopupNonBlocking('button = %s' % event, 'Values dictionary', values)
    if event is None:           # always,  always give a way out!
        break
