import cv2 as cv
from PIL import Image
import tempfile
import PySimpleGUI as sg
import os

"""
Demo program to open and play a file using OpenCV
Unsure how to get the frames coming from OpenCV into the right format, so saving each frame to
a temp file.  Clearly... clearly... this is not the optimal solution and one is being searched for now.

Until then enjoy it working somewhat slowly.
"""


def main():
    filename = 'C:/Python/MIDIVideo/PlainVideos/- 08-30 Ted Talk/TED Talk Short - Video+.mp4'
    # filename = sg.PopupGetFile('Filename to play')
    if filename is None:
        exit(69)
    vidFile = cv.VideoCapture(filename)
    # ---===--- Get some Stats --- #
    num_frames = vidFile.get(cv.CAP_PROP_FRAME_COUNT)
    fps = vidFile.get(cv.CAP_PROP_FPS)

    sg.ChangeLookAndFeel('Dark')

    # define the form layout
    layout = [[sg.Text('OpenCV Demo', size=(15, 1),pad=((510,0),3), justification='center', font='Helvetica 20')],
              [sg.Image(filename='', key='image')],
              [sg.Slider(range=(0, num_frames), size=(115, 10), orientation='h', key='slider')],
              [sg.ReadFormButton('Exit', size=(10, 2), pad=((600, 0), 3), font='Helvetica 14')]]

    # create the form and show it without the plot
    form = sg.FlexForm('Demo Application - OpenCV Integration', no_titlebar=False, location=(0,0))
    form.Layout(layout)
    form.ReadNonBlocking()


    # ---===--- LOOP through video file by frame --- #
    i = 0
    temp_filename = next(tempfile._get_candidate_names()) + '.png'
    while vidFile.isOpened():
        button, values = form.ReadNonBlocking()
        if button is 'Exit' or values is None:
            os.remove(temp_filename)
            exit(69)
        ret, frame = vidFile.read()
        if not ret:  # if out of data stop looping
            break

        form.FindElement('slider').Update(i)
        i += 1

        with open(temp_filename, 'wb') as f:
            Image.fromarray(frame).save(temp_filename, 'PNG')  # save the PIL image as file
            form.FindElement('image').Update(filename=temp_filename)


main()