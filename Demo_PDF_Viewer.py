"""
@created: 2018-08-19 18:00:00

@author: (c) 2018 Jorj X. McKie

Display a PyMuPDF Document using Tkinter
-------------------------------------------------------------------------------

Dependencies:
-------------
PyMuPDF, PySimpleGUI > v2.9.0, Tkinter with Tk v8.6+, Python 3


License:
--------
GNU GPL V3+

Description
------------
Read filename from command line and start display with page 1.
Pages can be directly jumped to, or buttons for paging can be used.
For experimental / demonstration purposes, we have included options to zoom
into the four page quadrants (top-left, bottom-right, etc.).

We also interpret keyboard events to support paging by PageDown / PageUp
keys as if the resp. buttons were clicked. Similarly, we do not include
a 'Quit' button. Instead, the ESCAPE key can be used, or cancelling the window.

To improve paging performance, we are not directly creating pixmaps from
pages, but instead from the fitz.DisplayList of the page. A display list
will be stored in a list and looked up by page number. This way, zooming
pixmaps and page re-visits will re-use a once-created display list.

"""
import sys
import fitz
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg
from sys import exit as exit
from binascii import hexlify

sg.ChangeLookAndFeel('GreenTan')

if len(sys.argv) == 1:
    rc, fname = sg.PopupGetFile('PDF Browser', 'PDF file to open', file_types=(("PDF Files", "*.pdf"),))
    if rc is False:
        sg.PopupCancel('Cancelling')
        exit(0)
else:
    fname = sys.argv[1]

doc = fitz.open(fname)
page_count = len(doc)

# storage for page display lists
dlist_tab = [None] * page_count

title = "PyMuPDF display of '%s', pages: %i" % (fname, page_count)


def get_page(pno, zoom=0):
    """Return a PNG image for a document page number. If zoom is other than 0, one of the 4 page quadrants are zoomed-in instead and the corresponding clip returned.

    """
    dlist = dlist_tab[pno]  # get display list
    if not dlist:  # create if not yet there
        dlist_tab[pno] = doc[pno].getDisplayList()
        dlist = dlist_tab[pno]
    r = dlist.rect  # page rectangle
    mp = r.tl + (r.br - r.tl) * 0.5  # rect middle point
    mt = r.tl + (r.tr - r.tl) * 0.5  # middle of top edge
    ml = r.tl + (r.bl - r.tl) * 0.5  # middle of left edge
    mr = r.tr + (r.br - r.tr) * 0.5  # middle of right egde
    mb = r.bl + (r.br - r.bl) * 0.5  # middle of bottom edge
    mat = fitz.Matrix(2, 2)  # zoom matrix
    if zoom == 1:  # top-left quadrant
        clip = fitz.Rect(r.tl, mp)
    elif zoom == 4:  # bot-right quadrant
        clip = fitz.Rect(mp, r.br)
    elif zoom == 2:  # top-right
        clip = fitz.Rect(mt, mr)
    elif zoom == 3:  # bot-left
        clip = fitz.Rect(ml, mb)
    if zoom == 0:  # total page
        pix = dlist.getPixmap(alpha=False)
    else:
        pix = dlist.getPixmap(alpha=False, matrix=mat, clip=clip)
    return pix.getPNGData()  # return the PNG image


window = sg.Window(title, return_keyboard_events=True, use_default_focus=False)

cur_page = 0
data = get_page(cur_page)  # show page 1 for start
image_elem = sg.Image(data=data)
goto = sg.InputText(str(cur_page + 1), size=(5, 1), do_not_clear=True)

layout = [
    [
        sg.ReadButton('Next'),
        sg.ReadButton('Prev'),
        sg.Text('Page:'),
        goto,
    ],
    [
        sg.Text("Zoom:"),
        sg.ReadButton('Top-L'),
        sg.ReadButton('Top-R'),
        sg.ReadButton('Bot-L'),
        sg.ReadButton('Bot-R'),
    ],
    [image_elem],
]

window.Layout(layout)
my_keys = ("Next", "Next:34", "Prev", "Prior:33", "Top-L", "Top-R",
           "Bot-L", "Bot-R", "MouseWheel:Down", "MouseWheel:Up")
zoom_buttons = ("Top-L", "Top-R", "Bot-L", "Bot-R")

old_page = 0
old_zoom = 0  # used for zoom on/off
# the zoom buttons work in on/off mode.

while True:
    button, value = window.ReadNonBlocking()
    zoom = 0
    force_page = False
    if button is None and value is None:
        break
    if button is None:
        continue

    if button in ("Escape:27",):  # this spares me a 'Quit' button!
        break
    # print("hex(button)", hexlify(button.encode()))
    if button[0] == chr(13):  # surprise: this is 'Enter'!
        try:
            cur_page = int(value[0]) - 1  # check if valid
            while cur_page < 0:
                cur_page += page_count
        except:
            cur_page = 0  # this guy's trying to fool me
        goto.Update(str(cur_page + 1))
        # goto.TKStringVar.set(str(cur_page + 1))

    elif button in ("Next", "Next:34", "MouseWheel:Down"):
        cur_page += 1
    elif button in ("Prev", "Prior:33", "MouseWheel:Up"):
        cur_page -= 1
    elif button == "Top-L":
        zoom = 1
    elif button == "Top-R":
        zoom = 2
    elif button == "Bot-L":
        zoom = 3
    elif button == "Bot-R":
        zoom = 4

    # sanitize page number
    if cur_page >= page_count:  # wrap around
        cur_page = 0
    while cur_page < 0:  # we show conventional page numbers
        cur_page += page_count

    # prevent creating same data again
    if cur_page != old_page:
        zoom = old_zoom = 0
        force_page = True

    if button in zoom_buttons:
        if 0 < zoom == old_zoom:
            zoom = 0
            force_page = True

        if zoom != old_zoom:
            force_page = True

    if force_page:
        data = get_page(cur_page, zoom)
        image_elem.Update(data=data)
        old_page = cur_page
    old_zoom = zoom

    # update page number field
    if button in my_keys or not value[0]:
        goto.Update(str(cur_page + 1))
        # goto.TKStringVar.set(str(cur_page + 1))
