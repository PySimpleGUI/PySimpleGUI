#!/usr/bin/env python
import sys
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg

import os

BUTTON_PATH =  '.'
button_names = ('close', 'cookbook', 'cpu', 'github', 'pysimplegui', 'run', 'storage', 'timer', 'checkmark', 'camera', 'house', 'download')


def ShowMeTheButtons():
    button_files = [os.path.join(BUTTON_PATH, b+'.png') for b in button_names]

    sg.SetOptions(auto_size_buttons=True, margins=(0,0), button_color=sg.COLOR_SYSTEM_DEFAULT)

    toolbar_buttons = [[sg.RButton('{}'.format(button_names[i]), image_size=(32,32), image_filename=f, pad=(0,0), tooltip=button_names[i]) for i, f in enumerate(button_files)],]

    layout =  [[sg.Frame('', toolbar_buttons,)]]

    form = sg.FlexForm('Toolbar',
                       no_titlebar=True,
                       grab_anywhere=True,
                       background_color='grey76',
                       keep_on_top=True,
                       ).Layout(layout)

    # ---===--- Loop taking in user input --- #
    while True:
        button, value = form.Read()
        print(button)
        if button == 'close' or button is None:
            break           # exit button clicked

if __name__ == '__main__':
    ShowMeTheButtons()