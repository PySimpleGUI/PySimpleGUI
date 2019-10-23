#!/usr/bin/env python
import PySimpleGUI as sg
import os

'''
    Simple Image Browser based on PySimpleGUI
'''


def main():

    # Get the folder containing the images from the user
    folder = sg.popup_get_folder('Image folder to open')
    if folder is None:
        sg.popup_cancel('Cancelling')
        return

    # get list of PNG files in folder
    png_files = [folder + '\\' + f for f in os.listdir(folder) if '.png' in f]
    filenames_only = [f for f in os.listdir(folder) if '.png' in f]

    if len(png_files) == 0:
        sg.popup('No PNG images in folder')
        return

    # define menu layout
    menu = [['File', ['Open Folder', 'Exit']], ['Help', ['About', ]]]

    # define layout, show and read the window
    col = [[sg.Text(png_files[0], size=(80, 3), key='filename')],
           [sg.Image(filename=png_files[0], key='image')],
           [sg.Button('Next', size=(8, 2)), sg.Button('Prev', size=(8, 2)),
               sg.Text('File 1 of {}'.format(len(png_files)), size=(15, 1), key='filenum')]]

    col_files = [[sg.Listbox(values=filenames_only, size=(60, 30), key='listbox')],
                 [sg.Button('Read')]]
    layout = [[sg.Menu(menu)], [sg.Col(col_files), sg.Col(col)]]
    window = sg.Window('Image Browser', layout,
            return_keyboard_events=True,
            location=(0, 0),
            use_default_focus=False)

    # loop reading the user input and displaying image, filename
    i = 0
    while True:

        event, values = window.read()
        # --------------------- Button & Keyboard ---------------------
        if event is None:
            break
        elif event in ('Next', 'MouseWheel:Down', 'Down:40', 'Next:34') and i < len(png_files)-1:
            i += 1
        elif event in ('Prev', 'MouseWheel:Up', 'Up:38', 'Prior:33') and i > 0:
            i -= 1
        elif event == 'Exit':
            break

        if event == 'Read':
            filename = folder + '/' + values['listbox'][0]
        else:
            filename = png_files[i]

        # ----------------- Menu choices -----------------
        if event == 'Open Folder':
            newfolder = sg.popup_get_folder('New folder', no_window=True)
            if newfolder is None:
                continue

            folder = newfolder
            png_files = [folder + '/' +
                         f for f in os.listdir(folder) if '.png' in f]
            filenames_only = [f for f in os.listdir(folder) if '.png' in f]

            window['listbox'].update(values=filenames_only)
            window.refresh()

            i = 0
        elif event == 'About':
            sg.popup('Demo PNG Viewer Program',
                     'Please give PySimpleGUI a try!')

        # update window with new image
        window['image'].update(filename=filename)
        # update window with filename
        window['filename'].update(filename)
        # update page display
        window['filenum'].update('File {} of {}'.format(i+1, len(png_files)))

    window.close()

if __name__ == '__main__':
    main()