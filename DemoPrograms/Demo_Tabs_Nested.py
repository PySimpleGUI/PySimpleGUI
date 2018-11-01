#!/usr/bin/env python
import sys
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg

sg.ChangeLookAndFeel('GreenTan')
tab2_layout = [[sg.T('This is inside tab 2')],
               [sg.T('Tabs can be anywhere now!')]]

tab1_layout = [[sg.T('Type something here and click button'), sg.In(key='in')]]

tab3_layout = [[sg.T('This is inside tab 3')]]
tab4_layout = [[sg.T('This is inside tab 4')]]

tab_layout = [[sg.T('This is inside of a tab')]]
tab_group = sg.TabGroup([[sg.Tab('Tab 7', tab_layout), sg.Tab('Tab 8', tab_layout)]])

tab5_layout = [[sg.T('Watch this window')],
                [sg.Output(size=(40,5))]]
tab6_layout = [[sg.T('This is inside tab 6')],
               [sg.T('How about a second row of stuff in tab 6?'), tab_group]]

layout = [[sg.T('My Window!')], [sg.Frame('A Frame', layout=
    [[sg.TabGroup([[sg.Tab('Tab 1', tab1_layout), sg.Tab('Tab 2', tab2_layout)]]), sg.TabGroup([[sg.Tab('Tab3', tab3_layout), sg.Tab('Tab 4', tab4_layout)]])]])],
    [sg.T('This text is on a row with a column'),sg.Column(layout=[[sg.T('In a column')],
    [sg.TabGroup([[sg.Tab('Tab 5', tab5_layout), sg.Tab('Tab 6', tab6_layout)]])],
          [sg.Button('Click me')]])],]

window = sg.Window('My window with tabs', default_element_size=(12,1)).Layout(layout).Finalize()

print('Are there enough tabs for you?')

while True:
    event, values = window.Read()
    print(event, values)
    if event is None:           # always,  always give a way out!
        break