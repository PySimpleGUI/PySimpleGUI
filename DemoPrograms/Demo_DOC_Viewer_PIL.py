"""
@created: 2018-08-19 18:00:00
@author: (c) 2018 Jorj X. McKie
Display a PyMuPDF Document using Tkinter
-------------------------------------------------------------------------------
Dependencies:
-------------
PyMuPDF, PySimpleGUI (requires Python 3), Tkinter, PIL
License:
--------
GNU GPL V3+
Description
------------
Get filename and start displaying page 1. Please note that all file types
of MuPDF are supported (including EPUB e-books and HTML files for example).
Pages can be directly jumped to, or buttons can be used for paging.

This version contains enhancements:
* Use of PIL improves response times by a factor 3 or more.
* Zooming is now flexible: only one button serves as a toggle. Arrow keys can
  be used for moving the window when zooming.

We also interpret keyboard events (PageDown / PageUp) and mouse wheel actions
to support paging as if a button was clicked. Similarly, we do not include
a 'Quit' button. Instead, the ESCAPE key can be used, or cancelling the window.
To improve paging performance, we are not directly creating pixmaps from
pages, but instead from the fitz.DisplayList of the page. A display list
will be stored in a list and looked up by page number. This way, zooming
pixmaps and page re-visits will re-use a once-created display list.

"""
import sys
import fitz
import sys
import PySimpleGUI as sg

import tkinter as tk
from PIL import Image, ImageTk
import time

if len(sys.argv) == 1:
    fname = sg.popup_get_file('Document Browser', 'Document file to open',
                              no_window=True,
                              file_types=(
                                  ("PDF Files",     "*.pdf"),
                                  ("XPS Files",     "*.*xps"),
                                  ("Epub Files",    "*.epub"),
                                  ("Fiction Books", "*.fb2"),
                                  ("Comic Books",   "*.cbz"),
                                  ("HTML",   "*.htm*")
                                  # add more document types here
                              )
                              )
else:
    fname = sys.argv[1]

if not fname:
    sg.popup("Cancelling:", "No filename supplied")
    raise SystemExit("Cancelled: no filename supplied")

doc = fitz.open(fname)
page_count = len(doc)

# used for response time statistics only
fitz_img_time = 0.0
tk_img_time = 0.0
img_count = 1

# allocate storage for page display lists
dlist_tab = [None] * page_count

title = "PyMuPDF display of '%s', pages: %i" % (fname, page_count)


def get_page(pno, zoom=False, max_size=None, first=False):
    """Return a PNG image for a document page number.
    """
    dlist = dlist_tab[pno]   # get display list of page number
    if not dlist:            # create if not yet there
        dlist_tab[pno] = doc[pno].getDisplayList()
        dlist = dlist_tab[pno]
    r = dlist.rect           # the page rectangle
    clip = r
    # ensure image fits screen:
    # exploit, but do not exceed width or height
    zoom_0 = 1
    if max_size:
        zoom_0 = min(1, max_size[0] / r.width, max_size[1] / r.height)
        if zoom_0 == 1:
            zoom_0 = min(max_size[0] / r.width, max_size[1] / r.height)
    mat_0 = fitz.Matrix(zoom_0, zoom_0)

    if not zoom:             # show total page
        pix = dlist.getPixmap(matrix=mat_0, alpha=False)
    else:
        mp = r.tl + (r.br - r.tl) * 0.5     # page rect center
        w2 = r.width / 2
        h2 = r.height / 2
        clip = r * 0.5
        tl = zoom[0]          # old top-left
        tl.x += zoom[1] * (w2 / 2)
        tl.x = max(0, tl.x)
        tl.x = min(w2, tl.x)
        tl.y += zoom[2] * (h2 / 2)
        tl.y = max(0, tl.y)
        tl.y = min(h2, tl.y)
        clip = fitz.Rect(tl, tl.x + w2, tl.y + h2)

        mat = mat_0 * fitz.Matrix(2, 2)      # zoom matrix
        pix = dlist.getPixmap(alpha=False, matrix=mat, clip=clip)

    if first:                     # first call: tkinter still inactive
        img = pix.getPNGData()    # so use fitz png output
    else:                         # else take tk photo image
        pilimg = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        img = ImageTk.PhotoImage(pilimg)

    return img, clip.tl           # return image, clip position


