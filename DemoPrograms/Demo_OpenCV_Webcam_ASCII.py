from PIL import Image
import numpy as np
import PySimpleGUI as sg; font_size=6; USING_QT=False
# import PySimpleGUIQt as sg; font_size=8; USING_QT=True            # if using, be sure and use the second layout that is commented out
# import PySimpleGUIWeb as sg; font_size=12; USING_QT=False           # yes, it runs in a webpage too! Not as good as tkinter but works
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
    Also added onto this are a spinner and a slider. They do essentially the same thing, enable a pair of parameters
    to be modified on the fly. 
    
    You need PySimpleGUI installed as well as OpenCV.  Both are easily installed via pip:
    pip install PySimpleGUI
    pip install opencv-python
    
    On Linux / Mac use pip3 instead of pip
"""

# The magic bits that make the ASCII stuff work shamelessly taken from https://gist.github.com/cdiener/10491632
chars = np.asarray(list(' .,:;irsXA253hMHGS#9B&@'))
SC, GCF, WCF = .1, 1, 7/4

sg.ChangeLookAndFeel('Black')   # make it look cool

# define the window layout
NUM_LINES = 48  # number of lines of text elements. Depends on cameras image size and the variable SC (scaller)
if USING_QT:
    layout = [[sg.T(i, size_px=(800, 12), font=('Courier', font_size), key='_OUT_' + str(i))] for i in range(NUM_LINES)]

else:
    layout =  [[sg.T(i,size=(120,1), font=('Courier', font_size), pad=(0,0), key='_OUT_'+str(i))] for i in range(NUM_LINES)]

layout += [[ sg.Button('Exit', size=(5,1)),
            sg.T('GCF', size=(4,1)), sg.Spin([round(i,2) for i in np.arange(0.1,20.0,0.1)], initial_value=1,  key='_SPIN_GCF_', size=(5,1)),
            sg.T('WCF', size=(4,1)), sg.Slider((1,4), resolution=.05, default_value=1.75, orientation='h', key='_SLIDER_WCF_', size=(15,15))
            ]]

# create the window and show it without the plot
window = sg.Window('Demo Application - OpenCV Integration', layout, location=(800,400), font='Any 18')

# ---===--- Event LOOP Read and display frames, operate the GUI --- #
cap = cv2.VideoCapture(0)                               # Setup the OpenCV capture device (webcam)
while True:
    event, values = window.Read(timeout=0)
    if event in ('Exit', None):
        break
    ret, frame = cap.read()                             # Read image from capture device (camera)

    img = Image.fromarray(frame)  # create PIL image from frame
    GCF = float(values['_SPIN_GCF_'])
    WCF = values['_SLIDER_WCF_']
    # More magic that coverts the image to ascii
    S = (round(img.size[0] * SC * WCF), round(img.size[1] * SC))
    img = np.sum(np.asarray(img.resize(S)), axis=2)
    img -= img.min()
    img = (1.0 - img / img.max()) ** GCF * (chars.size - 1)

    # "Draw" the image in the window, one line of text at a time!
    for i, r in enumerate(chars[img.astype(int)]):
        window.Element('_OUT_'+str(i)).Update("".join(r))
window.Close()
