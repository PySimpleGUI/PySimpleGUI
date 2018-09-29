#!/usr/bin/env python
import sys
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg

# Here, have some windows on me....
[sg.PopupNoWait(location=(500+100*x,500)) for x in range(10)]

answer = sg.PopupYesNo('Do not worry about all those open windows... they will disappear at the end', 'Are you OK with that?')

if answer == 'No':
    sg.PopupCancel('OK, we will destroy those windows as soon as you close this window')
    sys.exit()

sg.PopupNonBlocking('Your answer was',answer, location=(1000,600))

text = sg.PopupGetText('This is a call to PopopGetText', location=(1000,200))
sg.PopupGetFile('Get file')
sg.PopupGetFolder('Get folder')


sg.Popup('Simple popup')

sg.PopupNoTitlebar('No titlebar')
sg.PopupNoBorder('No border')
sg.PopupNoFrame('No frame')
# sg.PopupNoButtons('No Buttons')        # don't mix with non-blocking... disaster ahead...
sg.PopupCancel('Cancel')
sg.PopupOKCancel('OK Cancel')
sg.PopupAutoClose('Autoclose')
