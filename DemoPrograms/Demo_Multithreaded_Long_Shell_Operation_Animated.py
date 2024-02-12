import PySimpleGUI as sg

"""
    Demo shell_with_animation call

    This is a high-level function that could easily live in user's code instead of PySimpleGUI.  The
    rationale for bringing it into PySimpleGUI is to encourage users to experiment with working with
    more external tools like ffmpeg.  The shell_with_animation function allows users to easily start
    a long-operation without fearing that the GUI will appear to be frozen.  It offers a wide range
    of parameters to help create a custom animation window.
    
    Copyright 2023 PySimpleSoft, Inc. and/or its licensors. All rights reserved.
    
    Redistribution, modification, or any other use of PySimpleGUI or any portion thereof is subject to the terms of the PySimpleGUI License Agreement available at https://eula.pysimplegui.com.
    
    You may not redistribute, modify or otherwise use PySimpleGUI or its contents except pursuant to the PySimpleGUI License Agreement.
"""

# Here we're running a simple "pip list" command and using the built-in animated GIF.

output = sg.shell_with_animation('pip', ('list',), message='Loading...', font='Helvetica 15')
sg.popup_scrolled(output, font='Courier 10')
output = sg.shell_with_animation('dir', message='Loading...', font='Helvetica 15')
# output = sg.shell_with_animation(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe", message='Loading...', font='Helvetica 15')

sg.popup_scrolled(output, font='Courier 10')
