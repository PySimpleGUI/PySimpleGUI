import PySimpleGUI as sg
from PIL import ImageGrab

"""
    Demo - Drawing and moving demo

    This demo shows how to use a Graph Element to (optionally) display an image and then use the
    mouse to "drag" and draw rectangles and circles.

    This demo is an adaptation of a single-window version called Demo_Graph_Drawing_And_Dragging_Figures.  The 
    difference between the 2 programs is that the "action" portion of the interface is split into a floating
    toolbar kind of interface in this version.
    
    Copyright 2020 PySimpleGUI.org
"""

def save_element_as_file(element, filename):
    """
    Saves any element as an image file.  Element needs to have an underlyiong Widget available (almost if not all of them do)
    :param element: The element to save
    :param filename: The filename to save to. The extension of the filename determines the format (jpg, png, gif, ?)
    """
    widget = element.Widget
    box = (widget.winfo_rootx(), widget.winfo_rooty(), widget.winfo_rootx() + widget.winfo_width(), widget.winfo_rooty() + widget.winfo_height())
    grab = ImageGrab.grab(bbox=box)
    grab.save(filename)



def main():

    sg.theme('Dark Blue 3')

    layout2 = [[sg.T('Choose what clicking a figure does', enable_events=True)],
               [sg.R('Draw Rectangles', 1, key='-RECT-', enable_events=True)],
               [sg.R('Draw Circle', 1, key='-CIRCLE-', enable_events=True)],
               [sg.R('Draw Line', 1, key='-LINE-', enable_events=True)],
               [sg.R('Draw points', 1,  key='-POINT-', enable_events=True)],
               [sg.R('Erase item', 1, key='-ERASE-', enable_events=True)],
               [sg.R('Erase all', 1, key='-CLEAR-', enable_events=True)],
               [sg.R('Send to back', 1, key='-BACK-', enable_events=True)],
               [sg.R('Bring to front', 1, key='-FRONT-', enable_events=True)],
               [sg.R('Move Everything', 1, key='-MOVEALL-', enable_events=True)],
               [sg.R('Move Stuff', 1,  key='-MOVE-', enable_events=True)],
               [sg.B('Save Image', key='-SAVE-')]]

    window2 = sg.Window('Your Palette', layout2, finalize=True)

    layout1 = [[sg.Graph(
                canvas_size=(400, 400),
                graph_bottom_left=(0, 0),
                graph_top_right=(800, 800),
                key="-GRAPH-",
                enable_events=True,
                background_color='lightblue',
                drag_submits=True) ],
            [sg.Text(key='info', size=(40, 1))]]

    window1 = sg.Window("Drawing and Moving Stuff Around", layout1, keep_on_top=True, finalize=True)

    # get the graph element for ease of use later
    graph = window1["-GRAPH-"]  # type: sg.Graph
    graph.draw_image(data=logo200, location=(0,400))

    dragging = False
    start_point = end_point = prior_rect = None
    graph.bind('<Button-3>', '+RIGHT+')
    drawing_setting = window2.read(timeout=0)[1]

    window2.move(window1.current_location()[0]+window1.size[0], window1.current_location()[1])

    while True:
        window, event, values = sg.read_all_windows()
        # event, values = window.read()
        # print(event, values)
        if window == window2:
            drawing_setting = values
        if event == sg.WIN_CLOSED:
            break  # exit
        if event in ('-MOVE-', '-MOVEALL-'):
            # graph.Widget.config(cursor='fleur')
            graph.set_cursor(cursor='fleur')          # not yet released method... coming soon!
        elif not event.startswith('-GRAPH-'):
            graph.set_cursor(cursor='left_ptr')       # not yet released method... coming soon!
            # graph.Widget.config(cursor='left_ptr')

        if event == "-GRAPH-":  # if there's a "Graph" event, then it's a mouse
            x, y = values["-GRAPH-"]
            if not dragging:
                start_point = (x, y)
                dragging = True
                drag_figures = graph.get_figures_at_location((x,y))
                lastxy = x, y
            else:
                end_point = (x, y)
            if prior_rect:
                graph.delete_figure(prior_rect)
            delta_x, delta_y = x - lastxy[0], y - lastxy[1]
            lastxy = x,y
            if None not in (start_point, end_point) or drawing_setting['-ERASE-'] or drawing_setting['-CLEAR-']:
                if drawing_setting['-RECT-']:
                    prior_rect = graph.draw_rectangle(start_point, end_point,fill_color='green', line_color='red')
                elif drawing_setting['-CIRCLE-']:
                    prior_rect = graph.draw_circle(start_point, end_point[0]-start_point[0], fill_color='red', line_color='green')
                elif drawing_setting['-LINE-']:
                    prior_rect = graph.draw_line(start_point, end_point, width=4)
                elif drawing_setting['-MOVE-']:
                    for fig in drag_figures:
                        graph.move_figure(fig, delta_x, delta_y)
                        graph.update()
                elif drawing_setting['-POINT-']:
                    graph.draw_point((x,y), size=8)
                elif drawing_setting['-ERASE-']:
                    for figure in drag_figures:
                        graph.delete_figure(figure)
                elif drawing_setting['-CLEAR-']:
                    graph.erase()
                elif drawing_setting['-MOVEALL-']:
                    graph.move(delta_x, delta_y)
                elif drawing_setting['-FRONT-']:
                    for fig in drag_figures:
                        graph.bring_figure_to_front(fig)
                elif drawing_setting['-BACK-']:
                    for fig in drag_figures:
                        graph.send_figure_to_back(fig)
        elif event.endswith('+UP'):  # The drawing has ended because mouse up
            info = window["info"]
            info.update(value=f"grabbed rectangle from {start_point} to {end_point}")
            start_point, end_point = None, None  # enable grabbing a new rect
            dragging = False
            prior_rect = None
        elif event == '-SAVE-':
            # filename = sg.popup_get_file('Choose file (PNG, JPG, GIF) to save to', save_as=True)
            filename=r'test.jpg'
            save_element_as_file(window['-GRAPH-'], filename)

    window.close()

logo200 = b'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'

main()