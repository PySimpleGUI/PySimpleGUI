import PySimpleGUI as sg
import os

# Simple Image Browser based on PySimpleGUI

# Get the folder containing the images from the user
folder = sg.PopupGetFolder('Image folder to open')
if folder is None:
    sg.PopupCancel('Cancelling')
    exit(0)

# get list of PNG files in folder
png_files = [folder + '\\' + f for f in os.listdir(folder) if '.png' in f]
filenames_only = [f for f in os.listdir(folder) if '.png' in f]

if len(png_files) == 0:
    sg.Popup('No PNG images in folder')
    exit(0)


# define menu layout
menu = [['File', ['Open Folder', 'Exit']], ['Help', ['About',]]]
# create the form that also returns keyboard events
form = sg.FlexForm('Image Browser', return_keyboard_events=True, location=(0,0), use_default_focus=False )

# define layout, show and read the form
col = [[sg.Text(png_files[0], size=(80, 3), key='filename')],
          [sg.Image(filename=png_files[0], key='image')],
          [sg.ReadFormButton('Next', size=(8,2)), sg.ReadFormButton('Prev', size=(8,2)),
           sg.Text('File 1 of {}'.format(len(png_files)), size=(15,1), key='filenum')]]

col_files = [[sg.Listbox(values=filenames_only, size=(60,30), key='listbox')],
             [sg.ReadFormButton('Read')]]
layout = [[sg.Menu(menu)], [sg.Column(col_files), sg.Column(col)]]
button, values = form.LayoutAndRead(layout)          # Shows form on screen

# loop reading the user input and displaying image, filename
i=0
while True:

    # --------------------- Button & Keyboard ---------------------
    if button is None:
        break
    elif button in ('Next', 'MouseWheel:Down', 'Down:40', 'Next:34') and i < len(png_files)-1:
        i += 1
    elif button in ('Prev', 'MouseWheel:Up', 'Up:38', 'Prior:33') and i > 0:
        i -= 1
    elif button == 'Exit':
        exit(69)

    filename = folder + '/' + values['listbox'][0] if button == 'Read' else png_files[i]

    # ----------------- Menu choices -----------------
    if button == 'Open Folder':
        newfolder = sg.PopupGetFolder('New folder', no_window=True)
        if newfolder is None:
            continue
        folder = newfolder
        png_files = [folder + '/' + f for f in os.listdir(folder) if '.png' in f]
        filenames_only = [f for f in os.listdir(folder) if '.png' in f]
        form.FindElement('listbox').Update(values=filenames_only)
        form.Refresh()
        i = 0
    elif button == 'About':
        sg.Popup('Demo PNG Viewer Program', 'Please give PySimpleGUI a try!')

    # update window with new image
    form.FindElement('image').Update(filename=filename)
    # update window with filename
    form.FindElement('filename').Update(filename)
    # update page display
    form.FindElement('filenum').Update('File {} of {}'.format(i+1, len(png_files)))

    # read the form
    button, values = form.Read()
