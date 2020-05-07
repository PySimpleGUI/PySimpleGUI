#!/usr/bin/env python
import PySimpleGUI as sg
import random
import psutil
from threading import Thread


STEP_SIZE = 3
SAMPLES = 300
SAMPLE_MAX = 500
CANVAS_SIZE = (300, 200)


g_interval = .25
g_cpu_percent = 0
g_procs = None
g_exit = False


def CPU_thread(args):
    global g_interval, g_cpu_percent, g_procs, g_exit

    while not g_exit:
        try:
            g_cpu_percent = psutil.cpu_percent(interval=g_interval)
            g_procs = psutil.process_iter()
        except:
            pass


def main():
    global g_exit, g_response_time
    # start ping measurement thread

    sg.theme('Black')
    sg.set_options(element_padding=(0, 0))

    layout = [
        [sg.Quit(button_color=('white', 'black')),
         sg.Text('', pad=((100, 0), 0), font='Any 15', key='output')],
        [sg.Graph(CANVAS_SIZE, (0, 0), (SAMPLES, SAMPLE_MAX),
          background_color='black', key='graph')]
    ]

    window = sg.Window('CPU Graph', layout,
                       grab_anywhere=True, keep_on_top=True,
                       background_color='black', no_titlebar=True,
                       use_default_focus=False)

    graph = window['graph']
    output = window['output']
    # start cpu measurement thread
    thread = Thread(target=CPU_thread, args=(None,))
    thread.start()

    last_cpu = i = 0
    prev_x, prev_y = 0, 0
    while True:                                 # the Event Loop
        event, values = window.read(timeout=500)
        if event in ('Quit', None):  # always give ths user a way out
            break
        # do CPU measurement and graph it
        current_cpu = int(g_cpu_percent*10)

        if current_cpu == last_cpu:
            continue
        # show current cpu usage at top
        output.update(current_cpu/10)

        if current_cpu > SAMPLE_MAX:
            current_cpu = SAMPLE_MAX
        new_x, new_y = i, current_cpu

        if i >= SAMPLES:
            # shift graph over if full of data
            graph.move(-STEP_SIZE, 0)
            prev_x = prev_x - STEP_SIZE
        graph.draw_line((prev_x, prev_y), (new_x, new_y), color='white')
        prev_x, prev_y = new_x, new_y
        i += STEP_SIZE if i < SAMPLES else 0
        last_cpu = current_cpu

    g_exit = True
    window.close()


if __name__ == '__main__':
    main()
