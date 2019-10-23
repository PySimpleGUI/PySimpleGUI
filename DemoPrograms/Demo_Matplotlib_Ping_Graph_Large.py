#!/usr/bin/env python
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, FigureCanvasAgg
import matplotlib.backends.tkagg as tkagg
import matplotlib.pyplot as plt
import PySimpleGUI as sg
import tkinter as tk
import ping

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


def run_a_ping_and_graph():
    # graphs are global so that can be retained across multiple calls to this callback
    global g_my_globals

    #===================== Do the ping =====================#
    response = ping.quiet_ping('google.com', timeout=1000)
    if response[0] == 0:
        ping_time = 1000
    else:
        ping_time = response[0]
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


def set_chart_labels():
    global g_my_globals

    g_my_globals.axis_ping.set_xlabel('Time')
    g_my_globals.axis_ping.set_ylabel('Ping (ms)')
    g_my_globals.axis_ping.set_title('Current Ping Duration', fontsize=12)


def draw(fig, canvas):
    # Magic code that draws the figure onto the Canvas Element's canvas
    figure_x, figure_y, figure_w, figure_h = fig.bbox.bounds
    figure_w, figure_h = int(figure_w), int(figure_h)
    photo = tk.PhotoImage(master=canvas, width=figure_w, height=figure_h)
    canvas.create_image(640 / 2, 480 / 2, image=photo)
    figure_canvas_agg = FigureCanvasAgg(fig)
    figure_canvas_agg.draw()
    tkagg.blit(photo, figure_canvas_agg.get_renderer()._renderer, colormode=2)
    return photo

# ================================================================================
#   Function:   MAIN
# ================================================================================


def main():
    global g_my_globals

    # define the form layout
    layout = [[sg.Text('Animated Ping', size=(40, 1),
                    justification='center', font='Helvetica 20')],
              [sg.Canvas(size=(640, 480), key='canvas')],
              [sg.Button('Exit', size=(10, 2), pad=((280, 0), 3), font='Helvetica 14')]]

    # create the form and show it without the plot
    window = sg.Window(
        'Demo Application - Embedding Matplotlib In PySimpleGUI', layout, finalize=True)

    canvas_elem = window['canvas']
    canvas = canvas_elem.TKCanvas

    fig = plt.figure()
    g_my_globals.axis_ping = fig.add_subplot(1, 1, 1)
    set_chart_labels()
    plt.tight_layout()

    while True:
        event, values = window.read(timeout=0)
        if event in ('Exit', None):
            break

        run_a_ping_and_graph()
        photo = draw(fig, canvas)


if __name__ == '__main__':
    main()
