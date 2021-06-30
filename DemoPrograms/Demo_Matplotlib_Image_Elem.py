import PySimpleGUI as sg
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasAgg
import matplotlib.pyplot as plt
import io

"""
    Demo_Matplotlib_Image_Elem Demo
    
    Demo to show
        * How to use an Image element to show a Matplotlib figure
        * How to draw a Spectrogram
        * Hide the Image when a figure isn't present (shrinks the window automatically)
        
    The example graph can be found in the matplotlib gallery:
    https://matplotlib.org/stable/gallery/images_contours_and_fields/specgram_demo.html        
    
    Copyright 2021 PySimpleGUI
"""


# .d88888b    dP                       dP
# 88.    "'   88                       88
# `Y88888b. d8888P .d8888b. 88d888b. d8888P
#       `8b   88   88'  `88 88'  `88   88
# d8'   .8P   88   88.  .88 88         88
#  Y88888P    dP   `88888P8 dP         dP
# oooooooooooooooooooooooooooooooooooooooooo of your Matplotlib code


def your_matplotlib_code():
    # Fixing random state for reproducibility
    np.random.seed(19680801)

    dt = 0.0005
    t = np.arange(0.0, 20.0, dt)
    s1 = np.sin(2 * np.pi * 100 * t)
    s2 = 2 * np.sin(2 * np.pi * 400 * t)

    # create a transient "chirp"
    s2[t <= 10] = s2[12 <= t] = 0

    # add some noise into the mix
    nse = 0.01 * np.random.random(size=len(t))

    x = s1 + s2 + nse  # the signal
    NFFT = 1024  # the length of the windowing segments
    Fs = int(1.0 / dt)  # the sampling frequency

    fig, (ax1, ax2) = plt.subplots(nrows=2)
    ax1.plot(t, x)
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
# ooooooooooooooooooooooo~88~oooooooooooooooooooooooo function starts below
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
    layout = [[sg.Text('Spectrogram test')],
              [sg.pin(sg.Image(key='-IMAGE-'))],
              [sg.Button('Ok'), sg.B('Clear')]]

    # create the form and show it without the plot
    window = sg.Window('Spectrogram', layout, element_justification='c', font='Helvetica 14')

    while True:
        # add the plot to the window
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'Ok':
            draw_figure(window['-IMAGE-'], your_matplotlib_code())
            window['-IMAGE-'].update(visible=True)
        elif event == 'Clear':
            plt.close('all')                                # close all plots
            window['-IMAGE-'].update()                      # clears the image
            window['-IMAGE-'].update(visible=False)         # hides the blank image


    window.close()


if __name__ == '__main__':
    main()