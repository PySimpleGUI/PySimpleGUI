#!/usr/bin/env python
import sys
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg

if not sys.platform.startswith('win'):
    sg.PopupError('Sorry, you gotta be on Windows')
    sys.exit()
import winsound


sg.ChangeLookAndFeel('Dark')
sg.SetOptions(element_padding=(0,0))

layout = [
          [sg.ReadButton('Start', button_color=('white', 'black'), key='start'),
           sg.ReadButton('Stop', button_color=('white', 'black'), key='stop'),
           sg.ReadButton('Reset', button_color=('white', 'firebrick3'), key='reset'),
           sg.ReadButton('Submit', button_color=('white', 'springgreen4'), key='submit')]
          ]

window = sg.Window("Button Click", default_element_size=(12,1), text_justification='r', auto_size_text=False, auto_size_buttons=False, default_button_element_size=(12,1), use_default_focus=False).Layout(layout).Finalize()

window.FindElement('submit').Update(disabled=True)

recording = have_data = False
while True:
    event, values = window.Read()
    if event is None:
        sys.exit(69)
    winsound.PlaySound("ButtonClick.wav", 1)
