#!/usr/bin/env python
import PySimpleGUI as sg
import random
import sys

'''
    Example of random line in Graph element.
'''

STEP_SIZE = 1
SAMPLES = 300
SAMPLE_MAX = 300
CANVAS_SIZE = (300, 300)


def main():
    global g_exit, g_response_time

    layout = [[sg.Text('Enter width, height of graph')],
              [sg.Input(size=(6, 1), key='w'), sg.Input(size=(6, 1), key='h')],
              [sg.Ok(), sg.Cancel()]]

    window = sg.Window('Enter graph size', layout)
    event, values = window.read()
    if event is None or event == 'Cancel':
        return

    CANVAS_SIZE = int(values['w']), int(values['h'])
    window.close()

    # start ping measurement thread

    sg.change_look_and_feel('Black')
    sg.set_options(element_padding=(0, 0))

    layout = [[sg.Button('Quit', button_color=('white', 'black'))],
              [sg.Graph(CANVAS_SIZE, (0, 0), (SAMPLES, SAMPLE_MAX)
                        background_color='black', key='graph')], ]

    window = sg.Window('Canvas test', layout, grab_anywhere=True,
                       background_color='black', no_titlebar=False,
                       use_default_focus=False, finalize=True)
    graph = window['graph']

    prev_response_time = None
    i = 0
    prev_x, prev_y = 0, 0
    graph_value = 250
    while True:
        event, values = window.read(timeout=0)
        if event == 'Quit' or event is None:
            break

        graph_offset = random.randint(-10, 10)
        graph_value = graph_value + graph_offset

        if graph_value > SAMPLE_MAX:
            graph_value = SAMPLE_MAX
        if graph_value < 0:
            graph_value = 0

        new_x, new_y = i, graph_value
        prev_value = graph_value

        if i >= SAMPLES:
            graph.move(-STEP_SIZE, 0)
            prev_x = prev_x - STEP_SIZE

        graph.draw_line((prev_x, prev_y), (new_x, new_y), color='white')
        prev_x, prev_y = new_x, new_y
        i += STEP_SIZE if i < SAMPLES else 0

    window.close()


if __name__ == '__main__':
    main()
