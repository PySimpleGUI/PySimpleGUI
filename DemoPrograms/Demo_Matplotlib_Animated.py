#!/usr/bin/env python
import sys
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg

from random import randint
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, FigureCanvasAgg
from matplotlib.figure import Figure
import matplotlib.backends.tkagg as tkagg
import tkinter as tk


def main():
    fig = Figure()

    ax = fig.add_subplot(111)
    ax.set_xlabel("X axis")
    ax.set_ylabel("Y axis")
    ax.grid()

    # define the form layout
    layout = [[sg.Text('Animated Matplotlib', size=(40, 1), justification='center', font='Helvetica 20')],
              [sg.Canvas(size=(640, 480), key='canvas')],
              [sg.Slider(range=(0, 10000), size=(60, 10), orientation='h', key='slider')],
              [sg.ReadButton('Exit', size=(10, 2), pad=((280, 0), 3), font='Helvetica 14')]]

    # create the form and show it without the plot
    window = sg.Window('Demo Application - Embedding Matplotlib In PySimpleGUI').Layout(layout).Finalize()

    canvas_elem = window.FindElement('canvas')
    slider_elem = window.FindElement('slider')
    graph = FigureCanvasTkAgg(fig, master=canvas_elem.TKCanvas)
    canvas = canvas_elem.TKCanvas

    dpts = [randint(0, 10) for x in range(10000)]
    for i in range(len(dpts)):
        event, values = window.Read(timeout=10)
        if event is 'Exit' or event is None:
            exit(69)

        slider_elem.Update(i)
        ax.cla()
        ax.grid()
        DATA_POINTS_PER_SCREEN = 40
        ax.plot(range(DATA_POINTS_PER_SCREEN), dpts[i:i+DATA_POINTS_PER_SCREEN],  color='purple')
        graph.draw()
        figure_x, figure_y, figure_w, figure_h = fig.bbox.bounds
        figure_w, figure_h = int(figure_w), int(figure_h)
        photo = tk.PhotoImage(master=canvas, width=figure_w, height=figure_h)

        canvas.create_image(640/2, 480/2, image=photo)

        figure_canvas_agg = FigureCanvasAgg(fig)
        figure_canvas_agg.draw()

        # Unfortunately, there's no accessor for the pointer to the native renderer
        tkagg.blit(photo, figure_canvas_agg.get_renderer()._renderer, colormode=2)

        # time.sleep(.1)


if __name__ == '__main__':
    main()
