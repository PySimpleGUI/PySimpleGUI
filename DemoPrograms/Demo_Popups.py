#!/usr/bin/env python
import PySimpleGUI as sg

'''
    Usage of all Popups in PSG
'''

sg.Print('test')
sg.popup_get_file('Get file', save_as=True,
                  file_types=(("ALL Files", "*.jpg"),))

# Here, have some windows on me....
[sg.popup_no_wait('No-wait Popup', location=(500+100*x, 500))
 for x in range(10)]
answer = sg.popup_yes_no(
    'Do not worry about all those open windows... they will disappear at the end', 'Are you OK with that?')

if answer == 'No':
    sg.popup_cancel(
        'OK, we will destroy those windows as soon as you close this window')
    sys.exit()

sg.popup_non_blocking('Your answer was', answer, location=(1000, 600))
text = sg.popup_get_text(
    'This is a call to PopopGetText', location=(1000, 200))
sg.popup_get_file('Get file')
sg.popup_get_folder('Get folder')
sg.popup('Simple popup')
sg.popup_no_titlebar('No titlebar')
sg.popup_no_border('No border')
sg.popup_no_frame('No frame')
sg.popup_cancel('Cancel')
sg.popup_okCancel('OK Cancel')
sg.popup_auto_close('Autoclose')
