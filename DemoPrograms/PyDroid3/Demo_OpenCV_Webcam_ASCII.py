import tkinter
import cv2
from PIL import Image
import numpy as np
import PySimpleGUI as sg

font_size = 3
CAMERA_FRONT = 1
CAMERA_REAR = 0

USE_CAMERA = CAMERA_REAR

"""
Interesting program that shows your webcam's image as ASCII text. Runs in realtime, producing a stream of
images so that it is actually animated ASCII text. Wild stuff that came about from a post on Reddit of all
places. The software bits that turn the image into ASCII text were shamelessly taken from this gist:
https://gist.github.com/cdiener/10491632
Brilliant work to have pulled off so much with so little Numpy
What's remarkable about this program is that the animation is created by updating individual Text Elements going
down the window, one line at a time, every time through the loop. That's 48 lines of text every time. Rough
timing shows an animation of more than 10 fps when running any of the PySimpleGUI ports.
Also added onto this are a spinner and a slider. They do essentially the same thing, enable a pair of parameters
to be modified on the fly.

You need PySimpleGUI installed as well as OpenCV. Both are easily installed via pip:
pip install PySimpleGUI
pip install opencv-python

On Linux / Mac use pip3 instead of pip
"""

# The magic bits that make the ASCII stuff work shamelessly taken from https://gist.github.com/cdiener/10491632
chars = np.asarray(list(' .,:;irsXA253hMHGS#9B&@'))
SC, GCF, WCF = .1, 1, 7/4

sg.change_look_and_feel('Dark Black 1') # make it look cool

# ---------------- A Quick Little Window - to get camera to use ----------------
win_get_cam = sg.Window('Which Camera?',[[sg.T('Which camera?')],[sg.Combo(['Front', 'Rear'], default_value='Rear', font='any 20')],[sg.T(size=(1,2))], [sg.Ok()]], location=(0,0))
event, values = win_get_cam.read()
win_get_cam.close()
if event != 'Ok': exit()
USE_CAMERA = [CAMERA_FRONT, CAMERA_REAR][values[0]=='Rear']

# ------------ Turn on camera and read a frame to find the number of lines of text needed ---------
cap = cv2.VideoCapture(USE_CAMERA)      # Setup camera using your camera choice

ret, frame = cap.read()

img = Image.fromarray(frame)    # create PIL image from frame
GCF = 1.0                       # Variable user will be able to change
WCF = 1.75                      # Variable user will be able to change
# ----------- magic that coverts the image to ascii -----------
S = (round(img.size[0] * SC * WCF), round(img.size[1] * SC))
img = np.sum(np.asarray(img.resize(S)), axis=2)
img -= img.min()
img = (1.0 - img / img.max()) ** GCF * (chars.size - 1)

# Find number of lines of text that will be drawn so can create the right size of window
NUM_LINES = len(chars[img.astype(int)])
LINE_LENGTH = len("".join(chars[img.astype(int)][0]))
print(f'line len = {LINE_LENGTH}')
#  ------------- define the window layout -------------
# number of lines of text elements. Depends on cameras image size and the variable SC (scaller)

layout = [[sg.Text(i, size=(LINE_LENGTH, 1), font=('Courier', font_size), pad=(0, 0), key='-OUT-'+str(i))] for i in range(NUM_LINES)]

layout += [[sg.Button('Exit', size=(5, 1)),
            sg.Text('GCF', size=(4, 1)),
            sg.Spin([round(i, 2) for i in np.arange(0.1, 20.0, 0.1)], initial_value=1, key='-SPIN-GCF-', size=(5, 1), font='any 20')],
            [sg.Text('WCF', size=(4, 1)),
            sg.Slider((1, 4), resolution=.05, default_value=1.75, orientation='h', key='-SLIDER-WCF-', size=(15, 30))]]

# ------------- create the window -------------
window = sg.Window('Demo Application - OpenCV Integration', layout, location=(0,0))

# ---===--- Event LOOP Read and display frames, operate the GUI --- #
while True:

    event, values = window.read(timeout=0)
    if event in ('Exit', None):
        break
    # Read image from capture device (camera)
    ret, frame = cap.read()

    img = Image.fromarray(frame) # create PIL image from frame
    GCF = float(values['-SPIN-GCF-'])
    WCF = values['-SLIDER-WCF-']
    # More magic that coverts the image to ascii
    S = (round(img.size[0] * SC * WCF), round(img.size[1] * SC))
    img = np.sum(np.asarray(img.resize(S)), axis=2)
    img -= img.min()
    img = (1.0 - img / img.max()) ** GCF * (chars.size - 1)

    # "Draw" the image in the window, one line of text at a time!
    for i, r in enumerate(chars[img.astype(int)]):
        window['-OUT-'+str(i)].update("".join(r))

window.close()
