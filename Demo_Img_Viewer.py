import PySimpleGUI as sg
import os
from PIL import Image, ImageTk
import io
"""
Simple Image Browser based on PySimpleGUI
--------------------------------------------
There are some improvements compared to the PNG browser of the repository:
1. Paging is cyclic, i.e. automatically wraps around if file index is outside
2. Supports all file types that are valid PIL images
3. Limits the maximum form size to the physical screen
4. When selecting an image from the listbox, subsequent paging uses its index
5. Paging performance improved significantly because of using PIL

Dependecies
------------
Python v3
PIL
"""
# Get the folder containing the images from the user
rc, folder = sg.GetPathBox('Image Browser', 'Image folder to open', default_path='')
if not rc or not folder:
    sg.PopupCancel('Cancelling')
    raise SystemExit()

# PIL supported image types
img_types = (".png", ".jpg", "jpeg", ".tiff", ".bmp")

# get list of files in folder
flist0 = os.listdir(folder)

# create sub list of image files (no sub folders, no wrong file types)
fnames = [f for f in flist0 if os.path.isfile(os.path.join(folder,f)) and f.lower().endswith(img_types)]

num_files = len(fnames)                # number of iamges found
if num_files == 0:
    sg.Popup('No files in folder')
    raise SystemExit()

del flist0                             # no longer needed

#------------------------------------------------------------------------------
# use PIL to read data of one image
#------------------------------------------------------------------------------
def get_img_data(f, maxsize = (1200, 850), first = False):
    """Generate image data using PIL
    """
    img = Image.open(f)
    img.thumbnail(maxsize)
    if first:                     # tkinter is inactive the first time
        bio = io.BytesIO()
        img.save(bio, format = "PNG")
        del img
        return bio.getvalue()
    return ImageTk.PhotoImage(img)
#------------------------------------------------------------------------------


# create the form that also returns keyboard events
form = sg.FlexForm('Image Browser', return_keyboard_events=True,
                   location=(0, 0), use_default_focus=False)

# make these 2 elements outside the layout as we want to "update" them later
# initialize to the first file in the list
filename = os.path.join(folder, fnames[0])  # name of first file in list
image_elem = sg.Image(data = get_img_data(filename, first = True))
filename_display_elem = sg.Text(filename, size=(80, 3))
file_num_display_elem = sg.Text('File 1 of {}'.format(num_files), size=(15,1))

# define layout, show and read the form
col = [[filename_display_elem],
          [image_elem]]

col_files = [[sg.Listbox(values = fnames, select_submits=True, size=(60,30), key='listbox')],
             [sg.ReadFormButton('Next', size=(8,2)), sg.ReadFormButton('Prev',
                             size=(8,2)), file_num_display_elem]]

layout = [[sg.Column(col_files), sg.Column(col)]]

form.Layout(layout)          # Shows form on screen

# loop reading the user input and displaying image, filename
i=0
while True:
    # read the form
    button, values = form.Read()

    # perform button and keyboard operations
    if button is None:
        break
    elif button in ('Next', 'MouseWheel:Down', 'Down:40', 'Next:34'):
        i += 1
        if i >= num_files:
            i -= num_files
        filename = os.path.join(folder, fnames[i])
    elif button in ('Prev', 'MouseWheel:Up', 'Up:38', 'Prior:33'):
        i -= 1
        if i < 0:
            i = num_files + i
        filename = os.path.join(folder, fnames[i])
    elif button in ('Read', ''):            # something from the listbox
        f = values["listbox"][0]            # selected filename
        filename = os.path.join(folder, f)  # read this file
        i = fnames.index(f)                 # update running index
    else:
        filename = os.path.join(folder, fnames[i])

    # update window with new image
    image_elem.Update(data=get_img_data(filename))
    # update window with filename
    filename_display_elem.Update(filename)
    # update page display
    file_num_display_elem.Update('File {} of {}'.format(i+1, num_files))


