#!/usr/bin/env python

"""
    Demo Thumbnail Grid Image Viewer
    Displays image files from a folder.
    
    Probably the best Demo Program, according to a sample of 1 PyAutoGUI user(s)
    that tried to study it in 2023!

    Copyright 2021-2023 PySimpleGUI.org
"""

from pathlib import Path
import io
import base64

import PIL
from PIL import Image
import PySimpleGUI as sg

thumbnails = {}
img_files = []
    
ROWS = 8
COLUMNS = 8

sg.set_options(border_width=0)

def valid_image(path):
    if not path.is_file():
        return False
    elif path.suffix.lower() in ('.png', '.jpg', '.jpeg', '.gif', '.tif'):
        return True
    else:
        try:
            PIL.Image.open(path)
            return True
        except:
            return False

def convert_to_bytes(path_or_bytes, resize=None):
    """
    Will convert into bytes and optionally resize an image that is a file or a base64 bytes object.
    Turns into  PNG format in the process so that can be displayed by tkinter
    :param path_or_bytes: either a string filename or a bytes base64 image object
    :type path_or_bytes:  (Union[pathlib.Path, bytes])
    :param resize:  optional new size
    :type resize: (Tuple[int, int] or None)
    :param fill: If True then the image is filled/padded so that the image is not distorted
    :type fill: (bool)
    :return: (bytes) a byte-string object
    :rtype: (bytes)
    """
    if isinstance(path_or_bytes, Path):
        img = PIL.Image.open(path_or_bytes)
    else:
        try:
            img = PIL.Image.open(io.BytesIO(base64.b64decode(path_or_bytes)))
        except Exception as e:
            dataBytesIO = io.BytesIO(path_or_bytes)
            img = PIL.Image.open(dataBytesIO)

    cur_width, cur_height = img.size
    if resize:
        new_width, new_height = resize
        scale = min(new_height / cur_height, new_width / cur_width)
        img = img.resize((int(cur_width * scale), int(cur_height * scale)), PIL.Image.LANCZOS)
    with io.BytesIO() as bio:
        img.save(bio, format="PNG")
        del img
        return bio.getvalue()

def blank_image(size_tuple):
    img = PIL.Image.new('RGB', size_tuple, (255, 255, 255))
    bio = io.BytesIO()
    img.save(bio, format='PNG')
    return bio.getvalue()
    
def set_image_to_blank(key, blank_imgbytes=blank_image((100, 100))):
    window[key].update(image_data=blank_imgbytes)

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
col = [ 
   [sg.Text('Select a folder with images.', size=(80, 3), key='filename')],
   [sg.Image(data=blank_image((500, 1)), key='image')],
   [sg.Button('Open Folder', size=(8, 2)),
    sg.Button('Prev', size=(8, 2)), sg.Button('Next', size=(8, 2))
    ],   
]

layout = [
    [sg.Menu(menu)],
    [sg.Col(buttons),
#      sg.Col([[sg.Slider((len(img_files), 0),
#      default_value=0, size=(38, 20),
#      orientation='v', key='-slider-',
#      change_submits=True)]]),
     sg.Col(col)
    ]
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
            if cur_index < len(img_files):
                filename = img_files[cur_index]
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
    #display_index = int(values['-slider-'])
    # --------------------- Button & Keyboard ---------------------
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    elif event in ('MouseWheel:Down', 'Down:40',):
        display_index += COLUMNS
    elif event in ('MouseWheel:Up', 'Up:38',):
        display_index -= COLUMNS
    elif event in ('Prior:33', 'Prev'):
        display_index -= COLUMNS * ROWS
    elif event in ('Next:34', 'Next'):
        display_index += COLUMNS * ROWS
    if display_index < 0:
        display_index = 0
    if display_index >= len(img_files) - COLUMNS * ROWS:
        display_index = len(img_files) - COLUMNS * ROWS - 1
    #window['-slider-'].update(display_index)
    # ----------------- Menu choices -----------------
    if event == 'Open Folder':
        newfolder = sg.popup_get_folder('New folder', no_window=True)
        if newfolder is None:
            continue
        folder = Path(newfolder)
        img_files = [f for f in folder.iterdir() if valid_image(f)]
        display_index = 0
        thumbnail = {}
        for j in range(ROWS):
            for i in range(COLUMNS):
                set_image_to_blank((i, j))
        window['image'].update(data=blank_image((500, 2)))
        message = ('\n\nClick on thumbnails to see enlarged images.\n'
                   if img_files else '\n\nNo readable images found.\n')
        window['filename'].update(f'Folder selected: {folder}' + message)

    elif event == 'About':
        sg.popup('Demo Thumbnail Grid Image Viewer Program', 'Please give PySimpleGUI a try!')
    elif type(event) is tuple:
        x, y = event
        image_index = display_index + (x * COLUMNS) + y
        if image_index < len(img_files):
            filename = img_files[image_index]
            imgbytes = convert_to_bytes(filename, (500, 500))
            window['image'].update(data=imgbytes)
            window['filename'].update(filename)

window.close()
