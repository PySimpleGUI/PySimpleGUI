#!/usr/bin/env python
import PySimpleGUI as sg
import ping
from threading import Thread
import time


STEP_SIZE = 1
SAMPLES = 1000
CANVAS_SIZE = (1000, 500)

# globale used to communicate with thread.. yea yea... it's working fine
g_exit = False
g_response_time = None


def ping_thread(args):
    global g_exit, g_response_time
    while not g_exit:
        g_response_time = ping.quiet_ping('google.com', timeout=1000)


def main():
    global g_exit, g_response_time

    # start ping measurement thread
    thread = Thread(target=ping_thread, args=(None,))
    thread.start()

    sg.theme('Black')
    sg.set_options(element_padding=(0, 0))

    layout = [
        [sg.Text('Ping times to Google.com', font='Any 12'),
         sg.Quit(pad=((100, 0), 0), button_color=('white', 'black'))],
        [sg.Graph(CANVAS_SIZE, (0, 0), (SAMPLES, 500),
                  background_color='black', key='graph')]
    ]

    window = sg.Window('Canvas test', layout,
               grab_anywhere=True, background_color='black',
               no_titlebar=False, use_default_focus=False)

    graph = window['graph']
    prev_response_time = None
    i = 0
    prev_x, prev_y = 0, 0

    while True:
        event, values = window.read(timeout=200)
        if event == 'Quit' or event == sg.WIN_CLOSED:
            break
        if g_response_time is None or prev_response_time == g_response_time:
            continue
        new_x, new_y = i, g_response_time[0]
        prev_response_time = g_response_time
        if i >= SAMPLES:
            graph.move(-STEP_SIZE, 0)
            prev_x = prev_x - STEP_SIZE
        graph.draw_line((prev_x, prev_y), (new_x, new_y), color='white')
        # window['graph'].draw_point((new_x, new_y), color='red')
        prev_x, prev_y = new_x, new_y
        i += STEP_SIZE if i < SAMPLES else 0

    # tell thread we're done. wait for thread to exit
    g_exit = True
    thread.join()

    window.close()


if __name__ == '__main__':
    main()
