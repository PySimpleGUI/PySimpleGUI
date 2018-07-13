import PySimpleGUI as sg

rc, number = sg.GetTextBox('Title goes here', 'Enter a number')
if not rc:
    sg.MsgBoxError('You have cancelled')
    exit(0)

msg = '\n'.join([f'{i}' for i in range(0,int(number))])

sg.ScrolledTextBox(msg, Height=10)