import PySimpleGUI as sg
from PIL import ImageGrab

"""
    Demo - Saving the contents of a window as an image file
    
    This demo will teach you how to save any portion of your window to an image file.
    You can save in JPG, GIF, or PNG format.
    
    In this example the entire window's layout is placed into a single Column Element.  This allows
    us to save an image of the Column which saves the entire window layout
    
    Portions of windows can be saved, such as a Graph Element, by specifying the Graph Element instead of the Column
"""

def save_element_as_file(element, filename):
    """
    Saves any element as an image file.  Element needs to have an underlyiong Widget available (almost if not all of them do)
    :param element: The element to save
    :param filename: The filename to save to. The extension of the filename determines the format (jpg, png, gif, ?)
    """
    widget = element.Widget
    box = (widget.winfo_rootx(), widget.winfo_rooty(), widget.winfo_rootx() + widget.winfo_width(), widget.winfo_rooty() + widget.winfo_height())
    grab = ImageGrab.grab(bbox=box)
    grab.save(filename)


def main():

    col = [[sg.Text('This is the first line')],
           [sg.In()],
           [sg.Button('Save'), sg.Button('Exit')]]

    layout = [[sg.Column(col, key='-COLUMN-')]]     # put entire layout into a column so it can be saved

    window = sg.Window("Drawing and Moving Stuff Around", layout)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break  # exit
        elif event == 'Save':
            filename = sg.popup_get_file('Choose file (PNG, JPG, GIF) to save to', save_as=True)
            save_element_as_file(window['-COLUMN-'], filename)

    window.close()

main()