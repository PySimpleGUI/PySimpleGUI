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
        if sg.MENU_SHORTCUT_CHARACTER in text:
            text = text.replace(sg.MENU_SHORTCUT_CHARACTER, '')
        if text.startswith(sg.MENU_DISABLED_CHARACTER):
            disabled = True
            text = text[len(sg.MENU_DISABLED_CHARACTER):]
        else:
            disabled = False
        row += [sg.ButtonMenu(text, menu, border_width=0, button_color=f'{text_color} on {background_color}',key=text, pad=pad, disabled=disabled)]

    return sg.Column([row], background_color=background_color, pad=(0,0), expand_x=True)

def main():
    sg.theme('dark green 7')

    menu_def = [['&File', ['&Open   &  Ctrl-O', '&Save   &    Ctrl-S', '&Properties', 'E&xit']],
                ['&Edit', [['Special', 'Normal',['Normal1', 'Normal2'] ], 'Undo'], ],
                ['!Disabled', [['Special', 'Normal',['Normal1', 'Normal2'] ], 'Undo'], ],
                ['&Toolbar', ['---', 'Command &1::Command_Key', 'Command &2', '---', 'Command &3', 'Command &4']],
                ['&Help', ['&About...']], ]

    layout = [[Menubar(menu_def, sg.theme_button_color()[1], sg.theme_button_color()[0], (5, 0))],
                [sg.Text('This is the "Simulated" Titlebar and Menubar Window')],
                [sg.Checkbox('Checkbox 1', k='-C1W1-'), sg.Checkbox('Checkbox 2', k='-C2W1-')],
                [sg.Slider((0,100), orientation='h', size=(20,20), k='-S1-')],
                [sg.HorizontalSeparator()],
                [sg.Radio('Radio 1', 1, k='-R1W1-'), sg.Radio('Radio 2', 1, k='-R2W1-')],
                [sg.Ok(k='OK 1'), sg.Cancel(k='Cancel 1')],]

    layout2 = [[sg.Menu(menu_def, tearoff=False, key='-MENU BAR-')],     # This is how a Menu is normally defined
                [sg.Text('This is the "Traditional" Titlebar and Menubar Window')],
                [sg.Checkbox('Checkbox 1', k='-C1W2-'), sg.Checkbox('Checkbox 2', k='-C2W2-')],
                [sg.Slider((0,100), orientation='h', size=(20,20), k='-S2-')],
                [sg.HorizontalSeparator()],
                [sg.Radio('Radio 1', 1, k='-R1W2-'), sg.Radio('Radio 2', 1, k='-R2W2-')],
                [sg.Ok(k='OK 2'), sg.Cancel(k='Cancel 2')],]

    layout3 = [[sg.Multiline(size=(70, 20), reroute_stdout=True, reroute_cprint=True, write_only=True)],]

    window = sg.Window("Custom Titlebar and Menu", layout, use_custom_titlebar=True, finalize=True, right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_VER_EXIT)

    win_loc = window.current_location()

    window2 = sg.Window("Traditional Titlebar and Menu", layout2, finalize=True, location=(win_loc[0]-window.size[0]-40, win_loc[1]), right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_VER_EXIT)

    window3 = sg.Window("Output Window", layout3, finalize=True, location=(int(win_loc[0]-window.size[0]//1.5), int(win_loc[1]+window.size[1]+30)), use_custom_titlebar=True, right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_VER_EXIT)


    # ------ Event Loop ------ #
    while True:
        window, event, values = sg.read_all_windows()
        # convert ButtonMenu event so they look like Menu events
        elem = window.find_element(event, silent_on_error=True)
        if elem and elem.Type == sg.ELEM_TYPE_BUTTONMENU:
            event = values[event]

        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        elif event == 'Edit Me':
            sg.execute_editor(__file__)
        elif event == 'Version':
            sg.popup_scrolled(__file__, sg.get_versions(), keep_on_top=True, non_blocking=True)
            
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
