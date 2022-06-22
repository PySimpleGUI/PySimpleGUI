import cv2
from PIL import Image
import numpy as np
import PySimpleGUI as sg

"""
    Interesting program that shows your webcam's image as ASCII text.  Runs in realtime, producing a stream of
    images so that it is actually animated ASCII text. Wild stuff that came about from a post on Reddit of all
    places.  The software bits that turn the image into ASCII text were shamelessly taken from this gist:
    https://gist.github.com/cdiener/10491632
    Brilliant work to have pulled off so much with so little Numpy
    What's remarkable about this program is that the animation is created by updating individual Text Elements going
    down the window, one line at a time, every time through the loop.  That's 48 lines of text every time. Rough
    timing shows an animation of more than 10 fps when running any of the PySimpleGUI ports.
    Also added onto this are a spinner and a slider. They do essentially the same thing, enable a pair of parameters
    to be modified on the fly. 
    
    You need PySimpleGUI installed as well as OpenCV.  Both are easily installed via pip:
    pip install PySimpleGUI
    pip install opencv-python
    
    On Linux / Mac use pip3 instead of pip
    
    Copyright 2022, PySimpleGUI
"""

# The magic bits that make the ASCII stuff work shamelessly taken from https://gist.github.com/cdiener/10491632
chars = np.asarray(list(' .,:;irsXA253hMHGS#9B&@'))
SC, GCF, WCF = .1, 1, 7/4

sg.theme('Black')   # make it look cool with white chars on black background
font_size = 6

# define the window layout
# number of lines of text elements. Depends on cameras image size and the variable SC (scaller)
NUM_LINES = 48

layout  = [[[sg.Text(i,  font=('Courier', font_size), pad=(0, 0), key=('-OUT-', i))] for i in range(NUM_LINES)],
           [sg.Text('GCF', s=9, justification='r'), sg.Slider((0.1, 20), resolution=.05, default_value=1, orientation='h', key='-SPIN-GCF-', size=(15, 15))],
           [sg.Text('Font Size', s=9, justification='r'), sg.Slider((4, 20), resolution=1, default_value=font_size, orientation='h', key='-FONT SIZE-', size=(15, 15)),
            sg.Push(), sg.Button('Exit')]]

# create the window and show it without the plot
window = sg.Window('Demo Application - OpenCV - ASCII Chars Output', layout,  font='Any 18', resizable=True)

# ---===--- Event LOOP Read and display frames, operate the GUI --- #
# Setup the OpenCV capture device (webcam)

cap = cv2.VideoCapture(0)

while True:
    
    event, values = window.read(timeout=0)
    if event in ('Exit', sg.WIN_CLOSED):
        break
    # Read image from capture device (camera)
    ret, frame = cap.read()

    img = Image.fromarray(frame)  # create PIL image from frame
    GCF = float(values['-SPIN-GCF-'])
    WCF = 1.75
    # More magic that coverts the image to ascii
    S = (round(img.size[0] * SC * WCF), round(img.size[1] * SC))
    img = np.sum(np.asarray(img.resize(S)), axis=2)
    img -= img.min()
    img = (1.0 - img / img.max()) ** GCF * (chars.size - 1)

    # "Draw" the image in the window, one line of text at a time!
    font_size = int(values['-FONT SIZE-'])
    for i, r in enumerate(chars[img.astype(int)]):
        window[('-OUT-', i)].update("".join(r), font=('Courier', font_size))

window.close()
