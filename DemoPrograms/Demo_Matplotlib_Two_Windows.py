import PySimpleGUI as sg
import matplotlib.pyplot as plt

"""
    Simultaneous PySimpleGUI Window AND a Matplotlib Interactive Window
    A number of people have requested the ability to run a normal PySimpleGUI window that
    launches a MatplotLib window that is interactive with the usual Matplotlib controls.
    It turns out to be a rather simple thing to do.  The secret is to add parameter block=False to plt.show()
"""


layout = [[sg.Button('Plot'), sg.Cancel(), sg.Button('Popup')]]
window = sg.Window('Have some Matplotlib....', layout)

while True:
    event, values = window.read()
    if event in (None, 'Cancel'):
        break
    elif event == 'Plot':
        history = [0.1, 0.2, 0.5, 0.7]
        plt.plot(history)
        plt.show(block=False)
    elif event == 'Popup':
        sg.popup('Yes, your application is still running')
window.close()
