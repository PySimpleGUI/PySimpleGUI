#!/usr/bin/env python
import PySimpleGUI as sg
from typing import Tuple, List, Any
from packaging.version import Version

"""
    Demo of creating simple "Mini Windows" that don't create an icon in the taskbar. Good for
    simple model-type windows.

    Simply replace your call of sg.Window with MiniWindow to use this style of window.

    NOTE - requires that your version of PySimpleGUI is >= 6.2 due to use of the
    Frame element's border_width_no_relief parameter.  You can remove these
    two parms from the Frame element to get around this requirement.
    You'll see a warning if you have a version less than 6.2 when the window is created.

    Copyright 2026 PySimpleGUI. All rights reserved.
"""


#   ███╗   ███╗██╗███╗   ██╗██╗    ██╗    ██╗██╗███╗   ██╗██████╗  ██████╗ ██╗    ██╗
#   ████╗ ████║██║████╗  ██║██║    ██║    ██║██║████╗  ██║██╔══██╗██╔═══██╗██║    ██║
#   ██╔████╔██║██║██╔██╗ ██║██║    ██║ █╗ ██║██║██╔██╗ ██║██║  ██║██║   ██║██║ █╗ ██║
#   ██║╚██╔╝██║██║██║╚██╗██║██║    ██║███╗██║██║██║╚██╗██║██║  ██║██║   ██║██║███╗██║
#   ██║ ╚═╝ ██║██║██║ ╚████║██║    ╚███╔███╔╝██║██║ ╚████║██████╔╝╚██████╔╝╚███╔███╔╝
#   ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝     ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝╚═════╝  ╚═════╝  ╚══╝╚══╝

def MiniWindow(title: str, layout: List, **kwargs: Any) -> sg.Window:
    """
    A function that returns a Window object. The snake case MiniWindow name means we're acting like an object. An object is returned so the use won't notice
    :param title:       Title for the window titlebar
    :type title:        str
    :param layout:      The window layout
    :type layout:       List[List[sg.Element]]
    :param kwargs:      The normal Window arguments that a user is using to create the window
    :type kwargs:       Any
    :return:            A Window object that's a mini window with no titlebar
    :rtype:             sg.Window
    """

    # first embed the supplied layout into a layout that has a fake titlebar and frame used to draw the border
    layout = wrap_in_border(title, layout)

    # now create a Window using the wrapped layout and return the Window object
    return sg.Window(title, layout, no_titlebar=True, grab_anywhere=True, keep_on_top=True, finalize=True, margins=(0, 0), **kwargs)


def wrap_in_border(title: str, layout_rows: list, close_key: Any = 'Exit') -> list:
    """
      Wraps a Window Layout with a mini window outline with a titlebar and close button. Helper function to the
      MiniWindow function.  This does all the fancyh window styling

        ┌──────────────────────────┐
        │ ▌  Title              ✕  │
        ├──────────────────────────┤
        │   ...layout_rows...      │
        └──────────────────────────┘
    :param title:               Title for the window titlebar
    :type title:                str
    :param layout_rows:         The layout for the window
    :type layout_rows:          List[List[sg.Element]]
    :param close_key:           Key to use for the window close button
    :type close_key:            Any
    :return:                    A layout to put into an sg.Window
    :rtype:                     List[List[sg.Element]]
    """

    titlebar = [sg.Text("▌", text_color=sg.theme_button_color_background(), font=("Segoe UI", 14)),
                sg.Text(title, font=("Segoe UI", 14, "bold"), expand_x=True),
                sg.Button(sg.SYMBOL_X_SMALL, key=close_key, border_width=0, pad=(2, 0), font=("Segoe UI", 11, "bold"), mouseover_colors=("#ffffff", "#a13544"),
                          tooltip="Close")]

    layout = [[sg.Column([titlebar], expand_x=True, pad=0)],
              [sg.HorizontalSeparator(color=sg.theme_text_color(), pad=0)],
              *layout_rows]

    try:
        # Create the new layout inside a frame element so that it'll have a nice border. Requires PySimpleGUI version >= 6.2
        new_layout = [[sg.Frame("", layout, border_width_no_relief=2, p=0, expand_x=True, expand_y=True)]]
    except NameError:
        # If NameError then likely due to the border parameter.  Try again without the border
        new_layout = [[sg.Frame("", layout, p=0, expand_x=True, expand_y=True)]]
        if Version(sg.version) < Version("6.3"):
            print(f'Warning - skipping adding a border to your window because your PySimpleGUI version ({sg.version}) is less then 6.2')

    return new_layout


#   ███████╗██╗  ██╗ █████╗ ███╗   ███╗██████╗ ██╗     ███████╗
#   ██╔════╝╚██╗██╔╝██╔══██╗████╗ ████║██╔══██╗██║     ██╔════╝
#   █████╗   ╚███╔╝ ███████║██╔████╔██║██████╔╝██║     █████╗
#   ██╔══╝   ██╔██╗ ██╔══██║██║╚██╔╝██║██╔═══╝ ██║     ██╔══╝
#   ███████╗██╔╝ ██╗██║  ██║██║ ╚═╝ ██║██║     ███████╗███████╗
#   ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚══════╝╚══════╝
#
#   ██╗    ██╗██╗███╗   ██╗██████╗  ██████╗ ██╗    ██╗
#   ██║    ██║██║████╗  ██║██╔══██╗██╔═══██╗██║    ██║
#   ██║ █╗ ██║██║██╔██╗ ██║██║  ██║██║   ██║██║ █╗ ██║
#   ██║███╗██║██║██║╚██╗██║██║  ██║██║   ██║██║███╗██║
#   ╚███╔███╔╝██║██║ ╚████║██████╔╝╚██████╔╝╚███╔███╔╝
#    ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝╚═════╝  ╚═════╝  ╚══╝╚══╝

def show_settings_window(location: Tuple[int | None, int | None] = (None, None)):
    """
    Shows the settings window

    :param location:        Location of the icon window
    :type location:         Tuple[int, int]
    """

    layout = [[sg.T('Drag and Drop Icon Settings', font='_ 15')],
              [sg.Input(setting=0, justification='r', s=3, ), sg.T('%  Default JPG quality', p=(0, 2))],
              [sg.Input(setting=10, justification='r', s=3, ), sg.T('Alpha channel for icon (1-10)')],
              [sg.Input(setting='', justification='r', s=40), sg.T('Icon filename')],
              [sg.Input(setting='', justification='r', s=40), sg.T('Icon Base64')],
              [sg.Push(), sg.OK(), sg.Cancel()]]

    window = MiniWindow('Settings', layout, location=location)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Cancel', 'Exit'):
            break
        elif event == 'OK':
            window.settings_save(values)
            break
    window.close()


if __name__ == "__main__":
    sg.theme('Dark red')
    show_settings_window()