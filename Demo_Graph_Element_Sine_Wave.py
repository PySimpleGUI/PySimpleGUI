import math
import PySimpleGUI as sg

layout = [[sg.Graph(canvas_size=(400, 400), graph_bottom_left=(-100,-100), graph_top_right=(100,100), background_color='white', key='graph', tooltip='This is a cool graph!')],]

window = sg.Window('Graph of Sine Function', grab_anywhere=True).Layout(layout).Finalize()
graph = window.FindElement('graph')

graph.DrawLine((-100,0), (100,0))
graph.DrawLine((0,-100), (0,100))

for x in range(-100,100):
    y = math.sin(x/20)*50
    graph.DrawPoint((x,y), color='red')

button, values = window.Read()
