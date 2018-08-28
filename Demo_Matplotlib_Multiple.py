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

def PyplotGGPlotSytleSheet():
    import numpy as np
    import matplotlib.pyplot as plt

    plt.style.use('ggplot')

    # Fixing random state for reproducibility
    np.random.seed(19680801)

    fig, axes = plt.subplots(ncols=2, nrows=2)
    ax1, ax2, ax3, ax4 = axes.ravel()

    # scatter plot (Note: `plt.scatter` doesn't use default colors)
    x, y = np.random.normal(size=(2, 200))
    ax1.plot(x, y, 'o')

    # sinusoidal lines with colors from default color cycle
    L = 2 * np.pi
    x = np.linspace(0, L)
    ncolors = len(plt.rcParams['axes.prop_cycle'])
    shift = np.linspace(0, L, ncolors, endpoint=False)
    for s in shift:
        ax2.plot(x, np.sin(x + s), '-')
    ax2.margins(0)

    # bar graphs
    x = np.arange(5)
    y1, y2 = np.random.randint(1, 25, size=(2, 5))
    width = 0.25
    ax3.bar(x, y1, width)
    ax3.bar(x + width, y2, width,
            color=list(plt.rcParams['axes.prop_cycle'])[2]['color'])
    ax3.set_xticks(x + width)
    ax3.set_xticklabels(['a', 'b', 'c', 'd', 'e'])

    # circles with colors from default color cycle
    for i, color in enumerate(plt.rcParams['axes.prop_cycle']):
        xy = np.random.normal(size=2)
        ax4.add_patch(plt.Circle(xy, radius=0.3, color=color['color']))
    ax4.axis('equal')
    ax4.margins(0)
    fig = plt.gcf()             # get the figure to show
    return fig

def PyplotBoxPlot():
    import numpy as np
    import matplotlib.pyplot as plt

    # Fixing random state for reproducibility
    np.random.seed(19680801)

    # fake up some data
    spread = np.random.rand(50) * 100
    center = np.ones(25) * 50
    flier_high = np.random.rand(10) * 100 + 100
    flier_low = np.random.rand(10) * -100
    data = np.concatenate((spread, center, flier_high, flier_low), 0)
    fig1, ax1 = plt.subplots()
    ax1.set_title('Basic Plot')
    ax1.boxplot(data)
    return fig1

