"""

Creates what appears to be an icon on your desktop, but is in reality a PySimpleGUI program.

Requires modules:  psgdnd, tkinterdnd2, PIL

Ways to interface with the icon include:
* Right click menu
* Double click of icon
* Dropping files onto icon
* Dropping text onto icon

Features:
* When JPG, PNG, GIF images are dropped onto icon, a popup window of options is shown.
    - Images can be converted to PNG and JPG
    - An image can be converted to base64 encoded PNG. The result is put onto clipboard
* If the icon is double clicked, it launches Explorer
* When other file types is dropped onto icon, a popup is shown with the list of files
* Toggle keep on top using right click menu

Copyright 2018-2026 PySimpleGUI. All rights reserved.

"""

import PySimpleGUI as sg
import psgdnd as dnd
import random
from typing import Tuple
from PIL import Image
import io
import base64
import os


def convert_formats(input_file:str, encode_format:str='PNG') -> bool:
    image = Image.open(input_file)

    if encode_format.lower() == 'jpeg':
        image = image.convert("RGB")
        encode_format = 'jpg'
    output_file = f'{os.path.splitext(input_file)[0]}.{encode_format.lower()}'
    print(f'{output_file=}')
    if not os.path.exists(output_file):
        image.save(output_file)
    else:
        return False
    return True


def encode_image_base64(input_file):
    if not input_file.lower().endswith('.png'):
        print('Error - Can only base64 encode PNG files')
        return None

    image = Image.open(input_file)

    # encode a PNG formatted version of image into BASE64
    with io.BytesIO() as bio:
        image.save(bio, format='PNG')
        contents = bio.getvalue()
        encoded = base64.b64encode(contents)
    return encoded



def show_choices(filenames:str, location: Tuple[int, int] | Tuple[None, None]):
    file_list = filenames.split(',')
    image_files = all(file.endswith(('jpg', 'png', 'gif')) for file in file_list)
    # location = (location[0]-400, location[1]-200)
    if image_files:
        actions = ('Convert to JPG', 'Convert to PNG', 'Convert to Base64 PNG')
        button_size = max(len(a) for a in actions)
        layout = [[sg.Text('Images dropped - What do you want to do with them?')],
                  [sg.Text('\n'.join(file_list))],
                  [[sg.Button(action, s=button_size)] for action in actions],
                    [sg.Button('Cancel', s=button_size)]]
        window = sg.Window('Image actions', layout, location=location, keep_on_top=True, no_titlebar=True, finalize=True)
        window.refresh()
        location = (location[0]-window.size[0]-10, location[1]-window.size[1]-10)
        window.move(location[0], location[1])
        print(f'{location=}  {window.size=}')
        event, values = window.read(close=True)
        # Perform actions
        if event == 'Convert to Base64 PNG':
            encoded = encode_image_base64(file_list[0])
            if not encoded:
                sg.popup_no_titlebar(f'Error trying to encode {file_list[0]}')
            else:
                sg.clipboard_set(encoded)
                sg.popup_no_titlebar(f'Image {file_list[0]} encoded and copied to clipboard')
        elif event == 'Convert to JPG':
            for file in file_list:
                if convert_formats(file, 'jpeg'):
                    sg.popup_no_titlebar(f'Image {file} converted to JPG')
                else:
                    sg.popup_no_titlebar('JPG file already exists')
        elif event == 'Convert to PNG':
            for file in file_list:
                if convert_formats(file, 'png'):
                    sg.popup_no_titlebar(f'Image {file} converted to PNG')
                else:
                    sg.popup_no_titlebar('PNG file already exists')
    else:
        location = (location[0]-600, location[1]-200)
        sg.popup(f'Dropped files:', '\n'.join(file_list), non_blocking=True, line_width=max(len(f)+1 for f in file_list), location=location, no_titlebar=True)


def main():

    PROGRAM_TO_LAUNCH_WHEN_DOUBLE_CLICKED = 'explorer'      # This will be run when icon is double-clicked. Change to any program you want.

    # Set to your own custom icon. This is displayed on the desktop
    # For fun, the icon is changes every couple of hours
    icon=sg.EMOJI_BASE64_COOL

    #------- GUI definition & setup --------#

    keep_on_top = sg.user_settings_get_entry('-keep on top-', False)

    RIGHT_CLICK_MENU = ['', ['Edit Me', f'Keep on top is {"ON" if keep_on_top else "OFF"}', 'Version', 'Exit']]
    layout = [[sg.Image(source=icon, key='-IMAGE-', p=0, background_color='black', enable_events=True)]]

    window = sg.Window('Desktop Icon Demo', layout, element_justification='center', resizable=True, no_titlebar=True, right_click_menu=RIGHT_CLICK_MENU, margins=(0,0), grab_anywhere=True, auto_save_location=True, keep_on_top=keep_on_top,  finalize=True)

    dnd.register_element_dnd(window['-IMAGE-'], window, dnd.DROP_TYPE_FILES)        # The one line of code needed to add drag and drop

    window['-IMAGE-'].bind('<Double-Button-1>', '+DOUBLE_CLICK+')

    window.timer_start(120*60*1000)         # every 120 minutes, change the icon (totally optional... just for fun)

    #------------ The Event Loop ------------#
    while True:
        event, values = window.read()
        # print(event, values)
        if event in (sg.WIN_CLOSED, 'Exit'):
            break

        if dnd.is_drop_event(event):                            # Drag and Drop event
            dnd_event: dnd.DropEvent = event
            if dnd_event.drop_type == dnd.DROP_TYPE_FILES:      # If files are dropped, show a window with choices of what to do with them
                show_choices(values[event], window.current_location())

        if event == '-IMAGE-+DOUBLE_CLICK+':                    # Add your double-click action here... such as launching another program
            loc = window.current_location()
            loc = (loc[0]-40, loc[1]-50)
            sg.popup_quick_message(f'Launching {PROGRAM_TO_LAUNCH_WHEN_DOUBLE_CLICKED}',  font='_ 10', background_color="#ffffe0",text_color='black', location=loc, auto_close_duration=3)
            sg.execute_command_subprocess(PROGRAM_TO_LAUNCH_WHEN_DOUBLE_CLICKED, wait=False)
        elif event == sg.TIMER_KEY:                                         # Change the icon shown every TIMER event
            window['-IMAGE-'].update(random.choice(sg.EMOJI_BASE64_HAPPY_LIST))
        elif event in ('Keep on top is OFF', 'Keep on top is ON'):          # Keep on top right click menu
            window.keep_on_top_set() if event.endswith('OFF') else window.keep_on_top_clear()
            RIGHT_CLICK_MENU[1][1] = f'Keep on top is {"ON" if event.endswith("OFF") else "OFF"}'
            window['-IMAGE-'].set_right_click_menu(RIGHT_CLICK_MENU)
            sg.user_settings_set_entry('-keep on top-', event.endswith("OFF"))
        elif event == 'Version':
            sg.popup_scrolled(sg.get_versions(), f'This Program: {__file__}' ,keep_on_top=True, non_blocking=True, location=window.current_location())
        elif event == 'Edit Me':
            sg.execute_editor(__file__)

    window.close()

if __name__ == '__main__':

    main()