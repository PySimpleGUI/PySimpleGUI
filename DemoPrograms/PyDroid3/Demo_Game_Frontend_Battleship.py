import tkinter
import PySimpleGUI as sg
from random import randint

def Battleship():
    sg.change_look_and_feel('Dark Blue 3')
    MAX_ROWS = MAX_COL = 8

    # Start building layout with the top 2 rows that contain Text elements
    layout =   [[sg.Text('BATTLESHIP', font='Default 12')],
               [sg.Text(size=(15,1), key='-MESSAGE-', font='any 8')]]
    # Add the board, a grid a buttons
    layout +=  [[sg.Button(str('O'), size=(1, 1), pad=(0,0), border_width=0, font='any 8',key=(row,col)) for col in range(MAX_COL)] for row in range(MAX_ROWS)]
    # Add the exit button as the last row
    layout +=  [[sg.Button('Exit', button_color=('white', 'red'))]]

    window = sg.Window('Battleship', layout, location=(0,0))

    while True:         # The Event Loop
        event, values = window.read()
        print(event, values)
        if event in (None, 'Exit'):
            break
        if randint(1,10) < 5:           # simulate a hit or a miss
            window[event].update('H', button_color=('white','red'))
            window['-MESSAGE-'].update('Hit')
        else:
            window[event].update('M', button_color=('white','black'))
            window['-MESSAGE-'].update('Miss')
    window.close()

Battleship()
