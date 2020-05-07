#!/usr/bin/env python
import PySimpleGUI as sg

# Usage of Graph element.

layout = [[sg.Graph(canvas_size=(400, 400), graph_bottom_left=(0, 0), graph_top_right=(400, 400), background_color='red', enable_events=True, key='graph')],
          [sg.Text('Change circle color to:'), sg.Button('Red'), sg.Button('Blue'), sg.Button('Move')]]

window = sg.Window('Graph test', layout, finalize=True)

graph = window['graph']         # type: sg.Graph
circle = graph.draw_circle((75, 75), 25, fill_color='black', line_color='white')
point = graph.draw_point((75, 75), 10, color='green')
oval = graph.draw_oval((25, 300), (100, 280), fill_color='purple', line_color='purple')
rectangle = graph.draw_rectangle((25, 300), (100, 280), line_color='purple')
line = graph.draw_line((0, 0), (100, 100))
arc = graph.draw_arc((0, 0), (400, 400), 160, 10, style='arc', arc_color='blue')
poly = graph.draw_polygon(((10,10), (20,0), (40,200), (10,10)), fill_color='green')
while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED:
        break
    if event in ('Blue', 'Red'):
        graph.TKCanvas.itemconfig(circle, fill=event)
    elif event == 'Move':
        graph.MoveFigure(point, 10, 10)
        graph.MoveFigure(circle, 10, 10)
        graph.MoveFigure(oval, 10, 10)
        graph.MoveFigure(rectangle, 10, 10)
        graph.MoveFigure(arc, 10, 10)
        graph.MoveFigure(poly, 10, 10)

window.close()