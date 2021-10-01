import PySimpleGUI as sg

"""
    Demo Launcher Bar

    A 2021 version of a PySimpleGUI based launcher.
    Once making the GUI leap, it's hard to go back.... at least for some people.
    This tool will perhaps help make for a more GUI-like environment for your Python activities


    Copyright 2021 PySimpleGUI
"""

# This is your master table.... keys are what will be shown on the bar.  The item is what you want to happen.
launcher_buttons = {'PSG Main': sg.main,
                    'Word': r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE",
                    'Notepad++': r"C:\Program Files\NotePad++\notepad++.exe",
                    sg.EMOJI_BASE64_HAPPY_IDEA: sg.main_sdk_help,
                    'All Elements' : r'C:\Python\PycharmProjects\PSG\DemoPrograms\Demo_All_Elements.py',
                    'Exit': None}

DEFAULT_SCREEN_BACKGROUND_COLOR = 'black'
DEFAULT_BUTTON_SIZE = (None, None)

def settings(window:sg.Window):
    layout = [[sg.T(f'Screen size = {sg.Window.get_screen_size()}')],
              [sg.T(f'Your launcher is currently located at {window.current_location()}')],
              [sg.T('Enable autosave and position your window where you want it to appear next time you run.')],
              [sg.T('Your Screen Background Color'), sg.In(sg.user_settings_get_entry('-screen color-', DEFAULT_SCREEN_BACKGROUND_COLOR), s=15,k='-SCREEN COLOR-')],
              [sg.CBox('Autosave Location on Exit', default=sg.user_settings_get_entry('-auto save location-', True), k='-AUTO SAVE LOCATION-')],
              [sg.CBox('Keep launcher on top', default=sg.user_settings_get_entry('-keep on top-', True), k='-KEEP ON TOP-')],
              [sg.OK(), sg.Cancel()]]
    event, values = sg.Window('Settings', layout).read(close=True)
    if event == 'OK':
        sg.user_settings_set_entry('-auto save location-', values['-AUTO SAVE LOCATION-'])
        sg.user_settings_set_entry('-keep on top-', values['-KEEP ON TOP-'])
        sg.user_settings_set_entry('-screen color-', values['-SCREEN COLOR-'])
        if values['-KEEP ON TOP-']:
            window.keep_on_top_set()
        else:
            window.keep_on_top_clear()


def make_window():

    screen_background_color = sg.user_settings_get_entry('-screen color-', DEFAULT_SCREEN_BACKGROUND_COLOR)

    button_row = []
    for item in launcher_buttons.keys():
        tip = 'Grab anywhere to move the launcher\nClick an item to launch something\nRight Click to get to settings'
        if isinstance(item, bytes):
            button = sg.Button(image_data=item, key=item, metadata=launcher_buttons[item], button_color=screen_background_color,tooltip=tip, border_width=0)
        else:
            button = sg.Button(item, key=item, metadata=launcher_buttons[item],  tooltip=tip, border_width=0)
        button_row.append(button)

    layout = [button_row]

    screen_size = sg.Window.get_screen_size()
    location = screen_size[0] // 2, screen_size[1] - 200        # set a default location centered and near the bottom of the screen
    location = sg.user_settings_get_entry('-window location-', location)
    keep_on_top = sg.user_settings_get_entry('-keep on top-', True)

    window = sg.Window('Window Title', layout, location=location,
                       keep_on_top=keep_on_top, no_titlebar=True, grab_anywhere=True, background_color=screen_background_color,
                       auto_size_buttons=False, default_button_element_size=DEFAULT_BUTTON_SIZE, right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_VER_SETTINGS_EXIT,
                       enable_close_attempted_event=True, use_default_focus=False)

    return window


def main():
    window = make_window()

    while True:
        event, values = window.read()
        # print(event, values)
        if event in (sg.WIN_CLOSE_ATTEMPTED_EVENT, 'Exit', sg.WIN_CLOSED):
            if event != sg.WIN_CLOSED:
                if sg.user_settings_get_entry('-auto save location-', True):
                    print('saving locatoin', window.current_location())
                    sg.user_settings_set_entry('-window location-', window.current_location())
            break
        if event in launcher_buttons:
            action = window[event].metadata
            if isinstance(action, str):
                if action.endswith(('.py', '.pyw')):
                    sg.execute_py_file(action)
                else:
                    sg.execute_command_subprocess(action)
            elif callable(action):
                action()
        if event == 'Edit Me':
            sg.execute_editor(__file__)
        elif event == 'Version':
            sg.popup_scrolled(sg.get_versions())
        elif event == 'Settings':
            settings(window)
            window.close()
            window = make_window()
    window.close()


if __name__ == '__main__':
    main()