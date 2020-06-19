import PySimpleGUI as sg

"""
    Demo - Separator Elements

    Shows usage of both Horizontal and Vertical Separator Elements
    Vertical Separators are placed BETWEEN 2 elements ON the same row.  These work well when one
        of the elements is a Column or the element spans several rows

    Horizontal separators are placed BETWEEN 2 rows.  They will occupy the entire span of the row they
        are located on. If that row is constrained within a container, then it will spand the widget of
        the container.

    Copyright 2020 PySimpleGUI.org
"""


left_col = sg.Column([[sg.Listbox((1,2,3,4,5,6), size=(6,4))]])

right_col = sg.Column([[sg.Input(), sg.Input()],
            [sg.HorizontalSeparator()],
            [sg.Column([[sg.In()], [sg.HorizontalSeparator()]], pad=(0,0))],])

layout = [
        [sg.Text('Window with some separators')],
        [left_col, sg.VerticalSeparator(), right_col],
        [sg.Button('Go'), sg.Button('Exit')]
        ]

window = sg.Window('Window Title', layout)

while True:             # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
window.close()
