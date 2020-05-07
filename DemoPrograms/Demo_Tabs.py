#!/usr/bin/env python
import sys
import PySimpleGUI as sg
# import PySimpleGUIWeb as sg

# Usage of Tabs in PSG
#
# sg.set_options(background_color='cornsilk4',
#         element_background_color='cornsilk2',
#         input_elements_background_color='cornsilk2')

sg.theme('Light Green 5')

tab1_layout = [[sg.Text('This is inside tab 1', background_color='darkslateblue', text_color='white')],
               [sg.Input(key='-in0-')]]

tab2_layout = [[sg.Text('This is inside tab 2', background_color='tan1')],
               [sg.Input(key='-in2-')]]


tab3_layout = [[sg.Text('This is inside tab 3')],
               [sg.Input(key='-in2-')]]

tab4_layout = [[sg.Text('This is inside tab 4', background_color='darkseagreen')],
               [sg.Input(key='-in3-')]]

tab5_layout = [[sg.Text('This is inside tab 5')],
               [sg.Input(key='-in4-')]]


layout = [[sg.TabGroup([[sg.Tab('Tab 1', tab1_layout, background_color='darkslateblue', key='-mykey-'),
                         sg.Tab('Tab 2', tab2_layout, background_color='tan1'),
                         sg.Tab('Tab 3', tab3_layout)]],
                       key='-group2-', title_color='red',
                       selected_title_color='green', tab_location='right'),
           sg.TabGroup([[sg.Tab('Tab 4', tab4_layout, background_color='darkseagreen', key='-mykey-'),
                         sg.Tab('Tab 5', tab5_layout)]], key='-group1-', tab_location='top', selected_title_color='purple')],
          # [sg.TabGroup([[sg.Tab('Tab 1', tab1_layout, background_color='darkslateblue', key='-mykey-'),
          #                sg.Tab('Tab 2', tab2_layout, background_color='tan1'),
          #                sg.Tab('Tab 3', tab3_layout)]],
          #              key='-group3-', title_color='red',
          #              selected_title_color='green', tab_location='left'),
          #  sg.TabGroup([[sg.Tab('Tab 4', tab4_layout, background_color='darkseagreen', key='-mykey-'),
          #                sg.Tab('Tab 5', tab5_layout)]], key='-group4-', tab_location='bottom', selected_title_color='purple')],
          [sg.Button('Read')]]

window = sg.Window('My window with tabs', layout,
                   default_element_size=(12, 1))


while True:
    event, values = window.read()
    sg.popup_non_blocking(event, values)
    print(event, values)
    if event == sg.WIN_CLOSED:           # always,  always give a way out!
        break
window.close()
