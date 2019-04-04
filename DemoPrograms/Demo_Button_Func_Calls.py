#!/usr/bin/env python
import sys
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg


"""
Demo Button Function Calls
Typically GUI packages in Python (tkinter, Qt, WxPython, etc) will call a user's function
when a button is clicked.  This "Callback" model versus "Message Passing" model is a fundamental
difference between PySimpleGUI and all other GUI.

There are NO BUTTON CALLBACKS in the PySimpleGUI Architecture

It is quite easy to simulate these callbacks however.  The way to do this is to add the calls
to your Event Loop
"""

def callback_function1():
    sg.Popup('In Callback Function 1')
    print('In the callback function 1')

def callback_function2():
    sg.Popup('In Callback Function 2')
    print('In the callback function 2')

layout = [ [sg.Text('Demo of Button Callbacks')],
           [sg.Button('Button 1'), sg.Button('Button 2')] ]

window = sg.Window('Button Callback Simulation').Layout(layout)

while True:             # Event Loop
    event, values = window.Read()
    if event is None:
        break
    elif event == 'Button 1':
        callback_function1()        # call the "Callback" function
    elif event == 'Button 2':
        callback_function2()        # call the "Callback" function

window.Close()
