import PySimpleGUI as sg

"""
    Demo Launcher Bar

    A 2021 version of a PySimpleGUI based launcher.
    Once making the GUI leap, it's hard to go back.... at least for some people.
    This tool will perhaps help make for a more GUI-like environment for your Python activities


    Copyright 2021 PySimpleGUI
"""



excel_icon = b'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAIAAAD8GO2jAAAACXBIWXMAAAsSAAALEgHS3X78AAAFB0lEQVRIx51We0xTZxQ/X3t5lZY+QLwgLYgg4MSJOAQCOgED23SgMjedr2mY2UQhwblHNpK5xCxTM+Nkf+Dc2NTMZJCpEF3YsqU6y5ZsGpextSD0AcKlBeVR+rrt/fbHhcv1tlTGSdN8j3O/33mfgxiGAR4hhDDG7D/MTgghAGA5+efcCbdAAgA+jGDLYDzuspuGByZck7JwSZYmw/9dARgAEEHE9Hhp08iAftBooEx6ytg1ZB4YtblpDwCsVKe11ZzlC8sJxNmA3c4A0D7vg0fWbqtZP2gyUCYDZTIO97tozyw2mhGce4t9mv86QggxDNOobW69p+219U+4HQEt5k8xMsXGFWv9zzEGDBghFCImSjJyC1KzCISQrufeXYse/g+FikNTYjVBGMac9vorDb8cPU8Ej5ZZNZAqXiuo4Ftf4I/BMds3utYnODkIDYxa6680AEBRek5GfHLDz5fxtGvyU1aWPpUPABgwxnieAMP20fO3vgcAZaSclMd8+esVzhKEWMwCIEDz10ASGp5GJgEAGRUdERqWpU7HMAWwSBE7HUKAECL8U0ytIqVhEqOt30m7AWBLdkmiitR2/XnH/C/HlhKraT38Gbe9dviMf54DIIwxIchABKhxd31mQurbzacvdrQlL0g4ta3O46MvdLTx2fSUMf/4LkBQtbZyXVr2rnPvcRrsWPP8oeIdAAgBIIREgihiMNOobcYYb88pA4CdeRtDiZCLHW3D9lFBklseUpYRasw5QXu97Jr9PXKMY4wBMCAI7OTWv7R1pXsyE5ZmJy17afUGu8vRqG0R8JDy6N15LwJA7pIVMTLlW2V7AYDVYVViOj+TAwDQXu8Xt1o+qqj+eGuNUhJ17mbL0PiIgCcqQlq6PJ9NaVmYhA0bllSRcn49CRxFzX/8VFuyMyMu2eFxNd5s9mfooszFJ6sA4EjpnucyC0pOvc6Z+sC6yg82HeAKqmiWcg8+zCCExCJROBH2xMYgqIOPmSgAB8Ce/PKFUdF3zP9kaTLeWL/t6HefChiWkomf73wfAC+QKmXhkT/WNcKUE5AqMoorfQAQQAN5hLRq7ZZJt7P28gmnx7U1uyQxOk7AM+6cbO/UtXd29Nj67W5He6eO3bZ36rqGzFOKYAjsg32Fm6Oliku/Xe+x9l27p335mdKDRa8IlKDGhj+58RUAHCnbK5dIT/zQNOODZysLU1cBYBzQBwqJbH/BZi/j+1p3FQCabl/1MUzl6g1qFflYuSZC1CpSrSLlEZEhIkKtWshu1SpSESHjcwo1cNGe8rM1YpGoe8gCAH8/uP9Oy+lFytikmPi+hxTHlk4uvl7bwG11716YLQT8Adw91j5+4/729xv+X963WjadOQQAr+a9kL/k6epLx7mCsHlV0f7CLTMazK/hODwutgkWL8t10u67FgP3Ts7i5Xz5AofpXDpaedZ6AMjSpCklUfsKKrirNcmZ/Flmnv0gXhH7YfmbXKIdqzjoNx1NddB5AozYR5tuXw3e9OUS6VQURYSEiUUi39wGFpbcPrrH1j+TsXhqUoLp1kyIiGPlBxE7AdA+78CotXvIwk5wBsrUa+t3etxBAASTnWCg4wcOgTEOERMaVZxGFVeyLJe9o31e88iggTLqB416ytQ1ZH7wyOqi3YLJzn9uFIBhjINN0ZxEDGYmnJPGkQH9YK+BMjs8TrWSrC7ePhdjBgYPuAgyu8/I63f1H5J3l/PVeWn1AAAAAElFTkSuQmCC'

