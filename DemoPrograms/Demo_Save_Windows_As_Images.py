#!/usr/bin/env python
import PySimpleGUI as sg
import os
import psutil
import win32api
import win32con
import win32gui
import win32process
from PIL import ImageGrab

"""
    Demo - Save Windows as Images
    
    Works on WINDOWS only.
    Saves a window as an image file.  Tested saving as PNG and JPG.
    saved in the format indicated by the filename.
    The window needs to be on the primary display.
    2022 update was to remove OpenCV requirement.

    Copyright 2020, 2022 PySimpleGUI.org
"""

def convert_string_to_tuple(string):
    """
    Converts a string that represents a tuple.  These strings have the format:
    "('item 1', 'item 2')"
    The desired return value is ('item 1', 'item 2')
    :param string:
    :return:
    """
    parts = string[1:-1].split(',')
    part1 = parts[0][1:-1]
    part2 = parts[1][2:-1]
    return part1, part2


def show_list_by_name(window, output_key, python_only):
    process_list = get_window_list()

    title_list = []
    for proc in process_list:
        names = convert_string_to_tuple(proc)
        if python_only and names[0] == 'python.exe':
            title_list.append(names[1])
        elif not python_only:
            title_list.append(names[1])
    title_list.sort()
    window[output_key].update(title_list)
    return title_list


def get_window_list():
    titles = []
    t = []
    pidList = [(p.pid, p.name()) for p in psutil.process_iter()]

    def enumWindowsProc(hwnd, lParam):
        """ append window titles which match a pid """
        if (lParam is None) or ((lParam is not None) and (win32process.GetWindowThreadProcessId(hwnd)[1] == lParam)):
            text = win32gui.GetWindowText(hwnd)
            if text:
                wStyle = win32api.GetWindowLong(hwnd, win32con.GWL_STYLE)
                if wStyle & win32con.WS_VISIBLE:
                    t.append("%s" % (text))
                    return

    def enumProcWnds(pid=None):
        win32gui.EnumWindows(enumWindowsProc, pid)

    for pid, pName in pidList:
        enumProcWnds(pid)
        if t:
            for title in t:
                titles.append("('{0}', '{1}')".format(pName, title))
            t = []
    titles = sorted(titles, key=lambda x: x[0].lower())
    return titles

def save_win(filename=None, title=None, crop=True):
    """
    Saves a window with the title provided as a file using the provided filename.
    If one of them is missing, then a window is created and the information collected

    :param filename:
    :param title:
    :return:
    """
    C = 7 if crop else 0  # pixels to crop
    try:
        fceuxHWND = win32gui.FindWindow(None, title)
        rect = win32gui.GetWindowRect(fceuxHWND)
        rect_cropped = (rect[0] + C, rect[1], rect[2] - C, rect[3] - C)
        grab = ImageGrab.grab(bbox=rect_cropped)
        grab.save(filename)
        sg.cprint('Wrote image to file:')
        sg.cprint(filename, c='white on purple')
    except Exception as e:
        sg.popup('Error trying to save screenshot file', e, keep_on_top=True)


def main():
    layout = [[sg.Text('Window Snapshot', key='-T-', font='Any 20', justification='c')],
              [sg.Text('Choose one or more window titles from list')],
              [sg.Listbox(values=[' '], size=(50, 20), select_mode=sg.SELECT_MODE_EXTENDED, font=('Courier', 12), key='-PROCESSES-')],
              [sg.Checkbox('Show only Python programs', default=True, key='-PYTHON ONLY-')],
              [sg.Checkbox('Crop image', default=True, key='-CROP-')],
              [sg.Multiline(size=(63, 10), font=('Courier', 10), key='-ML-')],
              [sg.Text('Output folder:', size=(15,1)), sg.In(os.path.dirname(__file__), key='-FOLDER-'), sg.FolderBrowse()],
              [sg.Text('Hardcode filename:', size=(15,1)), sg.In(key='-HARDCODED FILENAME-')],
              [sg.Button('Refresh'),
               sg.Button('Snapshot', button_color=('white', 'DarkOrange2')),
               sg.Exit(button_color=('white', 'sea green'))]]

    window = sg.Window('Window Snapshot', layout, keep_on_top=True, auto_size_buttons=False, default_button_element_size=(12, 1), finalize=True)

    window['-T-'].expand(True, False, False)  # causes text to center by expanding the element

    sg.cprint_set_output_destination(window, '-ML-')
    show_list_by_name(window, '-PROCESSES-', True)

    # ----------------  main loop  ----------------
    while True:
        # --------- Read and update window --------
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break

        # --------- Do Button Operations --------
        if event == 'Refresh':
            show_list_by_name(window, '-PROCESSES-', values['-PYTHON ONLY-'])
        elif event == 'Snapshot':
            for i, title in enumerate(values['-PROCESSES-']):
                sg.cprint('Saving:', end='', c='white on red')
                sg.cprint(' ', title, colors='white on green')
                if values['-HARDCODED FILENAME-']:
                    fname = values['-HARDCODED FILENAME-']
                    fname = f'{fname[:-4]}{i}{fname[-4:]}'
                    output_filename = os.path.join(values['-FOLDER-'], fname)
                else:
                    output_filename = os.path.join(values['-FOLDER-'], f'{title}.png')
                save_win(output_filename, title, values['-CROP-'])
    window.close()


if __name__ == "__main__":
    main()
