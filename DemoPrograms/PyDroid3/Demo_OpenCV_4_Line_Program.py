import tkinter
import cv2, PySimpleGUI as sg
USE_CAMERA = 0      # change to 1 for front facing camera
window, cap = sg.Window('Demo Application - OpenCV Integration', [[sg.Image(filename='', key='image')], ], location=(0, 0), grab_anywhere=True), cv2.VideoCapture(USE_CAMERA)
while window(timeout=20)[0] is not None:
    window['image'](data=cv2.imencode('.png', cap.read()[1])[1].tobytes())
