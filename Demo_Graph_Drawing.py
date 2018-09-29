#!/usr/bin/env python
import sys
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg

layout = [[sg.Graph(canvas_size=(400, 400), graph_bottom_left=(0,0), graph_top_right=(400, 400), background_color='red', key='graph')],
           [sg.T('Change circle color to:'), sg.ReadButton('Red'), sg.ReadButton('Blue'), sg.ReadButton('Move')]]

window = sg.Window('Graph test').Layout(layout).Finalize()

graph = window.FindElement('graph')
circle = graph.DrawCircle((75,75), 25, fill_color='black',line_color='white')
point = graph.DrawPoint((75,75), 10, color='green')
oval = graph.DrawOval((25,300), (100,280), fill_color='purple', line_color='purple' )
rectangle = graph.DrawRectangle((25,300), (100,280), line_color='purple' )
line = graph.DrawLine((0,0), (100,100))

while True:
    button, values = window.Read()
    if button is None:
        break
    if button is 'Blue':
        graph.TKCanvas.itemconfig(circle, fill = "Blue")
    elif button is 'Red':
        graph.TKCanvas.itemconfig(circle, fill = "Red")
    elif button is 'Move':
        graph.MoveFigure(point, 10,10)
        graph.MoveFigure(circle, 10,10)
        graph.MoveFigure(oval, 10,10)
        graph.MoveFigure(rectangle, 10,10)
