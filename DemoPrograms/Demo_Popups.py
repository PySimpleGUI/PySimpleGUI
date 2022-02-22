#!/usr/bin/env python
import PySimpleGUI as sg
import sys
'''
    Usage of  Popups in PSG
    
    While this is an older demo, it is a good instroduction to a FEW of the popups available to you.
    Check out the System Call Reference for the full list: http://www.PySimpleGUI.org
    
    Copyright 2022 PySimpleGUI
    
'''
# Here, have some windows on me....
[sg.popup_no_wait('No-wait Popup', relative_location=(-500+100*x, -500)) for x in range(10)]
answer = sg.popup_yes_no('Do not worry about all those open windows... they will disappear at the end', 'Are you OK with that?')

if answer == 'No':
    sg.popup_cancel('OK, we will destroy those windows as soon as you close this window')
    sys.exit()

sg.popup_no_buttons('Your answer was', answer, relative_location=(0, -200), non_blocking=True)
text = sg.popup_get_text('This is a call to PopopGetText')
sg.popup_get_file('Get file')
sg.popup_get_folder('Get folder')
sg.popup('Simple popup')
sg.popup_no_titlebar('No titlebar')
sg.popup_no_border('No border')
sg.popup_no_frame('No frame')
sg.popup_cancel('Cancel')
sg.popup_auto_close('This window will Autoclose and then everything else will close too....')
