#!/usr/bin/env python
import PySimpleGUI as sg
import turtle

"""
    Demo showing how to integrate drawing on a Canvas using  Turtle with PySimpleGUI
    The patern to follow:
        Create Window & Finalize
        Get the tkinter Canvas from the Canvas element
        Draw on the tkinter Canvas using turtle commands.
        Results are shown on the canvas immiedately after button press / drawing command
"""


layout = [[sg.Text('My layout')],
          [sg.Canvas(size=(800, 800), key='-canvas-')],
          [sg.Button('F'), sg.Button('B'), sg.Button('L'), sg.Button('R')],
          [sg.Button('Spiral'), sg.Button('Inside Out'), sg.Button('Circles')]]

window = sg.Window('My new window', layout, finalize=True)

canvas = window['-canvas-'].TKCanvas

a_turtle = turtle.RawTurtle(canvas)
a_turtle.pencolor("#ff0000")  # Red
a_turtle.penup()
a_turtle.pendown()

while True:     # Event Loop
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == 'F':
        a_turtle.forward(100)
    elif event == 'B':
        a_turtle.back(100)
    elif event == 'L':
        a_turtle.left(90)
    elif event == 'R':
        a_turtle.right(90)
    elif event == 'Spiral':
        canvas.config(bg='light green')
        a_turtle.color("blue")

        def sqrfunc(size):
            for i in range(4):
                a_turtle.fd(size)
                a_turtle.left(90)
                size = size - 5
        sqrfunc(146)
        sqrfunc(126)
        sqrfunc(106)
        sqrfunc(86)
        sqrfunc(66)
        sqrfunc(46)
        sqrfunc(26)
    elif event == 'Inside Out':
        canvas.config(bg="light green")
        a_turtle.color("blue")

        def sqrfunc(size):
            for i in range(4):
                a_turtle.fd(size)
                a_turtle.left(90)
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
        a_turtle.speed(0)
        for i in range(400):
            a_turtle.circle(2 * i*.25)
            a_turtle.circle(-2 * i*.25)
            a_turtle.left(i)
window.close()
