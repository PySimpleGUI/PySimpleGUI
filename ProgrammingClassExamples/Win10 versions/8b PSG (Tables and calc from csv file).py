# PySimple examples (v 3.9.3)
# Tony Crewe
# Sep 2018 - updated Oct 2018

# Based of Example program from MikeTheWatchGuy
# https://gitlab.com/lotspaih/PySimpleGUI

import sys
import PySimpleGUI as sg
import csv

sg.ChangeLookAndFeel('BrownBlue')


def calc_ladder():
    filename = sg.PopupGetFile('Get required file', no_window=True, file_types=(("CSV Files", "*.csv"),))
    # populate table with file contents
    # Assume we know csv has heading in row 1
    # Assume we know 7 columns of data - relevenat to AFL w/o Pts or % shown
    # data is a list of lists containing data about each team
    # data[0] is one teams data data[0[[0] = team, data[0][1] P, data[0] [2] W,
    # data[0][3] L, data [0][4] D, data [0][5] F, data [0][6] A
    # no error checking or validation used.

    # initialise variable
    data = []
    header_list = []
    # read csv
    with open(filename, "r") as infile:
        reader = csv.reader(infile)
        for i in range(1):
            # get headings
            header = next(reader)
            # read everything else into a list of rows
            data = list(reader)
            # add headings
    header = header + ['%', 'Pts']
    for i in range(len(data)):
        # calculate % and format to 2 decimal places
        percent = str('{:.2f}'.format(int(data[i][5]) / int(data[i][6]) * 100))
        data[i] = data[i] + [percent]  # add to data
        pts = int(data[i][2]) * 4 + int(data[i][4]) * 2
        data[i] = data[i] + [pts]  # add to data

    # use Table (explore settings) and add to column layout
    col_layout = [[sg.Table(values=data, headings=header, auto_size_columns=True,
                            max_col_width=12, justification='right', background_color='White',
                            text_color='Black', alternating_row_color='LightBlue', size=(None, len(data)))]]

    layout = [[sg.Column(col_layout, size=(500, 400), scrollable=True)], ]

    window = sg.Window('Table', location=(700, 325), grab_anywhere=False).Layout(layout)
    b, v = window.Read()


slayout = [
    [sg.Text('Load AFL file to display results with points and percentage'), sg.ReadButton('Load File', size=(20, 1))]]
swindow = sg.Window('Load File', location=(700, 250)).Layout(slayout)

while True:
    button, value = swindow.Read()
    if button is not None:
        if button == 'Load File':
            calc_ladder()
    else:
        break
    