def PyplotRadarChart():
    import numpy as np

    import matplotlib.pyplot as plt
    from matplotlib.path import Path
    from matplotlib.spines import Spine
    from matplotlib.projections.polar import PolarAxes
    from matplotlib.projections import register_projection

    def radar_factory(num_vars, frame='circle'):
        """Create a radar chart with `num_vars` axes.

        This function creates a RadarAxes projection and registers it.

        Parameters
        ----------
        num_vars : int
            Number of variables for radar chart.
        frame : {'circle' | 'polygon'}
            Shape of frame surrounding axes.

        """
        # calculate evenly-spaced axis angles
        theta = np.linspace(0, 2 * np.pi, num_vars, endpoint=False)

        def draw_poly_patch(self):
            # rotate theta such that the first axis is at the top
            verts = unit_poly_verts(theta + np.pi / 2)
            return plt.Polygon(verts, closed=True, edgecolor='k')

        def draw_circle_patch(self):
            # unit circle centered on (0.5, 0.5)
            return plt.Circle((0.5, 0.5), 0.5)

        patch_dict = {'polygon': draw_poly_patch, 'circle': draw_circle_patch}
        if frame not in patch_dict:
            raise ValueError('unknown value for `frame`: %s' % frame)

        class RadarAxes(PolarAxes):

            name = 'radar'
            # use 1 line segment to connect specified points
            RESOLUTION = 1
            # define draw_frame method
            draw_patch = patch_dict[frame]

            def __init__(self, *args, **kwargs):
                super(RadarAxes, self).__init__(*args, **kwargs)
                # rotate plot such that the first axis is at the top
                self.set_theta_zero_location('N')

            def fill(self, *args, **kwargs):
                """Override fill so that line is closed by default"""
                closed = kwargs.pop('closed', True)
                return super(RadarAxes, self).fill(closed=closed, *args, **kwargs)

            def plot(self, *args, **kwargs):
                """Override plot so that line is closed by default"""
                lines = super(RadarAxes, self).plot(*args, **kwargs)
                for line in lines:
                    self._close_line(line)

            def _close_line(self, line):
                x, y = line.get_data()
                # FIXME: markers at x[0], y[0] get doubled-up
                if x[0] != x[-1]:
                    x = np.concatenate((x, [x[0]]))
                    y = np.concatenate((y, [y[0]]))
                    line.set_data(x, y)

            def set_varlabels(self, labels):
                self.set_thetagrids(np.degrees(theta), labels)

            def _gen_axes_patch(self):
                return self.draw_patch()

            def _gen_axes_spines(self):
                if frame == 'circle':
                    return PolarAxes._gen_axes_spines(self)
                # The following is a hack to get the spines (i.e. the axes frame)
                # to draw correctly for a polygon frame.

                # spine_type must be 'left', 'right', 'top', 'bottom', or `circle`.
                spine_type = 'circle'
                verts = unit_poly_verts(theta + np.pi / 2)
                # close off polygon by repeating first vertex
                verts.append(verts[0])
                path = Path(verts)

                spine = Spine(self, spine_type, path)
                spine.set_transform(self.transAxes)
                return {'polar': spine}

        register_projection(RadarAxes)
        return theta

    def unit_poly_verts(theta):
        """Return vertices of polygon for subplot axes.

        This polygon is circumscribed by a unit circle centered at (0.5, 0.5)
        """
        x0, y0, r = [0.5] * 3
        verts = [(r * np.cos(t) + x0, r * np.sin(t) + y0) for t in theta]
        return verts

    def example_data():
        # The following data is from the Denver Aerosol Sources and Health study.
        # See  doi:10.1016/j.atmosenv.2008.12.017
        #
        # The data are pollution source profile estimates for five modeled
        # pollution sources (e.g., cars, wood-burning, etc) that emit 7-9 chemical
        # species. The radar charts are experimented with here to see if we can
        # nicely visualize how the modeled source profiles change across four
        # scenarios:
        #  1) No gas-phase species present, just seven particulate counts on
        #     Sulfate
        #     Nitrate
        #     Elemental Carbon (EC)
        #     Organic Carbon fraction 1 (OC)
        #     Organic Carbon fraction 2 (OC2)
        #     Organic Carbon fraction 3 (OC3)
        #     Pyrolized Organic Carbon (OP)
        #  2)Inclusion of gas-phase specie carbon monoxide (CO)
        #  3)Inclusion of gas-phase specie ozone (O3).
        #  4)Inclusion of both gas-phase species is present...
        data = [
            ['Sulfate', 'Nitrate', 'EC', 'OC1', 'OC2', 'OC3', 'OP', 'CO', 'O3'],
            ('Basecase', [
                [0.88, 0.01, 0.03, 0.03, 0.00, 0.06, 0.01, 0.00, 0.00],
                [0.07, 0.95, 0.04, 0.05, 0.00, 0.02, 0.01, 0.00, 0.00],
                [0.01, 0.02, 0.85, 0.19, 0.05, 0.10, 0.00, 0.00, 0.00],
                [0.02, 0.01, 0.07, 0.01, 0.21, 0.12, 0.98, 0.00, 0.00],
                [0.01, 0.01, 0.02, 0.71, 0.74, 0.70, 0.00, 0.00, 0.00]]),
            ('With CO', [
                [0.88, 0.02, 0.02, 0.02, 0.00, 0.05, 0.00, 0.05, 0.00],
                [0.08, 0.94, 0.04, 0.02, 0.00, 0.01, 0.12, 0.04, 0.00],
                [0.01, 0.01, 0.79, 0.10, 0.00, 0.05, 0.00, 0.31, 0.00],
                [0.00, 0.02, 0.03, 0.38, 0.31, 0.31, 0.00, 0.59, 0.00],
                [0.02, 0.02, 0.11, 0.47, 0.69, 0.58, 0.88, 0.00, 0.00]]),
            ('With O3', [
                [0.89, 0.01, 0.07, 0.00, 0.00, 0.05, 0.00, 0.00, 0.03],
                [0.07, 0.95, 0.05, 0.04, 0.00, 0.02, 0.12, 0.00, 0.00],
                [0.01, 0.02, 0.86, 0.27, 0.16, 0.19, 0.00, 0.00, 0.00],
                [0.01, 0.03, 0.00, 0.32, 0.29, 0.27, 0.00, 0.00, 0.95],
                [0.02, 0.00, 0.03, 0.37, 0.56, 0.47, 0.87, 0.00, 0.00]]),
            ('CO & O3', [
                [0.87, 0.01, 0.08, 0.00, 0.00, 0.04, 0.00, 0.00, 0.01],
                [0.09, 0.95, 0.02, 0.03, 0.00, 0.01, 0.13, 0.06, 0.00],
                [0.01, 0.02, 0.71, 0.24, 0.13, 0.16, 0.00, 0.50, 0.00],
                [0.01, 0.03, 0.00, 0.28, 0.24, 0.23, 0.00, 0.44, 0.88],
                [0.02, 0.00, 0.18, 0.45, 0.64, 0.55, 0.86, 0.00, 0.16]])
        ]
        return data

    N = 9
    theta = radar_factory(N, frame='polygon')

    data = example_data()
    spoke_labels = data.pop(0)

    fig, axes = plt.subplots(figsize=(9, 9), nrows=2, ncols=2,
                             subplot_kw=dict(projection='radar'))
    fig.subplots_adjust(wspace=0.25, hspace=0.20, top=0.85, bottom=0.05)

    colors = ['b', 'r', 'g', 'm', 'y']
    # Plot the four cases from the example data on separate axes
    for ax, (title, case_data) in zip(axes.flatten(), data):
        ax.set_rgrids([0.2, 0.4, 0.6, 0.8])
        ax.set_title(title, weight='bold', size='medium', position=(0.5, 1.1),
                     horizontalalignment='center', verticalalignment='center')
        for d, color in zip(case_data, colors):
            ax.plot(theta, d, color=color)
            ax.fill(theta, d, facecolor=color, alpha=0.25)
        ax.set_varlabels(spoke_labels)

    # add legend relative to top-left plot
    ax = axes[0, 0]
    labels = ('Factor 1', 'Factor 2', 'Factor 3', 'Factor 4', 'Factor 5')
    legend = ax.legend(labels, loc=(0.9, .95),
                       labelspacing=0.1, fontsize='small')

    fig.text(0.5, 0.965, '5-Factor Solution Profiles Across Four Scenarios',
             horizontalalignment='center', color='black', weight='bold',
             size='large')
    return fig

