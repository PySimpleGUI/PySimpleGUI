#PySimple examples (v 3.9.3)
#Tony Crewe
#Oct 2018 MacOs

#Based of Example program from MikeTheWatchGuy
#https://gitlab.com/lotspaih/PySimpleGUI

import sys
import PySimpleGUI as sg
import csv
import operator
import os

sg.SetOptions(background_color = 'Black',
              element_background_color = 'Black',
              font = ('Calibri', 16, 'bold'),
              text_color = 'White')

#get pathname to current file and add  file name for image 
dirname, filename = os.path.split(os.path.abspath(__file__))

pathname = os.path.join(dirname , 'AFL.png' )                                         

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

    col_layout = [[sg.Table(values=data, headings=header, col_widths = (16, 3,3,3,3,6,6,6,4), auto_size_columns=False,
                    max_col_width = 30,justification='right', size=(None, len(data)))]]

    layout = [[sg.Column(col_layout, size=(480,360), scrollable=True)],]

    window = sg.Window('Table', no_titlebar = False, location = (350, 318), grab_anywhere = False).Layout(layout)
    b, v = window.Read()

slayout = [[sg.Image(pathname),sg.Text(' Load AFL (csv) file to display results. '),
            sg.ReadButton('Load File', size = (10,1))]]
swindow = sg.Window('Load File', location = (350,250)).Layout(slayout)

while True:
    button, value = swindow.Read()
    if button is not None:
        if button == 'Load File':
            table_example()
    else:
        break

