#!/usr/bin/env python
import PySimpleGUI as sg


"""
    Demo of Net API - Download a PNG Image using net_download_file_binary & Display in a Window

    This Demo Program shows how to download a binary file (an image) and display it in a window.

    
    Copyright 2018-2023 PySimpleSoft, Inc. and/or its licensors. All rights reserved.
    
    Redistribution, modification, or any other use of PySimpleGUI or any portion thereof is subject to the terms of the PySimpleGUI License Agreement available at https://eula.pysimplegui.com.
    
    You may not redistribute, modify or otherwise use PySimpleGUI or its contents except pursuant to the PySimpleGUI License Agreement.
"""


sg.theme('black')

# First the easy case.... display a PNG image

sg.Window('PNG Download', [[sg.Image(sg.net_download_file_binary(r'https://pysimplegui.net/images/tests/powered-by-pysimplegui-5.png'))]]).read(close=True)

