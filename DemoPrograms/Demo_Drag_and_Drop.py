import psgdnd as dnd
import PySimpleGUI as sg

"""
    Demo - Drag and Drop using tkinterdnd2

    Experimental drag and drop demo using tkinterdnd2 (you'll need to pip install it)
        python -m pip install tkinterdnd2
    Routes drop event through the window.read.

    Usage:
        * Register elements for drop events
            register_element_dnd(element, window, drop_type)

        * In event loop - drop events signaled via DropEvent object and value in values dict
            DropEvent object has fields:
                key
                element
                drop_type
                window
            values[event] = filename(s) or text that was dropped as a string            

    Copyright 2026 PySimpleGUI. All rights reserved.
"""

def main():
    layout = [[sg.Text('Filename to process')],
              [sg.Input(key="-INPUT-", expand_x=True), sg.FileBrowse('Browse')],
              [sg.Button("OK"), sg.Button("Cancel")]]

    # layout = [[sg.Column(layout, p=0, k='-COL-', expand_y=True, expand_x=True)]]  # if want to make the entire window the target

    window = sg.Window("File Drop Example", layout, finalize=True, auto_save_location=True, resizable=True)

    # register all elements to receive drop events
    for key, element in window.key_dict.items():
        dnd.register_element_dnd(element, window, dnd.DROP_TYPE_FILES)

    while True:
        event, values = window.read()
        # print(event, values)
        if event in (sg.WIN_CLOSED, "Cancel"):
            break
        if dnd.is_drop_event(event):                        # if it's a drag and drop event
            if event.key == '-INPUT-':                      # see what element was dropped on
                window['-INPUT-'].update(values[event])     # update the Input Element with text from event

    window.close()


if __name__ == '__main__':
    main()
