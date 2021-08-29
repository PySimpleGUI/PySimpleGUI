import PySimpleGUI as sg

"""
    Demo Element Justification In A Window Using A Text Element That Expands

    How to Justify elements on 1 row to be left, right or left, middle, right

    Additionally, locate these buttons at the bottom of the screen

    The key concepts to use are the newly added expand_x and expand_y

    To get 2 buttons to be all the way to the left and to the far right, then
        you want to place a text element between them that expands
    If you want a third button that is centered, then add TWO Text elements, one
        on each side of the middle one

    Copyright 2021 PySimpleGUI
"""


layout = [  [sg.Text('Window with elements on the left and the right')],
            [sg.T('Using a text element that expands enables you to "push" other elements around')],
            [sg.HorizontalSeparator()],
            [sg.T(expand_y=True, pad=(0,0), font='_ 1')],   # Take as little room as possible
            [sg.Button('Left'), sg.Text(expand_x=True, pad=(0,0)), sg.Button('Right')],
            [sg.Text(expand_x=True), sg.B('Right')],
            [sg.Button('Left'), sg.Text(expand_x=True, pad=(0,0)), sg.B('Middle'), sg.Text(expand_x=True, pad=(0,0)),  sg.Button('Right')]  ]

window = sg.Window('Left and Right Justification', layout, resizable=True)

while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

window.close()
