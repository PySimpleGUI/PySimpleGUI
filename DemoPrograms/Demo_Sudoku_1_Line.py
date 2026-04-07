import PySimpleGUI as sg

"""
    Demo 1-line Sudoku Board

    A silly display of what 1 line of PySimpleGUI is capable of producing by
    utilizing the power of Python.  The power isn't a PySimpleGUI trick.
    The power is Python List Comprehensions and using them in your layout.

    Copyright 2018-2026 PySimpleGUI. All rights reserved.
    
    
"""

sg.Window('Sudoku', [[sg.Frame('', [[sg.Input(justification='r', size=(3,1))
                                    for col in range(3)]
                                    for row in range(3)])
                                    for frame_col in range(3)]
                                    for frame_row in range(3)],
                                    use_custom_titlebar=True).read()
