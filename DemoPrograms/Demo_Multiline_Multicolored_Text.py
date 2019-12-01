import PySimpleGUI as sg
# import PySimpleGUIQt as sg

"""
    Demonstration of how to work with multiple colors when outputting text to a multiline element
"""

sg.change_look_and_feel('Dark Blue 3')

MLINE_KEY = '-MLINE-'+sg.WRITE_ONLY_KEY
layout = [  [sg.Text('Demonstration of Multiline Element\'s ability to show multiple colors ')],
            [sg.Multiline(size=(60,20), key=MLINE_KEY)],
            [sg.B('Plain'), sg.Button('Text Blue Line'), sg.Button('Text Green Line'),sg.Button('Background Blue Line'),sg.Button('Background Green Line'), sg.B('White on Green')
             ]  ]

window = sg.Window('Demonstration of Multicolored Multline Text', layout)

while True:
    event, values = window.read()       # type: (str, dict)
    print(event, values)
    if event in (None, 'Exit'):
        break
    if 'Text Blue' in event:
        window[MLINE_KEY].update('This is blue text', text_color_for_value='blue', append=True)
    if 'Text Green' in event:
        window[MLINE_KEY].update('This is green text', text_color_for_value='green', append=True)
    if 'Background Blue' in event:
        window[MLINE_KEY].update('This is Blue Background', background_color_for_value='blue', append=True)
    if 'Background Green' in event:
        window[MLINE_KEY].update('This is Green Backgroundt', background_color_for_value='green', append=True)
    if 'White on Green' in event:
        window[MLINE_KEY].update('This is white text on a green background',  text_color_for_value='white', background_color_for_value='green', append=True)
    if event == 'Plain':
        window[MLINE_KEY].update('This is plain text with no extra coloring', append=True)
window.close()
