from PIL import Image, ImageTk, ImageSequence
import PySimpleGUI as sg

"""
    Demo_Animated_GIFs_Using_PIL.py
    
    You'll find other animated GIF playback demos for PySimpleGUI that use the tkinter built-in GIF parser.
    That is how the built-in PySimpleGUI Image.update_animation is used.
    
    If you want to do the GIF file parsing yourself using PIL and update your Image element yourself, then
    this is one possible technique.

    This particular demo will loop playing the GIF file over and over.  To not loop, remove the while True statement.
    Copyright 2020 PySimpleGUI.org
"""

gif_filename = r'ExampleGIF.gif'

layout = [[sg.Text('Happy Thursday!', background_color='#A37A3B', text_color='#FFF000',  justification='c', key='-T-', font=("Bodoni MT", 40))],
          [sg.Image(key='-IMAGE-')]]

window = sg.Window('Window Title', layout, element_justification='c', margins=(0,0), element_padding=(0,0), finalize=True)

window['-T-'].expand(True, True, True)      # Make the Text element expand to take up all available space

interframe_duration = Image.open(gif_filename).info['duration']     # get how long to delay between frames

while True:
    for frame in ImageSequence.Iterator(Image.open(gif_filename)):
        event, values = window.read(timeout=interframe_duration)
        if event == sg.WIN_CLOSED:
            exit(0)
        window['-IMAGE-'].update(data=ImageTk.PhotoImage(frame) )