#!/usr/bin/env python
import PySimpleGUI as sg

'''
    Example of colors in PySimpleGUI
'''

def main():
    s10 = (10, 2)

    window = sg.Window('GoodColors', [
        [sg.Text('Having trouble picking good colors? Try this')],
        [sg.Text('Here come the good colors as defined by PySimpleGUI')],
        [sg.Text('Button Colors Using PySimpleGUI.BLUES')],

        [*[sg.Button('BLUES[{}]\n{}'.format(j, c), button_color=(sg.YELLOWS[0], c), size=s10)
           for j, c in enumerate(sg.BLUES)]],
        [sg.Text('_' * 100, size=(65, 1))],
        [sg.Text('Button Colors Using PySimpleGUI.PURPLES')],

        [*[sg.Button('PURPLES[{}]\n{}'.format(j, c), button_color=(sg.YELLOWS[0], c), size=s10)
           for j, c in enumerate(sg.PURPLES)]],
        [sg.Text('_' * 100, size=(65, 1))],
        [sg.Text('Button Colors Using PySimpleGUI.GREENS')],

        [*[sg.Button('GREENS[{}]\n{}'.format(j, c), button_color=(sg.YELLOWS[0], c), size=s10)
           for j, c in enumerate(sg.GREENS)]],
        [sg.Text('_' * 100, size=(65, 1))],
        [sg.Text('Button Colors Using PySimpleGUI.TANS')],

        [*[sg.Button('TANS[{}]\n{}'.format(j, c), button_color=(sg.GREENS[0], c), size=s10)
           for j, c in enumerate(sg.TANS)]],
        [sg.Text('_' * 100, size=(65, 1))],
        [sg.Text('Button Colors Using PySimpleGUI.YELLOWS')],

        [*[sg.Button('YELLOWS[{}]\n{}'.format(j, c), button_color=('black', c), size=s10)
           for j, c in enumerate(sg.YELLOWS)]],

        [sg.Text('_' * 100, size=(65, 1))],
        [sg.Button('Click ME!')]
    ], default_element_size=(30, 2))

    event, values = window.read()
    window.close()


if __name__ == '__main__':
    main()
