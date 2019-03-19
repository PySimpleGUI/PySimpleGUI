#!/usr/bin/env python
import PySimpleGUIQt as sg

treedata = sg.TreeData()
green = r'C:/Python/PycharmProjects/GooeyGUI/ButtonGraphics/Oct16/Mac/green30.png'
orange = r'C:\Python\PycharmProjects\GooeyGUI\ButtonGraphics\Oct16\Mac\orange30.png'
red = r'C:\Python\PycharmProjects\GooeyGUI\ButtonGraphics\Oct16\Mac\red30.png'
treedata.Insert("", '_A_', 'A', [1,2,3], orange)
treedata.Insert("", '_B_', 'B', [4,5,6], green)
treedata.Insert("_A_", '_A1_', 'A1', ['can','be','anything'], red)
treedata.Insert("", '_C_', 'C', [], red)
treedata.Insert("_C_", '_C1_', 'C1', ['or'], green)
treedata.Insert("_A_", '_A2_', 'A2', [None, None])
treedata.Insert("_A1_", '_A3_', 'A30', ['getting deep'])
treedata.Insert("_C_", '_C2_', 'C2', ['nothing', 'at', 'all'])

for i in range(100):
    treedata.Insert('_C_', i, i, [])

layout = [[ sg.Text('Tree Test') ],
          [ sg.Tree(data=treedata, headings=['col1', 'col2', 'col3'],change_submits=True, auto_size_columns=True, num_rows=10, col0_width=10, key='_TREE_', show_expanded=True, size=(300,300)),
            ],
          [ sg.Button('Read'), sg.Button('Update')]]

window = sg.Window('Tree Element Test').Layout(layout)

print(treedata)
filename = r'C:/Python/PycharmProjects/GooeyGUI/ButtonGraphics/Oct16/Mac/green30.png'
while True:     # Event Loop
    event, values = window.Read()
    if event is None:
        break
    if event == 'Update':
        treedata = sg.TreeData()
        treedata.Insert("", '_A_', 'A', [1, 2, 3], filename )
        treedata.Insert("", '_B_', 'B', [4, 5, 6], filename)
        treedata.Insert("_A_", '_A1_', 'A1', ['can', 'be', 'anything'], filename)
        treedata.Insert("", '_C_', 'C', [], filename)
        treedata.Insert("_C_", '_C1_', 'C1', ['or'])
        treedata.Insert("_A_", '_A2_', 'A2', [None, None])
        window.FindElement('_TREE_').Update(treedata)
    elif event == 'Read':
        print(event, values)
