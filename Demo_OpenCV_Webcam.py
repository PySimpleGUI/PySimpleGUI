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
Demo program that displays a webcam using OpenCV
"""
def main():

    sg.ChangeLookAndFeel('LightGreen')

    # define the window layout
    layout = [[sg.Text('OpenCV Demo', size=(40, 1), justification='center', font='Helvetica 20')],
              [sg.Image(filename='', key='image')],
              [sg.ReadButton('Exit', size=(10, 1), pad=((200, 0), 3), font='Helvetica 14'),
               sg.RButton('About', size=(10,1), font='Any 14')]]

    # create the window and show it without the plot
    window = sg.Window('Demo Application - OpenCV Integration',
                       location=(800,400))
    window.Layout(layout)
    window.ReadNonBlocking()

    # ---===--- Event LOOP Read and display frames, operate the GUI --- #
    cap = cv.VideoCapture(0)
    while True:
        button, values = window.ReadNonBlocking()

        if button is 'Exit' or values is None:
            sys.exit(0)
        elif button == 'About':
            sg.PopupNoWait('Made with PySimpleGUI',
                           'www.PySimpleGUI.org',
                           'Check out how the video keeps playing behind this window.',
                           'I finally figured out how to display frames from a webcam.',
                           'ENJOY!  Go make something really cool with this... please!',
                           keep_on_top=True)

        ret, frame = cap.read()

        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        # let img be the PIL image
        img = Image.fromarray(gray)  # create PIL image from frame
        bio = io.BytesIO()  # a binary memory resident stream
        img.save(bio, format= 'PNG')  # save image as png to it
        imgbytes = bio.getvalue()  # this can be used by OpenCV hopefully
        window.FindElement('image').Update(data=imgbytes)

main()