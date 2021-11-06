#!/usr/bin/env python
import PySimpleGUI as sg
import os

"""
    Demo Image Album... NO PIL version.... displays images on Graph Element and has a visual "slide transition"

    Click on right side of image to navigate down through filenames, left side for up.

    Same program as the Demo_Graph_Elem_Image_Album.py, but without using PIL

    Not using PIL has 2 impacts:
    1. The images are not resized to fit the window
    2. The images are limited to PNG and GIF files

    Copyright 2021 PySimpleGUI.org
"""

G_SIZE = (800, 600)  # Size of the Graph in pixels. Using a 1 to 1 mapping of pixels to pixels

sg.theme('black')
folder = sg.popup_get_folder('Where are your images?')
if not folder:
    exit(0)

file_list = os.listdir(folder)
fnames = [f for f in file_list if os.path.isfile(
    os.path.join(folder, f)) and f.lower().endswith((".png", ".gif"))]
num_files = len(fnames)

graph = sg.Graph(canvas_size=G_SIZE, graph_bottom_left=(0, 0), graph_top_right=G_SIZE, enable_events=True, key='-GRAPH-', pad=(0, 0))

layout = [[sg.Text('Click on the right side of the window to navigate forward, the left side to go backwards')],
          [sg.Text(f'Displaying image: '), sg.Text(k='-FILENAME-')],
          [graph]]

window = sg.Window('Scrolling Image Viewer', layout, margins=(0, 0), use_default_focus=False, finalize=True)

offset, move_amount, direction = 0, 5, 'left'

while True:
    file_to_display = os.path.join(folder, fnames[offset])
    window['-FILENAME-'].update(file_to_display)

    image_id = graph.draw_image(filename=file_to_display, location=(0, G_SIZE[1]))

    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    # if image is clicked, then move in the left direction if clicked on left half of the image
    if event == '-GRAPH-':
        direction = 'left' if values['-GRAPH-'][0] < (G_SIZE[0] // 2) else 'right'

    # Do the animation
    for i in range(G_SIZE[0] // move_amount):
        graph.move_figure(image_id, -move_amount if direction == 'left' else move_amount, 0)
        window.refresh()
    graph.delete_figure(image_id)

    # Bump the image index
    if direction == 'left':
        offset = (offset + (num_files - 1)) % num_files  # Decrement - roll over to MAX from 0
    else:
        offset = (offset + 1) % num_files  # Increment to MAX then roll over to 0

window.close()
