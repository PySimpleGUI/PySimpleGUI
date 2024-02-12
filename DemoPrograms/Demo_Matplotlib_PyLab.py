#!/usr/bin/env python
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import PySimpleGUI as sg
import matplotlib
import pylab
matplotlib.use('TkAgg')

"""
Demonstrates one way of embedding PyLab figures into a PySimpleGUI window.

Copyright 2023 PySimpleSoft, Inc. and/or its licensors. All rights reserved.

Redistribution, modification, or any other use of PySimpleGUI or any portion thereof is subject to the terms of the PySimpleGUI License Agreement available at https://eula.pysimplegui.com.

You may not redistribute, modify or otherwise use PySimpleGUI or its contents except pursuant to the PySimpleGUI License Agreement.
"""


# ------------------------------- PASTE YOUR PYLAB CODE HERE -------------------------------
from numpy import sin
from numpy import cos

x = pylab.linspace(-3, 3, 30)
y = x**2
pylab.plot(x, sin(x))
pylab.plot(x, cos(x), 'r-')
pylab.plot(x, -sin(x), 'g--')

fig = pylab.gcf()
figure_x, figure_y, figure_w, figure_h = fig.bbox.bounds

# ------------------------------- END OF YOUR MATPLOTLIB CODE -------------------------------

# ------------------------------- Beginning of Matplotlib helper code -----------------------


def draw_figure(canvas, figure, loc=(0, 0)):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg
# ------------------------------- Beginning of GUI CODE -------------------------------


# define the window layout
layout = [[sg.Text('Plot test', font='Any 18')],
          [sg.Canvas(size=(figure_w, figure_h), key='canvas')],
          [sg.OK(pad=((figure_w / 2, 0), 3), size=(4, 2))]]

# create the form and show it without the plot
window = sg.Window('Demo Application - Embedding Matplotlib In PySimpleGUI',
                   layout, finalize=True)

# add the plot to the window
fig_canvas_agg = draw_figure(window['canvas'].TKCanvas, fig)

event, values = window.read()

window.close()
