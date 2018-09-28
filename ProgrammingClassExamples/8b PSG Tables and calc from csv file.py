#PySimple examples (v 3.8)
#Tony Crewe
#Sep 2018

#Based of Example program from MikeTheWatchGuy
#https://gitlab.com/lotspaih/PySimpleGUI

import sys
import PySimpleGUI as sg
import csv

def table_example():
    filename = sg.PopupGetFile('filename to open', no_window=True, file_types=(("CSV Files","*.csv"),))
    #populate table with file contents
    #Assume we know csv has haeding in row 1
    #assume we know 7 columns of data - relevenat to AFL w/o Pts or % shown
    #data will be data[0] = team, data [1] P, data [2] W, data[3] L
    #data [4] D, data[5] F, data[6] A
    #no error checking or validation used.

    data = []
    header_list = []
    with open(filename, "r") as infile:
        reader = csv.reader(infile)
        for i in range (1):             #get headings
            header = next(reader)
        data = list(reader)             # read everything else into a list of rows


    col_layout = [[sg.Table(values=data, headings=header, max_col_width=25,
                            auto_size_columns=True, justification='right', size=(None, len(data)))]]

    canvas_size = (13*10*len(header), 600)      # estimate canvas size - 13 pixels per char * 10 char per column * num columns
    layout = [[sg.Column(col_layout, size=canvas_size, scrollable=True)],]

    window = sg.Window('Table', grab_anywhere=False).Layout(layout)
    b, v = window.Read()

    sys.exit(69)

table_example()
