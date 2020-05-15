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

gif_filename = r'my_gif_file.gif'

layout = [[sg.Image(key='-IMAGE-')]]

window = sg.Window('Window Title', layout, element_justification='c', margins=(0,0), element_padding=(0,0), finalize=True)

sequence = [ImageTk.PhotoImage(img) for img in ImageSequence.Iterator(Image.open(gif_filename))]    # must has finalized to do this

interframe_duration = Image.open(gif_filename).info['duration']     # get how long to delay between frames

while True:
    for frame in sequence:
        event, values = window.read(timeout=interframe_duration)
        if event == sg.WIN_CLOSED:
            exit()
        window['-IMAGE-'].update(data=frame)
