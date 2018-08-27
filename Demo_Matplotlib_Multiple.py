import PySimpleGUI as g
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasAgg
import matplotlib.backends.tkagg as tkagg
import tkinter as Tk

"""
Demonstrates one way of embedding Matplotlib figures into a PySimpleGUI window.

Basic steps are:
 * Create a Canvas Element
 * Layout form
 * Display form (NON BLOCKING)
 * Draw plots onto convas
 * Display form (BLOCKING)
"""



import numpy as np
import matplotlib.pyplot as plt


def PyplotSimple():
    import numpy as np
    import matplotlib.pyplot as plt

    # evenly sampled time at 200ms intervals
    t = np.arange(0., 5., 0.2)

    # red dashes, blue squares and green triangles
    plt.plot(t, t, 'r--', t, t ** 2, 'bs', t, t ** 3, 'g^')

    fig = plt.gcf()  # get the figure to show
    return fig

def PyplotFormatstr():

    def f(t):
        return np.exp(-t) * np.cos(2*np.pi*t)

    t1 = np.arange(0.0, 5.0, 0.1)
    t2 = np.arange(0.0, 5.0, 0.02)

    plt.figure(1)
    plt.subplot(211)
    plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

    plt.subplot(212)
    plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
    fig = plt.gcf()             # get the figure to show
    return fig

def UnicodeMinus():
    import numpy as np
    import matplotlib
    import matplotlib.pyplot as plt

    # Fixing random state for reproducibility
    np.random.seed(19680801)

    matplotlib.rcParams['axes.unicode_minus'] = False
    fig, ax = plt.subplots()
    ax.plot(10 * np.random.randn(100), 10 * np.random.randn(100), 'o')
    ax.set_title('Using hyphen instead of Unicode minus')
    return fig

def Subplot3d():
    from mpl_toolkits.mplot3d.axes3d import Axes3D
    from matplotlib import cm
    # from matplotlib.ticker import LinearLocator, FixedLocator, FormatStrFormatter
    import matplotlib.pyplot as plt
    import numpy as np

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

    # ax.w_zaxis.set_major_locator(LinearLocator(10))
    # ax.w_zaxis.set_major_formatter(FormatStrFormatter('%.03f'))

    fig.colorbar(surf, shrink=0.5, aspect=5)

    from mpl_toolkits.mplot3d.axes3d import get_test_data
    ax = fig.add_subplot(1, 2, 2, projection='3d')
    X, Y, Z = get_test_data(0.05)
    ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)
    return fig

def PyplotScales():
    import numpy as np
    import matplotlib.pyplot as plt

    from matplotlib.ticker import NullFormatter  # useful for `logit` scale

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


def AxesGrid():
    import numpy as np
    import matplotlib.pyplot as plt
    from mpl_toolkits.axes_grid1.axes_rgb import RGBAxes

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

    # Position: convert from top-left anchor to center anchor
    canvas.create_image(loc[0] + figure_w/2, loc[1] + figure_h/2, image=photo)

    # Unfortunately, there's no accessor for the pointer to the native renderer
    tkagg.blit(photo, figure_canvas_agg.get_renderer()._renderer, colormode=2)

    # Return a handle which contains a reference to the photo object
    # which must be kept live or else the picture disappears
    return photo

#------------------------------- PASTE YOUR MATPLOTLIB CODE HERE -------------------------------


# -------------------------------- GUI Starts Here -------------------------------#
# fig = your figure you want to display.  Assumption is that 'fig' holds the      #
#       information to display.                                                   #
# --------------------------------------------------------------------------------#

fig_dict = {'Pyplot Simple':PyplotSimple, 'Pyplot Formatstr':PyplotFormatstr,'PyPlot Three':Subplot3d,
            'Unicode Minus': UnicodeMinus, 'Pyplot Scales' : PyplotScales, 'Axes Grid' : AxesGrid}

figure_w, figure_h = 640,480
canvas_elem = g.Canvas(size=(figure_w, figure_h))         # get the canvas we'll be drawing on
# define the form layout
listbox_values = [key for key in fig_dict.keys()]
col_listbox = [[g.Listbox(values=listbox_values,size=(20,8), key='func')],
               [g.ReadFormButton('Plot', pad=((50,0), 3))]]

layout = [[g.Text('Matplotlib Plot Test', font=('current 18'))],
          [g.Column(col_listbox), canvas_elem],
          [g.Exit(pad=((50,0), 3), size=(4,2))]]

# create the form and show it without the plot
form = g.FlexForm('Demo Application - Embedding Matplotlib In PySimpleGUI')
form.Layout(layout)
form.Show(non_blocking=True)
form.NonBlocking = False

# add the plot to the window
while True:
    button, values = form.Read()
    # show it all again and get buttons
    if button is None or button is 'Exit':
        break
    choice = values['func'][0]
    try:
        func = fig_dict[choice]
    except:
        func = fig_dict['Pyplot Simple']
    fig = func()
    fig_photo = draw_figure(canvas_elem.TKCanvas, fig)
