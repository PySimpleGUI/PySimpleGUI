import PySimpleGUI as sg
import random

"""
    Using Python's Walrus Operator in Layouts

    Some elements you call many different memeber functions for. Rather than looking up the element by the key and storing
        into a variable, you can use the walrus operator to store the element, right from the layout itself.

    Copyright 2024 PySimpleSoft, Inc. and/or its licensors. All rights reserved.

    Redistribution, modification, or any other use of PySimpleGUI or any portion thereof is subject to the terms of the PySimpleGUI License Agreement available at https://eula.pysimplegui.com.

    You may not redistribute, modify or otherwise use PySimpleGUI or its contents except pursuant to the PySimpleGUI License Agreement.
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
