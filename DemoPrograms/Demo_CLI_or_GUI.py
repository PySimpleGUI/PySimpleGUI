"""
    Demo Command Line Application or GUI Application

    If your program is run with arguments, then a command line version is used.
    If no arguments are given, then a GUI is shown that asks for a filename.

    http://www.PySimpleGUI.org
    Copyright 2022 PySimpleGUI
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
