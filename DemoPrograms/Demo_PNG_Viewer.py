#!/usr/bin/env python
import PySimpleGUI as sg
import os

'''
    Simple Image Browser 
    
    This is an early demo program, so perhaps not quite as sophisticated as later ones.
    
    Copyright 2021 PySimpleGUI
'''


def main():

    # Get the folder containing the images from the user
    folder = sg.popup_get_folder('Image folder to open')
    if folder is None:
        sg.popup_cancel('Cancelling')
        return

    # get list of PNG files in folder
    png_files = [os.path.join(folder, f) for f in os.listdir(folder) if f.lower().endswith('.png')]
    filenames_only = [f for f in os.listdir(folder) if f.lower().endswith('.png')]

    if len(png_files) == 0:
        sg.popup('No PNG images in folder')
        return

    # define menu layout
    menu = [['File', ['Open Folder', 'Exit']], ['Help', ['About', ]]]

    # define layout, show and read the window
    col = [[sg.Text(png_files[0], size=(80, 3), key='-FILENAME-')],
           [sg.Image(filename=png_files[0], key='-IMAGE-', expand_x=True, expand_y=True)],
           [sg.Button('Next', size=(8, 2)), sg.Button('Prev', size=(8, 2)),
               sg.Text('File 1 of {}'.format(len(png_files)), size=(15, 1), key='-FILENUM-')]]

    col_files = [[sg.Listbox(values=filenames_only, size=(60, 30), key='-LISTBOX-', enable_events=True)],
                 [sg.Text('Select a file.  Use scrollwheel or arrow keys on keyboard to scroll through files one by one.')]]

    layout = [[sg.Menu(menu)], [sg.Col(col_files), sg.Col(col, expand_x=True, expand_y=True)]]

    window = sg.Window('Image Browser', layout, return_keyboard_events=True, use_default_focus=False)

    # loop reading the user input and displaying image, filename
    filenum, filename = 0, png_files[0]
    while True:

        event, values = window.read()
        # --------------------- Button & Keyboard ---------------------
        if event == sg.WIN_CLOSED:
            break
        elif event in ('Next', 'MouseWheel:Down', 'Down:40', 'Next:34') and filenum < len(png_files)-1:
            filenum += 1
            filename = os.path.join(folder, filenames_only[filenum])
            window['-LISTBOX-'].update(set_to_index=filenum, scroll_to_index=filenum)
        elif event in ('Prev', 'MouseWheel:Up', 'Up:38', 'Prior:33') and filenum > 0:
            filenum -= 1
            filename = os.path.join(folder, filenames_only[filenum])
            window['-LISTBOX-'].update(set_to_index=filenum, scroll_to_index=filenum)
        elif event == 'Exit':
            break
        elif event == '-LISTBOX-':
            filename = os.path.join(folder, values['-LISTBOX-'][0])
            filenum = png_files.index(filename)
        # ----------------- Menu choices -----------------
        if event == 'Open Folder':
            newfolder = sg.popup_get_folder('New folder', no_window=True)
            if newfolder is None:
                continue

            folder = newfolder
            png_files = [os.path.join(folder, f) for f in os.listdir(folder) if f.lower().endswith('.png')]
            filenames_only = [f for f in os.listdir(folder) if f.lower().endswith('.png')]

            window['-LISTBOX-'].update(values=filenames_only)
            window.refresh()

            filenum = 0
        elif event == 'About':
            sg.popup('Demo PNG Viewer Program',
                     'Please give PySimpleGUI a try!')

        # update window with new image
        window['-IMAGE-'].update(filename=filename)
        # update window with filename
        window['-FILENAME-'].update(filename)
        # update page display
        window['-FILENUM-'].update('File {} of {}'.format(filenum + 1, len(png_files)))

    window.close()

if __name__ == '__main__':
    main()