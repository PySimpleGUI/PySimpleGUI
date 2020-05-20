import PySimpleGUI as sg

"""
    Demo - Splash Screen
    
    Displays a PNG image with transparent areas as see-through on the center
    of the screen for a set amount of time.
    
    Copyright 2020 PySimpleGUI.org
"""

IMAGE_FILE = r'A:\- TEMP 2019 -\PySimpleGUI_Logo.png'
DISPLAY_TIME_MILLISECONDS = 4000

sg.Window('Window Title', [[sg.Image(IMAGE_FILE)]], transparent_color=sg.theme_background_color(), no_titlebar=True, keep_on_top=True).read(timeout=DISPLAY_TIME_MILLISECONDS, close=True)

