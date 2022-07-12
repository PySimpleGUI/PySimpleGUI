import PySimpleGUI as sg
from PIL import Image
import os
import base64
import io
import webbrowser

"""
    Demo Image Resize and Base64 Encode

    This demo has been released to PyPI as the commnand `psgresizer`.  It is also in in this repo:
        https://github.com/PySimpleGUI/psgresizer
    A quick little utility that will resize an image, convert between formats, and also Base64 Encode it.

    Base64 is particularly good to use to make icons or other images that you include in your sourcecode.

    Use this Demo to help you code your PySimpleGUI programs.  Here's how:
    1. Select PNG as the output format
    2. Set "Encode to Base64" checkbox to True
    2. Click resize button
    2. Paste the base64 encoded byte-string left on the clipboard into your code as a variable
    3. Use your variable for things like an icon, an image for buttons, etc.

    Copyright 2021 PySimpleGUI
"""

version = '1.6.0'
__version__ = version.split()[0]

'''
Change log
    1.6.0   12-July-2022
        Fixed output filename to match the size indicated under the filename.
    1.5.4   10-May-2022
        Had to mess around with the entry point due to setuptools
    1.5.0   10-May-2022
        Moved icon to bottom of file and called set_global_icon so all windows in this application (including popups) will use this icon
    1.4.0   16-Nov-2021
        Explicitly set the settings filename. I'm still learning about these PyPI .EXE releases. Need to be explicit rather than default
    1.3.1   16-Nov-2021
        Added correct readme to PyPI
    1.3.0   16-Nov-2021
        Fixed bug - MUST always include the icon in the main function for these psg commands
    1.2.0   16-Nov-2021
        Somewhat extensive reworking of the functionality
        Added a drop-down list of formats to convert to
        Automatically save all the settings
        And more I'm sure!
'''


def resize(input_file, size, output_file=None, encode_format='PNG'):
    image = Image.open(input_file)
    width, height = image.size
    new_width, new_height = size
    if new_width != width or new_height != height:  # if the requested size is different than original size
        scale = min(new_height / height, new_width / width)
        resized_image = image.resize((int(width * scale), int(height * scale)), Image.ANTIALIAS)
    else:
        resized_image = image

    if output_file is not None:
        resized_image.save(output_file)

    # encode a PNG formatted version of image into BASE64
    with io.BytesIO() as bio:
        resized_image.save(bio, format=encode_format)
        contents = bio.getvalue()
        encoded = base64.b64encode(contents)
    return encoded


