import PySimpleGUI as sg

"""
    Columns with a hard coded size that can have elements justified within it.
    
    The Column element can have the size set to a fixed size, but when doing so, PySimpleGUI has
        a limitation that the contents can't be justified using the normal element_justification parameter.
        
    What to do?
    
    The Sizer Element to the rescue.
    
    PySimpleGUI likes to have layouts that size themselves rather than hard coded using a size parameter. The
    Sizer Element enables you to create columns with fixed size by making the contents of your column a fixed size.
    It is an invisible "padding" type of element.  It has a width and a height parameter.


    Copyright 2021 PySimpleGUI
"""


'''
M#"""""""'M                    dP                         
##  mmmm. `M                   88                         
#'        .M 88d888b. .d8888b. 88  .dP  .d8888b. 88d888b. 
M#  MMMb.'YM 88'  `88 88'  `88 88888"   88ooood8 88'  `88 
M#  MMMM'  M 88       88.  .88 88  `8b. 88.  ... 88    88 
M#       .;M dP       `88888P' dP   `YP `88888P' dP    dP 
M#########M
'''


# Let's say this is your layout and you want to center it in a 500 x 300 pixel Column Element.
col_interior = [[sg.Text('My Window')],
              [sg.In()],
              [sg.In()],
              [sg.Button('Go'), sg.Button('Exit'), sg.Cancel(), sg.Ok()]]

# Intuition would be to write it as this:
layout = [[sg.Text('This layout is broken.  The size of the Column is correct, but the elements are not justified')],
          [sg.Column(col_interior, element_justification='c', size=(500, 300), background_color='red')]]

# But when you run it, you'll see that your interior is not centered.

window = sg.Window('Window Title', layout)

window.read(close=True)


'''
M""MMM""MMM""M                   dP                
M  MMM  MMM  M                   88                
M  MMP  MMP  M .d8888b. 88d888b. 88  .dP  .d8888b. 
M  MM'  MM' .M 88'  `88 88'  `88 88888"   Y8ooooo. 
M  `' . '' .MM 88.  .88 88       88  `8b.       88 
M    .d  .dMMM `88888P' dP       dP   `YP `88888P' 
MMMMMMMMMMMMMM
'''

def ColumnFixedSize(layout, size=(None, None), *args, **kwargs):
    # An addition column is needed to wrap the column with the Sizers because the colors will not be set on the space the sizers take
    return sg.Column([[sg.Column([[sg.Sizer(0,size[1]-1), sg.Column([[sg.Sizer(size[0]-2,0)]] + layout, *args, **kwargs, pad=(0,0))]], *args, **kwargs)]],pad=(0,0))

col_interior = [[sg.Text('My Window')],
                [sg.In()],
                [sg.In()],
                [sg.Button('Go'), sg.Button('Exit'), sg.Cancel(), sg.Ok()]]


layout = [[sg.Text('Below is a column that is 500 x 300')],
          [sg.Text('With the interior centered')],
          [ColumnFixedSize(col_interior, size=(500, 300),  background_color='red', element_justification='c', vertical_alignment='t')]]

window = sg.Window('Window Title', layout)

window.read(close=True)

