#!/usr/bin/env python
import PySimpleGUI as sg
# import PySimpleGUIQt as sg
import cv2
import numpy as np
import sys
from sys import exit as exit

"""
Demo program that displays a webcam using OpenCV
"""
def main():

    sg.ChangeLookAndFeel('Black')

    # define the window layout
    layout = [[sg.Text('OpenCV Demo', size=(40, 1), justification='center', font='Helvetica 20')],
              [sg.Image(filename='', key='image')],
              [sg.Button('Record', size=(10, 1), font='Helvetica 14'),
               sg.Button('Stop', size=(10, 1), font='Any 14'),
              sg.Button('Exit', size=(10, 1), font='Helvetica 14'),]]

    # create the window and show it without the plot
    window = sg.Window('Demo Application - OpenCV Integration', layout,
                       location=(800,400))

    # ---===--- Event LOOP Read and display frames, operate the GUI --- #
    cap = cv2.VideoCapture(0)
    recording = False
    while True:
        event, values = window.Read(timeout=20)
        if event == 'Exit' or event is None:
            sys.exit(0)
        elif event == 'Record':
            recording = True
        elif event == 'Stop':
            recording = False
            img = np.full((480, 640),255)
            imgbytes=cv2.imencode('.png', img)[1].tobytes() #this is faster, shorter and needs less includes
            window.FindElement('image').Update(data=imgbytes)

        if recording:
            ret, frame = cap.read()
            imgbytes=cv2.imencode('.png', frame)[1].tobytes() #ditto
            window.FindElement('image').Update(data=imgbytes)

main()
exit()