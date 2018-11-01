#!/usr/bin/env python
import sys
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg

sg.SetOptions(background_color='cornsilk4', element_background_color='cornsilk2', input_elements_background_color='cornsilk2')

tab1_layout =  [[sg.T('This is inside tab 1', background_color='darkslateblue', text_color='white')],
                [sg.In(key='_in0_')]]

tab2_layout = [[sg.T('This is inside tab 2', background_color='tan1')],
               [sg.In(key='_in2_')]]


tab3_layout = [[sg.T('This is inside tab 3')],
               [sg.In(key='_in2_')]]

tab4_layout = [[sg.T('This is inside tab 4', background_color='darkseagreen')],
               [sg.In(key='_in3_')]]

tab5_layout = [[sg.T('This is inside tab 5')],
               [sg.In(key='_in4_')]]


layout = [[sg.TabGroup([[sg.Tab('Tab 1', tab1_layout, background_color='darkslateblue', key='_mykey_'),
                         sg.Tab('Tab 2', tab2_layout, background_color='tan1'),
                         sg.Tab('Tab 3', tab3_layout)]],
                         key='_group2_', title_color='red',
                         selected_title_color='green', tab_location='right'),
        sg.TabGroup([[sg.Tab('Tab 4', tab4_layout,background_color='darkseagreen', key='_mykey_'),
                      sg.Tab('Tab 5', tab5_layout)]], key='_group1_', tab_location='top', selected_title_color='purple')],
          [sg.TabGroup([[sg.Tab('Tab 1', tab1_layout, background_color='darkslateblue', key='_mykey_'),
                         sg.Tab('Tab 2', tab2_layout, background_color='tan1'),
                         sg.Tab('Tab 3', tab3_layout)]],
                         key='_group3_', title_color='red',
                         selected_title_color='green', tab_location='left'),
        sg.TabGroup([[sg.Tab('Tab 4', tab4_layout,background_color='darkseagreen', key='_mykey_'),
                      sg.Tab('Tab 5', tab5_layout)]], key='_group4_', tab_location='bottom', selected_title_color='purple')],
                     [sg.Button('Read')]]

window = sg.Window('My window with tabs', default_element_size=(12,1)).Layout(layout)


while True:
    event, values = window.Read()
    sg.PopupNonBlocking(event, values)
    print(event, values)
    if event is None:           # always,  always give a way out!
        break
