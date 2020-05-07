import PySimpleGUI as sg
import random

#      Bars drawing in PySimpleGUI
#                                 
#                 .--.
#                 |  |
#             .--.|  |.--.
#             |  ||  ||  |
#             |  ||  ||  |
#             |  ||  ||  |
#         .--.|  ||  ||  |
#     .--.|  ||  ||  ||  |.--.
#     |  ||  ||  ||  ||  ||  |
#     |  ||  ||  ||  ||  ||  |
# .--.|  ||  ||  ||  ||  ||  |.--.
# |  ||  ||  ||  ||  ||  ||  ||  |.--.
# |  ||  ||  ||  ||  ||  ||  ||  ||  |
# '--''--''--''--''--''--''--''--''--'


BAR_WIDTH = 50
BAR_SPACING = 75
EDGE_OFFSET = 3
GRAPH_SIZE = (500,500)
DATA_SIZE = (500,500)

sg.theme('Light Brown 1')

graph = sg.Graph(GRAPH_SIZE, (0,0), DATA_SIZE)

layout = [[sg.Text('Labelled Bar graphs using PySimpleGUI')],
          [graph],
          [sg.Button('OK'), sg.T('Click to display more data'), sg.Exit()]]

window = sg.Window('Window Title', layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break

    graph.erase()
    for i in range(7):
        graph_value = random.randint(0, 400)
        graph.draw_rectangle(top_left=(i * BAR_SPACING + EDGE_OFFSET, graph_value),
                            bottom_right=(i * BAR_SPACING + EDGE_OFFSET + BAR_WIDTH, 0), fill_color='blue')
        graph.draw_text(text=graph_value, location=(i*BAR_SPACING+EDGE_OFFSET+25, graph_value+10))
window.close()
