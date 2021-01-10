#!/usr/bin/env python
import PySimpleGUI as sg

'''
    App that shows "how fonts work in PySimpleGUI".
'''

layout = [[sg.Text('This is my sample text', size=(20, 1), key='-text-')],
          [sg.CB('Bold', key='-bold-', change_submits=True),
           sg.CB('Italics', key='-italics-', change_submits=True),
           sg.CB('Underline', key='-underline-', change_submits=True)],
          [sg.Slider((6, 50), default_value=12, size=(14, 20),
                     orientation='h', key='-slider-', change_submits=True),
           sg.Text('Font size')],
          [sg.Text('Font string = '), sg.Text('', size=(25, 1), key='-fontstring-')],
          [sg.Button('Exit')]]

window = sg.Window('Font string builder', layout)

text_elem = window['-text-']
while True:     # Event Loop
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    font_string = 'Helvitica '
    font_string += str(int(values['-slider-']))
    if values['-bold-']:
        font_string += ' bold'
    if values['-italics-']:
        font_string += ' italic'
    if values['-underline-']:
        font_string += ' underline'
    text_elem.update(font=font_string)
    window['-fontstring-'].update('"'+font_string+'"')
    print(event, values)

window.close()
