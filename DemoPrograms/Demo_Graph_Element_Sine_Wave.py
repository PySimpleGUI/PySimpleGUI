# import PySimpleGUIWeb as sg
# import PySimpleGUIQt as sg
import PySimpleGUI as sg
import math

SIZE_X = 200
SIZE_Y = 100
NUMBER_MARKER_FREQUENCY = 25

def draw_axis():
    graph.DrawLine((-SIZE_X,0), (SIZE_X, 0))                # axis lines
    graph.DrawLine((0,-SIZE_Y), (0,SIZE_Y))

    for x in range(-SIZE_X, SIZE_X+1, NUMBER_MARKER_FREQUENCY):
        graph.DrawLine((x,-3), (x,3))                       # tick marks
        if x != 0:
            graph.DrawText( str(x), (x,-10), color='green')      # numeric labels

    for y in range(-SIZE_Y, SIZE_Y+1, NUMBER_MARKER_FREQUENCY):
        graph.DrawLine((-3,y), (3,y))
        if y != 0:
            graph.DrawText( str(y), (-10,y), color='blue')

# Create the graph that will be put into the window
graph = sg.Graph(canvas_size=(400, 400),
          graph_bottom_left=(-(SIZE_X+5), -(SIZE_Y+5)),
          graph_top_right=(SIZE_X+5, SIZE_Y+5),
          background_color='white',
          key='graph')
# Window layout
layout = [[sg.Text('Example of Using Math with a Graph', justification='center', size=(50,1), relief=sg.RELIEF_SUNKEN)],
          [graph],
          [sg.Text('y = sin(x / x2 * x1)', font='COURIER 18')],
          [sg.Text('x1'),sg.Slider((0,200), orientation='h', enable_events=True,key='_SLIDER_')],
          [sg.Text('x2'),sg.Slider((1,200), orientation='h', enable_events=True,key='_SLIDER2_')]]

window = sg.Window('Graph of Sine Function', layout)

while True:
    event, values = window.Read()
    if event is None:
        break
    graph.Erase()
    draw_axis()
    prev_x = prev_y = None
    for x in range(-SIZE_X,SIZE_X):
        y = math.sin(x/int(values['_SLIDER2_']))*int(values['_SLIDER_'])
        if prev_x is not None:
            graph.DrawLine((prev_x, prev_y), (x,y), color='red')
        prev_x, prev_y = x, y

