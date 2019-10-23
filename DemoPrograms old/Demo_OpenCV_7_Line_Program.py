import cv2, PySimpleGUI as sg
window = sg.Window('Demo Application - OpenCV Integration', [[sg.Image(filename='', key='image')],], location=(800,400))
cap = cv2.VideoCapture(0)       # Setup the camera as a capture device
while True:                     # The PSG "Event Loop"
    event, values = window.Read(timeout=20, timeout_key='timeout')      # get events for the window with 20ms max wait
    if event is None:  break                                            # if user closed window, quit
    window.FindElement('image').Update(data=cv2.imencode('.png', cap.read()[1])[1].tobytes()) # Update image in window

"""
Putting the comment at the bottom so that you can see that the code is indeed 7 lines long.  And, there is nothing
done out of the ordinary to make it 7 lines long.  There are no ; for example.  OK, so the if statement is on one line
but that's the only place that you would traditionally see one more line.  So, call it 8 if you want.
"""