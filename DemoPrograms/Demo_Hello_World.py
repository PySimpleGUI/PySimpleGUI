import PySimpleGUI as sg

"""
    Oh yes, the classic "Hello World". The problem is that you
    can do it so many ways using PySimpleGUI
    
    Copyright 2023 PySimpleSoft, Inc. and/or its licensors. All rights reserved.
    
    Redistribution, modification, or any other use of PySimpleGUI or any portion thereof is subject to the terms of the PySimpleGUI License Agreement available at https://eula.pysimplegui.com.
    
    You may not redistribute, modify or otherwise use PySimpleGUI or its contents except pursuant to the PySimpleGUI License Agreement.
"""

sg.popup_no_buttons('Hello World')         # the single line

# single line using a real window
sg.Window('Hello world', [[sg.Text('Hello World')]]).read()

# This is a "Traditional" PySimpleGUI window code. First make a layout, then a window, the read it
layout = [[sg.Text('Hello World')]]
window = sg.Window('Hello world', layout)
event, values = window.read()

window.close()
