#!/usr/bin/env python
import sys
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg
import os
from sys import exit as exit
from  PIL import Image
import io
import numpy as np

thumbnails = {}

ROWS = 8
COLUMNS = 8
sg.SetOptions(border_width=0)
# Get the folder containing the images from the user
# folder = 'A:/TEMP/pdfs'
folder = sg.PopupGetFolder('Image folder to open')
if folder is None:
    sg.PopupCancel('Cancelling')
    exit(0)
def image_file_to_bytes(filename, size):
    try:
        image = Image.open(filename)
        image.thumbnail(size, Image.ANTIALIAS)
        bio = io.BytesIO()  # a binary memory resident stream
        image.save(bio, format='PNG')  # save image as png to it
        imgbytes = bio.getvalue()
    except:
        imgbytes = None
    return imgbytes

def set_image_to_blank(key):
    img = Image.new('RGB', (100, 100), (255, 255, 255))
    img.thumbnail((1, 1), Image.ANTIALIAS)
    bio = io.BytesIO()
    img.save(bio, format='PNG')
    imgbytes = bio.getvalue()
    window.FindElement(key).Update(image_data=imgbytes)



# get list of PNG files in folder
png_files = [os.path.join(folder, f) for f in os.listdir(folder) if '.png' in f]
filenames_only = [f for f in os.listdir(folder) if '.png' in f]

if len(png_files) == 0:
    sg.Popup('No PNG images in folder')
    exit(0)

# define menu layout
menu = [['&File', ['&Open Folder', 'E&xit']], ['&Help', ['&About',]]]

buttons = []
for display_index in range(ROWS):
    row = []
    for j in range(COLUMNS):
        row.append(sg.Button('',border_width=0,button_color=sg.COLOR_SYSTEM_DEFAULT, key=(display_index, j)))
    buttons.append(row)

col_buttons = [[]]

# define layout, show and read the window
col = [[sg.Text(png_files[0], size=(80, 3), key='filename')],
          [sg.Image(data=image_file_to_bytes(png_files[0], (500,500)), key='image')],]

layout = [[sg.Menu(menu)], [sg.Column(buttons), sg.Column([[sg.Slider((len(png_files),0),default_value=0,size=(38,20),orientation='v', key='_slider_', change_submits=True)]]), sg.Column(col)]]
window = sg.Window('Image Browser',
                   return_keyboard_events=True,
                   use_default_focus=False ).Layout(layout).Finalize()

# -------========= Event Loop =========--------
display_index=0
while True:
    for x in range(ROWS):               # update thumbnails
        for y in range(COLUMNS):
            cur_index = display_index + (x * 4) + y
            if cur_index < len(png_files):
                filename = png_files[cur_index]
                if filename not in thumbnails:
                    imgbytes = image_file_to_bytes(filename, (100,100))
                    thumbnails[filename] = imgbytes
                else:
                    imgbytes = thumbnails[filename]
                button_elem = window.FindElement(key=(x,y))
                button_elem.Update(image_data=imgbytes)
            else:
                set_image_to_blank((x,y))

    event, values = window.Read()
    display_index = values['_slider_']
    # --------------------- Button & Keyboard ---------------------
    if event in (None, 'Exit'):
        break
    elif event in ('MouseWheel:Down', 'Down:40',) and display_index < len(png_files)-1:
        display_index += 4
    elif event in ('MouseWheel:Up', 'Up:38',) and display_index > 0:
        display_index -= 4
    elif event in ('Prior:33', 'Prev'):
        display_index -= 16
    elif event in ('Next:34', 'Next'):
        display_index += 16

    window.FindElement('_slider_').Update(display_index)
    # ----------------- Menu choices -----------------
    if event == 'Open Folder':
        newfolder = sg.PopupGetFolder('New folder', no_window=True)
        if newfolder is None:
            continue
        folder = newfolder
        png_files = [os.path.join(folder, f) for f in os.listdir(folder) if '.png' in f]
        filenames_only = [f for f in os.listdir(folder) if '.png' in f]
        display_index = 0
        thumbnail = {}
        for j in range(ROWS):
            for i in range(COLUMNS):
                set_image_to_blank((i,j))
    elif event == 'About':
        sg.Popup('Demo PNG Viewer Program', 'Please give PySimpleGUI a try!')
    elif type(event) is tuple:
        x, y = event
        image_index = display_index + (x * 4) + y
        if image_index < len(png_files):
            filename = png_files[image_index]
            imgbytes = image_file_to_bytes(filename, (500, 500))
            window.FindElement('image').Update(data=imgbytes)
            window.FindElement('filename').Update(filename)

