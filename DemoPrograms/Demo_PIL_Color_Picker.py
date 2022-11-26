import PySimpleGUI as sg
import PIL.ImageGrab

"""
    Color Picker Using Mouse

    Move your mouse anywhere on the screen and the window will show you to
    location of the mouse and a square containing the color being shown.
    You're also shown the RGB hex value for the color.

    Requires PIL package (and thus only picks colors on primary monitor at the moment)

    You can move the window by grabbing it anywhere and dragging it

    Pressing the F1 key puts the RBG hex value on the clipboard
    Pressing the F2 key exits
    Clicking moves the window to that location

    If you accidently do something that causes the window to lose focus (e.g. click the mouse)
        then the window will move to where your mouse is and force focus back to the window

    As always, there is a right click menu with handy options

    Copyright 2022 PySimpleGUI
"""

layout = [  [sg.Graph((100,100), (0,100), (100,0), key='-GRAPH-')],
            [sg.T(k='-OUT-')],
            [sg.T(k='-OUT LOC-')],
            [sg.T('F1 copy F2 Exit')]]

window = sg.Window('Color Picker', layout, no_titlebar=False, keep_on_top=True, grab_anywhere=True, right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_VER_EXIT, finalize=True)

window.bind('<F1>', '-COPY-')
window.bind('<F2>', 'Exit')
window.bind('<FocusOut>', '-MOVE-')

while True:
    event, values = window.read(timeout=30)
    # print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        sg.popup_quick_message(f'Exiting', background_color='red', text_color='white', keep_on_top=True, font='_ 20', non_blocking=False)

        break
    if event == 'Edit Me':
        sp = sg.execute_editor(__file__)
    elif event == 'Version':
        sg.popup_scrolled(__file__, sg.get_versions(), keep_on_top=True, location=window.current_location(), non_blocking=True)

    window['-GRAPH-'].erase()
    x, y = window.mouse_location()
    rgb = PIL.ImageGrab.grab().load()[x, y]
    hex_color = sg.rgb(*rgb)
    window['-OUT-'].update(f'{hex_color}')
    window['-OUT LOC-'].update(f'{window.mouse_location()}')
    window['-GRAPH-'].draw_rectangle((0,0), (100,100), hex_color)

    if event == '-COPY-':
        sg.clipboard_set(hex_color)
        sg.popup_quick_message(f'{hex_color} copied to clipboard', keep_on_top=True, font='_ 20', non_blocking=True, auto_close_duration=1)
    elif event == '-MOVE-':
        window.move(x,y)
        window.force_focus()


window.close()