root = tk.Tk()
max_width = root.winfo_screenwidth() - 20
max_height = root.winfo_screenheight() - 135
max_size = (max_width, max_height)
root.destroy()
del root


cur_page = 0
data, clip_pos = get_page(cur_page, zoom=False, max_size=max_size, first=True)

image_elem = sg.Image(data=data)

goto = sg.InputText(str(cur_page + 1), size=(5, 1), key="-PageNumber-")

layout = [[
        sg.ReadButton('Next'),
        sg.ReadButton('Prev'),
        sg.Text('Page:'),
        goto,
        sg.Text('(%i)' % page_count),
        sg.ReadButton('Zoom'),
        sg.Text('(toggle on/off, use arrows to navigate while zooming)'),
    ],
    [image_elem],
]

window = sg.Window(title, layout, return_keyboard_events=True,
                   location=(0, 0), use_default_focus=False, no_titlebar=False)

# now define the buttons / events we want to handle
enter_buttons = [chr(13), "Return:13"]
quit_buttons = ["Escape:27", chr(27)]
next_buttons = ["Next", "Next:34", "MouseWheel:Down"]
prev_buttons = ["Prev", "Prior:33", "MouseWheel:Up"]
Up = "Up:38"
Left = "Left:37"
Right = "Right:39"
Down = "Down:40"
zoom_buttons = ["Zoom", Up, Down, Left, Right]

# all the buttons we will handle
my_keys = enter_buttons + next_buttons + prev_buttons + zoom_buttons

# old page store and zoom toggle
old_page = 0
old_zoom = False

while True:
    event, value = window.read()
    if event == sg.WIN_CLOSED and (value is None or value['-PageNumber-'] is None):
        break
    if event in quit_buttons:
        break

    zoom_pressed = False
    zoom = False

    if event in enter_buttons:
        try:
            cur_page = int(value['-PageNumber-']) - 1  # check if valid
            while cur_page < 0:
                cur_page += page_count
        except:
            cur_page = 0  # this guy's trying to fool me

    elif event in next_buttons:
        cur_page += 1
    elif event in prev_buttons:
        cur_page -= 1
    elif event == Up:
        zoom = (clip_pos, 0, -1)
    elif event == Down:
        zoom = (clip_pos, 0, 1)
    elif event == Left:
        zoom = (clip_pos, -1, 0)
    elif event == Right:
        zoom = (clip_pos, 1, 0)
    elif event == "Zoom":
        zoom_pressed = True
        zoom = (clip_pos, 0, 0)

    # sanitize page number
    if cur_page >= page_count:  # wrap around
        cur_page = 0
    while cur_page < 0:         # pages > 0 look nicer
        cur_page += page_count

    if zoom_pressed and old_zoom:
        zoom = zoom_pressed = old_zoom = False

    t0 = time.perf_counter()
    data, clip_pos = get_page(cur_page, zoom=zoom, max_size=max_size,
                              first=False)
    t1 = time.perf_counter()
    image_elem.update(data=data)
    t2 = time.perf_counter()
    fitz_img_time += t1 - t0
    tk_img_time += t2 - t1
    img_count += 1
    old_page = cur_page
    old_zoom = zoom_pressed or zoom

    # update page number field
    if event in my_keys:
        goto.update(str(cur_page + 1))

window.close()

# print some response time statistics
if img_count > 0:
    print("response times for '%s'" % doc.name)
    print("%.4f" % (fitz_img_time/img_count), "sec fitz avg. image time")
    print("%.4f" % (tk_img_time/img_count), "sec tk avg. image time")
    print("%.4f" % ((fitz_img_time + tk_img_time)/img_count), "sec avg. total time")
    print(img_count, "images read")
    print(page_count, "pages")
