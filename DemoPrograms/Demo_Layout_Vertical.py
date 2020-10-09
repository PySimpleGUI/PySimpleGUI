import PySimpleGUI as sg

"""
    Demo of using the vertical layout parameters and layout helper functions.
    Three methods of vertical alignment are shown:
    1. Using Column element to align a single element
    2. Using vtop layout helper function to align a single element
    3. Using vtop layout helper function to align an entire row

    There is also a funciton provided that will convert an entire layout into 
    a top aligned layout.
    
    Copyright 2020 PySimpleGUI.org    
"""

def top_align_layout(layout):
    """
    Given a layout, return a layout with all rows vertically adjusted to the top

    :param layout: List[List[sg.Element]] The layout to justify
    :return: List[List[sg.Element]]  The new layout that is all top justified
    """
    new_layout = []
    for row in layout:
        new_layout.append(sg.vtop(row))
    return new_layout


def main():
    # -------------------- Example 1 - No alignment --------------------
    layout = [ [sg.T('This layout uses no vertical alignment. The default is "center"')],
               [sg.Text('On row 1'), sg.Listbox(list(range(10)), size=(5,4)), sg.Text('On row 1')],
               [sg.Button('OK')]  ]

    sg.Window('Window Title', layout).read(close=True)

    # -------------------- Example 2 - Top aligned Text element using Column --------------------
    layout = [ [sg.T('This uses a Column Element to align 1 element')],
               [sg.Col([[sg.Text('On row 1')]], vertical_alignment='top', pad=(0,0)), sg.Listbox(list(range(10)), size=(5,4)), sg.Text('On row 1')],
               [sg.Button('OK')]  ]

    sg.Window('Window Title', layout).read(close=True)


    # -------------------- Example 3 - Top aligned Text element using Column --------------------
    layout = [ [sg.T('This layout uses the "vtop" layout helper function on 1 element')],
               [sg.vtop(sg.Text('On row 1')), sg.Listbox(list(range(10)), size=(5,4)), sg.Text('On row 1')],
               [sg.Button('OK')]  ]

    sg.Window('Window Title', layout).read(close=True)

    # -------------------- Example 4 - Top align an entire row --------------------
    # Note that the vtop function takes a row as input and returns a row.  DO NOT place [ ] around vtop
    # because it is a row already.
    layout = [ [sg.T('This layout uses the "vtop" layout helper function on 1 row')],
               sg.vtop([sg.Text('On row 1'), sg.Listbox(list(range(10)), size=(5,4)), sg.Text('On row 1')]),
               [sg.Button('OK')]  ]

    sg.Window('Window Title', layout).read(close=True)


    # -------------------- Example 5 - Use function to align all rows in layout --------------------
    layout = [ [sg.T('This layout has all rows top aligned using function')],
               [sg.Text('On row 1'), sg.Listbox(list(range(10)), size=(5,4)), sg.Text('On row 1')],
               [sg.Text('On row 2'), sg.Listbox(list(range(10)), size=(5,4)), sg.Text('On row 2')],
               [sg.Button('OK')]  ]

    layout = top_align_layout(layout)       # pass in a layout, get a loyout back

    sg.Window('Window Title', layout).read(close=True)



if __name__ == '__main__':
    main()