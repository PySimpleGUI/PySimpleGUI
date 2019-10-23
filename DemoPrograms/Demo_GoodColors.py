#!/usr/bin/env python
import sys
import PySimpleGUI as sg

# Example of colors in PSG

def main():
    # -------  Make a new Window  ------- #
    window = sg.Window('GoodColors', default_element_size=(30, 2))
    window.AddRow(sg.Text('Having trouble picking good colors? Try this'))
    window.AddRow(sg.Text('Here come the good colors as defined by PySimpleGUI'))

    #===== Show some nice BLUE colors with yellow text ===== ===== ===== ===== ===== =====  =====#
    text_color = sg.YELLOWS[0]
    buttons = (sg.Button('BLUES[{}]\n{}'.format(j, c), button_color=(
        text_color, c), size=(10, 2)) for j, c in enumerate(sg.BLUES))
    window.AddRow(sg.Text('Button Colors Using PySimpleGUI.BLUES'))
    window.AddRow(*buttons)
    window.AddRow(sg.Text('_' * 100, size=(65, 1)))

    #===== Show some nice PURPLE colors with yellow text ===== ===== ===== ===== ===== =====  =====#
    buttons = (sg.Button('PURPLES[{}]\n{}'.format(j, c), button_color=(
        text_color, c), size=(10, 2)) for j, c in enumerate(sg.PURPLES))
    window.AddRow(sg.Text('Button Colors Using PySimpleGUI.PURPLES'))
    window.AddRow(*buttons)
    window.AddRow(sg.Text('_' * 100, size=(65, 1)))

    #===== Show some nice GREEN colors with yellow text ===== ===== ===== ===== ===== =====  =====#
    buttons = (sg.Button('GREENS[{}]\n{}'.format(j, c), button_color=(
        text_color, c),  size=(10, 2)) for j, c in enumerate(sg.GREENS))
    window.AddRow(sg.Text('Button Colors Using PySimpleGUI.GREENS'))
    window.AddRow(*buttons)
    window.AddRow(sg.Text('_' * 100, size=(65, 1)))

    #===== Show some nice TAN colors with yellow text ===== ===== ===== ===== ===== =====  =====#
    text_color = sg.GREENS[0]        # let's use GREEN text on the tan
    buttons = (sg.Button('TANS[{}]\n{}'.format(j, c), button_color=(
        text_color, c),  size=(10, 2)) for j, c in enumerate(sg.TANS))
    window.AddRow(sg.Text('Button Colors Using PySimpleGUI.TANS'))
    window.AddRow(*buttons)
    window.AddRow(sg.Text('_' * 100, size=(65, 1)))

    #===== Show some nice YELLOWS colors with black text ===== ===== ===== ===== ===== =====  =====#
    text_color = 'black'       # let's use black text on the tan
    buttons = (sg.Button('YELLOWS[{}]\n{}'.format(j, c), button_color=(
        text_color, c),  size=(10, 2)) for j, c in enumerate(sg.YELLOWS))
    window.AddRow(sg.Text('Button Colors Using PySimpleGUI.YELLOWS'))
    window.AddRow(*buttons)
    window.AddRow(sg.Text('_' * 100, size=(65, 1)))

    #===== Add a click me button for fun and SHOW the window ===== ===== ===== ===== ===== =====  =====#
    window.AddRow(sg.Button('Click ME!'))
    event, values = window.read()

    window.close()


if __name__ == '__main__':
    main()
