#!/usr/bin/env python
import sys
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg

import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasAgg
import matplotlib.backends.tkagg as tkagg
import tkinter as Tk

"""
Demonstrates one way of embedding Matplotlib figures into a PySimpleGUI window.

Paste your Pyplot code into the section marked below.

Do all of your plotting as you normally would, but do NOT call plt.show().
Stop just short of calling plt.show() and let the GUI do the rest.

The remainder of the program will convert your plot and display it in the GUI.
If you want to change the GUI, make changes to the GUI portion marked below.

"""

#------------------------------- PASTE YOUR MATPLOTLIB CODE HERE -------------------------------
import matplotlib.pyplot as plt
import numpy as np
label = ['Adventure', 'Action', 'Drama', 'Comedy', 'Thriller/Suspense', 'Horror', 'Romantic Comedy', 'Musical',
         'Documentary', 'Black Comedy', 'Western', 'Concert/Performance', 'Multiple Genres', 'Reality']
no_movies = [941, 854, 4595, 2125, 942, 509, 548, 149, 1952, 161, 64, 61, 35, 5]

index = np.arange(len(label))
plt.bar(index, no_movies)
plt.xlabel('Genre', fontsize=5)
plt.ylabel('No of Movies', fontsize=5)
plt.xticks(index, label, fontsize=5, rotation=30)
plt.title('Market Share for Each Genre 1995-2017')

#------------------------------- END OF YOUR MATPLOTLIB CODE -------------------------------

#------------------------------- Beginning of Matplotlib helper code -----------------------


def draw_figure(canvas, figure, loc=(0, 0)):
    """ Draw a matplotlib figure onto a Tk canvas

    loc: location of top-left corner of figure on canvas in pixels.

    Inspired by matplotlib source: lib/matplotlib/backends/backend_tkagg.py
    """
    figure_canvas_agg = FigureCanvasAgg(figure)
    figure_canvas_agg.draw()
    figure_x, figure_y, figure_w, figure_h = figure.bbox.bounds
    figure_w, figure_h = int(figure_w), int(figure_h)
    photo = Tk.PhotoImage(master=canvas, width=figure_w, height=figure_h)
    canvas.create_image(loc[0] + figure_w/2, loc[1] + figure_h/2, image=photo)
    tkagg.blit(photo, figure_canvas_agg.get_renderer()._renderer, colormode=2)
    return photo

#------------------------------- Beginning of GUI CODE -------------------------------

fig = plt.gcf()             # if using Pyplot then get the figure from the plot
figure_x, figure_y, figure_w, figure_h = fig.bbox.bounds

# define the window layout
layout = [[sg.Text('Plot test', font='Any 18')],
          [sg.Canvas(size=(figure_w, figure_h), key='canvas')],
          [sg.OK(pad=((figure_w / 2, 0), 3), size=(4, 2))]]

# create the form and show it without the plot
window = sg.Window('Demo Application - Embedding Matplotlib In PySimpleGUI', force_toplevel=True).Layout(layout).Finalize()

# add the plot to the window
fig_photo = draw_figure(window.FindElement('canvas').TKCanvas, fig)

# show it all again and get buttons
event, values = window.Read()
