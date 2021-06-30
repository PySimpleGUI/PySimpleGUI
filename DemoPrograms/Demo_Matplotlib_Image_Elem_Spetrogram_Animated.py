import PySimpleGUI as sg
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasAgg
import matplotlib.pyplot as plt
import io
import time

"""
    Demo_Matplotlib_Image_Elem_Spetrogram_Animated Demo

    Demo to show
        * How to use an Image element to show a Matplotlib figure
        * How to draw a Spectrogram
        * How to animate the drawing by simply erasing and drawing the entire figure

    The point here is to keep things simple to enable you to get started.
    
    The example static graph can be found in the matplotlib gallery:
    https://matplotlib.org/stable/gallery/images_contours_and_fields/specgram_demo.html        

    Copyright 2021 PySimpleGUI
"""

np.random.seed(19801)

# .d88888b    dP                       dP
# 88.    "'   88                       88
# `Y88888b. d8888P .d8888b. 88d888b. d8888P
#       `8b   88   88'  `88 88'  `88   88
# d8'   .8P   88   88.  .88 88         88
#  Y88888P    dP   `88888P8 dP         dP
# oooooooooooooooooooooooooooooooooooooooooo of your Matplotlib code


def your_matplotlib_code():
    # The animated part of this is the t_lower, t_upper terms as well as the entire dataset that's graphed.
    # An entirely new graph is created from scratch every time... implying here that optimization is possible.
    if not hasattr(your_matplotlib_code, 't_lower'):
        your_matplotlib_code.t_lower = 10
        your_matplotlib_code.t_upper = 12
    else:
        your_matplotlib_code.t_lower = (your_matplotlib_code.t_lower + .5) % 18
        your_matplotlib_code.t_upper = (your_matplotlib_code.t_upper + .5) % 18

    dt = 0.0005
    t = np.arange(0.0, 20.0, dt)
    s1 = np.sin(2 * np.pi * 100 * t)
    s2 = 2 * np.sin(2 * np.pi * 400 * t)

    # create a transient "chirp"
    # s2[t <= 5] = s2[15 <= t] = 0      # original line of code (not animated)
    # If running the animation, use the t_lower and t_upper values
    s2[t <= your_matplotlib_code.t_lower] = s2[your_matplotlib_code.t_upper <= t] = 0

    # add some noise into the mix
    nse = 0.01 * np.random.random(size=len(t))

    x = s1 + s2 + nse  # the signal
    NFFT = 1024  # the length of the windowing segments
    Fs = int(1.0 / dt)  # the sampling frequency

    fig, (ax2) = plt.subplots(nrows=1)
    # ax1.plot(t, x)
    Pxx, freqs, bins, im = ax2.specgram(x, NFFT=NFFT, Fs=Fs, noverlap=900)

    return fig


#  88888888b                dP
#  88                       88
#  88aaaa    88d888b. .d888b88
#  88        88'  `88 88'  `88
#  88        88    88 88.  .88
#  88888888P dP    dP `88888P8
# ooooooooooooooooooooooooooooo of your Matplotlib code


# ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo


# dP     dP           dP
# 88     88           88
# 88aaaaa88a .d8888b. 88  88d888b. .d8888b. 88d888b.
# 88     88  88ooood8 88  88'  `88 88ooood8 88'  `88
# 88     88  88.  ... 88  88.  .88 88.  ... 88
# dP     dP  `88888P' dP  88Y888P' `88888P' dP
# ooooooooooooooooooooooo~88~oooooooooooooooooooooooo function starts here
#                         dP

def draw_figure(element, figure):
    """
    Draws the previously created "figure" in the supplied Image Element

    :param element: an Image Element
    :param figure: a Matplotlib figure
    :return: The figure canvas
    """

    plt.close('all')  # erases previously drawn plots
    canv = FigureCanvasAgg(figure)
    buf = io.BytesIO()
    canv.print_figure(buf, format='png')
    if buf is not None:
        buf.seek(0)
        element.update(data=buf.read())
        return canv
    else:
        return None


#  .88888.  dP     dP dP
# d8'   `88 88     88 88
# 88        88     88 88
# 88   YP88 88     88 88
# Y8.   .88 Y8.   .8P 88
#  `88888'  `Y88888P' dP
# ooooooooooooooooooooooo


def main():
    # define the window layout
    layout = [[sg.Text('Spectrogram Animated - Not Threaded', font='Helvetica 24')],
              [sg.pin(sg.Image(key='-IMAGE-'))],
              [sg.T(size=(50, 1), k='-STATS-')],
              [sg.B('Animate', focus=True, k='-ANIMATE-')]]

    # create the form and show it without the plot
    window = sg.Window('Animated Spectrogram', layout, element_justification='c', font='Helvetica 14')

    counter = delta = start_time = 0
    timeout = None
    while True:
        event, values = window.read(timeout=timeout)
        if event == sg.WIN_CLOSED:
            break
        sg.timer_start()
        if event == '-ANIMATE-':
            timeout = 0
            window['-IMAGE-'].update(visible=True)
            start_time = time.time()
        elif event == sg.TIMEOUT_EVENT:
            plt.close('all')  # close all plots
            window['-IMAGE-'].update()  # clears the image
            draw_figure(window['-IMAGE-'], your_matplotlib_code())
            seconds_elapsed = int(time.time() - start_time)
            fps = counter/seconds_elapsed if seconds_elapsed != 0 else 1.0
            window['-STATS-'].update(f'Frame {counter} Write Time {delta} FPS = {fps:2.2} seconds = {seconds_elapsed}')
            counter += 1
        delta = sg.timer_stop()
    window.close()


if __name__ == '__main__':
    main()