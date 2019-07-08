#!/usr/bin/env python
import sys
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg
import cv2 as cv
from PIL import Image
import io
from sys import exit as exit

"""
Demo program to open and play a file using OpenCV
It's main purpose is to show you:
1. How to get a frame at a time from a video file using OpenCV
2. How to display an image in a PySimpleGUI Window

For added fun, you can reposition the video using the slider.
"""

def main():
    # ---===--- Get the filename --- #
    filename = sg.PopupGetFile('Filename to play')
    if filename is None:
        exit(69)
    vidFile = cv.VideoCapture(filename)
    # ---===--- Get some Stats --- #
    num_frames = vidFile.get(cv.CAP_PROP_FRAME_COUNT)
    fps = vidFile.get(cv.CAP_PROP_FPS)

    sg.ChangeLookAndFeel('Black')

    # ---===--- define the window layout --- #
    layout = [[sg.Text('OpenCV Demo', size=(15, 1), font='Helvetica 20')],
              [sg.Image(filename='', key='_image_')],
              [sg.Slider(range=(0, num_frames), size=(60, 10), orientation='h', key='_slider_')],
              [sg.Button('Exit', size=(7, 1), pad=((600, 0), 3), font='Helvetica 14')]]

    # create the window and show it without the plot
    window = sg.Window('Demo Application - OpenCV Integration', no_titlebar=False, location=(0,0)).Layout(layout)

    image_elem = window.Element('_image_')    # locate the elements we'll be updating. Does the search only 1 time
    slider_elem = window.Element('_slider_')

    # ---===--- LOOP through video file by frame --- #
    cur_frame = 0
    while vidFile.isOpened():
        event, values = window.Read(timeout=0)
        if event in ('Exit', None):
            exit(69)
        ret, frame = vidFile.read()
        if not ret:  # if out of data stop looping
            break
        if int(values['_slider_']) != cur_frame-1:        # if someone moved the slider manually, the jump to that frame
            cur_frame = int(values['_slider_'])
            vidFile.set(cv.CAP_PROP_POS_FRAMES, cur_frame)
        slider_elem.Update(cur_frame)
        cur_frame += 1

        img = Image.fromarray(frame)    # create PIL image from frame
        bio = io.BytesIO()              # a binary memory resident stream
        img.save(bio, format= 'PNG')    # save image as png to it
        imgbytes = bio.getvalue()       # this can be used by OpenCV hopefully
        image_elem.Update(data=imgbytes)

main()