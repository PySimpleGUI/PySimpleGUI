#matplotlib, numpy, pyplot
#Tony Crewe
#Oct 2018

import PySimpleGUI as sg
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.backends.backend_tkagg import FigureCanvasAgg
import matplotlib.backends.tkagg as tkagg
import numpy as np
import tkinter as tk

sg.ChangeLookAndFeel('Purple')
sg.SetOptions(font = ('Calibri', 14, 'bold'))

def draw_figure(canvas, figure, loc = (0,0)):

    figure_canvas_agg = FigureCanvasAgg(figure) 
    figure_canvas_agg.draw()
    figure_x, figure_y, figure_w, figure_h = figure.bbox.bounds
    figure_w, figure_h = int(figure_w), int(figure_h)
    photo = tk.PhotoImage(master=canvas, width=figure_w, height=figure_h)
    canvas.create_image(loc[0] + figure_w/2, loc[1] + figure_h/2, image=photo)
    tkagg.blit(photo, figure_canvas_agg.get_renderer()._renderer, colormode=2)
    return photo


#------------ Matplotlib code --------------------

def set_plot(a,b,c, function):
    global figure_w, figure_h, fig
    fig=plt.figure()
    ax = fig.add_subplot(111)
    x = np.linspace(-10, 10, 100)
    if function == 'y = ax + b':
        y= a*x + b
        if a == 1:
            a = ''
        if a == -1:
            a = '-'
        title = str('y = ') + str(a) + 'x + ' + str(b)
        ax.set_title(title)
    else:
        y = a*x**2 + b*x + c
        #avoiding getting -1x or -1x**2 instead of -x for title
        if a == 1:
            a = ''
        if a == -1:
            a = '-'
        if b == 1:
            b = ''
        if b == -1:
            b = '-'
        title = str('y = ') + str(a) + 'x**2 + ' + str(b) + 'x + ' + str(c) 
        ax.set_title(title)
    plt.plot(x,y)

    
    #centre bottom and left axes to zero

    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position('zero')
    ax.spines['top'].set_color('none')


    figure_x, figure_y, figure_w, figure_h = fig.bbox.bounds
amp = 1
function = 'y = ax + b'
set_plot(1,1,1, function)

#------------End Matplotlib code --------------------

#column 1 for function type and constant values ...

column1 = [
           [sg.Text('Select constants and function type', )],
           [sg.InputCombo(['y = ax + b', 'y = ax^2 + bx + c'], size = (12, 4), key = '_function_'),
            sg.Text('Function', size = (10, 1))], [sg.Text('', size = (1, 2))],
            [sg.Spin([sz for sz in range (-6,6)], initial_value =1, size = (2,1), key = '_a_'),
                sg.Text('a', size = (3, 1)),
           sg.Spin([sz for sz in range (-6,6)], initial_value =1, size = (2,1), key = '_b_'),
                sg.Text('b', size = (3, 1)),
           sg.Spin([sz for sz in range (-6,6)], initial_value =1, size = (2,1), key = '_c_'),
                sg.Text('c', size = (3, 1))], [sg.Text('', size = (1, 1))],   
               [sg.ReadButton('Redraw Plot')],
               [sg.Text('', size = (1, 14))]]
               
column2 = [[sg.Text('Plot Test - PySimpleGUI and Matplotlib and options')],
          [sg.Canvas(size = (figure_w, figure_h), key = '_canvas_')],
          [sg.OK(pad=((figure_w / 2, 0), 1), size=(4, 1))]]

layout = [[sg.Column(column1), sg.Column(column2)]]
window = sg.Window('Matplot, PySimpleGUI and options', force_toplevel = True).Layout(layout).Finalize()

fig_photo = draw_figure(window.FindElement('_canvas_').TKCanvas, fig)

while True:
    button, value = window.Read()
    if button == 'Redraw Plot':
        a = int(value['_a_'])
        b = int(value['_b_'])
        c = int(value['_c_'])
        function = value['_function_']
        set_plot(a,b,c,function)
        fig_photo = draw_figure(window.FindElement('_canvas_').TKCanvas, fig)
        
    if button is None:   
        break


