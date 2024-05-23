#!/usr/bin/env python
"""
    Obtain the version number for a package installed on any versions of Python on your system by uysing
    the sg.execute_pip_get_local_package_version() call.

    Copyright 2024 PySimpleSoft, Inc. and/or its licensors. All rights reserved.

    Redistribution, modification, or any other use of PySimpleGUI or any portion thereof is subject to the terms of the PySimpleGUI License Agreement available at https://eula.pysimplegui.com.

    You may not redistribute, modify or otherwise use PySimpleGUI or its contents except pursuant to the PySimpleGUI License Agreement.
"""

import PySimpleGUI as sg


layout = [  [sg.T('Package Name:'), sg.In(s=15, setting='', k='-PACKAGE-')],
            [sg.T('Full path to interpreter'), sg.In(setting='', k='-INT-')],
            [sg.CB('Use threading', setting=False, k='-THREADED-')],
            [sg.MLine(s=(80,20), reroute_cprint=True, k='-ML-')],
            [sg.Button('Show', bind_return_key=True), sg.Button('Exit')] ]

window = sg.Window('Get PIP Installed Versions', layout, print_event_values=False, enable_close_attempted_event=True, auto_save_location=True)

while True:             # Event Loop
    event, values = window.read()
    if event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT:
        window.settings_save(values)
    if event in (None, 'Exit'):
        break
    if event == 'Show':
        package = values['-PACKAGE-']
        if not package:
            continue

        win = window if values['-THREADED-'] else None

        out = sg.execute_pip_get_local_package_version(package, interpreter=values['-INT-'] if values['-INT-'] else None, window=win, key='-PIP VER-')
        if win is None:
            if not out:
                out = 'Not Installed'
            sg.cprint(f'Not threaded {package} ', end='', c='white on green')
            sg.cprint(f'version = {out}', end='', c='white on red')
            sg.cprint('')
    elif event == '-PIP VER-':
            out = values[event] if values[event] else 'Not Installed'
            sg.cprint(f'{package} ', end='', c='white on blue')
            sg.cprint(f'version = {out}', end='', c='white on red')
            sg.cprint('')

window.close()
