#!/usr/bin/env python
import PySimpleGUI as sg
import random
import time
try:
    import ping3
except:
    ping3 = None
    sg.popup_quick_message('WARNING!  You do not have ping3 installed so data will be simulated', font='_ 18', text_color='white', background_color='red', auto_close_duration=6)

"""
    Use a Graph element to show ping times to a URL using a line graph

    Copyright 2023 PySimpleSoft, Inc. and/or its licensors. All rights reserved.

    Redistribution, modification, or any other use of PySimpleGUI or any portion thereof is subject to the terms of the PySimpleGUI License Agreement available at https://eula.pysimplegui.com.

    You may not redistribute, modify or otherwise use PySimpleGUI or its contents except pursuant to the PySimpleGUI License Agreement.
"""

if ping3:
    ping_url = 'google.com'
else:
    ping_url = 'simulated data'


def ping_thread(window: sg.Window):
    while True:
        if ping3:
            ping_time = int(ping3.ping(ping_url) * 1000)
        else:
            time.sleep(.001)
            ping_time = random.randint(0, 100)
        if ping_time:
            window.write_event_value('-THREAD-', ping_time)


def main():
    global ping_url

    STEP_SIZE = 1
    SAMPLES = 100
    CANVAS_SIZE = (1000, 500)
    Y_MAX = 500
    X_MAX = 500

    sg.theme('Black')

    layout = [
        sg.vbottom(
        [sg.Column([[sg.T('Ping in MS'), sg.T(k='-TIME-', s=4)],[sg.Slider((50, Y_MAX), default_value=Y_MAX, orientation='v', size=(20, 20), k='-Y SLIDER-', expand_y=True, enable_events=True)]], expand_y=True, element_justification='r'),
        sg.Column([
        [sg.Graph(CANVAS_SIZE, (0, 0), (SAMPLES, 200), background_color='black', key='-GRAPH-')],
        [sg.Text('# Samples:'), sg.Slider((50, X_MAX), default_value=SAMPLES, orientation='h', size=(50, 20), k='-X SLIDER-', expand_x=True, enable_events=True)],
        [sg.Text('Ping times to:'), sg.Input(ping_url, size=15, key='-URL-', readonly=not ping3, use_readonly_for_disable=True, disabled_readonly_text_color='black', disabled=not ping3), sg.B('Set', disabled=not ping3)],])],
            expand_x=True, expand_y=True)
    ]

    window = sg.Window('Ping Graph', layout, background_color='black',  finalize=True, font='_ 16')

    graph = window['-GRAPH-']

    i = prev_x = prev_y = 0

    window.start_thread(lambda : ping_thread(window))

    while True:
        event, values = window.read()
        if event == 'Quit' or event == sg.WIN_CLOSED:
            break
        if event == '-THREAD-':
            new_x, new_y = i, values[event]
            window['-TIME-'].update(values[event])
        if i >= SAMPLES:
            graph.move(-STEP_SIZE, 0)
            prev_x = prev_x - STEP_SIZE
        graph.draw_line((prev_x, prev_y), (new_x, new_y), color='white')
        prev_x, prev_y = new_x, new_y
        i += STEP_SIZE if i < SAMPLES else 0
        if event == '-X SLIDER-' or event == '-Y SLIDER-':
            graph.change_coordinates((0,0), (values['-X SLIDER-'], values['-Y SLIDER-']))
            graph.erase()
            i = 0
            prev_x, prev_y = 0, 0
            SAMPLES = values['-X SLIDER-']
        if event == 'Set':      # set a new URL to ping
            ping_url = values['-URL-']
    window.close()


if __name__ == '__main__':
    main()
