#!/usr/bin/env python
import PySimpleGUI as sg
from PIL import Image
import PIL
import io
import base64
import os

"""
    Demo Image Album.... displays images on Graph Element and transitions
    by sliding them across.  Click on right side of image to navigate down through filenames, left side for up.
    
    Contains a couple of handy PIL-based image functions that resize an image while maintaining correct proportion.
    One you pass a filename, the other a BASE64 string.
    
    Copyright 2020 PySimpleGUI.org
"""

G_SIZE = (400,400)

def get_img_filename(f, resize=None):
    """Generate image data using PIL
    """
    img = PIL.Image.open(f)
    cur_width, cur_height = img.size
    if resize:
        new_width, new_height = resize
        if cur_width > cur_height:
            new_height = int(new_height * cur_height/cur_width)
        else:
            new_width = int(new_width * cur_width/cur_height)
        img = img.resize((new_width, new_height), PIL.Image.ANTIALIAS)
    bio = io.BytesIO()
    img.save(bio, format="PNG")
    del img
    return bio.getvalue()


def get_img_data(data, resize=None):
    """Generate PIL.Image data using PIL
    """
    img = PIL.Image.open(io.BytesIO(base64.b64decode(data)))
    cur_width, cur_height = img.size
    if resize:
        new_width, new_height = resize
        if cur_width > cur_height:
            new_height = int(new_height * cur_height/cur_width)
        else:
            new_width = int(new_width * cur_width/cur_height)
        img = img.resize((new_width, new_height), PIL.Image.ANTIALIAS)
    bio = io.BytesIO()
    img.save(bio, format="PNG")
    del img
    return bio.getvalue()

folder = sg.popup_get_folder('Where are your images?')
if not folder:
    exit(0)

file_list = os.listdir(folder)
fnames = [f for f in file_list if os.path.isfile(
    os.path.join(folder, f)) and f.lower().endswith((".png", ".jpg", "jpeg", ".tiff", ".bmp"))]
num_files = len(fnames)

graph = sg.Graph(canvas_size=G_SIZE, graph_bottom_left=(0, 0), graph_top_right=G_SIZE, enable_events=True, key='-GRAPH-')
layout = [[graph]]

window = sg.Window('Scrolling Image Viewer', layout, margins=(0,0), element_padding=(0,0), use_default_focus=False, finalize=True)

offset, move_amount, direction  = 0, 5, 'left'
while True:
    file_to_display = os.path.join(folder, fnames[offset])
    img_data = get_img_filename(file_to_display, resize=G_SIZE)
    id = graph.draw_image(data=img_data, location=(0, G_SIZE[1]))

    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event in ('<', '>'):
        direction = 'left' if event == '<' else 'right'
    elif event == '-GRAPH-':
        direction = 'left' if values['-GRAPH-'][0] < (G_SIZE[0] // 2) else 'right'

    for i in range(G_SIZE[0]//move_amount):
        graph.move_figure(id, -move_amount if direction == 'left' else move_amount, 0)
        window.read(timeout=0)
    graph.delete_figure(id)

    if direction == 'left':
        offset = (offset + (num_files - 1)) % num_files     # Decrement - roll over to MAX from 0
    else:
        offset = (offset + 1) % num_files                   # Increment to MAX then roll over to 0

window.close()