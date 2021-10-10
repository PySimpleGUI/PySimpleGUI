import PySimpleGUI as sg
from PIL import Image
import os
import base64

"""
    Demo Image Resize and Base64 Encode

    A quick little utility that will resize an image and also Base64 Encode it.

    Base64 is particualr good to use to make icons or other images that you include in your sourcecode.

    Copyright 2021 PySimpleGUI
"""

def resize(input_file, output_file, size):
    image = Image.open(input_file)
    width, height = image.size
    print(f"The original image size is {width} wide x {height} high")
    new_width, new_height = size
    scale = min(new_height / height, new_width / width)
    resized_image = image.resize((int(width * scale), int(height * scale)), Image.ANTIALIAS)
    # resized_image = image.resize(size)
    width, height = resized_image.size
    print(f"The resized image size is {width} wide x {height} high")
    resized_image.save(output_file)

def convert_file_to_base64(filename):
    try:
        contents = open(filename, 'rb').read()
        encoded = base64.b64encode(contents)
        sg.clipboard_set(encoded)
        sg.popup('Copied to your clipboard!', 'Keep window open until you have pasted the base64 bytestring')
    except Exception as error:
        sg.popup_error('Cancelled - An error occurred', error)

def main():
    layout = [  [sg.Text('Image Resizer')],
                [sg.Frame('Input Image', [[sg.Input(key='-IN-', enable_events=True), sg.FileBrowse()],
                [sg.T('Original size'), sg.T(k='-ORIG WIDTH-'), sg.T('X'), sg.T(k='-ORIG HEIGHT-')]])],
                [sg.Frame('New Size', [[sg.In(50, s=4, k='-WIDTH-'), sg.T('X'), sg.In(50, s=4, k='-HEIGHT-')]])],
                [sg.CBox('Encode to Base64 and leave on Clipboard', default=True,k='-BASE64-')],
                [sg.Button('Resize', bind_return_key=True), sg.Button('Exit')]  ]

    window = sg.Window('Resize Image', layout, icon=image_resize_icon, right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_VER_EXIT)

    while True:
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        infile = values['-IN-']
        if event == '-IN-':
            if os.path.isfile(infile):
                image = Image.open(infile)
                window['-ORIG WIDTH-'].update(image.size[0])
                window['-ORIG HEIGHT-'].update(image.size[1])
        if event == 'Resize':
            if os.path.isfile(infile):
                infilename = os.path.basename(infile)
                infilenameonly, infileext = os.path.splitext(infilename)
                outfile = f'{infilenameonly}50x50{infileext}'
                outfullfilename = os.path.join(os.path.dirname(infile), outfile)
                try:
                    resize(input_file=infile, output_file=outfullfilename, size=(int(values['-WIDTH-']), int(values['-HEIGHT-'])))
                    if values['-BASE64-']:
                        convert_file_to_base64(outfullfilename)
                except Exception as e:
                    sg.popup_error_with_traceback('Error resizing or converting', 'Error encountered during the resize or Base64 encoding', e)
                sg.popup_quick_message('DONE!', font='_ 40', background_color='red', text_color='white')
        elif event == 'Version':
            sg.popup_scrolled(sg.get_versions(), non_blocking=True)
        elif event == 'Edit Me':
            sg.execute_editor(__file__)
    window.close()


if __name__ == '__main__':
    image_resize_icon = b'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'

    main()