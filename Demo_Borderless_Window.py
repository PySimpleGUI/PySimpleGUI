#!/usr/bin/env python
import sys
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg

"""
Turn off padding in order to get a really tight looking layout.
"""

sg.ChangeLookAndFeel('Dark')
sg.SetOptions(element_padding=(0, 0))

layout = [[sg.T('User:', pad=((3, 0), 0)), sg.OptionMenu(values=('User 1', 'User 2'), size=(20, 1)),
           sg.T('0', size=(8, 1))],
          [sg.T('Customer:', pad=((3, 0), 0)), sg.OptionMenu(values=('Customer 1', 'Customer 2'), size=(20, 1)),
           sg.T('1', size=(8, 1))],
          [sg.T('Notes:', pad=((3, 0), 0)), sg.In(size=(44, 1), background_color='white', text_color='black')],
          [sg.ReadButton('Start', button_color=('white', 'black')),
           sg.ReadButton('Stop', button_color=('gray50', 'black')),
           sg.ReadButton('Reset', button_color=('white', '#9B0023')),
           sg.ReadButton('Submit', button_color=('gray60', 'springgreen4')),
           sg.Button('Exit', button_color=('white', '#00406B'))]]

window = sg.Window("Borderless Window",
                   default_element_size=(12, 1),
                   text_justification='r',
                   auto_size_text=False,
                   auto_size_buttons=False,
                   no_titlebar=True,
                   grab_anywhere=True,
                   default_button_element_size=(12, 1))

window.Layout(layout)

while True:
    event, values = window.Read()
    if event is None or event == 'Exit':
        break


