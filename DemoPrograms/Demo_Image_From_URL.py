import PySimpleGUI as sg
import urllib.request

"""
    Display an Image Located at a URL

    Downloads and displays a PNG (or GIF) image given a URL
    
    NOTE:
        Early versions of tkinter (for example 8.6.6 found in Python 3.6) have trouble with some PNG formats.
        Moving to Python 3.7 fixes this or you can use a tool to re-encode the image (e.g. psgresizer) save it and 
        it will then work OK in Python 3.6.
        Example of one of these images - https://www.python.org/static/community_logos/python-logo-master-v3-TM.png

    Copyright 2022 PySimpleGUI.org
"""


image_URL = r'https://upload.wikimedia.org/wikipedia/commons/4/47/PNG_transparency_demonstration_1.png'

layout = [[sg.Image(urllib.request.urlopen(image_URL).read())]]

window = sg.Window('Image From URL', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

window.close()


