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
          [sg.Canvas(size=(800,800), key='_canvas_')],
          [ sg.Button('F'), sg.Button('B'), sg.Button('L'), sg.Button('R')],
          [sg.Button('Spiral'), sg.Button('Inside Out'), sg.Button('Circles')]]

window = sg.Window('My new window').Layout(layout).Finalize()

canvas = window.FindElement('_canvas_').TKCanvas

t = turtle.RawTurtle(canvas)
t.pencolor("#ff0000") # Red

t.penup()
t.pendown()

while True:     # Event Loop
    event, values = window.Read()
    if event is None:
        break

    if event == 'F':
        t.forward(100)
    elif event == 'B':
        t.back(100)
    elif event == 'L':
        t.left(90)
    elif event == 'R':
        t.right(90)
    elif event == 'Spiral':
        canvas.config(bg='light green')
        t.color("blue")
        def sqrfunc(size):
            for i in range(4):
                t.fd(size)
                t.left(90)
                size = size - 5
        sqrfunc(146)
        sqrfunc(126)
        sqrfunc(106)
        sqrfunc(86)
        sqrfunc(66)
        sqrfunc(46)
        sqrfunc(26)
    elif event == 'Inside Out':
        canvas.config(bg = "light green")
        t.color("blue")
        def sqrfunc(size):
            for i in range(4):
                t.fd(size)
                t.left(90)
                size = size + 5
        sqrfunc(6)
        sqrfunc(26)
        sqrfunc(46)
        sqrfunc(66)
        sqrfunc(86)
        sqrfunc(106)
        sqrfunc(126)
        sqrfunc(146)
    elif event == 'Circles':
        t.speed(0)
        for i in range(400):
            t.circle(2 * i*.25)
            t.circle(-2 * i*.25)
            t.left(i)
