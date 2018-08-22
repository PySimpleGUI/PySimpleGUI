import PySimpleGUI as sg
import os

# Simple Image Browser based on PySimpleGUI

# sg.ChangeLookAndFeel('GreenTan')

# Get the folder containing the images from the user
rc, folder = sg.GetPathBox('Image Browser', 'Image folder to open', default_path='A:/TEMP/PDFs')
if rc is False or folder is '':
    sg.MsgBoxCancel('Cancelling')
    exit(0)

# get list of PNG files in folder
png_files = [folder + '\\' + f for f in os.listdir(folder) if '.png' in f]

if len(png_files) == 0:
    sg.MsgBox('No PNG images in folder')
    exit(0)

# create the form
form = sg.FlexForm('Image Browser', return_keyboard_events=True)

# make these 2 elements outside the layout because want to "update" them later
image_elem = sg.Image(filename=png_files[0])
text_elem = sg.Text(png_files[0], size=(80,3))

# define layout, show and read the form
layout = [[text_elem],
          [image_elem],
          [sg.ReadFormButton('Next', size=(8,2)), sg.ReadFormButton('Prev', size=(8,2))]]

form.LayoutAndRead(layout)

# loop reading the user input and display each image and the filename
i=0
while True:
    f = png_files[i]
    # update window with new image
    image_elem.Update(filename=f)
    # update window with filename
    text_elem.Update(f)
    # read the form
    button, values = form.Read()

    # perform button operations
    if button is None:
        break
    elif button in ('Next', 'MouseWheel:Down', 'Down:40', 'Next:34') and i < len(png_files):
        i += 1
    elif button in ('Prev', 'MouseWheel:Up', 'Up:38', 'Prior:33') and i > 0:
        i -= 1
    # else:
    #     print(button)


