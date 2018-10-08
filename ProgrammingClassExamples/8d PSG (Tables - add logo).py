#PySimple examples (v 3.8)
#Tony Crewe
#Sep 2018

#Based of Example program from MikeTheWatchGuy
#https://gitlab.com/lotspaih/PySimpleGUI

import sys
import PySimpleGUI as sg
import csv
import operator
import os

#get pathname to current file and add  file name for image 
dirname, filename = os.path.split(os.path.abspath(__file__))
pathname = dirname + '\\AFL.png'                                          

def table_example():

    filename = sg.PopupGetFile('Get required file', no_window = True,file_types=(("CSV Files","*.csv"),))


    data = []
    header_list = []

    with open(filename, "r") as infile:    
        reader = csv.reader(infile)
        for i in range (1):                
            header = next(reader)
            data = list(reader)          
    header = header + ['%', 'Pts']         
    for i in range (len(data)):
 
        percent = int(data[i][5])/int(data[i][6])*100
        data[i] = data[i] + [percent]     
        pts = int(data[i][2])*4 + int(data[i][4])*2
        data[i] = data[i] + [pts]        

    data.sort(key = operator.itemgetter(7), reverse = True)    
    data.sort(key = operator.itemgetter(8), reverse = True)     

    for i in range(len(data)):
        data[i][7] = str('{:.2f}'.format(data[i][7]))

    col_layout = [[sg.Table(values=data, headings=header, auto_size_columns=True,
                            max_col_width = 12,justification='right', size=(None, len(data)))]]

    layout = [[sg.Column(col_layout, size=(443,400), scrollable=True)],]
    window = sg.Window('Table', location = (662, 328), no_titlebar=True, grab_anywhere=False).Layout(layout)
    b, v = window.Read()

slayout = [[sg.Image(pathname),sg.Text('Load AFL data to display results.', font = ('Calibri', 14, 'bold') ),
            sg.ReadButton('Load File', size = (14,1))]]
swindow = sg.Window('Load File', location = (654,250)).Layout(slayout)

while True:
    button, value = swindow.Read()
    if button == 'Load File':
        table_example()
