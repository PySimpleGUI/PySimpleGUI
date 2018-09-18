import PySimpleGUI as sg
import winsound


sg.ChangeLookAndFeel('Dark')
sg.SetOptions(element_padding=(0,0))

layout = [
          [sg.ReadFormButton('Start', button_color=('white', 'black'), key='start'),
           sg.ReadFormButton('Stop', button_color=('white', 'black'), key='stop'),
           sg.ReadFormButton('Reset', button_color=('white', 'firebrick3'), key='reset'),
           sg.ReadFormButton('Submit', button_color=('white', 'springgreen4'), key='submit')]
          ]

form = sg.FlexForm("Button Click", default_element_size=(12,1), text_justification='r', auto_size_text=False, auto_size_buttons=False,
                   default_button_element_size=(12,1))
form.Layout(layout)
form.Finalize()             # only needed if want to diable elements prior to showing form

form.FindElement('submit').Update(disabled=True)

recording = have_data = False
while True:
    button, values = form.Read()
    if button is None:
        exit(69)
    winsound.PlaySound("ButtonClick.wav", 1)
