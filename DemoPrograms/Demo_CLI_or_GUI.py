"""
    Demo Command Line Application or GUI Application

    If your program is run with arguments, then a command line version is used.
    If no arguments are given, then a GUI is shown that asks for a filename.

    http://www.PySimpleGUI.org
    Copyright 2022-2023 PySimpleSoft, Inc. and/or its licensors. All rights reserved.
    
    Redistribution, modification, or any other use of PySimpleGUI or any portion thereof is subject to the terms of the PySimpleGUI License Agreement available at https://eula.pysimplegui.com.
    
    You may not redistribute, modify or otherwise use PySimpleGUI or its contents except pursuant to the PySimpleGUI License Agreement.
"""

import PySimpleGUI as sg
import sys

def main_cli(filename):
    print(f'Your filename = {filename}')


def main_gui():
    filename = sg.popup_get_file('Please enter a filename:')
    main_cli(filename)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        main_gui()
    else:
        main_cli(sys.argv[1])
