import cv2, PySimpleGUI as sg
window, cap = sg.Window('Demo Application - OpenCV Integration', [[sg.Image(filename='', key='image')],], location=(800,400)), cv2.VideoCapture(0)
while window(timeout=20)[0] is not None:
    window['image'](data=cv2.imencode('.png', cap.read()[1])[1].tobytes())
