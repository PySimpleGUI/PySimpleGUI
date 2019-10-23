import PySimpleGUI as sg
import cv2

"""
    Demonstration of how to use a GRAPH ELEMENT to draw a webcam stream using OpenCV and PySimpleGUI.
    Additionally, the thing this demo is really showcasing, is the ability to draw over the top of this
    webcam stream, as it's being displayed.  To "Draw" simply move your mouse over the image, left click and hold, and
    then drag your mouse.  You'll see a series of red circles on top of your image.
    CURRENTLY ONLY WORKS WITH PySimpleGUI, NOT any of the other ports at this time.
"""

def main():
    layout = [[sg.Graph((600,450),(0,450), (600,0), key='_GRAPH_', enable_events=True, drag_submits=True)],]

    window = sg.Window('Demo Application - OpenCV Integration', layout)

    graph_elem = window.Element('_GRAPH_')      # type: sg.Graph

    id = None
    # ---===--- Event LOOP Read and display frames, operate the GUI --- #
    cap = cv2.VideoCapture(0)
    while True:
        event, values = window.Read(timeout=0)
        if event in ('Exit', None):
            break

        ret, frame = cap.read()
        imgbytes=cv2.imencode('.png', frame)[1].tobytes()
        if id:
            graph_elem.DeleteFigure(id)             # delete previous image
        id = graph_elem.DrawImage(data=imgbytes, location=(0,0))    # draw new image
        graph_elem.TKCanvas.tag_lower(id)           # move image to the "bottom" of all other drawings

        if event == '_GRAPH_':
            graph_elem.DrawCircle(values['_GRAPH_'], 5, fill_color='red', line_color='red')
    window.Close()

main()
