import PySimpleGUI as sg
import random

"""
    Using Python's Walrus Operator in Layouts

    Some elements you call many different memeber functions for. Rather than looking up the element by the key and storing
        into a variable, you can use the walrus operator to store the element, right from the layout itself.

    Copyright 2018-2026 PySimpleGUI. All rights reserved.


"""

layout = [[sg.Text('Using Walrus Operator In Layouts', font='_ 16')],
          [graph_elem := sg.Graph((500, 500), (0, 0), (100, 100), key='-GRAPH-')],
          [sg.Button('Draw'), sg.Button('Exit')]]

window = sg.Window('Walrus Operator In Layouts', layout, auto_save_location=True)

# graph_elem = window['-GRAPH-']      # This is the way elements are normally looked up and stored in a variable

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Draw':
        emoji = random.choice(sg.EMOJI_BASE64_HAPPY_LIST)
        location = random.randint(0, 100), random.randint(0, 100)
        graph_elem.draw_image(data=emoji, location=location)

window.close()
