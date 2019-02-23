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

def set_plot(amp, function):
    global figure_w, figure_h, fig
    fig=plt.figure()
    ax = fig.add_subplot(111)
    x = np.linspace(-np.pi*2, np.pi*2, 100)
    if function == 'sine':
        y= amp*np.sin(x)
        ax.set_title('sin(x)')
    else:
        y=amp*np.cos(x)
        ax.set_title('cos(x)')
    plt.plot(x/np.pi,y)

    
    #centre bottom and left axes to zero

    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position('zero')
    ax.spines['top'].set_color('none')

    #Format axes - nicer eh!
    ax.xaxis.set_major_formatter(ticker.FormatStrFormatter('%g $\pi$'))

    figure_x, figure_y, figure_w, figure_h = fig.bbox.bounds
amp = 1
function = 'sine'
set_plot(amp, function)

#------------End Matplotlib code --------------------

#use Tabs - one for options, one for canvas to be displayed
#set spinner for amplitude and combo for function type

tab1_layout = [[sg.Text('Select Amplitude and trig function type', font = ('Calibri', 18, 'bold'))],
               [sg.Spin([sz for sz in range (1,5)], initial_value =1, size = (2,1), key = '_spin_'),
                sg.Text('Amplitude', size = (10, 1), font = ('Calibri', 12, 'bold'))],
               [sg.InputCombo(['sine', 'cosine'], size = (8, 4), key = '_function_'),
                sg.Text('Function', size = (10, 1),font = ('Calibri', 12, 'bold'))],
               [sg.ReadButton('Redraw Plot')],
               [sg.Text('', size = (2, 25))]]
               
tab2_layout = [[sg.Text('Plot Test - PySimpleGUI and Matplotlib and options', font = ('Calibri', 18, 'bold'))],
          [sg.Canvas(size = (figure_w, figure_h), key = '_canvas_')],
          [sg.OK(pad=((figure_w / 2, 0), 3), size=(6, 2))]]

layout = [[sg.TabGroup([[sg.Tab('Select options', tab1_layout), sg.Tab('Display Plot', tab2_layout)]])]]
window = sg.Window('Matplot, PySimpleGUI and options', force_toplevel = True).Layout(layout).Finalize()

fig_photo = draw_figure(window.FindElement('_canvas_').TKCanvas, fig)

while True:
    button, value = window.Read()
    if button == 'Redraw Plot':
        amp = int(value['_spin_'])
        function = value['_function_']
        set_plot(amp,function)
        fig_photo = draw_figure(window.FindElement('_canvas_').TKCanvas, fig)
        
    if button is None:   
        break