def DifferentScales():
    import numpy as np
    import matplotlib.pyplot as plt

    # Create some mock data
    t = np.arange(0.01, 10.0, 0.01)
    data1 = np.exp(t)
    data2 = np.sin(2 * np.pi * t)

    fig, ax1 = plt.subplots()

    color = 'tab:red'
    ax1.set_xlabel('time (s)')
    ax1.set_ylabel('exp', color=color)
    ax1.plot(t, data1, color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

    color = 'tab:blue'
    ax2.set_ylabel('sin', color=color)  # we already handled the x-label with ax1
    ax2.plot(t, data2, color=color)
    ax2.tick_params(axis='y', labelcolor=color)

    fig.tight_layout()  # otherwise the right y-label is slightly clipped
    return fig

def ExploringNormalizations():
    import matplotlib.pyplot as plt
    import matplotlib.colors as mcolors
    import numpy as np
    from numpy.random import multivariate_normal

    data = np.vstack([
        multivariate_normal([10, 10], [[3, 2], [2, 3]], size=100000),
        multivariate_normal([30, 20], [[2, 3], [1, 3]], size=1000)
    ])

    gammas = [0.8, 0.5, 0.3]

    fig, axes = plt.subplots(nrows=2, ncols=2)

    axes[0, 0].set_title('Linear normalization')
    axes[0, 0].hist2d(data[:, 0], data[:, 1], bins=100)

    for ax, gamma in zip(axes.flat[1:], gammas):
        ax.set_title(r'Power law $(\gamma=%1.1f)$' % gamma)
        ax.hist2d(data[:, 0], data[:, 1],
                  bins=100, norm=mcolors.PowerNorm(gamma))

    fig.tight_layout()
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

#  The magic function that makes it possible.... glues together tkinter and pyplot using Canvas Widget
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


# -------------------------------- GUI Starts Here -------------------------------#
# fig = your figure you want to display.  Assumption is that 'fig' holds the      #
#       information to display.                                                   #
# --------------------------------------------------------------------------------#

fig_dict = {'Pyplot Simple':PyplotSimple, 'Pyplot Formatstr':PyplotFormatstr,'PyPlot Three':Subplot3d,
            'Unicode Minus': UnicodeMinus, 'Pyplot Scales' : PyplotScales, 'Axes Grid' : AxesGrid,
            'Exploring Normalizations' : ExploringNormalizations, 'Different Scales' : DifferentScales,
            'Pyplot Box Plot' : PyplotBoxPlot, 'Pyplot ggplot Style Sheet' : PyplotGGPlotSytleSheet}

figure_w, figure_h = 640,480
canvas_elem = g.Canvas(size=(figure_w, figure_h))         # get the canvas we'll be drawing on
# define the form layout
listbox_values = [key for key in fig_dict.keys()]
col_listbox = [[g.Listbox(values=listbox_values,size=(25,len(listbox_values)), key='func')],
               [g.T('    '), g.ReadFormButton('Plot', size=(5,2)), g.Exit(size=(5,2))]]

layout = [[g.Text('Matplotlib Plot Test', font=('current 18'))],
          [g.Column(col_listbox), canvas_elem]]

# create the form and show it without the plot
form = g.FlexForm('Demo Application - Embedding Matplotlib In PySimpleGUI')
form.Layout(layout)

while True:
    button, values = form.Read()
    # show it all again and get buttons
    if button is None or button is 'Exit':
        break
    if button is 'Clear':
        canvas_elem.TKCanvas.delete(Tk.ALL)
        continue

    choice = values['func'][0]
    try:
        func = fig_dict[choice]
    except:
        func = fig_dict['Pyplot Simple']

    plt.clf()
    fig = func()
    fig_photo = draw_figure(canvas_elem.TKCanvas, fig)


