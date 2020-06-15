#!/usr/bin/env python
import PySimpleGUI as sg
import psutil

"""
    Desktop "Rainmeter" style widget - Drive usage
    Requires: psutil
    Shows a bar graph of space used for each drive partician that psutil finds
"""

ALPHA = .7
UPDATE_FREQUENCY_MILLISECONDS = 20*1000

colors = ('#23a0a0', '#56d856', '#be45be', '#5681d8', '#d34545', '#BE7C29')


def human_size(bytes, units=(' bytes', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB')):
    """ Returns a human readable string reprentation of bytes"""
    return str(bytes) + ' ' + units[0] if bytes < 1024 else human_size(bytes >> 10, units[1:])

def update_window(window):
    particians = psutil.disk_partitions()
    for count, part in enumerate(particians):
        mount = part[0]
        try:
            usage = psutil.disk_usage(mount)
            window[('-NAME-', mount)].update(mount)
            window[('-PROG-', mount)].update_bar(int(usage.percent))
            window[('-%-', mount)].update(f'{usage.percent}%')
            window[('-STATS-', mount)].update(f'{human_size(usage.used)} / {human_size(usage.total)} = {human_size(usage.free)} free')
        except:
            pass

def main():
    sg.theme('black')

    # ----------------  Create Layout  ----------------

    layout = [[sg.Button('', image_data=sg.red_x, border_width=0, button_color=('black', 'black'), key='Exit', tooltip='Closes window'), sg.Text('Drive Status', font='Any 16')]]

    # Add a row for every partician that has a bar graph and text stats
    particians = psutil.disk_partitions()
    for count, part in enumerate(particians):
        mount = part[0]
        try:
            bar_color = sg.theme_progress_bar_color()
            this_color = colors[count%len(colors)]
            usage = psutil.disk_usage(mount)
            stats_info = f'{human_size(usage.used)} / {human_size(usage.total)} = {human_size(usage.free)} free'
            layout += [[sg.Text(mount, size=(5,1), key=('-NAME-', mount)), sg.ProgressBar(100, 'h', size=(10,15), key=('-PROG-', mount), bar_color=(this_color, bar_color[1])),
                        sg.Text(f'{usage.percent}%', size=(6,1), key=('-%-', mount)), sg.T(stats_info, size=(30,1), key=('-STATS-', mount))]]
        except:
            pass
    layout += [[sg.Text('Refresh', font='Any 8', size=(15,1), key='-REFRESH-', enable_events=True)]]
    # ----------------  Create Window  ----------------

    window = sg.Window('Drive status', layout, keep_on_top=True, grab_anywhere=True, no_titlebar=True, alpha_channel=ALPHA, use_default_focus=False, finalize=True)

    update_window(window)

    # ----------------  Event Loop  ----------------
    while True :
        event, values = window.read(timeout=UPDATE_FREQUENCY_MILLISECONDS)
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        update_window(window)

if __name__ == "__main__":
    main()
