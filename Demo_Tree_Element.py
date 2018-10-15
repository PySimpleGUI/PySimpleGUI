#!/usr/bin/env python
import sys
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg

treedata = sg.TreeData()

treedata.Insert("", '_A_', 'A', [1,2,3])
treedata.Insert("", '_B_', 'B', [4,5,6])
treedata.Insert("_A_", '_A1_', 'A1', ['can','be','anything'])
treedata.Insert("", '_C_', 'C', [])
treedata.Insert("_C_", '_C1_', 'C1', ['or'])
treedata.Insert("_A_", '_A2_', 'A2', [None, None])
treedata.Insert("_A1_", '_A3_', 'A30', ['getting deep'])
treedata.Insert("_C_", '_C2_', 'C2', ['nothing', 'at', 'all'])

layout = [[ sg.Text('Tree Test') ],
          [ sg.Tree(data=treedata, headings=['col1', 'col2', 'col3'], auto_size_columns=True, num_rows=10, col0_width=10)],
          [ sg.RButton('Read')]]

window = sg.Window('Tree Element Test').Layout(layout)

print(treedata)

while True:     # Event Loop
    event, values = window.Read()
    if event is None:
        break
    print(event, values)
