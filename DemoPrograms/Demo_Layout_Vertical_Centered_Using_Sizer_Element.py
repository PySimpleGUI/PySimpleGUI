import PySimpleGUI as sg

"""
    Sizer Element

    Using a Sizer Element to set the size of a window without setting the size on the Window.

    If you use the size parameter for a window, you may end up cutting off a portion of your Window
        if the contents of layout are greater in size than the hard coded size you used.

    You can use a Sizer element to "pad" a layout into something bigger.

    This Element is actually implemented using a Column inside of PySimpleGUI so it's not an
    element in reality, but more along the lines of a User Defined Element

    This demo shows how you can make a 500x500 pixel window without hardcoding the size and while
        also centering the contents of your layout.

    Copyright 2021 PySimpleGUI
"""


# "Centered in a large Window" version
# A simple layout that you want to "center" in the middle of a 500 x 500 pixel window (not counting titlebar)
layout = [  [sg.Text('My Window')],
            [sg.In()],
            [sg.In()],
            [sg.Button('Go'), sg.Button('Exit'), sg.Cancel(), sg.Ok()]  ]

# If you wanted to center it in a window, just put into a Column element
# and use the Sizer element to "pad" the layout

# The entire layout is a single row with a sizer that is 500 pixels high.
# Because elements on a row center themselves vertically, you'll end up with the layout centered vertically
layout = [[sg.Sizer(0,500), sg.Column([[sg.Sizer(500,0)]] + layout, element_justification='c', pad=(0,0))]]

window = sg.Window('Window Title', layout, margins=(0,0))

window.read(close=True)

