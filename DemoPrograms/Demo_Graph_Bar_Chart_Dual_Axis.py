import PySimpleGUI as sg
import random

"""
    Bar Chart - Dual Axis Version

    A simple bar chart with a twist
    If you've got 2 values to plot, this technique enables you to trivially plot them both.
    Simply set your Graph element coordinates to be negative. Make your y=0 line run through the middle

    Copyright 2022 PySimpleGUI
"""

BAR_WIDTH = 25              # width of each bar
BAR_SPACING = 30            # space between each bar
EDGE_OFFSET = 3             # offset from the left edge for first bar
GRAPH_SIZE= (500,500)       # size in pixels

sg.theme('Light brown 1')

layout = [[sg.Text('Dual-Axis Bar Chart')],
          [sg.Graph(GRAPH_SIZE, (0, -GRAPH_SIZE[0]//2), (GRAPH_SIZE[0]//2, GRAPH_SIZE[1]//2), k='-GRAPH-')],
          [sg.Button('OK'), sg.T('Click to display more data'), sg.Exit()]]

window = sg.Window('Bar Graph', layout, finalize=True)

# get the Graph Element into a variable to make code completion easier
graph:sg.Graph = window['-GRAPH-']

while True:
    graph.erase()
    for i in range(8):
        graph_value = random.randint(0, GRAPH_SIZE[1]//2)
        graph.draw_rectangle(top_left=(i * BAR_SPACING + EDGE_OFFSET, graph_value),
                             bottom_right=(i * BAR_SPACING + EDGE_OFFSET + BAR_WIDTH, 0),
                             fill_color='green', line_width=0)

        # get a second value and draw an inverted bar. Simply set the Y value to be negative and top to be 0
        graph_value = random.randint(0, GRAPH_SIZE[1]//2)
        graph.draw_rectangle(top_left=(i * BAR_SPACING + EDGE_OFFSET, 0),
                             bottom_right=(i * BAR_SPACING + EDGE_OFFSET + BAR_WIDTH, -graph_value),
                             fill_color='red', line_width=0)

    # Normally at the top of the loop, but because we're drawing the graph first, making it at the bottom
    event, values = window.read()

    if event in (sg.WIN_CLOSED, 'Exit'):
        break


window.close()