def main():

    def update_outfilename():
        infile = values['-IN-']
        if os.path.isfile(infile):

            image = Image.open(infile)
            width, height = image.size
            window['-ORIG WIDTH-'].update(image.size[0])
            if not values['-WIDTH-']:
                window['-WIDTH-'].update(image.size[0])
            else:
                width = values['-WIDTH-']
            if not values['-HEIGHT-']:
                window['-HEIGHT-'].update(image.size[1])
            else:
                height = values['-HEIGHT-']
            window['-ORIG HEIGHT-'].update(image.size[1])

            infilename = os.path.basename(infile)
            infilenameonly, infileext = os.path.splitext(infilename)
            if values['-NEW FORMAT-']:
                outfileext = values['-NEW FORMAT-'].lower()
                if outfileext == 'jpeg':
                    outfileext = 'jpg'
            else:
                outfileext = infileext[1:]  # strip off the .
            outfile = f'{infilenameonly}_{width}x{height}.{outfileext}'
            outfullfilename = os.path.join(os.path.dirname(infile), outfile)

            if values['-DO NOT SAVE-']:
                window['-NEW FILENAME-'].update('')
                window['-BASE64-'].update(True)
            else:
                window['-NEW FILENAME-'].update(outfullfilename)
        else:
            window['-NEW FILENAME-'].update('')
            window['-ORIG WIDTH-'].update('')
            # window['-WIDTH-'].update('')
            window['-ORIG HEIGHT-'].update('')
            # window['-HEIGHT-'].update('')
            window['-NEW FILENAME-'].update()

    sg.user_settings_filename(filename='psgresizer.json')


    format_list = ('', 'PNG', 'JPEG', 'BMP', 'ICO', 'GIF', 'TIFF')
    new_format_layout = [
        [sg.Combo(format_list, default_value=sg.user_settings_get_entry('-new format-', ''), readonly=True, enable_events=True, key='-NEW FORMAT-')]]

    layout = [[sg.Text('Image Resizer')],
              [sg.Frame('Input Filename', [[sg.Input(key='-IN-', enable_events=True, s=80), sg.FileBrowse(), ],
                                           [sg.T('Original size'), sg.T(k='-ORIG WIDTH-'), sg.T('X'), sg.T(k='-ORIG HEIGHT-')]])],
              [sg.Frame('Output Filename', [[sg.In(k='-NEW FILENAME-', s=80), sg.FileBrowse(), ],
                                            [sg.In(default_text=sg.user_settings_get_entry('-width-', ''), s=4, k='-WIDTH-', enable_events=True), sg.T('X'),
                                             sg.In(default_text=sg.user_settings_get_entry('-height-', ''), s=4, k='-HEIGHT-', enable_events=True)]])],
              [sg.Frame('Convert To New Format', new_format_layout)],
              [sg.CBox('Encode to Base64 and leave on Clipboard', k='-BASE64-', default=sg.user_settings_get_entry('-base64-', True))],
              # [sg.CBox('Use PNG for all Base64 Encoding', default=True, k='-PNG CONVERT-')],
              [sg.CBox('Do not save file - Only convert and Base64 Encode', k='-DO NOT SAVE-', enable_events=True,
                       default=sg.user_settings_get_entry('-do not save-', False))],
              [sg.CBox('Autoclose Immediately When Done', default=sg.user_settings_get_entry('-autoclose-', True if sg.running_windows() else False),
                       k='-AUTOCLOSE-')],
              [sg.Button('Resize', bind_return_key=True), sg.Button('Exit')],
              [sg.T('Note - on some systems, autoclose cannot be used because the clipboard is cleared by tkinter')],
              [sg.T('Your settings are automatically saved between runs')],
              [sg.T(f'Version {version}'), sg.T('Go to psgresizer GitHub Repo', font='_ 8', enable_events=True, k='-PSGRESIZER-'),
               sg.T('A PySimpleGUI Application - Go to PySimpleGUI home', font='_ 8', enable_events=True, k='-PYSIMPLEGUI-')],
              ]

    window = sg.Window('Resize Image', layout, right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_VER_LOC_EXIT,
                       enable_close_attempted_event=True, finalize=True)
    window['-PSGRESIZER-'].set_cursor('hand1')
    window['-PYSIMPLEGUI-'].set_cursor('hand1')
    while True:
        event, values = window.read()
        # print(event, values)
        if event in (sg.WIN_CLOSED, sg.WIN_CLOSE_ATTEMPTED_EVENT, 'Exit'):
            break
        infile = values['-IN-']
        update_outfilename()

        if event == '-DO NOT SAVE-':
            if values['-DO NOT SAVE-']:
                window['-NEW FILENAME-'].update('')
                window['-BASE64-'].update(True)
        if event == 'Resize':
            try:
                if os.path.isfile(infile):
                    update_outfilename()
                    infilename = os.path.basename(infile)
                    infilenameonly, infileext = os.path.splitext(infilename)
                    if values['-NEW FORMAT-']:
                        encode_format = values['-NEW FORMAT-'].upper()
                    else:
                        encode_format = infileext[1:].upper()  # strip off the .
                    if encode_format == 'JPG':
                        encode_format = 'JPEG'
                    outfullfilename = values['-NEW FILENAME-']
                    width, height = int(values['-WIDTH-']), int(values['-HEIGHT-'])
                    if values['-DO NOT SAVE-']:
                        encoded = resize(input_file=infile, size=(width, height), output_file=None, encode_format=encode_format)
                    else:
                        encoded = resize(input_file=infile, size=(width, height), output_file=outfullfilename, encode_format=encode_format)

                    if values['-BASE64-']:
                        sg.clipboard_set(encoded)

                    sg.popup_quick_message('DONE!', font='_ 40', background_color='red', text_color='white')

            except Exception as e:
                sg.popup_error_with_traceback('Error resizing or converting', 'Error encountered during the resize or Base64 encoding', e)
            if values['-AUTOCLOSE-']:
                break
        elif event == 'Version':
            sg.popup_scrolled(sg.get_versions(), non_blocking=True)
        elif event == 'Edit Me':
            sg.execute_editor(__file__)
        elif event == 'File Location':
            sg.popup_scrolled('This Python file is:', __file__)
        elif event == '-PYSIMPLEGUI-':
            webbrowser.open_new_tab(r'http://www.PySimpleGUI.com')
        elif event == '-PSGRESIZER-':
            webbrowser.open_new_tab(r'https://github.com/PySimpleGUI/psgresizer')
        elif event in ('-WIDTH-', '-HEIGHT-'):
            update_outfilename()

    if event != sg.WIN_CLOSED:
        sg.user_settings_set_entry('-autoclose-', values['-AUTOCLOSE-'])
        sg.user_settings_set_entry('-new format-', values['-NEW FORMAT-'])
        sg.user_settings_set_entry('-do not save-', values['-DO NOT SAVE-'])
        sg.user_settings_set_entry('-base64-', values['-BASE64-'])
        sg.user_settings_set_entry('-width-', values['-WIDTH-'])
        sg.user_settings_set_entry('-height-', values['-HEIGHT-'])
    window.close()


def main_entry_point():
    image_resize_icon = b'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'

    sg.set_global_icon(image_resize_icon)
    main()

if __name__ == '__main__':
    main_entry_point()
