#!/usr/bin/env python
import sys

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
else:
    sys.exit()

# sg.SetOptions(element_padding=(0,0))
headings = [data[0][x] for x in range(len(data[0]))]

layout = [[sg.Table(values=data[1:][:], headings=headings, max_col_width=25,
                        auto_size_columns=True, display_row_numbers=True, justification='right', num_rows=20, alternating_row_color='lightblue', key='_table_')],
          [sg.Button('Read'), sg.Button('Double')],
          [sg.T('Read = read which rows are selected')],[sg.T('Double = double the amount of data in the table')]]

window = sg.Window('Table', grab_anywhere=False, resizable=True).Layout(layout)

while True:
    event, values = window.Read()
    if event is None:
        break
    if event == 'Double':
        for i in range(len(data)):
            data.append(data[i])
        window.FindElement('_table_').Update(values = data)
    sg.Popup(event, values)
    # print(event, values)

sys.exit(69)
