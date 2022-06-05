import PySimpleGUI as sg
import math

"""
    Demo - Graph Element used to plot a mathematical formula
    
    The Graph element has a flexible coordinate system that you define.
    Thie makes is possible for you to work in your coordinates instead of an
    arbitrary system.
    
    For example, in a typical mathematics graph, (0,0) is located at the center
    of the graph / page / diagram.
    This Demo Program shows a graph with (0,0) being at the center of the Graph
    area rather than at one of the corners.
    
    It graphs the formula:
        y = sine(x/x2) * x1
        
    The values of x1 and x2 can be changed using 2 sliders

    Copyright 2018, 2019, 2020, 2021, 2022 PySimpleGUI
    
"""

SIZE_X = 200
SIZE_Y = 200
NUMBER_MARKER_FREQUENCY = SIZE_X//8     # How often to put tick marks on the axis


def draw_axis():
    graph.draw_line((-SIZE_X, 0), (SIZE_X, 0))                # axis lines
    graph.draw_line((0, -SIZE_Y), (0, SIZE_Y))

    for x in range(-SIZE_X, SIZE_X+1, NUMBER_MARKER_FREQUENCY):
        graph.draw_line((x, -SIZE_Y/66), (x, SIZE_Y/66))                       # tick marks
        if x != 0:
            # numeric labels
            graph.draw_text(str(x), (x, -SIZE_Y/15), color='green', font='courier 10')

    for y in range(-SIZE_Y, SIZE_Y+1, NUMBER_MARKER_FREQUENCY):
        graph.draw_line((-SIZE_X/66, y), (SIZE_X/66, y))
        if y != 0:
            graph.draw_text(str(y), (-SIZE_X/11, y), color='blue', font='courier 10')

# Create the graph that will be put into the window. Making outside of layout so have element in a variable
graph = sg.Graph(canvas_size=(500, 500),
                 graph_bottom_left=(-(SIZE_X+5), -(SIZE_Y+5)),
                 graph_top_right=(SIZE_X+5, SIZE_Y+5),
                 background_color='white', expand_x=True, expand_y=True,
                 key='-GRAPH-')
# Window layout
layout = [[sg.Text('Graph Element Combined with Math!', justification='center', relief=sg.RELIEF_SUNKEN, expand_x=True, font='Courier 18')],
          [graph],
          [sg.Text('y = sin(x / x2) * x1', font='COURIER 18')],
          [sg.Text('x1', font='Courier 14'), sg.Slider((0, SIZE_Y), orientation='h', enable_events=True, key='-SLIDER-', expand_x=True)],
          [sg.Text('x2', font='Courier 14'), sg.Slider((1, SIZE_Y), orientation='h', enable_events=True, key='-SLIDER2-', expand_x=True)]]

window = sg.Window('Graph of Sine Function', layout, finalize=True)

draw_axis()     # draw the axis (an empty graph)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
        
    graph.erase()           # erase entire graph every time there's a change to a slider
    draw_axis()             # redraw the axis

    # plot the function by drawing short line segments
    prev_x = prev_y = None
    for x in range(-SIZE_X, SIZE_X):
        y = math.sin(x/int(values['-SLIDER2-'])) * int(values['-SLIDER-'])
        if prev_x is not None:
            graph.draw_line((prev_x, prev_y), (x, y), color='red')
        prev_x, prev_y = x, y

window.close()
