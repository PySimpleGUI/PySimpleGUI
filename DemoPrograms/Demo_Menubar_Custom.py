#!/usr/bin/env python
import PySimpleGUI as sg
"""
    Demo - A Custom Menubar Element Simulated Using ButtonMenu Elements

    Because a Menubar is created by the OS and not the underlying GUI framework, the
    ability to customize the look and feel of the standard Menubar is not possible.

    Additionally, the Titlebar Element and the Meny Element don't work well together.
    The order gets swapped.

    One way to get around all of the problems above is to simulate a Menu Element.
    That's exactly what this demo does.

    The color choice for the menubar background and text use the theme's button colors.
    You can change these color choices by changing the Menubar in the layout.

    Copyright 2021 PySimpleGUI
"""

sg.MENU_SHORTCUT_CHARACTER = '&'

def Menubar(menu_def, text_color, background_color, pad=(0, 0)):
    """
    A User Defined element that simulates a Menu element by using ButtonMenu elements

    :param menu_def: A standard PySimpleGUI menu definition
    :type menu_def: List[List[Tuple[str, List[str]]]
    :param text_color: color for the menubar's text
    :type text_color:
    :param background_color: color for the menubar's background
    :type background_color:
    :param pad: Amount of padding around each menu entry
    :type pad:
    :return: A column element that has a row of ButtonMenu buttons
    :rtype: sg.Column
    """
    row = []
    for menu in menu_def:
        text = menu[0]
        if text.__contains__(sg.MENU_SHORTCUT_CHARACTER):
            text = text.replace(sg.MENU_SHORTCUT_CHARACTER, '')
        if text.startswith(sg.MENU_DISABLED_CHARACTER):
            disabled = True
            text = text[len(sg.MENU_DISABLED_CHARACTER):]
        else:
            disabled = False
        row += [sg.ButtonMenu(text, menu, border_width=0, button_color=f'{text_color} on {background_color}',key=text, pad=pad, disabled=disabled)]

    return sg.Column([row], background_color=background_color, pad=(0,0), expand_x=True)

def main():
    # sg.theme('dark green 7')
    # sg.theme('dark gray 14')

    menu_def = [['&File', ['&Open     Ctrl-O', '&Save       Ctrl-S', '&Properties', 'E&xit']],
                ['&Edit', [['Special', 'Normal',['Normal1', 'Normal2'] ], 'Undo'], ],
                ['!Disabled', [['Special', 'Normal',['Normal1', 'Normal2'] ], 'Undo'], ],
                ['&Toolbar', ['---', 'Command &1::Command_Key', 'Command &2', '---', 'Command &3', 'Command &4']],
                ['&Help', ['&About...']], ]

    layout = [
        # [sg.Menu(menu_def, tearoff=False, key='-MENU BAR-')],     # This is how a Menu is normally defined
        [Menubar(menu_def, sg.theme_button_color()[1], sg.theme_button_color()[0], (5, 0))],
        [sg.Multiline(size=(70, 20),  reroute_stdout=True, reroute_cprint=True, write_only=True)],
    ]

    window = sg.Window("Custom Titlebar with Custom (Simulated) Menubar", layout, use_custom_titlebar=True)

    # ------ Event Loop ------ #
    while True:
        event, values = window.read()
        # convert ButtonMenu event so they look like Menu events
        elem = window.find_element(event, silent_on_error=True)
        if elem and elem.Type == sg.ELEM_TYPE_BUTTONMENU:
            event = values[event]

        if event in (sg.WIN_CLOSED, 'Exit'):
            break

        sg.cprint(f'event = {event}', c='white on red')
        sg.cprint(f'values = {values}', c='white on green')

        # ------ Process menu choices ------ #
        if event == 'About...':
            window.disappear()
            sg.popup('About this program', 'Simulated Menubar to accompany a simulated Titlebar',
                     'PySimpleGUI Version', sg.version,  grab_anywhere=True, keep_on_top=True)
            window.reappear()
        elif event.startswith('Open'):
            filename = sg.popup_get_file('file to open', no_window=True)
            print(filename)

    window.close()


if __name__ == '__main__':
    main()