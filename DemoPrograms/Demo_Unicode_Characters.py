#!/usr/bin/env python
import PySimpleGUI as sg
from random import randint as randint

"""
    To get a good display of the unicode characters visit https://en.wikipedia.org/wiki/List_of_Unicode_characters
    You can directly copy and paste characters from the site into your strings.
    Unicode characters make it possible to add simple graphics to your windows by using text.  No Base64 required. They're plain chars.
    They're good for a quick status display / dashboard, for use on buttons (arrows), or as "simple clipart" to name a few uses
"""

sg.theme('Light Brown 4')

SQUARE = '█'
CIRCLE = '⚫'
CIRCLE_OUTLINE = '◯'
UP =    '▲'
RIGHT = '►'
DOWN =  '▼'
LEFT =  '◄'
ROAD = '⛖'

layout = [  [sg.Text('Unicode Characters Demo', font='Def 16')],
            [sg.T('Network Status', size=(12,1)), sg.Text(size=(10,1), font='Default 18', text_color='green', key='-OUT1-')],
            [sg.T('Gas Level', size=(12,1)), sg.Text(size=(10,1), font='Default 18', text_color='green', key='-OUT2-')],
            [sg.T('Oil Temp', size=(12,1)), sg.Text(size=(10,1), font='Default 18', text_color='blue', key='-OUT3-')],
            [sg.T('Status4', size=(12,1)), sg.Text(CIRCLE, size=(10,1), font='Default 18', text_color='green', key='-OUT4-')],
            [sg.T('Status5', size=(12,1)), sg.Text(CIRCLE_OUTLINE, size=(10,1), font='Default 18', text_color='green', key='-OUT5-')],
            [sg.Frame('Unicode Converter',
                    [[sg.T('Enter a Number'), sg.In(size=(6,1), key='-NUM-'), sg.T('Unicode char: '), sg.I(size=(2,1), font='Any 18', key='-OUT CHAR-')],
                    [sg.T('Enter a Char'), sg.In(size=(2,1), key='-CHAR-', font='Any 18'), sg.T('Unicode number: '), sg.T(size=(6,1), key='-OUT NUM-')]])],
            [sg.Frame('Display Unicode Characters In Range',
                      [[sg.T('Starting Number'), sg.In(size=(6, 1), key='-START-'), sg.T('Ending Number char: '), sg.I(size=(6, 1),  key='-END-')],
                       [sg.B('Display Chars', bind_return_key=True), sg.T('Display Font Size'),  sg.Spin(list(range(10,25)), initial_value=18, font='Any 14', key='-FONTSIZE-')],
                      ])],
            [sg.Multiline(size=(30,10), font='Any 18',key='-MLINE-'+sg.WRITE_ONLY_KEY)],
            [sg.B(UP), sg.B(DOWN), sg.B(LEFT), sg.B(RIGHT), sg.B('Exit')]  ]

window = sg.Window('Window Title', layout)

i = j = 0
multiline_font_size = 18
while True:
    event, values = window.read(timeout=200)
    print(f'{event} - {values}') if event != sg.TIMEOUT_KEY else None
    if event in (sg.WIN_CLOSED, 'Exit'):  # always,  always give a way out!
        break
    elif event == RIGHT:
        window['-OUT2-'](text_color='blue')
        window['-OUT5-']((UP,DOWN,RIGHT,LEFT)[j%4])
        window['-OUT5-'](chr(ord(ROAD)+j))
        j = j +1
    elif event == LEFT:
        window['-OUT2-'](text_color='yellow')
    elif event == UP:
        window['-OUT1-'](text_color='green')
        window['-OUT3-'](text_color='green')
        window['-OUT4-'](text_color='green')
    elif event == DOWN:
        window['-OUT1-'](text_color='red')
        window['-OUT3-'](text_color='red')
        window['-OUT4-'](text_color='red')
    elif event.startswith('Display'):               # process the dump range section
        try:
            for c in range(int(values['-START-']), int(values['-END-'])):
                window['-MLINE-'+sg.WRITE_ONLY_KEY](chr(c), append=True, text_color_for_value='red')
                window.refresh()
                sg.popup_animated(sg.DEFAULT_BASE64_LOADING_GIF, 'Writing chars to display', text_color='red', font='Any 20', time_between_frames=100)
        except: pass
        sg.popup_animated(None)

    window['-OUT1-']('◯' if i % randint(1,3) else '⚫')
    window['-OUT2-'](SQUARE * (i%10))
    window['-OUT3-'](SQUARE * (7-(i%8)))

    if multiline_font_size != int(values['-FONTSIZE-']):
        window['-MLINE-'+sg.WRITE_ONLY_KEY](font='Any '+ str(values['-FONTSIZE-']))
        multiline_font_size = int(values['-FONTSIZE-'])

    if not i % 15:
        window['-OUT1-'](text_color='red')
    i += 1
    # Output stuff for Unicode Converter Section
    try:
        window['-OUT CHAR-'](chr(int(values['-NUM-'])))
    except: pass
    try:
        window['-OUT NUM-'](ord(values['-CHAR-']))
    except: pass

window.close()
