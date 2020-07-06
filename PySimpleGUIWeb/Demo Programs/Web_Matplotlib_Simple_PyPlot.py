import PySimpleGUIWeb as sg
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasAgg
import matplotlib.pyplot as plt
import io


def draw_figure(fig, element):
    """
    Draws the previously created "figure" in the supplied Image Element

    :param fig: a Matplotlib figure
    :param element: an Image Element
    :return: The figure canvas
    """

    plt.close('all')  # erases previously drawn plots
    canv = FigureCanvasAgg(fig)
    buf = io.BytesIO()
    canv.print_figure(buf, format='png')
    if buf is None:
        return None
    buf.seek(0)
    element.update(data=buf.read())
    return canv


def main():
    layout = [[sg.Text('Matplotlib Simple Plot', font='Any 20')],
              [sg.Image(key='-IMAGE-')],
              [sg.Button('Exit')]]

    window = sg.Window('Matplotlib Example', layout, finalize=True)

    fig = plt.figure()
    x = np.arange(0, 5, 0.1)
    y = np.sin(x)
    plt.plot(x, y)
    draw_figure(fig, window['-IMAGE-'])

    window.read(close=True)


if __name__ == "__main__":
    main()
