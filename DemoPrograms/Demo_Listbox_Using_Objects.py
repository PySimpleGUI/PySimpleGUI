import PySimpleGUI as sg

"""
    Demo - Listbox Using Objects

    Several elements can take not just strings, but objects.  The Listsbox is one of them.
    This demo show how you can use objects directly in a Listbox in a way that you can access
        information about each object that is different than what is shown in the Window.

    The important part of this design pattern is the use of the __str__ method in your item objects.
        This method is what determines what is shown in the window.

    Copyright 2022-2023 PySimpleSoft, Inc. and/or its licensors. All rights reserved.
    
    Redistribution, modification, or any other use of PySimpleGUI or any portion thereof is subject to the terms of the PySimpleGUI License Agreement available at https://eula.pysimplegui.com.
    
    You may not redistribute, modify or otherwise use PySimpleGUI or its contents except pursuant to the PySimpleGUI License Agreement.
"""

class Item():
    def __init__(self, internal, shown):
        self.internal = internal
        self.shown = shown

    def __str__(self):
        return self.shown

# make list of some objects
my_item_list = [Item(f'Internal {i}', f'shown {i}') for i in range(100)]

layout = [  [sg.Text('Select 1 or more items and click "Go"')],
            [sg.Listbox(my_item_list, key='-LB-', s=(20,20), select_mode=sg.LISTBOX_SELECT_MODE_EXTENDED)],
            [sg.Output(s=(40,10))],
            [sg.Button('Go'), sg.Button('Exit')]  ]

window = sg.Window('Listbox Using Objects', layout)

while True:
    event, values = window.read()
    # print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    elif event == 'Go':
        print('You selected:')
        for item in values['-LB-']:
            print(item.internal)
window.close()
