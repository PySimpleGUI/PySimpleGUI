import PySimpleGUI as sg
# import PySimpleGUIQt as sg

"""
    Demonstration of how to work with multiple colors and fonts when outputting text to a multiline element or with Debug Print
    
    Copyright 2021 PySimpleGUI
"""

MLINE_KEY = '-MLINE-'

layout = [  [sg.Text('Demonstration of Multiline Element\'s ability to show multiple colors ')],
            [sg.Multiline(size=(60,20), key=MLINE_KEY, reroute_cprint=True, write_only=True)],
            [sg.Input(k='-IN-')],
            [sg.B('Plain'), sg.Button('Text Blue Line'), sg.Button('Text Green Line')],
            [sg.Button('Background Blue Line'),sg.Button('Background Green Line'), sg.B('White on Green'), sg.B('Font Courier 12')]  ]

window = sg.Window('Demonstration of Multicolored Multline Text', layout)

# print = lambda *args, **kwargs: window[MLINE_KEY].print(*args, **kwargs, text_color='red')
mline:sg.Multiline = window[MLINE_KEY]
while True:
    event, values = window.read()       # type: (str, dict)
    print(event, values)
    sg.cprint(event, values,  c='white on green', font='courier 12')
    sg.Print(event,  c='white on green', font='courier 12', end='')
    sg.Print(values,  c='white on red', font='Courier 12 underline italic bold', end='')
    sg.Print('')
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    if 'Text Blue' in event:
        mline.update('This is blue text\n', text_color_for_value='blue', append=True)
    if 'Text Green' in event:
        mline.update('This is green text\n', text_color_for_value='green', append=True)
    if 'Background Blue' in event:
        mline.update('This is Blue Background\n', background_color_for_value='blue', append=True)
    if 'Background Green' in event:
        mline.update('This is Green Background\n', background_color_for_value='green', append=True)
    if 'Font' in event:
        mline.update('This is Green Background\n', background_color_for_value='green', append=True, font_for_value=('Courier', 12, 'underline'))
        mline.print('\nThis is Green Background\n', c='white on green', font='Courier 12 bold ')
    if 'White on Green' in event:
        mline.update('This is white text on a green background\n',  text_color_for_value='white', background_color_for_value='green', append=True)
    if event == 'Plain':
        mline.update('This is plain text with no extra coloring\n', append=True)
window.close()
