#!/usr/bin/env python
import PySimpleGUI as sg
from PIL import Image
import PIL
import io
import base64
import os

"""
    Demo Image Album.... displays images on Graph Element and has a visual "slide transition"
    
    
    Click on right side of image to navigate down through filenames, left side for up.
    
    PIL is required for this particular demo because it displays PNG, JPG, TIFF, BMP, GIF and ICO files
    
    Contains a couple of handy PIL-based image functions that resize an image while maintaining correct proportion.
    One you pass a filename, the other a BASE64 string.
    
    Copyright 2020 PySimpleGUI.org
"""

G_SIZE = (800,600)          # Size of the Graph in pixels. Using a 1 to 1 mapping of pixels to pixels

sg.theme('black')


def convert_to_bytes(file_or_bytes, resize=None):
    '''
    Will convert into bytes and optionally resize an image that is a file or a base64 bytes object.
    :param file_or_bytes: either a string filename or a bytes base64 image object
    :type file_or_bytes:  (str | bytes)
    :param resize:  optional new size
    :type resize: ((int, int) | None)
    :return: (bytes) a byte-string object
    :rtype: (bytes)
    '''
    if isinstance(file_or_bytes, str):
        img = PIL.Image.open(file_or_bytes)
    else:
        img = PIL.Image.open(io.BytesIO(base64.b64decode(file_or_bytes)))

    cur_width, cur_height = img.size
    if resize:
        new_width, new_height = resize
        scale = min(new_height/cur_height, new_width/cur_width)
        img = img.resize((int(cur_width*scale), int(cur_height*scale)), PIL.Image.ANTIALIAS)
    bio = io.BytesIO()
    img.save(bio, format="PNG")
    del img
    return bio.getvalue()

folder = sg.popup_get_folder('Where are your images?')
if not folder:
    exit(0)

file_list = os.listdir(folder)
fnames = [f for f in file_list if os.path.isfile(
    os.path.join(folder, f)) and f.lower().endswith((".png", ".jpg", "jpeg", ".tiff", ".bmp", ".gif", ".ico"))]
num_files = len(fnames)

graph = sg.Graph(canvas_size=G_SIZE, graph_bottom_left=(0, 0), graph_top_right=G_SIZE, enable_events=True, key='-GRAPH-', pad=(0,0))

layout = [  [sg.Text('Click on the right side of the window to navigate forward, the left side to go backwards')],
            [sg.Text(f'Displaying image: '), sg.Text(k='-FILENAME-')],
            [graph]]

window = sg.Window('Scrolling Image Viewer', layout, margins=(0,0),  use_default_focus=False, finalize=True)

offset, move_amount, direction  = 0, 5, 'left'

while True:
    file_to_display = os.path.join(folder, fnames[offset])
    window['-FILENAME-'].update(file_to_display)
    img_data = convert_to_bytes(file_to_display, resize=G_SIZE)
    image_id = graph.draw_image(data=img_data, location=(0, G_SIZE[1]))

    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    # if image is clicked, then move in the left direction if clicked on left half of the image
    if event == '-GRAPH-':
        direction = 'left' if values['-GRAPH-'][0] < (G_SIZE[0] // 2) else 'right'

    # Do the animation
    for i in range(G_SIZE[0]//move_amount):
        graph.move_figure(image_id, -move_amount if direction == 'left' else move_amount, 0)
        window.refresh()
    graph.delete_figure(image_id)

    # Bump the image index
    if direction == 'left':
        offset = (offset + (num_files - 1)) % num_files     # Decrement - roll over to MAX from 0
    else:
        offset = (offset + 1) % num_files                   # Increment to MAX then roll over to 0

window.close()