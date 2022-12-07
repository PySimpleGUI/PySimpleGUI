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
    
    Copyright 2020, 2022 PySimpleGUI.org
"""

def make_square(im,  fill_color=(0, 0, 0, 0)):
    x, y = im.size
    size = max(x, y)
    new_im = Image.new('RGBA', (size, size), fill_color)
    new_im.paste(im, (int((size - x) / 2), int((size - y) / 2)))
    return new_im



def convert_to_bytes(source, size=(None, None), subsample=None, zoom=None, fill=False):
    """
    Will convert into bytes and optionally resize an image that is a file or a base64 bytes object.
    Turns into  PNG format in the process so that can be displayed by tkinter
    :param source: either a string filename or a bytes base64 image object
    :type source:  (Union[str, bytes])
    :param size:  optional new size (width, height)
    :type size: (Tuple[int, int] or None)
    :param subsample: change the size by multiplying width and height by 1/subsample
    :type subsample: (int)
    :param zoom: change the size by multiplying width and height by zoom
    :type zoom: (int)
    :param fill: If True then the image is filled/padded so that the image is square
    :type fill: (bool)
    :return: (bytes) a byte-string object
    :rtype: (bytes)
    """
    if isinstance(source, str):
        image = Image.open(source)
    elif isinstance(source, bytes):
        image = Image.open(io.BytesIO(base64.b64decode(source)))
    else:
        image = PIL.Image.open(io.BytesIO(source))

    width, height = image.size

    scale = None
    if size != (None, None):
        new_width, new_height = size
        scale = min(new_height/height, new_width/width)
    elif subsample is not None:
        scale = 1/subsample
    elif zoom is not None:
        scale = zoom

    resized_image = image.resize((int(width * scale), int(height * scale)), Image.ANTIALIAS) if scale is not None else image
    if fill and scale is not None:
        resized_image = make_square(resized_image)
    # encode a PNG formatted version of image into BASE64
    with io.BytesIO() as bio:
        resized_image.save(bio, format="PNG")
        contents = bio.getvalue()
        encoded = base64.b64encode(contents)
    return encoded




def random_image():
    return random.choice(sg.EMOJI_BASE64_LIST)

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
            image = random.choice(sg.EMOJI_BASE64_LIST)
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