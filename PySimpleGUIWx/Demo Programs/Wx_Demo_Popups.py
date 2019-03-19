import PySimpleGUIWx as sg
import sys
import time

sg.Popup('Test'*10, title='My title')
# sg.Print('test', location=(400,200))
# sg.PopupScrolled(sg.ObjToString(sg.Window), title='My scrolled popup', non_blocking=True)
# sg.Print('Outputting to another line\n')
sg.PopupNonBlocking('Issues changed on GitHub ', 'First issue # is {}'.format(1), background_color='red',
                    keep_on_top=False)
file = sg.PopupGetFile('Get file', save_as=False,file_types=(("ALL Files", "*.jpg"),), no_window=False)
folder = sg.PopupGetFolder('Getting a folder', no_window=False)
sg.Popup('Test'*10, title='My title')
sg.Print('file = ', file)
sg.Print('folder = ', folder)
sg.Print(file)
# sg.Print(file)
sg.PopupQuickMessage('This is a quick message', location=(1000,600))
# Here, have some windows on me....
[sg.PopupNoWait('No-wait Popup', location=(500+100*x,500)) for x in range(10)]

answer = sg.PopupYesNo('Do not worry about all those open windows... they will disappear at the end', 'Are you OK with that?')
print('answer=',answer)
if answer == 'No':
    # sg.PopupCancel('OK, we will destroy those windows as soon as you close this window', auto_close_duration=2, auto_close=True)
    sys.exit()

sg.PopupNonBlocking('Your answer was',answer, location=(1000,600))

text = sg.PopupGetText('This is a call to PopopGetText', location=(1000,200))
print(text)
sg.PopupGetFile('Get file')
sg.PopupGetFolder('Get folder')


sg.Popup('Simple popup')

sg.PopupNoTitlebar('No titlebar')
sg.PopupNoBorder('No border')
sg.PopupNoFrame('No frame')
sg.PopupCancel('Cancel')
sg.PopupOKCancel('OK Cancel')
sg.PopupAutoClose('Autoclose')
