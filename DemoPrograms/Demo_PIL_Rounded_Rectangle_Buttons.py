from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
import PySimpleGUI as sg

"""
    Demo Rounded Rectangle Buttons created using PIL
    
    A BIG thank you to @jason990420 for his talented work creating this demo.
    
    Demonstrates how you can draw buttons rather than using the built-in buttons
    with the help of the PIL module.
    
    One advantage is that the buttons will match your window's theme.
    
    You'll find more PySimpleGUI programs featured in 
    Mike Driscoll's PIL book - "Pillow: Image Processing with Python"
    
    Copyright 2021 PySimpleGUI, @jason990420 
"""


def im_to_data(im):
    """
    Convert a PIL.Image.Image to a bytes image
    :param im: Image
    :type: PIL.Image.Image object
    :return image in bytes
    :type: bytes
    """
    with BytesIO() as buffer:
        im.save(buffer, format='PNG')
        data = buffer.getvalue()
    return data


def rounded_rectangle(text,  font=('arial.ttf', 14), button_color=None,):
    """
    Generate rounded image with text aligned center.
    :param text: text to show on image, '\n' to split lines.
    :type text: str
    :param font: font for text
    :type font: Tuple
    :return image in bytes
    :type: bytes
    """
    pad, radius, spacing = 5, 10, 5
    ttf_font = ImageFont.truetype(font=font[0], size=font[1])
    if not text:
        text = ' '
    paragraph = text.split('\n')
    w = max(map(lambda x: ttf_font.getsize(x)[0], paragraph)) + 2 * pad
    h = sum(map(lambda x: ttf_font.getsize(x)[1], paragraph)) + 2 * pad + len(paragraph) * spacing
    c0, c1 = button_color if button_color else sg.theme_button_color()
    c0 = c0 if c0 != sg.COLOR_SYSTEM_DEFAULT else 'white'
    c1 = c1 if c1 != sg.COLOR_SYSTEM_DEFAULT else 'white'
    im = Image.new("RGBA", (w, h), (255, 255, 255, 0))
    draw = ImageDraw.Draw(im)
    draw.rounded_rectangle((0, 0, w-1, h-1), fill=c1, width=0, radius=radius)
    draw.multiline_text((pad, pad), text, align='center', font=ttf_font, fill=c0, spacing=spacing)
    return im_to_data(im)


# sg.theme("dark red")
sg.theme("dark green 7")
# sg.set_options(font=("Arial", 16))
layout = [[sg.Button('Normal Button')],
           [sg.Button('', image_data=sg.EMOJI_BASE64_HAPPY_THUMBS_UP, border_width=0, button_color=(sg.theme_background_color(), sg.theme_background_color()))],
          [sg.Button(image_data=rounded_rectangle('Button text\nwith 2 lines', font=('arial.ttf', 25)), button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0)]]

layout += [
      [sg.Button(
        image_data=rounded_rectangle(text, font=('cour.ttf', 25)),
        button_color=(sg.theme_button_color()[0], sg.theme_background_color()),
        border_width=0)]
     for text in (
        "My button",
        "Button with\n2 lines",
        "A long long ..................long line",
        "123\n2\n3")
    ]

window = sg.Window('Image and Rounded Button', layout, finalize=True, keep_on_top=True, use_custom_titlebar=True)

while True:

    event, values = window.read()
    if event in (sg.WINDOW_CLOSED, "Exit"):
        break

window.close()
