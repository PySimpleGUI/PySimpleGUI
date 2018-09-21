import math
import PySimpleGUI as sg

layout = [[sg.Graph(canvas_size=(400, 400), graph_bottom_left=(-100,-100), graph_top_right=(100,100), background_color='white', key='graph')],]

form = sg.FlexForm('Graph of Sine Function').Layout(layout)
form.Finalize()
graph = form.FindElement('graph')

for x in range(-100,100):
    y = math.sin(x/20)*50
    graph.DrawPoint((x,y))

button, values = form.Read()
