#!/usr/bin/env python
import PySimpleGUI as sg
import random
import sys

'''
    Example of random line in Graph element.
'''

sg.theme('black')

STEP_SIZE = 1
SAMPLES = 300
SAMPLE_MAX = 300
CANVAS_SIZE = (300, 300)


def main():
    global g_exit, g_response_time

    layout = [[sg.Text('Enter width, height of graph')],
              [sg.Input(300, size=(6, 1), key='w'), sg.Input(300, size=(6, 1), key='h')],
              [sg.Ok(), sg.Cancel()]]

    window = sg.Window('Enter graph size', layout)
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        return

    CANVAS_SIZE = int(values['w']), int(values['h'])
    window.close()

    # start ping measurement thread

    sg.theme('Black')
    sg.set_options(element_padding=(0, 0))

    layout = [[sg.Button('Quit', button_color=('white', 'black'))],
              [sg.Graph(CANVAS_SIZE, (0, 0), (SAMPLES, SAMPLE_MAX),
                        background_color='black', key='graph')], ]

    window = sg.Window('Canvas test', layout, grab_anywhere=True,
                       background_color='black', no_titlebar=False,
                       use_default_focus=False, finalize=True)
    graph = window['graph']     # type:sg.Graph

    graph.draw_line((SAMPLES//2, 0), (SAMPLES//2,SAMPLE_MAX),color='white')
    graph.draw_line((0,SAMPLE_MAX//2), (SAMPLES, SAMPLE_MAX//2),color='white')

    prev_response_time = None
    i = 0
    prev_x, prev_y = 0, 0
    graph_value = 250
    figures = []
    while True:
        event, values = window.read(timeout=0)
        if event == 'Quit' or event == sg.WIN_CLOSED:
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
            graph.delete_figure(figures[0])
            figures = figures[1:]
            for count, figure in enumerate(figures):
                graph.move_figure(figure, -STEP_SIZE, 0)
            prev_x = prev_x - STEP_SIZE

        last_figure = graph.draw_line((prev_x, prev_y), (new_x, new_y), color='white')
        figures.append(last_figure)
        prev_x, prev_y = new_x, new_y
        i += STEP_SIZE if i < SAMPLES else 0

    window.close()


if __name__ == '__main__':
    main()
