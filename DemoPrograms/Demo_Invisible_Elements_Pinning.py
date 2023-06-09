import PySimpleGUI as sg

"""
    Demo - "Pinning" an element into a location in a layout
    
    Requires PySimpleGUI version 4.28.0 and greater
    
    When using the tkinter port of PySimpleGUI, if you make an element invisible and then visible again,
    rather than the element appearing where it was originally located, it will be moved to the bottom
    of whatever it was contained within (a window or a container element (column, frame, tab))

    This demo uses a new "pin" function which will place the element inside of a Column element.  This will
    reserve a location for the element to be returned.
    
    Additionally, there will be a 1 pixel Canvas element inside the "pin". 
    This will cause the area to shrink when the element is made invisible. It's a weird tkinter thing. Not sure
    exactly why it works, but it works.
    
    For other ports of PySimpleGUI such as the Qt port, the position is remembered by Qt and as a
    result this technique using "pin" is not needed.
    
    Copyright 2020, 2022 PySimpleGUI.org
"""

layout = [  [sg.Text('Hide Button or Multiline. Buttons 1 & 2 hide Button 2')],
            [sg.pin(sg.Multiline(size=(60, 10), key='-MLINE-'))],
            [sg.pin(sg.Button('Button1')), sg.pin(sg.Button('Button2'), shrink=False), sg.B('Toggle Multiline')],
        ]

window = sg.Window('Visible / Invisible Element Demo', layout)

toggle = toggle_in = False
while True:             # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    if event in ('Button1', 'Button2'):
        window['Button2'].update(visible=toggle)
        toggle = not toggle
    elif event == 'Toggle Multiline':
        window['-MLINE-'].update(visible=not window['-MLINE-'].visible)
window.close()
