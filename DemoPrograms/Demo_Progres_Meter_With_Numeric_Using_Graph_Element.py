#!/usr/bin/env python
import PySimpleGUI as sg

#  ░█▀█░█▀▄░█▀█░█▀▀░█▀▄░█▀▀░█▀▀░█▀▀░░░█▀▄░█▀█░█▀▄
#  ░█▀▀░█▀▄░█░█░█░█░█▀▄░█▀▀░▀▀█░▀▀█░░░█▀▄░█▀█░█▀▄
#  ░▀░░░▀░▀░▀▀▀░▀▀▀░▀░▀░▀▀▀░▀▀▀░▀▀▀░░░▀▀░░▀░▀░▀░▀
#  ░░░░░░░█▀█░█░█░█▄█░█▀▀░█▀▄░▀█▀░█▀▀░░░█▀▄░▀█▀░█▀▀░█▀█░█░░░█▀█░█░█
#  ░▄█▄░░░█░█░█░█░█░█░█▀▀░█▀▄░░█░░█░░░░░█░█░░█░░▀▀█░█▀▀░█░░░█▀█░░█░
#  ░░▀░░░░▀░▀░▀▀▀░▀░▀░▀▀▀░▀░▀░▀▀▀░▀▀▀░░░▀▀░░▀▀▀░▀▀▀░▀░░░▀▀▀░▀░▀░░▀░

"""
    Demo - Progress Bar with text inside using Graph Element

    An easy to use progress bar that can be put anywhere and doesn't have the restrictions a normal tkinter progressbar has
    The part of the code needed below is the draw_progress function and the layout.  The rest of this program is for the window, etc.

    Copyright 2026 PySimpleGUI. All rights reserved.
"""

WIDTH, HEIGHT = 300, 25             # The size of the graph and the progress meter in pixels
BAR_MAX = 100                       # Max of 100 (percent)


#  8888b.  88""Yb    db    Yb        dP     88""Yb 88""Yb  dP"Yb   dP""b8 88""Yb 888888 .dP"Y8 .dP"Y8
#   8I  Yb 88__dP   dPYb    Yb  db  dP      88__dP 88__dP dP   Yb dP   `" 88__dP 88__   `Ybo." `Ybo."
#   8I  dY 88"Yb   dP__Yb    YbdPYbdP       88"""  88"Yb  Yb   dP Yb  "88 88"Yb  88""   o.`Y8b o.`Y8b
#  8888Y"  88  Yb dP""""Yb    YP  YP        88     88  Yb  YbodP   YboodP 88  Yb 888888 8bodP' 8bodP'

def draw_progress(graph, percent):
    """
    Draws a progress timer using a graph element.
    :param graph:       The graph element used to draw
    :type graph:        sg.Graph
    :param percent:     Percent complete to display
    :type percent:      int
    """
    graph.erase()
    graph.draw_rectangle((0, 0), (WIDTH, HEIGHT), fill_color='white', line_color='black')
    fill_width = WIDTH * percent / 100
    graph.draw_rectangle((0, 0), (fill_width, HEIGHT), fill_color='green', line_color='green')
    graph.draw_text(f'{percent}%', (WIDTH / 2, HEIGHT / 2), color='black', font=('Any', 12, 'bold'))


#  8b    d8    db    88 88b 88
#  88b  d88   dPYb   88 88Yb88
#  88YbdP88  dP__Yb  88 88 Y88
#  88 YY 88 dP""""Yb 88 88  Y8

def main():
    layout = [
        [sg.Button('Start'), sg.Graph(canvas_size=(WIDTH, HEIGHT), graph_bottom_left=(0, 0), graph_top_right=(WIDTH, HEIGHT), background_color='white', key='-GRAPH-')],
    ]

    window = sg.Window('Progress Bar With Text Inside', layout, finalize=True)

    graph = window['-GRAPH-']               # type: sg.Graph

    draw_progress(graph, 0)                 # Set bar to 0 initially
    percent_complete = 0                    # Counter for % compelte
    timer_running = False                   # Flag to block restarts if already running

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, None):
            break
        elif event == 'Start' and not timer_running:
            percent_complete = 0
            timer_running = True
            window.timer_start(15, repeating=True)
        elif event == sg.EVENT_TIMER:
            percent_complete += 1
            if percent_complete > BAR_MAX:
                window.timer_stop_all()
                timer_running = False
            else:
                draw_progress(graph, percent_complete)

    window.close()


if __name__ == '__main__':
    main()
