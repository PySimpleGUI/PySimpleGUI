import PySimpleGUI as sg
import cv2

"""
    Demonstration of how to use a GRAPH ELEMENT to draw a webcam stream using OpenCV and PySimpleGUI.
    Additionally, the thing this demo is really showcasing, is the ability to draw over the top of this
    webcam stream, as it's being displayed.  To "Draw" simply move your mouse over the image, left click and hold, and
    then drag your mouse.  You'll see a series of red circles on top of your image.
    CURRENTLY ONLY WORKS WITH PySimpleGUI, NOT any of the other ports at this time.
    
    Note also that this demo is using ppm as the image format.  This worked fine on all PySimpleGUI ports except 
    the web port.  If you have trouble with the imencode statement, change "ppm" to "png"
    
    Copyright 2021 PySimpleGUI
"""

def main():
    layout = [[sg.Graph((600,450),(0,450), (600,0), key='-GRAPH-', enable_events=True, drag_submits=True)],],

    window = sg.Window('Demo Application - OpenCV Integration', layout)
    graph_elem = window['-GRAPH-']      # type: sg.Graph
    a_id = None
    # ---===--- Event LOOP Read and display frames, operate the GUI --- #
    cap = cv2.VideoCapture(0)
    while True:
        event, values = window.read(timeout=0)
        if event in ('Exit', None):
            break

        ret, frame = cap.read()
        imgbytes=cv2.imencode('.ppm', frame)[1].tobytes()       # on some ports, will need to change to png
        if a_id:
            graph_elem.delete_figure(a_id)             # delete previous image
        a_id = graph_elem.draw_image(data=imgbytes, location=(0,0))    # draw new image
        graph_elem.send_figure_to_back(a_id)            # move image to the "bottom" of all other drawings

        if event == '-GRAPH-':
            graph_elem.draw_circle(values['-GRAPH-'], 5, fill_color='red', line_color='red')

    window.close()

main()