#!/usr/bin/env python
import PySimpleGUI as sg

# Turn off padding in order to get a really tight looking layout.

sg.theme('Dark')
sg.set_options(element_padding=(0, 0))

layout = [[sg.Text('User:', pad=((3, 0), 0)), sg.OptionMenu(values=('User 1', 'User 2'), size=(20, 1)),
           sg.Text('0', size=(8, 1))],
          [sg.Text('Customer:', pad=((3, 0), 0)), sg.OptionMenu(values=('Customer 1', 'Customer 2'), size=(20, 1)),
           sg.Text('1', size=(8, 1))],
          [sg.Text('Notes:', pad=((3, 0), 0)),
           sg.Input(size=(44, 1), background_color='white', text_color='black')],
          [sg.Button('Start', button_color=('white', 'black')),
           sg.Button('Stop', button_color=('gray50', 'black')),
           sg.Button('Reset', button_color=('white', '#9B0023')),
           sg.Button('Submit', button_color=('gray60', 'springgreen4')),
           sg.Button('Exit', button_color=('white', '#00406B'))]]

window = sg.Window("Borderless Window",
                   layout,
                   default_element_size=(12, 1),
                   text_justification='r',
                   auto_size_text=False,
                   auto_size_buttons=False,
                   no_titlebar=True,
                   grab_anywhere=True,
                   default_button_element_size=(12, 1))

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
