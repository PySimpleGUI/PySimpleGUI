import sys
import fitz
import PySimpleGUI as sg

try:
    fname = sys.argv[1]
except:
    fname = 'C:/Python/PycharmProjects/GooeyGUI/test.pdf'
doc = fitz.open(fname)
title = "PyMuPDF display of '%s' (%i pages)" % (fname, len(doc))

def get_page(pno, zoom = 0):
    page = doc[pno]
    r = page.rect
    mp = r.tl + (r.br - r.tl) * 0.5
    mt = r.tl + (r.tr - r.tl) * 0.5
    ml = r.tl + (r.bl - r.tl) * 0.5
    mr = r.tr + (r.br - r.tr) * 0.5
    mb = r.bl + (r.br - r.bl) * 0.5
    mat = fitz.Matrix(2, 2)
    if zoom == 1:
        clip = fitz.Rect(r.tl, mp)
    elif zoom == 4:
        clip = fitz.Rect(mp, r.br)
    elif zoom == 2:
        clip = fitz.Rect(mt, mr)
    elif zoom == 3:
        clip = fitz.Rect(ml, mb)
    if zoom == 0:
        pix = page.getPixmap(alpha = False)
    else:
        pix = page.getPixmap(alpha = False, matrix = mat, clip = clip)
    return pix.getPNGData()

form = sg.FlexForm(title, return_keyboard_events=True)

data = get_page(0)
image_elem = sg.Image(data=data)
layout = [  [image_elem],
            [sg.ReadFormButton('Next'),
             sg.ReadFormButton('Prev'),
             sg.ReadFormButton('First'),
             sg.ReadFormButton('Last'),
             sg.ReadFormButton('Zoom-1'),
             sg.ReadFormButton('Zoom-2'),
             sg.ReadFormButton('Zoom-3'),
             sg.ReadFormButton('Zoom-4'),
             sg.Quit()]  ]

form.Layout(layout)

i = 0
oldzoom = 0
while True:
    button,value = form.Read()
    zoom = 0
    if button in (None, 'Quit'):
        break
    if button in ("Next", 'Next:34'):
        i += 1
    elif button in ("Prev", "Prior:33"):
        i -= 1
    elif button == "First":
        i = 0
    elif button == "Last":
        i = -1
    elif button == "Zoom-1":
        if oldzoom == 1:
            zoom = oldzoom = 0
        else:
            zoom = oldzoom = 1
    elif button == "Zoom-2":
        if oldzoom == 2:
            zoom = oldzoom = 0
        else:
            zoom = oldzoom = 2
    elif button == "Zoom-3":
        if oldzoom == 3:
            zoom = oldzoom = 0
        else:
            zoom = oldzoom = 3
    elif button == "Zoom-4":
        if oldzoom == 4:
            zoom = oldzoom = 0
        else:
            zoom = oldzoom = 4
    try:
        data = get_page(i, zoom)
    except:
        i = 0
        data = get_page(i, zoom)
    image_elem.Update(data=data)
