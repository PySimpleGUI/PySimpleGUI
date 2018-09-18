import PySimpleGUI as sg

print (sg.PopupYesNo('Yes No'))

print(sg.PopupGetText('Get text', background_color='blue', text_color='white', location=(1000,200)))
print(sg.PopupGetFile('Get file', background_color='blue', text_color='white'))
print(sg.PopupGetFolder('Get folder', background_color='blue', text_color='white'))


sg.Popup('Simple popup')

sg.PopupNonBlocking('Non Blocking', location=(500,500))
sg.PopupNoTitlebar('No titlebar')
sg.PopupNoBorder('No border')
sg.PopupNoFrame('No frame')
sg.PopupNoButtons('No Buttons')
sg.PopupCancel('Cancel')
sg.PopupOKCancel('OK Cancel')
sg.PopupAutoClose('Autoclose')
