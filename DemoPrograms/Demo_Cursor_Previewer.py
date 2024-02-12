import PySimpleGUI as sg

"""
    Demo - Preview tkinter cursors

    Shows the standard tkinter cursors using Buttons

    The name of the cursor is on the Button.  Mouse over the Button and you'll see
    what that cursor looks like.
    This list of cursors is a constant defined in PySimpleGUI.  The constant name is:
        sg.TKINTER_CURSORS

    Copyright 2022-2023 PySimpleSoft, Inc. and/or its licensors. All rights reserved.
    
    Redistribution, modification, or any other use of PySimpleGUI or any portion thereof is subject to the terms of the PySimpleGUI License Agreement available at https://eula.pysimplegui.com.
    
    You may not redistribute, modify or otherwise use PySimpleGUI or its contents except pursuant to the PySimpleGUI License Agreement.

"""

cursors = sg.TKINTER_CURSORS
# Make a layout that's 10 buttons across
NUM_BUTTONS_PER_ROW = 10
layout = [[]]
row = []
for i, c in enumerate(cursors):
    # print(i, c)
    row.append(sg.Button(c, size=(14,3), k=c))
    if ((i+1) % NUM_BUTTONS_PER_ROW) == 0:
        layout.append(row)
        row = []
        # print(row)
# Add on the last, partial row
start = len(cursors)//NUM_BUTTONS_PER_ROW * NUM_BUTTONS_PER_ROW
row = []
for i in range(start, len(cursors)):
    row.append(sg.Button(cursors[i], size=(14,3), k=cursors[i]))
layout.append(row)

window = sg.Window('Cursor Previewer',layout, finalize=True)

# set the cursor on each of the buttons that has the name of the cursor as the text
for c in cursors:
    window[c].set_cursor(c)

# The ubiquitous event loop...
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

window.close()