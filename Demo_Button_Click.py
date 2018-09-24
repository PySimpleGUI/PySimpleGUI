import PySimpleGUI as sg
import winsound
import sys

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
    button, values = window.Read()
    if button is None:
        sys.exit(69)
    winsound.PlaySound("ButtonClick.wav", 1)
