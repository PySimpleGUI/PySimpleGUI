import PySimpleGUI as sg
import cv2

"""
    Demo of using OpenCV to show your webcam in a GUI window.
    This demo will run on tkinter, Qt, and Web(Remi).  The web version flickers at the moment though
    To exit, right click and choose exit. If on Qt, you'll have to kill the program as there are no right click menus
    in PySimpleGUIQt (yet).
"""

sg.theme('Black')

# define the window layout
layout = [[sg.Image(filename='', key='-IMAGE-', tooltip='Right click for exit menu')],]

# create the window and show it without the plot
window = sg.Window('Demo Application - OpenCV Integration', layout, location=(800,400),
                   no_titlebar=True, grab_anywhere=True,
                   right_click_menu=['&Right', ['E&xit']], )  # if trying Qt, you will need to remove this right click menu

# ---===--- Event LOOP Read and display frames, operate the GUI --- #
cap = cv2.VideoCapture(0)                               # Setup the OpenCV capture device (webcam)
while True:
    event, values = window.read(timeout=20)
    if event in ('Exit', None):
        break
    ret, frame = cap.read()                             # Read image from capture device (camera)
    imgbytes=cv2.imencode('.png', frame)[1].tobytes()   # Convert the image to PNG Bytes
    window['-IMAGE-'].update(data=imgbytes)   # Change the Image Element to show the new image

window.close()
