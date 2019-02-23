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
Unsure how to get the frames coming from OpenCV into the right format, so saving each frame to
a temp file.  Clearly... clearly... this is not the optimal solution and one is being searched for now.

Until then enjoy it working somewhat slowly.
"""

def main():
    filename = sg.PopupGetFile('Filename to play')
    if filename is None:
        exit(69)
    vidFile = cv.VideoCapture(filename)
    # ---===--- Get some Stats --- #
    num_frames = vidFile.get(cv.CAP_PROP_FRAME_COUNT)
    fps = vidFile.get(cv.CAP_PROP_FPS)

    sg.ChangeLookAndFeel('Dark')

    # define the window layout
    layout = [[sg.Text('OpenCV Demo', size=(15, 1),pad=((510,0),3), justification='center', font='Helvetica 20')],
              [sg.Image(filename='', key='image')],
              [sg.Slider(range=(0, num_frames), size=(115, 10), orientation='h', key='slider')],
              [sg.Button('Exit', size=(10, 2), pad=((600, 0), 3), font='Helvetica 14')]]

    # create the window and show it without the plot
    window = sg.Window('Demo Application - OpenCV Integration', no_titlebar=False, location=(0,0)).Layout(layout)

    # ---===--- LOOP through video file by frame --- #
    i = 0
    while vidFile.isOpened():
        event, values = window.Read(timeout=0)
        if event is 'Exit' or event is None:
            exit(69)
        ret, frame = vidFile.read()
        if not ret:  # if out of data stop looping
            break

        window.FindElement('slider').Update(i)
        i += 1

        # let img be the PIL image
        img = Image.fromarray(frame)  # create PIL image from frame
        bio = io.BytesIO()  # a binary memory resident stream
        img.save(bio, format= 'PNG')  # save image as png to it
        imgbytes = bio.getvalue()  # this can be used by OpenCV hopefully
        window.FindElement('image').Update(data=imgbytes)


main()