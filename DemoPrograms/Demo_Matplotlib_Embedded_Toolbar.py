import PySimpleGUI as sg
import numpy as np

"""
    Embedding the Matplotlib toolbar into your application

"""

# ------------------------------- This is to include a matplotlib figure in a Tkinter canvas
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk



# ------------------------------- PySimpleGUI CODE

layout = [
    [sg.T('Graph: y=sin(x)')],
    [sg.B('Randomize Plot'), sg.B('Exit')],
    [sg.T('Controls:')],
    [sg.Canvas(key='controls_cv')],
    [sg.T('Figure:')],
    [sg.Column(
        layout=[
            [sg.Canvas(key='fig_cv',
                       # it's important that you set this size
                       size=(400 * 2, 400)
                       )]
        ],
        background_color='#DAE0E6',
        pad=(0, 0)
    )],
    [sg.B('Alive?')]

]

window = sg.Window('Graph with controls', layout)

# apply the layout so that the canvas exists for matplotlib to use.
window.finalize()

# Set up the Matplotlib Figure
DPI = 100
fig = Figure((404 * 2 / float(DPI), 404 / float(DPI)), dpi=DPI)
canvas = FigureCanvasTkAgg(fig, master=window["fig_cv"].TKCanvas)  # A tk.DrawingArea.

toolbar = NavigationToolbar2Tk(canvas, window["controls_cv"].TKCanvas)
toolbar.update()
fig.set_size_inches(404 * 2 / float(DPI), 404 / float(DPI))
canvas.draw()
canvas.get_tk_widget().pack(side="right", fill="both", expand=1)

# Set up matplotlib styling
# This won't change each loop
ax = fig.gca()
ax.set_title("y=sin(1 * x)")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.grid(True)

# create initial line element
x = np.linspace(0, 2 * np.pi)
y = np.sin(x)
line = ax.plot(x, y)[0]

while True:
    event, values = window.read()
    print(event, values)
    if event in (sg.WIN_CLOSED, 'Exit'):  # always,  always give a way out!
        break
    elif event == "Randomize Plot":
        # ------------------------------- PASTE YOUR MATPLOTLIB CODE HERE
        tau = np.random.randn()
        line.set_ydata(np.sin(x * tau))
        ax.set_title(f"y=sin({tau:.2f} * x)")
        fig.canvas.draw_idle()

window.close()
