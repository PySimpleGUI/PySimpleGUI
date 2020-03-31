import math
import numpy as np
import PySimpleGUI as sg
import time

"""
    Fourier Transform Animated Graph
    
    A fun demonstration of the Graph Element and the drawing primitive draw_lines
    Written by Jason Yang, by an innovative PySimpleGUI user that has created a number
    of impressive animations using PySimpleGUI.
    
    Copyright 2020 Jason Yang
"""

def push(v):
    if len(buffer)==size:
        del buffer[-1]
    buffer[0:0] = [v]

def update(i):
    draw.Erase()
    x1 = x0 + r1*math.cos(v1*i*rad)
    y1 = y0 + r1*math.sin(v1*i*rad)
    x2 = x1 + r2*math.cos(v2*i*rad)
    y2 = y1 + r2*math.sin(v2*i*rad)
    x3 = x2 + r3*math.cos(v3*i*rad)
    y3 = y2 + r3*math.sin(v3*i*rad)
    push(y3)
    draw.DrawCircle((x0, y0), r1, line_color='blue')
    draw.DrawCircle((x1, y1), r2, line_color='yellow')
    draw.DrawCircle((x2, y2), r3, line_color='red')
    draw.DrawLine((x0, y0), (x1, y1), color='magenta')
    draw.DrawLine((x1, y1), (x2, y2), color='white')
    draw.DrawLine((x2, y2), (x3, y3), color='white')
    draw.DrawLine((x3, y3), (x[0]+xx, buffer[0]), color='ivory')
    draw.DrawPoint((x3, y3), size=10, color='red')
    lines = ((x[i]+xx, y) for i, y in enumerate(buffer))
    draw.DrawLines(lines, color='green1')

size = 720
distance = 100
r0, r1, r2, r3 = 90, 90, 30, 18
rad = math.pi/180
v1, v2, v3 = 1, 3, 5
x = np.array(list(range(size)))
x0 = y0 = r1+r2+r3
xx = x0*2 + distance
buffer = []
win_size = (xx+size, 2*x0)

layout = [[sg.Graph(canvas_size=win_size, graph_bottom_left=(0, 0),
                     graph_top_right=win_size, key='-GRAPH-')]]
window = sg.Window('Fourier', layout=layout)
draw = window['-GRAPH-']

i = 0
timeout = refresh_interval = 10    # Target refresh interval = 10 milliseconds

while True:
    start_time = time.time()

    event, values = window.read(timeout=timeout)
    if event == None:
        break

    update(i)
    i = i+1 if i<359 else 0

    timeout = max(0, (refresh_interval - (time.time()-start_time)*1000))

window.close()