# This is your master table.... keys are what will be shown on the bar.  The item is what you want to happen.
launcher_buttons1 = {sg.SYMBOL_DOWN_ARROWHEAD : None,
                    'PSG Main': sg.main,
                    'Word': r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE",
                    excel_icon: r"C:\Program Files\Microsoft Office\root\Office16\excel.EXE",
                    'Notepad++': r"C:\Program Files\NotePad++\notepad++.exe",
                    sg.EMOJI_BASE64_PONDER: sg.main_sdk_help,
                    sg.EMOJI_BASE64_HAPPY_IDEA: r'C:\Python\PycharmProjects\PSG\DemoPrograms\Demo_Desktop_Widget_Postit.py',
                    'All Elements' : r'C:\Python\PycharmProjects\PSG\DemoPrograms\Demo_All_Elements.py',
                    'Exit': None }

launcher_buttons2 = {sg.SYMBOL_DOWN_ARROWHEAD : None,
                    'PSG Main': sg.main,
                    'Exit': None}

panel_rows = (launcher_buttons1, launcher_buttons2)
col_panel_list = []
num_panels = len(panel_rows)
MINIMIZED_IMAGE = sg.EMOJI_BASE64_HAPPY_THUMBS_UP

DEFAULT_SCREEN_BACKGROUND_COLOR = 'black'
DEFAULT_BUTTON_SIZE = (None, None)

def settings(window:sg.Window):
    layout = [[sg.T(f'Screen size = {sg.Window.get_screen_size()}')],
              [sg.T(f'Your launcher is currently located at {window.current_location()}')],
              [sg.T('Enable autosave and position your window where you want it to appear next time you run.')],
              [sg.T('Your Screen Background Color'), sg.In(sg.user_settings_get_entry('-screen color-', DEFAULT_SCREEN_BACKGROUND_COLOR), s=15,k='-SCREEN COLOR-')],
              [sg.CBox('Autosave Location on Exit', default=sg.user_settings_get_entry('-auto save location-', True), k='-AUTO SAVE LOCATION-')],
              [sg.CBox('Keep launcher on top', default=sg.user_settings_get_entry('-keep on top-', True), k='-KEEP ON TOP-')],
              [sg.CBox('Reroute STDOUT to Debug Window', default=sg.user_settings_get_entry('-reroute stdout-', True), k='-REROUTE STDOUT-')],
              [sg.OK(), sg.Cancel()]]
    event, values = sg.Window('Settings', layout).read(close=True)
    if event == 'OK':
        sg.user_settings_set_entry('-auto save location-', values['-AUTO SAVE LOCATION-'])
        sg.user_settings_set_entry('-keep on top-', values['-KEEP ON TOP-'])
        sg.user_settings_set_entry('-screen color-', values['-SCREEN COLOR-'])
        sg.user_settings_set_entry('-reroute stdout-', values['-REROUTE STDOUT-'])
        if values['-KEEP ON TOP-']:
            window.keep_on_top_set()
        else:
            window.keep_on_top_clear()



def ToolButton(item, background, tip):
    if isinstance(item, bytes):
        button = sg.Button(image_data=item, key=item, metadata=launcher_buttons1[item], button_color=background, tooltip=tip, border_width=0,
                           pad=1)
    else:
        button = sg.Button(item, key=item, metadata=launcher_buttons1[item], tooltip=tip, border_width=0, pad=1)
    return button

