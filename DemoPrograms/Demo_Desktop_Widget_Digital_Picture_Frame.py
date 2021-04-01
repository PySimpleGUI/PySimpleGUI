import PySimpleGUI as sg
import sys
import datetime
import PIL, PIL.Image, PIL.ImageTk
import random
import os
import io

"""
    Another simple Desktop Widget using PySimpleGUI

    This one shows images from a folder of your choosing.
    You can change the new "Standard Desktop Widget Settings"
        * Theme, location, alpha channel, refresh info, 

    Specific to this Widget are
        * Image size
        * How long to show the image and if you wnt this time to vary semi-randomly
        * Folder containing your image
        

    Copyright 2021 PySimpleGUI
"""

ALPHA = 0.9  # Initial alpha until user changes
THEME = 'Dark green 3'  # Initial theme until user changes
refresh_font = sg.user_settings_get_entry('-refresh font-', 'Courier 8')

# May add ability to change theme from the user interface.  For now forcing to constant

UPDATE_FREQUENCY_MILLISECONDS = 1000 * 60 * 60  # update every hour

def convert_to_bytes(file_or_bytes, resize=None):
    image = PIL.Image.open(file_or_bytes)
    image.thumbnail(resize)
    photo_img = PIL.ImageTk.PhotoImage(image)
    return photo_img


def choose_theme(location):
    layout = [[sg.Text(f'Current theme {sg.theme()}')],
              [sg.Listbox(values=sg.theme_list(), size=(20, 20), key='-LIST-')],
              [sg.OK(), sg.Cancel()]]

    event, values = sg.Window('Look and Feel Browser', layout, location=location, keep_on_top=True).read(close=True)


    if event == 'OK' and values['-LIST-']:
        sg.theme(values['-LIST-'][0])
        sg.user_settings_set_entry('-theme-', values['-LIST-'][0])
        return values['-LIST-'][0]
    return None


def make_window(location):
    alpha = sg.user_settings_get_entry('-alpha-', ALPHA)

    # ------------------- Window Layout -------------------
    # If this is a test window (for choosing theme), then uses some extra Text Elements to display theme info
    # and also enables events for the elements to make the window easy to close
    right_click_menu = [[''], ['Choose Image Folder', 'Edit Me', 'Change Theme', 'Set Image Size',
                               'Set Time Per Image','Save Location', 'Refresh', 'Show Refresh Info', 'Hide Refresh Info', 'Alpha',
                                   [str(x) for x in range(1, 11)], 'Exit', ]]

    refresh_info = [[sg.T(size=(25, 1), font=refresh_font, k='-REFRESHED-', justification='c')],
                    [sg.T(size=(40,1), justification='c', font=refresh_font, k='-FOLDER-')],
                    [sg.T(size=(40,1), justification='c', font=refresh_font, k='-FILENAME-')]]

    main_layout = [[sg.Image(k='-IMAGE-', enable_events=True)]]

    layout = main_layout + \
             [[sg.pin(sg.Column(refresh_info, key='-REFRESH INFO-', element_justification='c', visible=sg.user_settings_get_entry('-show refresh-', True)))]]

    window = sg.Window('Photo Frame', layout, location=location, no_titlebar=True, grab_anywhere=True, margins=(0, 0), element_justification='c', element_padding=(0, 0), alpha_channel=alpha, finalize=True, right_click_menu=right_click_menu, keep_on_top=True)

    return window


