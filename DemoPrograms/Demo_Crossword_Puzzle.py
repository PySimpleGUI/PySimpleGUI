import PySimpleGUI as sg
import random
import string

"""
    Demo application to show how to draw rectangles and letters on a Graph Element
    This demo mocks up a crossword puzzle board
    It will place a letter where you click on the puzzle
"""


BOX_SIZE = 25

layout = [
    [sg.Text('Crossword Puzzle Using PySimpleGUI'), sg.Text('', key='-OUTPUT-')],
    [sg.Graph((800, 800), (0, 450), (450, 0), key='-GRAPH-',
              change_submits=True, drag_submits=False)],
    [sg.Button('Show'), sg.Button('Exit')]
]

window = sg.Window('Window Title', layout, finalize=True)

g = window['-GRAPH-']

for row in range(16):
    for col in range(16):
        if random.randint(0, 100) > 10:
            g.draw_rectangle((col * BOX_SIZE + 5, row * BOX_SIZE + 3), (col * BOX_SIZE + BOX_SIZE + 5, row * BOX_SIZE + BOX_SIZE + 3), line_color='black')
        else:
            g.draw_rectangle((col * BOX_SIZE + 5, row * BOX_SIZE + 3), (col * BOX_SIZE + BOX_SIZE + 5, row * BOX_SIZE + BOX_SIZE + 3), line_color='black', fill_color='black')

        g.draw_text('{}'.format(row * 6 + col + 1),
                    (col * BOX_SIZE + 10, row * BOX_SIZE + 8))

while True:             # Event Loop
    event, values = window.read()
    print(event, values)
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    mouse = values['-GRAPH-']

    if event == '-GRAPH-':
        if mouse == (None, None):
            continue
        box_x = mouse[0]//BOX_SIZE
        box_y = mouse[1]//BOX_SIZE
        letter_location = (box_x * BOX_SIZE + 18, box_y * BOX_SIZE + 17)
        print(box_x, box_y)
        g.draw_text('{}'.format(random.choice(string.ascii_uppercase)),
                    letter_location, font='Courier 25')

window.close()
