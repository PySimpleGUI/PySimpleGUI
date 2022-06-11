import PySimpleGUI as sg
import random

"""
    Demo - Using a Graph Element to make Bar Charts

    The Graph Element is very versatile. Because you can define your own
    coordinate system, it makes producing graphs of many lines (bar, line, etc) very
    straightforward.
    
    In this Demo a "bar" is nothing more than a rectangle drawn in a Graph Element (draw_rectangle).
    
    To make things a little more interesting, this is a barchart with that data values
    placed as labels atop each bar, another Graph element method (draw_text)

    Copyright 2022 PySimpleGUI
"""



BAR_WIDTH = 50      # width of each bar
BAR_SPACING = 75    # space between each bar
EDGE_OFFSET = 3     # offset from the left edge for first bar
GRAPH_SIZE= DATA_SIZE = (500,500)       # size in pixels

sg.theme('Light brown 1')

layout = [[sg.Text('Labelled Bar graphs using PySimpleGUI')],
          [sg.Graph(GRAPH_SIZE, (0,0), DATA_SIZE, k='-GRAPH-')],
          [sg.Button('OK'), sg.T('Click to display more data'), sg.Exit()]]

window = sg.Window('Bar Graph', layout, finalize=True)

graph = window['-GRAPH-']       # type: sg.Graph

while True:

    graph.erase()
    for i in range(7):
        graph_value = random.randint(0, GRAPH_SIZE[1]-25)       # choose an int just short of the max value to give room for the label
        graph.draw_rectangle(top_left=(i * BAR_SPACING + EDGE_OFFSET, graph_value),
                             bottom_right=(i * BAR_SPACING + EDGE_OFFSET + BAR_WIDTH, 0),
                             fill_color='green')
                             # fill_color=sg.theme_button_color()[1])

        graph.draw_text(text=graph_value, location=(i*BAR_SPACING+EDGE_OFFSET+25, graph_value+10), font='_ 14')

    # Normally at the top of the loop, but because we're drawing the graph first, making it at the bottom
    event, values = window.read()

    if event in (sg.WIN_CLOSED, 'Exit'):
        break


window.close()