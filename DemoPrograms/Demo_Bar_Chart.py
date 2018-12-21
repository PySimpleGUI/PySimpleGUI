import PySimpleGUI as sg
import random

BAR_WIDTH = 50
BAR_SPACING = 75
EDGE_OFFSET = 3
GRAPH_SIZE = (500,500)
DATA_SIZE = (500,500)

graph = sg.Graph(GRAPH_SIZE, (0, 0), DATA_SIZE)

layout = [[sg.Text('Bar graphs using PySimpleGUI')],
          [graph],
          [sg.Button('OK')]]

window = sg.Window('Window Title').Layout(layout)

while True:
    event, values = window.Read()
    graph.Erase()
    if event is None:
        break

    for i in range(7):
        graph_value = random.randint(0, 400)
        graph.DrawRectangle(top_left=(i * BAR_SPACING + EDGE_OFFSET, graph_value),
                            bottom_right=(i * BAR_SPACING + EDGE_OFFSET + BAR_WIDTH, 0), fill_color='blue')
        graph.DrawText(text=graph_value, location=(i*BAR_SPACING+EDGE_OFFSET+25, graph_value+10))