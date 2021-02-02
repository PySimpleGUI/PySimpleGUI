import PySimpleGUI as sg
import PIL
from PIL import Image
import io
import base64
import random

"""
    Using PIL with PySimpleGUI - for Images and Buttons
    
    The reason for this demo is to give you this nice PIL based function - convert_to_bytes
    
    This function is your gateway to using any format of image (not just PNG & GIF) and to 
    resize / convert it so that it can be used with the Button and Image elements.
    
    Copyright 2020 PySimpleGUI.org
"""

def make_square(im, min_size=256, fill_color=(0, 0, 0, 0)):
    x, y = im.size
    size = max(min_size, x, y)
    new_im = Image.new('RGBA', (size, size), fill_color)
    new_im.paste(im, (int((size - x) / 2), int((size - y) / 2)))
    return new_im


def convert_to_bytes(file_or_bytes, resize=None, fill=False):
    """
    Will convert into bytes and optionally resize an image that is a file or a base64 bytes object.
    Turns into  PNG format in the process so that can be displayed by tkinter
    :param file_or_bytes: either a string filename or a bytes base64 image object
    :type file_or_bytes:  (Union[str, bytes])
    :param resize:  optional new size
    :type resize: (Tuple[int, int] or None)
    :param fill: If True then the image is filled/padded so that the image is not distorted
    :type fill: (bool)
    :return: (bytes) a byte-string object
    :rtype: (bytes)
    """
    if isinstance(file_or_bytes, str):
        img = PIL.Image.open(file_or_bytes)
    else:
        try:
            img = PIL.Image.open(io.BytesIO(base64.b64decode(file_or_bytes)))
        except Exception as e:
            dataBytesIO = io.BytesIO(file_or_bytes)
            img = PIL.Image.open(dataBytesIO)

    cur_width, cur_height = img.size
    if resize:
        new_width, new_height = resize
        scale = min(new_height / cur_height, new_width / cur_width)
        img = img.resize((int(cur_width * scale), int(cur_height * scale)), PIL.Image.ANTIALIAS)
    if fill:
        if resize is not None:
            img = make_square(img, resize[0])
    with io.BytesIO() as bio:
        img.save(bio, format="PNG")
        del img
        return bio.getvalue()

def random_image():
    return random.choice(sg.ICON_BASE64_LIST)

def make_toolbar():
    layout = [[sg.T('❎', enable_events=True, key='Exit')]]
    for i in range(6):
        layout += [[sg.B(image_data = convert_to_bytes(random_image(), (30,30))),
                    sg.B(image_data = convert_to_bytes(random_image(), (30,30)))]]
    return sg.Window('', layout, element_padding=(0,0), margins=(0,0), finalize=True, no_titlebar=True, grab_anywhere=True)

def main():

    image = random_image()
    size = (60,60)
    image = convert_to_bytes(image, size, fill=False)

    layout =    [[sg.Button('+', size=(4,2)), sg.Button('-', size=(4,2)), sg.B('Next', size=(4,2)), sg.T(size, size=(10,1), k='-SIZE-')],
                [sg.Image(data=image, k='-IMAGE-')],
                [sg.Button(image_data=image, key='-BUTTON IMAGE-')],]

    window = sg.Window('Window Title', layout, finalize=True)
    toolbar = make_toolbar()

    while True:             # Event Loop
        event_window, event, values = sg.read_all_windows()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == '+':
            size = (size[0]+20, size[1]+20)
        elif event == '-':
            if size[0] > 20:
                size = (size[0]-20, size[1]-20)
        elif event in ('Next', '-BUTTON IMAGE-'):
            image = random.choice(sg.ICON_BASE64_LIST)
        elif event_window == toolbar:
            image = event_window[event].ImageData

        # Resize image and update the window
        image = convert_to_bytes(image, size, fill=True)
        window['-IMAGE-'].update(data=image)
        window['-BUTTON IMAGE-'].update(image_data=image)
        window['-SIZE-'].update(size)
    window.close()


if __name__ == '__main__':
    main()