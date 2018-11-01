#!/usr/bin/env python
import sys
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg

layout = [[sg.Text('This is my sample text',size=(20,1), key='_text_') ],
          [sg.CB('Bold', key='_bold_', change_submits=True),
           sg.CB('Italics', key='_italics_', change_submits=True),
           sg.CB('Underline', key='_underline_', change_submits=True)],
          [sg.Slider((6,50), default_value=12, size=(14,20), orientation='h', key='_slider_', change_submits=True),
           sg.Text('Font size')],
          [sg.Text('Font string = '), sg.Text('', size=(25,1), key='_fontstring_')],
          [ sg.Button('Exit')]]

window = sg.Window('Font string builder').Layout(layout)

text_elem = window.FindElement('_text_')
while True:     # Event Loop
    event, values = window.Read()
    if event in (None, 'Exit'):
        break
    font_string = 'Helvitica '
    font_string += str(values['_slider_'])
    if values['_bold_']:
        font_string += ' bold'
    if values['_italics_']:
        font_string += ' italic'
    if values['_underline_']:
        font_string += ' underline'
    text_elem.Update(font=font_string)
    window.FindElement('_fontstring_').Update('"'+font_string+'"')
    print(event, values)
