#!/usr/bin/env python
import sys
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg
import cv2
import numpy as np
from sys import exit as exit

"""
Demo program that displays a webcam using OpenCV
"""
def main():

    sg.ChangeLookAndFeel('LightGreen')

    # define the window layout
    layout = [[sg.Text('OpenCV Demo', size=(40, 1), justification='center', font='Helvetica 20')],
              [sg.Image(filename='', key='image')],
              [sg.Button('Record', size=(10, 1), font='Helvetica 14'),
               sg.Button('Stop', size=(10, 1), font='Any 14'),
              sg.Button('Exit', size=(10, 1), font='Helvetica 14'),
               sg.Button('About', size=(10,1), font='Any 14')]]

    # create the window and show it without the plot
    window = sg.Window('Demo Application - OpenCV Integration',
                       location=(800,400))
    window.Layout(layout).Finalize()

    # ---===--- Event LOOP Read and display frames, operate the GUI --- #
    cap = cv2.VideoCapture(0)
    recording = False
    while True:
        event, values = window.Read(timeout=0, timeout_key='timeout')
        if event == 'Exit' or event is None:
            sys.exit(0)
        elif event == 'Record':
            recording = True
        elif event == 'Stop':
            recording = False
            img = np.full((480, 640),255)
            imgbytes=cv2.imencode('.png', img)[1].tobytes() #this is faster, shorter and needs less includes
            window.FindElement('image').Update(data=imgbytes)
        elif event == 'About':
            sg.PopupNoWait('Made with PySimpleGUI',
                           'www.PySimpleGUI.org',
                           'Check out how the video keeps playing behind this window.',
                           'I finally figured out how to display frames from a webcam.',
                           'ENJOY!  Go make something really cool with this... please!',
                           keep_on_top=True)
        if recording:
            ret, frame = cap.read()
            imgbytes=cv2.imencode('.png', frame)[1].tobytes() #ditto
            window.FindElement('image').Update(data=imgbytes)

main()
exit()