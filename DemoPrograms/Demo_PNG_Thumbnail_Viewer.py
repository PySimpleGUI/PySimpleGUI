#!/usr/bin/env python
import PIL
from PIL import Image
from sys import exit
import PySimpleGUI as sg
import os
import io
import base64

"""
    Demo PNG Thumbnail Viewer

    Displays PNG files from a folder.
    
    OK, so... this isn't the best Demo Program, that's for sure.  It's one of the older
    demos in the repo.  There are likely better ones to use.  The convert_to_bytes function is
    the best thing in this demo.

    Copyright 2021 PySimpleGUI.org
"""


thumbnails = {}
ROWS = 8
COLUMNS = 8
sg.set_options(border_width=0)
# Get the folder containing the images from the user
folder = sg.popup_get_folder('Image folder to open')
if folder is None:
    sg.popup_cancel('Cancelling')
    exit(0)




def convert_to_bytes(file_or_bytes, resize=None):
    """
    Will convert into bytes and optionally resize an image that is a file or a base64 bytes object.
    Turns into  PNG format in the process so that can be displayed by tkinter
    :param file_or_bytes: either a string filename or a bytes base64 image object
    :type file_or_bytes:  (Union[str, bytes])
    :param resize:  optional new size
    :type resize: (Tuple[int, int] or None)
    :param fill: If True then the image is filled/padded so that the image is not distorted
    :type fill: (bool)
    :return: (bytes) a byte-string object
    :rtype: (bytes)
    """
    if isinstance(file_or_bytes, str):
        img = PIL.Image.open(file_or_bytes)
    else:
        try:
            img = PIL.Image.open(io.BytesIO(base64.b64decode(file_or_bytes)))
        except Exception as e:
            dataBytesIO = io.BytesIO(file_or_bytes)
            img = PIL.Image.open(dataBytesIO)

    cur_width, cur_height = img.size
    if resize:
        new_width, new_height = resize
        scale = min(new_height / cur_height, new_width / cur_width)
        img = img.resize((int(cur_width * scale), int(cur_height * scale)), PIL.Image.ANTIALIAS)
    with io.BytesIO() as bio:
        img.save(bio, format="PNG")
        del img
        return bio.getvalue()
#
# old, original PIL code.
# def image_file_to_bytes(filename, size):
#     try:
#         image = Image.open(filename)
#         image.thumbnail(size, Image.ANTIALIAS)
#         bio = io.BytesIO()  # a binary memory resident stream
#         image.save(bio, format='PNG')  # save image as png to it
#         imgbytes = bio.getvalue()
#     except:
#         imgbytes = None
#     return imgbytes


def set_image_to_blank(key):
    img = PIL.Image.new('RGB', (100, 100), (255, 255, 255))
    img.thumbnail((1, 1), PIL.Image.ANTIALIAS)
    bio = io.BytesIO()
    img.save(bio, format='PNG')
    imgbytes = bio.getvalue()
    window[key].update(image_data=imgbytes)


# get list of PNG files in folder
png_files = [os.path.join(folder, f)
             for f in os.listdir(folder) if f.endswith('.png')]
filenames_only = [f for f in os.listdir(folder) if f.endswith('.png')]

if len(png_files) == 0:
    sg.popup('No PNG images in folder')
    exit(0)

# define menu layout
menu = [['&File', ['&Open Folder', 'E&xit']], ['&Help', ['&About', ]]]

buttons = []
for display_index in range(ROWS):
    row = []
    for j in range(COLUMNS):
        row.append(sg.Button('', border_width=0,
                        button_color=sg.COLOR_SYSTEM_DEFAULT, key=(display_index, j)))
    buttons.append(row)

col_buttons = [[]]

# define layout, show and read the window
col = [[sg.Text(png_files[0], size=(80, 3), key='filename')],
       [sg.Image(data=convert_to_bytes(png_files[0], (500, 500)), key='image')], ]

layout = [
    [sg.Menu(menu)],
    [sg.Col(buttons), sg.Col([[sg.Slider((len(png_files), 0), default_value=0, size=(38, 20), orientation='v', key='-slider-', change_submits=True)]]), sg.Col(col)]
]

window = sg.Window('Image Browser', layout,
                   return_keyboard_events=True,
                   use_default_focus=False, finalize=True)

# -------========= Event Loop =========--------
display_index = 0
while True:
    
    for x in range(ROWS):               # update thumbnails
        for y in range(COLUMNS):
            cur_index = display_index + (x * COLUMNS) + y
            if cur_index < len(png_files):
                filename = png_files[cur_index]
                if filename not in thumbnails:
                    imgbytes = convert_to_bytes(filename, (100, 100))
                    thumbnails[filename] = imgbytes
                else:
                    imgbytes = thumbnails[filename]
                button_elem = window[(x, y)]
                button_elem.update(image_data=imgbytes)
            else:
                set_image_to_blank((x, y))

    event, values = window.read()
    display_index = int(values['-slider-'])
    # --------------------- Button & Keyboard ---------------------
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    elif event in ('MouseWheel:Down', 'Down:40',) and display_index < len(png_files)-1:
        display_index += 4
    elif event in ('MouseWheel:Up', 'Up:38',) and display_index > 0:
        display_index -= 4
    elif event in ('Prior:33', 'Prev'):
        display_index -= 16
    elif event in ('Next:34', 'Next'):
        display_index += 16

    window['-slider-'].update(display_index)
    # ----------------- Menu choices -----------------
    if event == 'Open Folder':
        newfolder = sg.popup_get_folder('New folder', no_window=True)
        if newfolder is None:
            continue
        folder = newfolder
        png_files = [os.path.join(folder, f)
                     for f in os.listdir(folder) if '.png' in f]
        filenames_only = [f for f in os.listdir(folder) if '.png' in f]
        display_index = 0
        thumbnail = {}
        for j in range(ROWS):
            for i in range(COLUMNS):
                set_image_to_blank((i, j))
    elif event == 'About':
        sg.popup('Demo PNG Viewer Program', 'Please give PySimpleGUI a try!')
    elif type(event) is tuple:
        x, y = event
        image_index = display_index + (x * COLUMNS) + y
        if image_index < len(png_files):
            filename = png_files[image_index]
            imgbytes = convert_to_bytes(filename, (500, 500))
            window['image'].update(data=imgbytes)
            window['filename'].update(filename)

window.close()
