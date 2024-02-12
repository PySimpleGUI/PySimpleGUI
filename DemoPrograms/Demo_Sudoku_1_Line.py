import PySimpleGUI as sg

"""
    Demo 1-line Sudoku Board

    A silly display of what 1 line of PySimpleGUI is capable of producing by
    utilizing the power of Python.  The power isn't a PySimpleGUI trick.
    The power is Python List Comprehensions and using them in your layout.

    Copyright 2021-2023 PySimpleSoft, Inc. and/or its licensors. All rights reserved.
    
    Redistribution, modification, or any other use of PySimpleGUI or any portion thereof is subject to the terms of the PySimpleGUI License Agreement available at https://eula.pysimplegui.com.
    
    You may not redistribute, modify or otherwise use PySimpleGUI or its contents except pursuant to the PySimpleGUI License Agreement.
"""

sg.Window('Sudoku', [[sg.Frame('', [[sg.Input(justification='r', size=(3,1))
                                    for col in range(3)]
                                    for row in range(3)])
                                    for frame_col in range(3)]
                                    for frame_row in range(3)],
                                    use_custom_titlebar=True).read()
