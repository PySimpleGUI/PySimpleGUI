#!/usr/bin/env python
import PySimpleGUI as sg

# Only need these imports if using JPGs
from PIL import Image
from io import BytesIO
import base64


"""
    Demo of Net API - Download Images using net_download_file_binary

    This Demo Program shows how to download a binary file (an image) and display in a window.
    The PNG image display is quite easy.  Displaying a JPG requires converting using PIL.
    
    Copyright 2018-2023 PySimpleSoft, Inc. and/or its licensors. All rights reserved.
    
    Redistribution, modification, or any other use of PySimpleGUI or any portion thereof is subject to the terms of the PySimpleGUI License Agreement available at https://eula.pysimplegui.com.
    
    You may not redistribute, modify or otherwise use PySimpleGUI or its contents except pursuant to the PySimpleGUI License Agreement.
"""


sg.theme('black')

# First the easy case.... display a PNG image

sg.Window('BIG News', [[sg.Image(sg.net_download_file_binary(r'https://pysimplegui.net/images/big_news_emoji.png'))]],
          use_custom_titlebar=True, titlebar_background_color='black', titlebar_text_color='white').read(close=True)


# Now display a JPG image. It requires converting the image to PNG before using with PySimpleGUI
jpg_data = sg.net_download_file_binary(r'https://pysimplegui.net/images/tests/powered-by-pysimplegui-5.jpg')

jpg_image = Image.open(BytesIO(jpg_data))

with BytesIO() as bio:
    jpg_image.save(bio, format='PNG')
    contents = bio.getvalue()
    encoded = base64.b64encode(contents)

sg.Window('Powered By', [[sg.Image(data=encoded)]],
          use_custom_titlebar=True, titlebar_background_color='black', titlebar_text_color='white').read(close=True)
