import cv2, PySimpleGUI as sg

"""
    Copyright 2023 PySimpleSoft, Inc. and/or its licensors. All rights reserved.

    Redistribution, modification, or any other use of PySimpleGUI or any portion thereof is subject to the terms of the PySimpleGUI License Agreement available at https://eula.pysimplegui.com.

    You may not redistribute, modify or otherwise use PySimpleGUI or its contents except pursuant to the PySimpleGUI License Agreement.
"""

window, cap = sg.Window('Demo Application - OpenCV Integration', [[sg.Image(key='-IMAGE-')], ], location=(800, 400)), cv2.VideoCapture(0)
while window(timeout=20)[0] is not None:
    window['-IMAGE-'](data=cv2.imencode('.png', cap.read()[1])[1].tobytes())
