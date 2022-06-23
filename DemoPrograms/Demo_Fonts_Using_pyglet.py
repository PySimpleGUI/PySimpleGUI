import pyglet
import PySimpleGUI as sg
import os

"""
    Demo - Using pyglet to get custom fonts into PySimpleGUI

    Original code by @jason990420 

    Copyright 2022 PySimpleGUI
    
    Font information:
        Copyright (c) 2020, Walter E Stewart,
        with Reserved Font Name Open Flame.
        https://www.1001freefonts.com/open-flame.font
        This Font Software is licensed under the SIL Open Font License, Version 1.1.
        This license is copied below, and is also available with a FAQ at:
        http://scripts.sil.org/OFL
"""

font_file = os.path.join(os.path.dirname(__file__), "OpenFlame.ttf")

pyglet.font.add_file(font_file)

# sg.execute_command_subprocess(font_file)
font1 = ("Open Flame", 40)      # Note - use the font "face name" not the filename when specifying the font
font2 = ("Courier New", 40)
font3 = ("Helvetica", 40)
text_string = "ABCDEFG abcdefg 1234567890"

layout = [  [sg.Text(text_string, font=font1)],
            [sg.Text(text_string, font=font2)],
            [sg.Text(text_string, font=font3)]  ]

window = sg.Window('Adding Fonts', layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break

window.close()
