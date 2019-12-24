import PySimpleGUI as sg
import math

# Yet another usage of Graph element.

SIZE_X = 200
SIZE_Y = 100
NUMBER_MARKER_FREQUENCY = 25


def draw_axis():
    graph.draw_line((-SIZE_X, 0), (SIZE_X, 0))                # axis lines
    graph.draw_line((0, -SIZE_Y), (0, SIZE_Y))

    for x in range(-SIZE_X, SIZE_X+1, NUMBER_MARKER_FREQUENCY):
        graph.draw_line((x, -3), (x, 3))                       # tick marks
        if x != 0:
            # numeric labels
            graph.draw_text(str(x), (x, -10), color='green')

    for y in range(-SIZE_Y, SIZE_Y+1, NUMBER_MARKER_FREQUENCY):
        graph.draw_line((-3, y), (3, y))
        if y != 0:
            graph.draw_text(str(y), (-10, y), color='blue')

sg.theme('DarkAmber')

# Create the graph that will be put into the window
graph = sg.Graph(canvas_size=(400, 400),
                 graph_bottom_left=(-(SIZE_X+5), -(SIZE_Y+5)),
                 graph_top_right=(SIZE_X+5, SIZE_Y+5),
                 background_color='white',
                 key='graph')
# Window layout
layout = [[sg.Text('Example of Using Math with a Graph', justification='center', size=(50, 1), relief=sg.RELIEF_SUNKEN)],
          [graph],
          [sg.Text('y = sin(x / x2 * x1)', font='COURIER 18')],
          [sg.Text('x1'), sg.Slider((0, 200), orientation='h',
                                 enable_events=True, key='-SLIDER-')],
          [sg.Text('x2'), sg.Slider((1, 200), orientation='h', enable_events=True, key='-SLIDER2-')]]

window = sg.Window('Graph of Sine Function', layout)

while True:
    event, values = window.read()
    if event is None:
        break
    graph.erase()
    draw_axis()
    prev_x = prev_y = None

    for x in range(-SIZE_X, SIZE_X):
        y = math.sin(x/int(values['-SLIDER2-']))*int(values['-SLIDER-'])
        if prev_x is not None:
            graph.draw_line((prev_x, prev_y), (x, y), color='red')
        prev_x, prev_y = x, y

window.close()
