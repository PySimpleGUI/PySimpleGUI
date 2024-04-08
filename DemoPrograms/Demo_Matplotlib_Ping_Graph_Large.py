#!/usr/bin/env python
from matplotlib.backends.backend_tkagg import FigureCanvasAgg
import matplotlib.pyplot as plt
import PySimpleGUI as sg
import io
import random
import time
import ping3

"""
    Shows ping time to google.com using Matplotlib and ping3 module.
    
    Note that you will need to pip install ping3 for this demo program.
    
    Copyright 2023-2024 PySimpleSoft, Inc. and/or its licensors. All rights reserved.

    Redistribution, modification, or any other use of PySimpleGUI or any portion thereof is subject to the terms of the PySimpleGUI License Agreement available at https://eula.pysimplegui.com.

    You may not redistribute, modify or otherwise use PySimpleGUI or its contents except pursuant to the PySimpleGUI License Agreement.
"""

# ================================================================================
#   Globals
#       These are needed because callback functions are used.
#       Need to retain state across calls
# ================================================================================


class MyGlobals:
    axis_pings = None
    ping_x_array = []
    ping_y_array = []


g_my_globals = MyGlobals()

# ================================================================================
#       Performs *** PING! ***
# ================================================================================


def graph_a_ping(ping_time):
    # graphs are global so that can be retained across multiple calls to this callback
    global g_my_globals

    #===================== Do the ping =====================#
    # Insert your code to run a ping
    # ping_time = random.randint(0, 100)
    #===================== Store current ping in historical array =====================#
    g_my_globals.ping_x_array.append(len(g_my_globals.ping_x_array))
    g_my_globals.ping_y_array.append(ping_time)
    # ===================== Only graph last 100 items =====================#
    if len(g_my_globals.ping_x_array) > 100:
        x_array = g_my_globals.ping_x_array[-100:]
        y_array = g_my_globals.ping_y_array[-100:]
    else:
        x_array = g_my_globals.ping_x_array
        y_array = g_my_globals.ping_y_array

    # ===================== Call graphinc functions =====================#
    # clear before graphing
    g_my_globals.axis_ping.clear()
    # graph the ping values
    g_my_globals.axis_ping.plot(x_array, y_array)

# ================================================================================
#   Function:   Set graph titles and Axis labels
#       Sets the text for the subplots
#       Have to do this in 2 places... initially when creating and when updating
#       So, putting into a function so don't have to duplicate code
# ================================================================================


def ping_thread(window: sg.Window):
    while True:
        # time.sleep(.1)
        # ping_time = random.randint(0, 100)
        ping_time = ping3.ping('google.com')
        window.write_event_value('-THREAD-', ping_time)


def set_chart_labels():
    global g_my_globals

    g_my_globals.axis_ping.set_xlabel('Time')
    g_my_globals.axis_ping.set_ylabel('Ping (ms)')
    g_my_globals.axis_ping.set_title('Current Ping Duration', fontsize=12)


def draw(element, figure):
    """
    Draws the previously created "figure" in the supplied Image Element

    :param element: an Image Element
    :param figure: a Matplotlib figure
    :return: The figure canvas
    """

    # plt.close('all')  # erases previously drawn plots
    canv = FigureCanvasAgg(figure)
    buf = io.BytesIO()
    canv.print_figure(buf, format='png')
    if buf is not None:
        buf.seek(0)
        element.update(data=buf.read())
        return canv
    else:
        return None

# ================================================================================
#   Function:   MAIN
# ================================================================================


def main():
    global g_my_globals

    # define the form layout
    layout = [[sg.Text('Animated Ping', size=(40, 1),
                    justification='center', font='Helvetica 20')],
              [sg.Image(size=(640, 480), key='-IMAGE-')],
              [sg.Button('Exit', size=(10, 2), pad=((280, 0), 3), font='Helvetica 14')]]

    # create the form and show it without the plot
    window = sg.Window(
        'Demo Application - Embedding Matplotlib In PySimpleGUI', layout, finalize=True)

    image_elem = window['-IMAGE-']

    fig = plt.figure()
    g_my_globals.axis_ping = fig.add_subplot(1, 1, 1)
    set_chart_labels()
    plt.tight_layout()
    window.start_thread(lambda: ping_thread(window))
    while True:
        event, values = window.read(timeout=0)
        if event in ('Exit', None):
            break
        if event == '-THREAD-':
            graph_a_ping(values[event])
            draw(image_elem, fig)



if __name__ == '__main__':
    main()
