import PySimpleGUI as sg

# Here, have some windows on me....
[sg.PopupNoWait(location=(10*x,0)) for x in range(10)]

print (sg.PopupYesNo('Yes No'))

print(sg.PopupGetText('Get text', location=(1000,200)))
print(sg.PopupGetFile('Get file'))
print(sg.PopupGetFolder('Get folder'))


sg.Popup('Simple popup')

sg.PopupNonBlocking('Non Blocking', location=(500,500))
sg.PopupNoTitlebar('No titlebar')
sg.PopupNoBorder('No border')
sg.PopupNoFrame('No frame')
# sg.PopupNoButtons('No Buttons')        # don't mix with non-blocking... disaster ahead...
sg.PopupCancel('Cancel')
sg.PopupOKCancel('OK Cancel')
sg.PopupAutoClose('Autoclose')
