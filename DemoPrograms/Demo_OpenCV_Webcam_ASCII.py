from PIL import Image
import numpy as np
import PySimpleGUI as sg; font_size=6
# import PySimpleGUIQt as sg; font_size=8            # if using, be sure and use the second layout that is commented out
# import PySimpleGUIWeb as sg; font_size=12           # yes, it runs in a webpage too!
import cv2

"""
    Interesting program that shows your webcam's image as ASCII text.  Runs in realtime, producing a stream of
    images so that it is actually animated ASCII text. Wild stuff that came about from a post on Reddit of all
    places.  The software bits that turn the image into ASCII text were shamelessly taken from this gist:
    https://gist.github.com/cdiener/10491632
    Brilliant work to have pulled off so much with so little Numpy
    What's remarkable about this program is that the animation is created by updating individual Text Elements going
    down the window, one line at a time, every time through the loop.  That's 48 lines of text every time. Rough
    timing shows an animation of more than 10 fps when running any of the PySimpleGUI ports.
"""

# The magic bits that make the ASCII stuff work shamelessly taken from https://gist.github.com/cdiener/10491632
chars = np.asarray(list(' .,:;irsXA253hMHGS#9B&@'))
SC, GCF, WCF = .1, 1, 7/4

sg.ChangeLookAndFeel('Black')   # make it look cool

# define the window layout
NUM_LINES = 48  # number of lines of text elements. Depends on cameras image size and the variable SC (scaller)
layout =  [*[[sg.T(i,size=(120,1), font=('Courier', font_size), key='_OUT_'+str(i))] for i in range(NUM_LINES)],
          [ sg.Button('Exit')]]

# if using PySimpleGUIQt, use this layout instead.  The text rows are too far apart otherwise.
# layout =  [*[[sg.T(i, size_px=(800,12), font=('Courier', font_size), key='_OUT_'+str(i))] for i in range(NUM_LINES)],
#           [ sg.Button('Exit')]]



# create the window and show it without the plot
window = sg.Window('Demo Application - OpenCV Integration', layout, location=(800,400),
                   no_titlebar=True, grab_anywhere=True, element_padding=(0,0))

# ---===--- Event LOOP Read and display frames, operate the GUI --- #
cap = cv2.VideoCapture(0)                               # Setup the OpenCV capture device (webcam)
while True:
    event, values = window.Read(timeout=0)
    if event in ('Exit', None):
        break
    ret, frame = cap.read()                             # Read image from capture device (camera)

    img = Image.fromarray(frame)  # create PIL image from frame
    # More magic that coverts the image to ascii
    S = (round(img.size[0] * SC * WCF), round(img.size[1] * SC))
    img = np.sum(np.asarray(img.resize(S)), axis=2)
    img -= img.min()
    img = (1.0 - img / img.max()) ** GCF * (chars.size - 1)

    # "Draw" the image in the window, one line of text at a time!
    for i, r in enumerate(chars[img.astype(int)]):
        window.Element('_OUT_'+str(i)).Update("".join(r))
window.Close()
