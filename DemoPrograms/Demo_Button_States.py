#!/usr/bin/env python
import sys
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg
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
          [sg.ReadButton('Start', button_color=('white', 'black'), key='_Start_'),
           sg.ReadButton('Stop', button_color=('white', 'black'), key='_Stop_'),
           sg.ReadButton('Reset', button_color=('white', 'firebrick3'), key='_Reset_'),
           sg.ReadButton('Submit', button_color=('white', 'springgreen4'), key='_Submit_')]]

window = sg.Window("Time Tracker", default_element_size=(12,1), text_justification='r', auto_size_text=False, auto_size_buttons=False,
                   default_button_element_size=(12,1)).Layout(layout).Finalize()


for key, state in {'_Start_': False, '_Stop_': True, '_Reset_': True, '_Submit_': True}.items():
    window.FindElement(key).Update(disabled=state)

recording = have_data = False
while True:
    event, values = window.Read()
    print(event)
    if event is None:
        sys.exit(69)
    if event == '_Start_':
        for key, state in {'_Start_':True, '_Stop_':False, '_Reset_':False, '_Submit_':True}.items():
            window.FindElement(key).Update(disabled=state)
        recording = True
    elif event ==  '_Stop_' and recording:
        [window.FindElement(key).Update(disabled=value) for key,value in {'_Start_':False, '_Stop_':True, '_Reset_':False, '_Submit_':False}.items()]
        recording = False
        have_data = True
    elif event == '_Reset_':
        [window.FindElement(key).Update(disabled=value) for key,value in {'_Start_':False, '_Stop_':True, '_Reset_':True, '_Submit_':True}.items()]
        recording = False
        have_data = False
    elif event is '_Submit_' and have_data:
        [window.FindElement(key).Update(disabled=value) for key,value in {'_Start_':False, '_Stop_':True, '_Reset_':True, '_Submit_':False}.items()]
        recording = False
