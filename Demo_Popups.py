import PySimpleGUI as sg



print(sg.PopupGetFolder('Get text', background_color='blue', text_color='white'))
print(sg.PopupGetFile('Get text', background_color='blue', text_color='white'))
print(sg.PopupGetFolder('Get text', background_color='blue', text_color='white'))


sg.Popup('Simple popup')

sg.PopupNonBlocking('Non Blocking')
sg.PopupError('Error')
sg.PopupYesNo('Yes No')
sg.PopupNoTitlebar('No titlebar')
sg.PopupNoBorder('No border')
sg.PopupNoFrame('No frame')
sg.PopupNoButtons('No Buttons')
sg.PopupCancel('Cancel')
sg.PopupOKCancel('OK Cancel')
sg.PopupAutoClose('Autoclose')
print(sg.PopupGetText('Get text'))
print(sg.PopupGetFile('Get File'))
print(sg.PopupGetFolder('Get folder'))
