#!/usr/bin/env python
import PySimpleGUI as sg

# Simple example of TabGroup element

tab1_layout = [[sg.Text('Tab 1')],
               [sg.Text('Put your layout in here')],
               [sg.Text('Input something'), sg.Input(key='-IN0-')]]

tab2_layout = [[sg.Text('Tab2')]]


layout = [[sg.TabGroup([[
                sg.Tab('Tab 1', tab1_layout),
                sg.Tab('Tab 2', tab2_layout)]], key='-TABGROUP-')],
          [sg.Button('Read')]]

window = sg.Window('My window with tabs', layout,
                   default_element_size=(12, 1))


while True:
    event, values = window.read()
    sg.popup_non_blocking('button = %s' % event, 'Values dictionary', values)
    if event is None:           # always,  always give a way out!
        break
        
window.close()
