#!/usr/bin/env python
import PySimpleGUI as sg
import cv2 as cv
# from PIL import Image
# import io

"""
    Demo program to open and play a file using OpenCV
    It's main purpose is to show you:
    1. How to get a frame at a time from a video file using OpenCV
    2. How to display an image in a PySimpleGUI Window
    
    For added fun, you can reposition the video using the slider.
    
    Copyright 2022 PySimpleGUI
"""


def main():
    # ---===--- Get the filename --- #
    filename = sg.popup_get_file('Filename to play')
    if filename is None:
        return
    vidFile = cv.VideoCapture(filename)
    # ---===--- Get some Stats --- #
    num_frames = vidFile.get(cv.CAP_PROP_FRAME_COUNT)
    fps = vidFile.get(cv.CAP_PROP_FPS)

    sg.theme('Black')

    # ---===--- define the window layout --- #
    layout = [[sg.Text('OpenCV Demo', size=(15, 1), font='Helvetica 20')],
              [sg.Image(key='-IMAGE-')],
              [sg.Slider(range=(0, num_frames), size=(60, 10), orientation='h', key='-SLIDER-')],
              [sg.Push(), sg.Button('Exit', font='Helvetica 14')]]

    # create the window and show it without the plot
    window = sg.Window('Demo Application - OpenCV Integration', layout, no_titlebar=False, location=(0, 0))

    # locate the elements we'll be updating. Does the search only 1 time
    image_elem = window['-IMAGE-']
    slider_elem = window['-SLIDER-']
    timeout = 1000//fps                 # time in ms to use for window reads
    
    # ---===--- LOOP through video file by frame --- #
    cur_frame = 0
    while vidFile.isOpened():
        event, values = window.read(timeout=timeout)
        if event in ('Exit', None):
            break
        ret, frame = vidFile.read()
        if not ret:  # if out of data stop looping
            break
        # if someone moved the slider manually, the jump to that frame
        if int(values['-SLIDER-']) != cur_frame-1:
            cur_frame = int(values['-SLIDER-'])
            vidFile.set(cv.CAP_PROP_POS_FRAMES, cur_frame)
        slider_elem.update(cur_frame)
        cur_frame += 1

        imgbytes = cv.imencode('.ppm', frame)[1].tobytes()  # can also use png.  ppm found to be more efficient
        image_elem.update(data=imgbytes)

main()

            #############
            #    | |    #
            #    | |    #
            #    |_|    #
            #  __   __  #
            #  \ \ / /  #
            #   \ V /   #
            #    \_/    #
"""         #############
        # This was another way updates were being done, but seems slower than the above
        img = Image.fromarray(frame)    # create PIL image from frame
        bio = io.BytesIO()              # a binary memory resident stream
        img.save(bio, format= 'PNG')    # save image as png to it
        imgbytes = bio.getvalue()       # this can be used by OpenCV hopefully
        image_elem.update(data=imgbytes)
"""