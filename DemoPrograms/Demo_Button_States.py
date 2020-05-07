#!/usr/bin/env python
import PySimpleGUI as sg

"""
Demonstrates using a "tight" layout with a Dark theme.
Shows how button states can be controlled by a user application.  The program manages the disabled/enabled
states for buttons and changes the text color to show greyed-out (disabled) buttons
"""

sg.theme('Dark')
sg.set_options(element_padding=(0, 0))

layout = [[sg.Text('User:', pad=((3, 0), 0)), sg.OptionMenu(values=('User 1', 'User 2'), size=(20, 1)), sg.Text('0', size=(8, 1))],
          [sg.Text('Customer:', pad=((3, 0), 0)), sg.OptionMenu(
              values=('Customer 1', 'Customer 2'), size=(20, 1)), sg.Text('1', size=(8, 1))],
          [sg.Text('Notes:', pad=((3, 0), 0)), sg.Input(size=(44, 1),
                                                 background_color='white', text_color='black')],
          [sg.Button('Start', button_color=('white', 'black'), key='-Start-'),
           sg.Button('Stop', button_color=('white', 'black'), key='-Stop-'),
           sg.Button('Reset', button_color=('white', 'firebrick3'), key='-Reset-'),
           sg.Button('Submit', button_color=('white', 'springgreen4'), key='-Submit-')]]

window = sg.Window("Time Tracker", layout,
          default_element_size=(12, 1),
          text_justification='r',
          auto_size_text=False,
          auto_size_buttons=False,
          default_button_element_size=(12, 1),
          finalize=True)


for key, state in {'-Start-': False, '-Stop-': True, '-Reset-': True, '-Submit-': True}.items():
    window[key].update(disabled=state)

recording = have_data = False
while True:
    event, values = window.read()
    print(event)
    if event == sg.WIN_CLOSED:
        break
    if event == '-Start-':
        for key, state in {'-Start-': True, '-Stop-': False, '-Reset-': False, '-Submit-': True}.items():
            window[key].update(disabled=state)
        recording = True
    elif event == '-Stop-' and recording:
        [window[key].update(disabled=value) for key, value in {
            '-Start-': False, '-Stop-': True, '-Reset-': False, '-Submit-': False}.items()]
        recording = False
        have_data = True
    elif event == '-Reset-':
        [window[key].update(disabled=value) for key, value in {
            '-Start-': False, '-Stop-': True, '-Reset-': True, '-Submit-': True}.items()]
        recording = False
        have_data = False
    elif event == '-Submit-' and have_data:
        [window[key].update(disabled=value) for key, value in {
            '-Start-': False, '-Stop-': True, '-Reset-': True, '-Submit-': False}.items()]
        recording = False

window.close()
