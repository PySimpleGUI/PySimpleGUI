import PySimpleGUI as sg
# import PySimpleGUIQt as sg
# import PySimpleGUIWeb as sg

import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasAgg
import matplotlib.figure
import matplotlib.pyplot as plt
import io

from matplotlib import cm
from mpl_toolkits.mplot3d.axes3d import get_test_data
from matplotlib.ticker import NullFormatter  # useful for `logit` scale


"""
    Demo - Matplotlib Embedded figure in a window TEMPLATE
    
    The reason this program is labelled as a "Template" is that it functions on 3 
    PySimpleGUI ports by only changing the import statement. tk, Qt, Web(Remi) all
    run this same code and produce identical results.
    
    Copyright 2020 PySimpleGUI.org
"""


def create_axis_grid():
    from mpl_toolkits.axes_grid1.axes_rgb import RGBAxes

    plt.close('all')

    def get_demo_image():
        # prepare image
        delta = 0.5

        extent = (-3, 4, -4, 3)
        x = np.arange(-3.0, 4.001, delta)
        y = np.arange(-4.0, 3.001, delta)
        X, Y = np.meshgrid(x, y)
        Z1 = np.exp(-X ** 2 - Y ** 2)
        Z2 = np.exp(-(X - 1) ** 2 - (Y - 1) ** 2)
        Z = (Z1 - Z2) * 2

        return Z, extent

    def get_rgb():
        Z, extent = get_demo_image()

        Z[Z < 0] = 0.
        Z = Z / Z.max()

        R = Z[:13, :13]
        G = Z[2:, 2:]
        B = Z[:13, 2:]

        return R, G, B

    fig = plt.figure(1)
    ax = RGBAxes(fig, [0.1, 0.1, 0.8, 0.8])

    r, g, b = get_rgb()
    kwargs = dict(origin="lower", interpolation="nearest")
    ax.imshow_rgb(r, g, b, **kwargs)

    ax.RGB.set_xlim(0., 9.5)
    ax.RGB.set_ylim(0.9, 10.6)

    plt.draw()
    return plt.gcf()



def create_figure():
    # ------------------------------- START OF YOUR MATPLOTLIB CODE -------------------------------
    fig = matplotlib.figure.Figure(figsize=(5, 4), dpi=100)
    t = np.arange(0, 3, .01)
    fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))

    return fig


def create_subplot_3d():


    fig = plt.figure()

    ax = fig.add_subplot(1, 2, 1, projection='3d')
    X = np.arange(-5, 5, 0.25)
    Y = np.arange(-5, 5, 0.25)
    X, Y = np.meshgrid(X, Y)
    R = np.sqrt(X ** 2 + Y ** 2)
    Z = np.sin(R)
    surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.jet,
                           linewidth=0, antialiased=False)
    ax.set_zlim3d(-1.01, 1.01)

    fig.colorbar(surf, shrink=0.5, aspect=5)

    ax = fig.add_subplot(1, 2, 2, projection='3d')
    X, Y, Z = get_test_data(0.05)
    ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)
    return fig




def create_pyplot_scales():

    plt.close('all')
    # Fixing random state for reproducibility
    np.random.seed(19680801)

    # make up some data in the interval ]0, 1[
    y = np.random.normal(loc=0.5, scale=0.4, size=1000)
    y = y[(y > 0) & (y < 1)]
    y.sort()
    x = np.arange(len(y))

    # plot with various axes scales
    plt.figure(1)

    # linear
    plt.subplot(221)
    plt.plot(x, y)
    plt.yscale('linear')
    plt.title('linear')
    plt.grid(True)

    # log
    plt.subplot(222)
    plt.plot(x, y)
    plt.yscale('log')
    plt.title('log')
    plt.grid(True)

    # symmetric log
    plt.subplot(223)
    plt.plot(x, y - y.mean())
    plt.yscale('symlog', linthreshy=0.01)
    plt.title('symlog')
    plt.grid(True)

    # logit
    plt.subplot(224)
    plt.plot(x, y)
    plt.yscale('logit')
    plt.title('logit')
    plt.grid(True)
    # Format the minor tick labels of the y-axis into empty strings with
    # `NullFormatter`, to avoid cumbering the axis with too many labels.
    plt.gca().yaxis.set_minor_formatter(NullFormatter())
    # Adjust the subplot layout, because the logit one may take more space
    # than usual, due to y-tick labels like "1 - 10^{-3}"
    plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25,
                        wspace=0.35)
    return plt.gcf()

# ----------------------------- The draw figure helpful function -----------------------------

def draw_figure(element, figure):
    """
    Draws the previously created "figure" in the supplied Image Element

    :param element: an Image Element
    :param figure: a Matplotlib figure
    :return: The figure canvas
    """


    plt.close('all')        # erases previously drawn plots
    canv = FigureCanvasAgg(figure)
    buf = io.BytesIO()
    canv.print_figure(buf, format='png')
    if buf is None:
        return None
    buf.seek(0)
    element.update(data=buf.read())
    return canv


# ----------------------------- The GUI Section -----------------------------

def main():
    dictionary_of_figures = {'Axis Grid': create_axis_grid,
                             'Subplot 3D': create_subplot_3d,
                             'Scales': create_pyplot_scales,
                             'Basic Figure': create_figure}


    left_col = [[sg.T('Figures to Draw')],
                [sg.Listbox(list(dictionary_of_figures), default_values=[list(dictionary_of_figures)[0]], size=(15, 5), key='-LB-')],
                [sg.T('Matplotlib Styles')],
                [sg.Combo(plt.style.available,  key='-STYLE-')]]

    layout = [ [sg.T('Matplotlib Example', font='Any 20')],
               [sg.Column(left_col), sg.Image(key='-IMAGE-')],
               [sg.B('Draw'), sg.B('Exit')] ]

    window = sg.Window('Matplotlib Template', layout)

    image_element = window['-IMAGE-']       # type: sg.Image

    while True:
        event, values = window.read()
        print(event, values)
        if event == 'Exit' or event == sg.WIN_CLOSED:
            break
        if event == 'Draw' and values['-LB-']:
            # Get the function to call to make figure. Done this way to get around bug in Web port (default value not working correctly for listbox)
            func = dictionary_of_figures.get(values['-LB-'][0], list(dictionary_of_figures.values())[0])
            if values['-STYLE-']:
                plt.style.use(values['-STYLE-'])
            draw_figure(image_element, func())

    window.close()


if __name__ == "__main__":
    main()
