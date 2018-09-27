#!/usr/bin/env python
import sys
if sys.version_info[0] < 3:
    import PySimpleGUI27 as sg
else:
    import PySimpleGUI as sg

"""
Demonstrates using a "tight" layout with a Dark theme.
Shows how button states can be controlled by a user application.  The program manages the disabled/enabled
states for buttons and changes the text color to show greyed-out (disabled) buttons
"""

sg.ChangeLookAndFeel('Dark')
sg.SetOptions(element_padding=(0,0))

layout = [[sg.T('User:', pad=((3,0),0)), sg.OptionMenu(values = ('User 1', 'User 2'), size=(20,1)), sg.T('0', size=(8,1))],
          [sg.T('Customer:', pad=((3,0),0)), sg.OptionMenu(values=('Customer 1', 'Customer 2'), size=(20,1)), sg.T('1', size=(8,1))],
          [sg.T('Notes:', pad=((3,0),0)), sg.In(size=(44,1), background_color='white', text_color='black')],
          [sg.ReadButton('Start', button_color=('white', 'black'), key='Start'),
           sg.ReadButton('Stop', button_color=('white', 'black'), key='Stop'),
           sg.ReadButton('Reset', button_color=('white', 'firebrick3'), key='Reset'),
           sg.ReadButton('Submit', button_color=('white', 'springgreen4'), key='Submit')]]

window = sg.Window("Time Tracker", default_element_size=(12,1), text_justification='r', auto_size_text=False, auto_size_buttons=False,
                   default_button_element_size=(12,1)).Layout(layout).Finalize()


for key, state in {'Start': False, 'Stop': True, 'Reset': True, 'Submit': True}.items():
    window.FindElement(key).Update(disabled=state)

recording = have_data = False
while True:
    button, values = window.Read()
    print(button)
    if button is None:
        sys.exit(69)
    if button is 'Start':
        for key, state in {'Start':True, 'Stop':False, 'Reset':False, 'Submit':True}.items():
            window.FindElement(key).Update(disabled=state)
        recording = True
    elif button is 'Stop' and recording:
        [window.FindElement(key).Update(disabled=value) for key,value in {'Start':False, 'Stop':True, 'Reset':False, 'Submit':False}.items()]
        recording = False
        have_data = True
    elif button is 'Reset':
        [window.FindElement(key).Update(disabled=value) for key,value in {'Start':False, 'Stop':True, 'Reset':True, 'Submit':True}.items()]
        recording = False
        have_data = False
    elif button is 'Submit' and have_data:
        [window.FindElement(key).Update(disabled=value) for key,value in {'Start':False, 'Stop':True, 'Reset':True, 'Submit':False}.items()]
        recording = False
