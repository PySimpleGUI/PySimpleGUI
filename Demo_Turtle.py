#!/usr/bin/env python
import sys
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg

import turtle

"""
    Demo showing how to integrate drawing on a Canvas using  Turtle with PySimpleGUI
    The patern to follow:
        Create Window & Finalize
        Get the tkinter Canvas from the Canvas element
        Draw on the tkinter Canvas using turtle commands.
        Results are shown on the canvas immiedately after button press / drawing command
"""


layout = [[ sg.Text('My layout') ],
          [sg.Canvas(size=(500,500), key='_canvas_')],
          [ sg.RButton('F'), sg.RButton('B'), sg.RButton('L'), sg.RButton('R')]]

window = sg.Window('My new window').Layout(layout).Finalize()

canvas = window.FindElement('_canvas_').TKCanvas

t = turtle.RawTurtle(canvas)
t.pencolor("#ff0000") # Red

t.penup()   # Regarding one of the comments
t.pendown() # Regarding one of the comments

while True:     # Event Loop
    button, value = window.Read()
    if button is None:
        break

    if button == 'F':
        t.forward(100)
    elif button == 'B':
        t.back(100)
    elif button == 'L':
        t.left(90)
    elif button == 'R':
        t.right(90)

