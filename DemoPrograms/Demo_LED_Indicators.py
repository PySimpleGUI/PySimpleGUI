#!/usr/bin/env python
import PySimpleGUI as sg
import time
import random

"""
    Demo program showing how to create your own "LED Indicators"
    The LEDIndicator function acts like a new Element that is directly placed in a window's layout
    After the Window is created, use the SetLED function to access the LED and set the color

"""


def LEDIndicator(key=None, radius=30):
    return sg.Graph(canvas_size=(radius, radius),
             graph_bottom_left=(-radius, -radius),
             graph_top_right=(radius, radius),
             pad=(0, 0), key=key)

def SetLED(window, key, color):
    graph = window[key]
    graph.erase()
    graph.draw_circle((0, 0), 12, fill_color=color, line_color=color)


layout = [[sg.Text('My LED Status Indicators', size=(20,1))],
          [sg.Text('CPU Use'), LEDIndicator('_cpu_')],
          [sg.Text('RAM'), LEDIndicator('_ram_')],
          [sg.Text('Temperature'), LEDIndicator('_temp_')],
          [sg.Text('Server 1'), LEDIndicator('_server1_')],
          [sg.Button('Exit')]]

window = sg.Window('My new window', layout, default_element_size=(12, 1), auto_size_text=False, finalize=True)

i = 0
while True:  # Event Loop
    event, value = window.read(timeout=400)
    if event == 'Exit' or event == sg.WIN_CLOSED:
        break
    if value is None:
        break
    i += 1
    SetLED(window, '_cpu_', 'green' if random.randint(1, 10) > 5 else 'red')
    SetLED(window, '_ram_', 'green' if random.randint(1, 10) > 5 else 'red')
    SetLED(window, '_temp_', 'green' if random.randint(1, 10) > 5 else 'red')
    SetLED(window, '_server1_', 'green' if random.randint(1, 10) > 5 else 'red')
window.close()
