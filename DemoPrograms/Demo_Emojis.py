"""
    Demo - the PySimpleGUI helpers (emojis)

    The list of characters available to you to use in your messages.
    They are used internally when you get an error or as the icon for windows like
    the SDK help window.
    
    Copyright 2021 PySimpleGUI
"""


import PySimpleGUI as sg

layout = [[sg.Text('The PySimpleGUI Helpers', font='_ 20')],
          [sg.Text('Sometimes frustrated or tired....', font='_ 15')],
          [sg.Image(data=emoji) for emoji in sg.EMOJI_BASE64_SAD_LIST],
          [sg.Text('But they are usually happy!', font='_ 15')],
          [sg.Image(data=emoji) for emoji in sg.EMOJI_BASE64_HAPPY_LIST],
          [sg.Button('Bad Key'), sg.Button('Hello'), sg.Button('Exit')]  ]

window = sg.Window('The PySimpleGUI Helpers', layout, icon=sg.EMOJI_BASE64_HAPPY_JOY, keep_on_top=True)

while True:             # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Bad Key':
        elem = window['-IM-']
    elif event == 'Hello':
        sg.popup('Hi!', image=sg.EMOJI_BASE64_HAPPY_JOY, keep_on_top=True)

window.close()