def make_window():
    global  col_panel_list
    screen_background_color = sg.user_settings_get_entry('-screen color-', None)
    old_bg = sg.theme_background_color()
    sg.set_options(border_width=0, background_color=screen_background_color)
    sg.theme_background_color(screen_background_color)
    col_panel_list = []
    for count, launcher_buttons in enumerate(panel_rows):
        button_row = []
        for item in launcher_buttons.keys():
            tip = 'Grab anywhere to move the launcher\nClick an item to launch something\nRight Click to get to settings'
            button = ToolButton(item, screen_background_color, tip)
            button_row.append(button)
        col_panel_list.append(button_row)


    col_up_down = sg.Col([[sg.B(sg.SYMBOL_UP, button_color=screen_background_color)], [sg.B(sg.SYMBOL_DOWN, button_color=screen_background_color)]], p=0, k='-COL UP DOWN-')
    col_buttons = sg.Column([col_panel_list[0], ], p=0, k='-BUTTON COL-',visible=True)
    col_buttons2 = sg.Column([col_panel_list[1], ], p=0, k='-BUTTON COL2-', visible=False,)
    col_minimized = sg.Column([[sg.Button(image_data=MINIMIZED_IMAGE, k='-MINIMIZED IMAGE-', button_color=screen_background_color, border_width=0)]], visible=False, k='-MINIMIZED COL-')
    col_panel_list = [col_buttons, col_buttons2, col_up_down]
    layout = [[sg.pin(col_minimized),sg.pin(col_up_down), sg.pin(col_buttons), sg.pin(col_buttons2), ]]

    screen_size = sg.Window.get_screen_size()
    location = screen_size[0] // 2, screen_size[1] - 200        # set a default location centered and near the bottom of the screen
    location = sg.user_settings_get_entry('-window location-', location)
    keep_on_top = sg.user_settings_get_entry('-keep on top-', True)



    window = sg.Window('Window Title', layout, location=location,
                       keep_on_top=keep_on_top, no_titlebar=True, grab_anywhere=True, background_color=screen_background_color,
                       auto_size_buttons=True, default_button_element_size=DEFAULT_BUTTON_SIZE, right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_VER_SETTINGS_EXIT,
                       enable_close_attempted_event=True, use_default_focus=False, transparent_color=screen_background_color)
    sg.theme_background_color(old_bg)

    return window, col_panel_list


def main():
    if sg.user_settings_get_entry('-reroute stdout-', False):
        mprint = sg.Print
    else:
        mprint = print
    window, col_panel_list = make_window()
    cur_panel = col_panel_list[0]
    count = 0
    while True:
        event, values = window.read(timeout=1000)        # Not needed but handy while debugging
        if event != sg.TIMEOUT_EVENT:
            mprint(event, values)
        else:
            continue
        if event in (sg.WIN_CLOSE_ATTEMPTED_EVENT, 'Exit', sg.WIN_CLOSED) or str(event).startswith('Exit'):
            if event != sg.WIN_CLOSED:
                if sg.user_settings_get_entry('-auto save location-', True):
                    mprint('saving location', window.current_location())
                    sg.user_settings_set_entry('-window location-', window.current_location())
            break
        try:
            action = window[event].metadata
        except:
            action = None
        if action is not None:
            if isinstance(action, str):
                if action.endswith(('.py', '.pyw')):
                    sg.execute_py_file(action)
                else:
                    sg.execute_command_subprocess(action)
            elif callable(action):
                action()
        event = str(event)
        if event == 'Edit Me':
            sg.execute_editor(__file__)
        elif event == 'Version':
            sg.popup_scrolled(sg.get_versions())
        elif event == 'Settings':
            settings(window)
            window.close()
            window, col_panel_list = make_window()
            if sg.user_settings_get_entry('-reroute stdout-', False):
                mprint = sg.Print
            else:
                mprint = print
        elif event.startswith(sg.SYMBOL_DOWN_ARROWHEAD):
            window['-BUTTON COL-'].update(visible=False)
            window['-BUTTON COL2-'].update(visible=False)
            window['-BUTTON COL2-'].update(visible=False)
            window['-COL UP DOWN-'].update(visible=False)
            window['-MINIMIZED COL-'].update(visible=True)
            cur_panel = col_panel_list[count]
        elif event == '-MINIMIZED IMAGE-':
            cur_panel.update(visible=True)
            window['-MINIMIZED COL-'].update(visible=False)
            window['-COL UP DOWN-'].update(visible=True)
        elif event.startswith(sg.SYMBOL_UP):
            cur_panel = col_panel_list[count]
            cur_panel.update(visible=False)
            count = (count + (num_panels - 1)) % num_panels           # Decrement - roll over to MAX from 0
            cur_panel = col_panel_list[count]
            cur_panel.update(visible=True)
        elif event == sg.SYMBOL_DOWN:
            cur_panel = col_panel_list[count]
            cur_panel.update(visible=False)
            count = (count + 1) % num_panels                   # Increment to MAX then roll over to 0
            cur_panel = col_panel_list[count]
            cur_panel.update(visible=True)
    window.close()


if __name__ == '__main__':
    main()