def main():
    loc = sg.user_settings_get_entry('-location-', (None, None))
    sg.theme(sg.user_settings_get_entry('-theme-', None))
    window = make_window(loc)

    time_per_image = sg.user_settings_get_entry('-time per image-', 60)
    vary_randomly = sg.user_settings_get_entry('-random time-', False)
    width, height = sg.user_settings_get_entry('-image size-', (400,300))
    image_folder = sg.user_settings_get_entry('-image_folder-', None)

    try:
        os.listdir(image_folder)        # Try reading the folder to check to see if it is read
    except:
        image_folder = None
        sg.user_settings_set_entry('-image_folder-', None)

    if image_folder is None:
        while True:
            image_folder = sg.popup_get_folder('Choose location of your images', location=window.current_location(), keep_on_top=True)
            if image_folder is not None:
                sg.user_settings_set_entry('-image_folder-', image_folder)
                break
            else:
                if sg.popup_yes_no('No folder entered','Go you want to exit the program entirely?', keep_on_top=True) == 'Yes':
                    exit()
    images = os.listdir(image_folder)
    images = [i for i in images if i.lower().endswith(('.png', '.jpg', '.gif'))]
    while True:  # Event Loop
        # First update the status information
        # for debugging show the last update date time
        image_name =random.choice(images)
        image_data = convert_to_bytes(os.path.join(image_folder, image_name), (width, height))
        window['-IMAGE-'].update(data=image_data)
        window['-FOLDER-'].update(image_folder)
        window['-FILENAME-'].update(image_name)
        print(f'showing {image_name}')
        window['-REFRESHED-'].update(datetime.datetime.now().strftime("%m/%d/%Y %I:%M:%S %p"))
        # -------------- Start of normal event loop --------------
        timeout = time_per_image * 1000 + (random.randint(int(-time_per_image * 500), int(time_per_image * 500)) if vary_randomly else 0)
        event, values = window.read(timeout=timeout)
        print(event, values)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == 'Edit Me':
            sg.execute_editor(__file__)
        elif event == 'Choose Image Folder':
            folder = sg.popup_get_folder('Choose location of your images', default_path=image_folder, location=window.current_location(), keep_on_top=True)
            if folder is not None:
                image_folder = folder
                window['-FOLDER-'].update(image_folder)
                sg.user_settings_set_entry('-image_folder-', image_folder)
                images = os.listdir(image_folder)
                images = [i for i in images if i.lower().endswith(('.png', '.jpg', '.gif'))]
        elif event == 'Set Time Per Image':
            layout = [[sg.T('Enter number of seconds each image should be displayed')],
                       [sg.I(time_per_image, size=(5,1),k='-TIME PER IMAGE-')],
                       [sg.CB('Use some randomness', vary_randomly, k='-RANDOM TIME-')],
                       [sg.Ok(), sg.Cancel()]]
            event, values = sg.Window('Display duration',layout, location=window.current_location(), keep_on_top=True, no_titlebar=True ).read(close=True)
            if event == 'Ok':
                try:
                    time_per_image = int(values['-TIME PER IMAGE-'])
                    vary_randomly = values['-RANDOM TIME-']
                    sg.user_settings_set_entry('-time per image-', time_per_image)
                    sg.user_settings_set_entry('-random time-', values['-RANDOM TIME-'])
                except:
                    sg.popup_error('Bad number of seconds entered', location=window.current_location(), keep_on_top=True)
        elif event == 'Set Image Size':
            layout = [[sg.T('Enter size should be shown at in pixels (width, height)')],
                       [sg.I(width, size=(4,1),k='-W-'), sg.I(height, size=(4,1),k='-H-')],
                       [sg.Ok(), sg.Cancel()]]
            event, values = sg.Window('Image Dimensions',layout, location=window.current_location(), keep_on_top=True, no_titlebar=True ).read(close=True)
            if event == 'Ok':
                try:
                    w,h = int(values['-W-']), int(values['-H-'])
                    sg.user_settings_set_entry('-image size-', (w,h))
                    width, height = w,h
                except:
                    sg.popup_error('Bad size specified. Use integers only', location=window.current_location(), keep_on_top=True)
        elif event == 'Show Refresh Info':
            window['-REFRESH INFO-'].update(visible=True)
            sg.user_settings_set_entry('-show refresh-', True)
        elif event == 'Save Location':
            sg.user_settings_set_entry('-location-', window.current_location())
        elif event == 'Hide Refresh Info':
            window['-REFRESH INFO-'].update(visible=False)
            sg.user_settings_set_entry('-show refresh-', False)
        elif event in [str(x) for x in range(1, 11)]:
            window.set_alpha(int(event) / 10)
            sg.user_settings_set_entry('-alpha-', int(event) / 10)
        elif event == 'Change Theme':
            loc = window.current_location()
            if choose_theme(loc) is not None:
                window.close()
                window = make_window(loc)

    window.close()

if __name__ == '__main__':
    main()