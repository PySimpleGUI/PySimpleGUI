#!/usr/bin/env python
import sys

from Demo_Turtle import canvas

if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg
import csv


filename = sg.PopupGetFile('filename to open', no_window=True, file_types=(("CSV Files","*.csv"),))
# --- populate table with file contents --- #
data = []
if filename is not None:
    with open(filename, "r") as infile:
        reader = csv.reader(infile)
        try:
            data = list(reader)  # read everything else into a list of rows
        except:
            sg.PopupError('Error reading file')
            sys.exit(69)

sg.SetOptions(element_padding=(0, 0))

headings = [data[0][x] for x in range(len(data[0]))]

col_layout = [[sg.Table(values=data[1:][:], headings=headings, max_col_width=25,
                        auto_size_columns=True, display_row_numbers=True, justification='right', num_rows=len(data), alternating_row_color='lightblue')]]

canvas_size = (13 * 10 * len(headings), 600)  # estimate canvas size - 13 pixels per char * 10 per column * num columns

layout = [[sg.Column(col_layout, size=canvas_size, scrollable=True)],]
window = sg.Window('Table', grab_anywhere=False).Layout(layout)

event, values = window.Read()

sys.exit(69)
