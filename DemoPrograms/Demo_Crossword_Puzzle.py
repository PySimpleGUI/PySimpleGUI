import sys
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg
import random
import string

"""
    Demo application to show how to draw rectangles and letters on a Graph Element
    This demo mocks up a crossword puzzle board
    It will place a letter where you click on the puzzle
"""


BOX_SIZE = 25

layout = [
            [sg.Text('Crossword Puzzle Using PySimpleGUI'), sg.Text('', key='_OUTPUT_')],
            [sg.Graph((800,800), (0,450), (450,0), key='_GRAPH_', change_submits=True, drag_submits=False)],
            [sg.Button('Show'), sg.Button('Exit')]
         ]

window = sg.Window('Window Title', ).Layout(layout).Finalize()

g = window.FindElement('_GRAPH_')

for row in range(16):
    for col in range(16):
        if random.randint(0,100) > 10:
            g.DrawRectangle((col * BOX_SIZE + 5, row * BOX_SIZE + 3), (col * BOX_SIZE + BOX_SIZE + 5, row * BOX_SIZE + BOX_SIZE + 3), line_color='black')
        else:
            g.DrawRectangle((col * BOX_SIZE + 5, row * BOX_SIZE + 3), (col * BOX_SIZE + BOX_SIZE + 5, row * BOX_SIZE + BOX_SIZE + 3), line_color='black', fill_color='black')

        g.DrawText('{}'.format(row * 6 + col + 1), (col * BOX_SIZE + 10, row * BOX_SIZE + 8))

while True:             # Event Loop
    event, values = window.Read()
    print(event, values)
    if event is None or event == 'Exit':
        break
    mouse = values['_GRAPH_']

    if event == '_GRAPH_':
        if mouse == (None, None):
            continue
        box_x = mouse[0]//BOX_SIZE
        box_y = mouse[1]//BOX_SIZE
        letter_location = (box_x * BOX_SIZE + 18, box_y * BOX_SIZE + 17)
        print(box_x, box_y)
        g.DrawText('{}'.format(random.choice(string.ascii_uppercase)), letter_location, font='Courier 25')

window.Close()
