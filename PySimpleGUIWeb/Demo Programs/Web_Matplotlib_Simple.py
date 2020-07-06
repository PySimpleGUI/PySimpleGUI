import PySimpleGUIWeb as sg
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasAgg
import matplotlib.figure
import io


def create_figure():
    # ------------------------------- START OF YOUR MATPLOTLIB CODE -------------------------------
    fig = matplotlib.figure.Figure(figsize=(5, 4), dpi=100)
    t = np.arange(0, 3, .01)
    fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))

    return fig


def draw_figure(fig, element):
    canv = FigureCanvasAgg(fig)
    buf = io.BytesIO()
    canv.print_figure(buf, format='png')

    if buf is None:
        return None
    buf.seek(0)
    data = buf.read()
    element.update(data=data)

def main():

    layout = [
                [sg.T('Matplotlib Example', font='Any 20')],
                [sg.Image(key='-IMAGE-')],
                [sg.B('Draw'), sg.B('Exit')],
            ]

    window = sg.Window('Title', layout)

    while True:
        event, values = window.read()
        if event == 'Exit' or event == sg.WIN_CLOSED:
            break
        if event == 'Draw':
            draw_figure(create_figure(), window['-IMAGE-'])
    window.close()


if __name__ == "__main__":
    main()
