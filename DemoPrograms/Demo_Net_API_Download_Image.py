#!/usr/bin/env python
import PySimpleGUI as sg


"""
    Demo of Net API - Download a PNG Image using net_download_file_binary & Display in a Window

    This Demo Program shows how to download a binary file (an image) and display it in a window.

    
    Copyright 2018-2026 PySimpleGUI. All rights reserved.
    
    
"""


sg.theme('black')

# First the easy case.... display a PNG image

sg.Window('PNG Download', [[sg.Image(sg.net_download_file_binary(r'https://pysimplegui.net/images/tests/powered-by-pysimplegui-5.png'))]]).read(close=True)

