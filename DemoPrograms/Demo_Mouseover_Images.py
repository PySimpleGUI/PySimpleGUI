import PySimpleGUI as sg
import os
import shutil
from pathlib import Path

"""
    Demo Mouseover Images - Using mouseover images with Button and Image elements.
    
    NOTE - Requires PySimpleGUI version 6.2.17 or greater.
    To install the latest from GitHub run:
        python -m pip install --upgrade https://github.com/PySimpleGUI/PySimpleGUI/zipball/master
    
    Demonstrates how to specify images and change them after window is created.

    Because the image and mouseover image can be specified as a file, this demo downloads some images
        that are then used as local files.  They're deleted upon exit.
    A mixture of parameters are used to both specify the inital images but also when the images are
        updated to new images.
    Of course you would likely not be downloading your image files.  This demo downloads them so that image
        files don't have to accompany the dempo programs.

    Copyright 2026 PySimpleGUI. All rights reserved.
"""

MOUSEOVER_TEMP_FOLDER = 'mouseover_test'  # Temp folder to create in working dir. Stores the png files downloaded
IMAGE_FILENAMES = ('no_speak_56.png', 'no_see_56.png', 'no_hear_56.png')
URL = r'https://pysimplegui.net/images/emojis/'  # URL where emojis are located to be downloaded

# The base64 emoji's being used
see = sg.EMOJI_BASE64_NO_SEE
speak = sg.EMOJI_BASE64_NO_SPEAK
hear = sg.EMOJI_BASE64_NO_HEAR


def main():
    create_image_files()

    layout = [
        [
            sg.Image(data=see, k='-I1-', mouseover_image_source=speak, enable_events=True),
            sg.Image(filename=image_file('no_speak_56.png'), mouseover_image_source=image_file('no_hear_56.png'), k='-I2-', enable_events=True),
            sg.Image(source=hear, k='-I3-', mouseover_image_source=see, enable_events=True)],

        [sg.Button(image_data=see, k='-B1-', mouseover_image_source=speak),
         sg.Button(image_filename=image_file('no_speak_56.png'), mouseover_image_source=image_file('no_hear_56.png'), k='-B2-'),
         sg.Button(image_source=hear, mouseover_image_source=see, k='-B3-')],
        [sg.Button('Update')],
        [sg.Text(k='-STATUS-')],
    ]

    window = sg.Window("Image Test", layout, resizable=True, finalize=True)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        window['-STATUS-'].update(f'{event=}')
        if event == 'Update':  # Change all images and mouseover images
            window['-I1-'].update(filename=image_file('no_speak_56.png'), mouseover_image_source=hear)
            window['-I2-'].update(data=hear, mouseover_image_source=image_file('no_see_56.png'))
            window['-I3-'].update(source=see, mouseover_image_source=speak)

            window['-B1-'].update(image_filename=image_file('no_speak_56.png'), mouseover_image_source=hear)
            window['-B2-'].update(image_data=hear, mouseover_image_source=image_file('no_see_56.png'))
            window['-B3-'].update(image_source=see, mouseover_image_source=speak)

    window.close()

    del_image_files()


def image_file(name):
    return str((Path(MOUSEOVER_TEMP_FOLDER) / name).resolve())


def create_image_files():
    del_image_files()

    try:
        os.mkdir(MOUSEOVER_TEMP_FOLDER)
    except FileExistsError:  # folder already exists is fine
        pass
    except PermissionError:
        sg.popup_error_with_traceback(f'Unable to create images folder at {Path(MOUSEOVER_TEMP_FOLDER).resolve()}')
        raise PermissionError()

    for file in IMAGE_FILENAMES:
        with open(Path(MOUSEOVER_TEMP_FOLDER) / file, 'wb') as f:
            f.write(sg.net_download_file_binary(url=f'{URL}/{file}'))


def del_image_files():
    shutil.rmtree(MOUSEOVER_TEMP_FOLDER, ignore_errors=True)


if __name__ == '__main__':
    main()