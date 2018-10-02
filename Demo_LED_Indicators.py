#!/usr/bin/env python
import sys

if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg
import time
import random

"""
    Demo program showing how to create your own "LED Indicators"
    The LEDIndicator function acts like a new Element that is directly placed in a window's layout
    After the Window is created, use the SetLED function to access the LED and set the color

"""


def LEDIndicator(key):
    return sg.Graph(canvas_size=(30, 30), graph_bottom_left=(-20, -20), graph_top_right=(20, 20),
                    pad=(0, 0), key=key)


def SetLED(window, key, color):
    graph = window.FindElement(key)
    graph.Erase()
    graph.DrawCircle((0, 0), 10, fill_color=color, line_color=color)


layout = [[sg.Text('My Status Report')],
          [sg.Text('CPU Use'), LEDIndicator('_cpu_')],
          [sg.Text('RAM'), LEDIndicator('_ram_')],
          [sg.Text('Temperature'), LEDIndicator('_temp_')],
          [sg.Text('Server 1'), LEDIndicator('_server1_')],
          [sg.Exit()]]

window = sg.Window('My new window', default_element_size=(12, 1), auto_size_text=False).Layout(layout).Finalize()

i = 0
while True:  # Event Loop
    button, value = window.ReadNonBlocking()
    if value is None:
        break
    i += 1
    SetLED(window, '_cpu_', 'green' if random.randint(1, 10) > 5 else 'red')
    SetLED(window, '_ram_', 'green' if random.randint(1, 10) > 5 else 'red')
    SetLED(window, '_temp_', 'green' if random.randint(1, 10) > 5 else 'red')
    SetLED(window, '_server1_', 'green' if random.randint(1, 10) > 5 else 'red')

    time.sleep(.400)
