#!/usr/bin/env python
import PySimpleGUI as sg
import psutil

"""
    Desktop "Rainmeter" style widget - Drive usage
    Requires: psutil
    Shows a bar graph of space used for each drive partician that psutil finds
"""

ALPHA = 0.7
THEME = 'black'
UPDATE_FREQUENCY_MILLISECONDS = 20 * 1000

BAR_COLORS = ('#23a0a0', '#56d856', '#be45be', '#5681d8', '#d34545', '#BE7C29')


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
    sg.theme(THEME)

    # ----------------  Create Layout  ----------------

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
    layout += [[sg.Text('Refresh', font='Any 8', key='-REFRESH-', enable_events=True), sg.Text('❎', enable_events=True, key='Exit Text')]]

    # ----------------  Create Window  ----------------
    window = sg.Window('Drive Status Widget', layout, keep_on_top=True, grab_anywhere=True, no_titlebar=True, alpha_channel=ALPHA, use_default_focus=False,
                       finalize=True)

    update_window(window)  # sets the progress bars

    # ----------------  Event Loop  ----------------
    while True:
        event, values = window.read(timeout=UPDATE_FREQUENCY_MILLISECONDS)
        if event == sg.WIN_CLOSED or event.startswith('Exit'):
            break
        update_window(window)


if __name__ == "__main__":
    main()
