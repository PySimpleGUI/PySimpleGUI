#!/usr/bin/env python
import PySimpleGUI as sg
import psutil
import sys

"""
    Desktop "Rainmeter" style widget - Drive usage
    Requires: psutil
    Shows a bar graph of space used for each drive partician that psutil finds
    Copyright 2022 PySimpleGUI
"""

ALPHA = 0.7
THEME = 'black'
UPDATE_FREQUENCY_MILLISECONDS = 20 * 1000

BAR_COLORS = ('#23a0a0', '#56d856', '#be45be', '#5681d8', '#d34545', '#BE7C29')


class Globals():
    drive_list = None
    def __init__(self):
        return


def human_size(bytes, units=(' bytes', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB')):
    """ Returns a human readable string reprentation of bytes"""
    return str(bytes) + ' ' + units[0] if bytes < 1024 else human_size(bytes >> 10, units[1:])


def update_window(window):
    drive_list = []
    particians = psutil.disk_partitions()
    all_ok = True
    for count, part in enumerate(particians):
        mount = part[0]
        try:
            usage = psutil.disk_usage(mount)
            window[('-NAME-', mount)].update(mount)
            window[('-PROG-', mount)].update_bar(int(usage.percent))
            window[('-%-', mount)].update(f'{usage.percent}%')
            window[('-STATS-', mount)].update(f'{human_size(usage.used)} / {human_size(usage.total)} = {human_size(usage.free)} free')
            drive_list.append(str(mount))
        except KeyError as e:       # A key error means a new drive was added
            all_ok = False
        except Exception as e:
            pass
    all_ok = Globals.drive_list == drive_list and all_ok
    Globals.drive_list = drive_list

    return all_ok


    # ----------------  Create Layout  ----------------
def create_window(location):
    layout = [[sg.Text('Drive Status', font='Any 16')]]

    # Add a row for every partician that has a bar graph and text stats
    particians = psutil.disk_partitions()
    for count, part in enumerate(particians):
        mount = part[0]
        try:
            bar_color = sg.theme_progress_bar_color()
            this_color = BAR_COLORS[count % len(BAR_COLORS)]
            usage = psutil.disk_usage(mount)
            stats_info = f'{human_size(usage.used)} / {human_size(usage.total)} = {human_size(usage.free)} free'
            layout += [[sg.Text(mount, size=(5, 1), key=('-NAME-', mount)),
                        sg.ProgressBar(100, 'h', size=(10, 15), key=('-PROG-', mount), bar_color=(this_color, bar_color[1])),
                        sg.Text(f'{usage.percent}%', size=(6, 1), key=('-%-', mount)), sg.T(stats_info, size=(30, 1), key=('-STATS-', mount))]]
        except:
            pass
    layout += [[sg.Text('Refresh', font='Any 8', key='-REFRESH-', enable_events=True)]]

    # ----------------  Create Window  ----------------
    window = sg.Window('Drive Status Widget', layout, location=location, keep_on_top=True, grab_anywhere=True, no_titlebar=True, alpha_channel=ALPHA, use_default_focus=False,right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_VER_EXIT,
                       finalize=True, enable_close_attempted_event=True)

    return window

def main(location):
    # we rely on a key error to tell us if a drive was added. So.... we don't want pesky popups or other key erros to be shown
    sg.set_options(suppress_error_popups=True, suppress_raise_key_errors=False, suppress_key_guessing=True)

    sg.theme(THEME)
    window = create_window(location)
    update_window(window)  # sets the progress bars
    try:
        # ----------------  Event Loop  ----------------
        while True:
            event, values = window.read(timeout=UPDATE_FREQUENCY_MILLISECONDS)
            if event in (sg.WIN_CLOSED, sg.WIN_CLOSE_ATTEMPTED_EVENT, 'Exit'):
                if event != sg.WIN_CLOSED:
                    sg.user_settings_set_entry('-location-', window.current_location())  # The line of code to save the position before exiting
                break

            if event == 'Edit Me':
                sp = sg.execute_editor(__file__)
            elif event == 'Version':
                sg.popup_scrolled(__file__, sg.get_versions(), keep_on_top=True, location=window.current_location())

            if not update_window(window):       # update the window.. if not True then something changed and need to make a new window
                window.close()
                window = create_window(location)
                update_window(window)


    except Exception as e:
        sg.Print('ERROR in event loop', e)
        sg.popup_error_with_traceback('Crashed', e)

        sg.popup('Check the error!')




if __name__ == '__main__':
    if len(sys.argv) > 1:
        location = sys.argv[1].split(',')
        location = (int(location[0]), int(location[1]))
    else:
        location = sg.user_settings_get_entry('-location-', (None, None))
    main(location)

