import PySimpleGUI as sg

"""
    VPush Element

    In version 4.49.0 a new VPush Element was added.
    It is not "True Element" but rather a "User Defined Element" because it's a function
        that returns elements versus a class based on the Element class.
    It's not an important detail in the use of it.
    
    Use a VPush to "Push" your elements vertically away from it.  
        * If you put one at the top of your layout, then your layout will be "pushed" to the bottom of the window.
        * If you put a VPush at the top and bottom of your layout, then your layout will be centered
        
    This Demo Program shows the "centered" use case.
    
     
    Copyright 2022 PySimpleGUI
"""


layout = [  [sg.VPush()],
            [sg.Text('Resize me to see that I am vertically centered')],
            [sg.In()],
            [sg.In()],
            [sg.Button('Go'), sg.Button('Exit'), sg.Cancel(), sg.Ok()],
            [sg.VPush(), sg.Sizegrip()] ]           # toss a Sizegrip onto the bottom corner to make it easier


window = sg.Window('Window Title', layout, resizable=True)

window.read(close=True)

