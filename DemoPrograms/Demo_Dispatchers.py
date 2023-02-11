"""
    Demo Dispatchers

    Alternative to if/else event processing

    Adapted from "The Official Python GUI Programming with PySimpleGUI Course"

    Most PySimpleGUI demos follow the simple if-else event processing, but there are
    other ways to process or dispatch events.

    Event Dispatchers:
        * If-Else
        * Dictionaries
        * Functions as keys
        * Lambda as key (callable like functions are)

    The handlers in this demo are all functions that are called once the event is detected

    The dispatch dictionary maps from an event to a function.  It's more compact than a series
    of if/else statements if you have a lot of different events and are handling events in functions

    Keep it SIMPLE.  Add complexity as you need it.   If it is clearer to do the event processing in the
    event loop rather than functions, then do it in the event loop.

    http://www.PySimpleGUI.org
    Copyright 2021, 2022, 2023 PySimpleGUI
"""

import PySimpleGUI as sg

SYMBOL_X = '❎'
SYMBOL_CHECK = '✅'


##   ##   ##   #    # ####   #      ###### #####   ####
##   ##  #  #  ##   #  #  #  #      #      #    # #    #
##   ## #    # # #  #  #   # #      #      #    # #
####### ###### #  # #  #   # #      ####   #####   ####
##   ## #    # #   ##  #   # #      #      #  #        #
##   ## #    # #    #  #  #  #      #      #   #  #    #
##   ## #    # #    # ####   ###### ###### #    #  ####

def do_go(window):
    window['-STATUS-'].update(SYMBOL_CHECK, text_color='pink')

def do_stop(window):
    window['-STATUS-'].update(SYMBOL_CHECK, text_color='pink')

def do_tuple(window):
    window['-STATUS-'].update(SYMBOL_CHECK, text_color='pink')

def do_other(window):
    window['-STATUS-'].update(SYMBOL_CHECK, text_color='yellow')

def do_simple(window):
    window['-STATUS-'].update(SYMBOL_CHECK, text_color='yellow')

def do_not_found(window):
    window['-STATUS-'].update(SYMBOL_X, text_color='red')


#    #   ##   ### #    #
##  ##  #  #   #  ##   #
# ## # #    #  #  # #  #
# ## # ######  #  #  # #
#    # #    #  #  #   ##
#    # #    #  #  #    #
#    # #    # ### #    #

def main():
    # --------- A Dispatch Dictionary -------
    dispatch_dict = {'Go':do_go, 'Stop':do_stop, (1,2):do_tuple}

    # --------- Define layout and create Window -------

    layout = [[sg.Text('Dispatching Approaches')],
              [sg.Text('Status:'), sg.Text(size=(3, 1), key='-STATUS-')],
              [sg.Text(size=(50, 1), key='-OUT-')],
              [sg.Button('Simple'), sg.Button('Go'), sg.Button('Stop'), sg.Button('Other', key=do_other),
               sg.Button('Tuple', key=(1,2)), sg.Button('Lambda', key= lambda window: do_other(window)), sg.Button('Bad')]]

    window = sg.Window('Dispatchers', layout, font='Default 16', keep_on_top=True)

    # --------- Event Loop -------
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:      # Test for window closed (always do this one)
            break

        window['-OUT-'].update(f'Event = {event}')

        # --------- Dispatching of events ---------
        # Event processing.... a minimal if-else to show 3 dispatchers
        if event == 'Simple':           # Dispatch using direct string compare
            do_simple(window)
        elif callable(event):           # Dispatch when event is a function
            event(window)
        elif event in dispatch_dict:    # Dispatch using a dispatch dictionary
            func = dispatch_dict.get(event)
            func(window)
        else:                           # None of the above
            do_not_found(window)

    # --------- After event loop ---------
    window.close()


if __name__ == '__main__':
    main()