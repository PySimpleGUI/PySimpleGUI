import PySimpleGUI as sg

"""
    Demo - "Pinning" an element into a location in a layout

    When using the tkinter port of PySimpleGUI, if you make an element invisible and then visible again,
    rather than the element appearing where it was originally located, it will be moved to the bottom
    of whatever it was contained within (a window or a container element (column, frame, tab))

    This demo adds a function "pin" which will place the element inside of a Column element.  This will
    reserve a location for the element to be returned.
    
    For other ports of PySimpleGUI such as the Qt port, the position is remembered by Qt and as a
    result this technique using Columns is not needed.
    
    Copyright 2020 PySimpleGUI.org
"""

def pin(elem):
    '''
    Pin's an element provided into a layout so that when it's made invisible and visible again, it will
     be in the correct place.  Otherwise it will be placed at the end of its containing window/column.

    :param elem: the element to put into the layout
    :return: A column element containing the provided element
    '''
    return sg.Column([[elem, sg.Canvas(size=(0,0), pad=(0,0))]], pad=(0,0))


layout = [  [sg.Text('Window with Hidden Button')],
            [sg.Input(key='-IN-')],
            [pin(sg.Button('Button1')), pin(sg.Button('Button2')), sg.B('Button3')],
        ]

window = sg.Window('Window Title', layout)

toggle = False
while True:             # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    window['Button2'].update(visible=toggle)
    toggle = not toggle

window.close()
