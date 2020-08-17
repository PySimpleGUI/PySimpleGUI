import PySimpleGUI as sg

"""
    Demo Status Bar
    
    This demo shows you how to create your statusbar in a way that will keep it at the bottom of
    a resizeable window.  The key is the correct setting of the Expand settings for both the 
    StatusBar (done for you) and for a line above it that will keep it pushed to the bottom of the window.
    It's possible to also "simulate" a statusbar (i.e. use a text element or something else) by also
    configuring that element with the correct expand setting (X direction = True, expand row=True)
    
    Copyright 2020 PySimpleGUI.org
"""

def main():

    layout = [  [sg.Text('StatusBar Demo', font='ANY 15')],
                [sg.Text('This window has a status bar that is at the bottom of the window')],
                [sg.Text('The key to getting your bar to stay at the bottom of the window when')],
                [sg.Text('the window is resizeed is to insert a line of text (or some other element)')],
                [sg.Text('that is configured to expand.  ')],
                [sg.Text('This is accomplished by calling the "expand" method')],
                [sg.Text('')],
                [sg.Button('Ok'), sg.B('Quit')],
                [sg.Text(key='-EXPAND-', font='ANY 1', pad=(0,0))],  # thin row (font size 1) that expands and keeps bar at the bottom
                [sg.StatusBar('This is the statusbar')]]


    window = sg.Window('Vertical Layout Example', layout, resizable=True, finalize=True)

    window['-EXPAND-'].expand(True, True, True)     # needed to make the window expand in a way that will cause status to be at the bottom

    while True:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, 'Quit'):   # if user closes window or clicks Quit
            break

if __name__ == '__main__':
    main()

