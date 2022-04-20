import PySimpleGUI as sg

"""
    Demo - Yet another example of TabGroup element

    These are simple tabs and tab groups.  This example simply shows groups within groups.
    Be careful with tabs to make sure you don't re-use a layout.  If you used a layout in one tab
        you cannot use it again in another tab.  
        
        There was an error in this demo for quite some time that makes for a great example of this error.  
        
        See how tab_layout is in both Tab elements?  That's a no-go and you'll get an error poup

        tab_group = sg.TabGroup([[sg.Tab('Tab 7', tab_layout), sg.Tab('Tab 8', tab_layout)]])

    Copyright 2022 PySimpleGUI
"""


sg.theme('GreenTan')
tab2_layout = [[sg.Text('This is inside tab 2')],
               [sg.Text('Tabs can be anywhere now!')]]

tab1_layout = [[sg.Text('Type something here and click button'), sg.Input(key='in')]]

tab3_layout = [[sg.Text('This is inside tab 3')]]
tab4_layout = [[sg.Text('This is inside tab 4')]]

tab_layout7 = [[sg.Text('This is inside of a tab')]]
tab_layout8 = [[sg.Text('This is inside of a tab')]]
tab_group = sg.TabGroup([[sg.Tab('Tab 7', tab_layout7), sg.Tab('Tab 8', tab_layout8)]])

tab5_layout = [[sg.Text('Watch this window')],
                [sg.Output(size=(40,5))]]       # generally better to use a Multline, but for super-simple examples, Output is OK
tab6_layout = [[sg.Text('This is inside tab 6')],
               [sg.Text('How about a second row of stuff in tab 6?'), tab_group]]

layout = [[sg.Text('My Window!')], [sg.Frame('A Frame', layout=
    [[sg.TabGroup([[sg.Tab('Tab 1', tab1_layout), sg.Tab('Tab 2', tab2_layout)]]), sg.TabGroup([[sg.Tab('Tab3', tab3_layout), sg.Tab('Tab 4', tab4_layout)]])]])],
    [sg.Text('This text is on a row with a column'),sg.Col(layout=[[sg.Text('In a column')],
    [sg.TabGroup([[sg.Tab('Tab 5', tab5_layout), sg.Tab('Tab 6', tab6_layout)]])],
          [sg.Button('Click me')]])],]

window = sg.Window('My window with tabs', layout, default_element_size=(12,1), finalize=True)

print('Are there enough tabs for you?')

while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED:           # always,  always give a way out!
        break

window.close()