import PySimpleGUI as sg

"""
    Demo - Drag a rectangle to draw it

    This demo shows how to use a Graph Element to (optionally) display an image and then use the
    mouse to "drag a rectangle".  This is sometimes called a rubber band and is an operation you
    see in things like editors
    
    Copyright 2022-2023 PySimpleSoft, Inc. and/or its licensors. All rights reserved.
    
    Redistribution, modification, or any other use of PySimpleGUI or any portion thereof is subject to the terms of the PySimpleGUI License Agreement available at https://eula.pysimplegui.com.
    
    You may not redistribute, modify or otherwise use PySimpleGUI or its contents except pursuant to the PySimpleGUI License Agreement.
"""

# image_file = r'Color-names.png'
# image_file = None  # image is optional
image_file = r'C:\Python\PycharmProjects\PSG\logo200.png'  # image is optional

layout = [[sg.Graph(
    canvas_size=(400, 400),
    graph_bottom_left=(0, 0),
    graph_top_right=(400, 400),
    key="-GRAPH-",
    change_submits=True,  # mouse click events
    background_color='lightblue',
    drag_submits=True), ],
    [sg.Text(key='info', size=(60, 1))]]

window = sg.Window("draw rect on image", layout, finalize=True)
# get the graph element for ease of use later
graph = window["-GRAPH-"]  # type: sg.Graph

graph.draw_image(image_file, location=(0,400)) if image_file else None
dragging = False
start_point = end_point = prior_rect = None

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break  # exit

    if event == "-GRAPH-":  # if there's a "Graph" event, then it's a mouse
        x, y = values["-GRAPH-"]
        if not dragging:
            start_point = (x, y)
            dragging = True
        else:
            end_point = (x, y)
        if prior_rect:
            graph.delete_figure(prior_rect)
        if None not in (start_point, end_point):
            prior_rect = graph.draw_rectangle(start_point, end_point, line_color='red')

    elif event.endswith('+UP'):  # The drawing has ended because mouse up
        info = window["info"]
        info.update(value=f"grabbed rectangle from {start_point} to {end_point}")
        start_point, end_point = None, None  # enable grabbing a new rect
        dragging = False

    else:
        print("unhandled event", event, values)
