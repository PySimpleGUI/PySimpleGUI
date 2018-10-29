#!/usr/bin/env python
import sys
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg

"""
    Simple Form showing how to use keys on your input fields
"""

layout = [
    [sg.Text('Please enter your Name, Address, Phone')],
    [sg.Text('Name', size=(15, 1)), sg.InputText('1', key='name'), sg.FileBrowse()],
    [sg.Text('Address', size=(15, 1)), sg.InputText('2', key='address')],
    [sg.Text('Phone', size=(15, 1)), sg.InputText('3', key='phone')],
    [sg.CloseButton('Submit'), sg.CloseButton('Cancel')]
        ]

window = sg.Window('Simple Data Entry Window').Layout(layout)
event, values = window.Read()

sg.Popup(event, values, values['name'], values['address'], values['phone'])