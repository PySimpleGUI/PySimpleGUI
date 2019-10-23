import PySimpleGUI as sg

'''
    Event Callback Simulation
    
    This design pattern simulates callbacks for events.  
    This is NOT the "normal" way things work in PySimpleGUI and is an architecture that is actively discouraged
    Unlike tkinter, Qt, etc, PySimpleGUI does not utilize callback
    functions as a mechanism for communicating when button presses or other events happen.
    BUT, should you want to quickly convert some existing code that does use callback functions, then this
    is one way to do a "quick and dirty" port to PySimpleGUI.
'''

# The callback functions
# These callbacks all display a message in a non-blocking way and immediately return


def button1(event, values):
    sg.popup_quick_message('Button 1 callback',
                           background_color='red',
                           text_color='white')


def button2(event, values):
    sg.popup_quick_message('Button 2 callback',
                           background_color='green',
                           text_color='white')


def catch_all(event, values):
    sg.popup_quick_message(f'An unplanned event = "{event}" happend',
                           background_color='blue',
                           text_color='white', auto_close_duration=6)


# Lookup dictionary that maps event to function to call. In this case, only 2 event have defined callbacks
func_dict = {'1': button1, '2': button2}

# Layout the design of the GUI
layout = [[sg.Text('Please click a button')],
          [sg.Button('1'), sg.Button('2'), sg.Button('Not defined', key='-MY-KEY-'), sg.Quit()]]

# Show the Window to the user
window = sg.Window('Button callback example', layout)

# Event loop. Read buttons, make callbacks
while True:
    # Read the Window
    event, values = window.read()
    # Lookup event in function dictionary and call the function, passing in the event and values variables
    try:
        func_dict[event](event, values)   # Call function with event and values
    except:
        catch_all(event, values)
    # See if should close the window
    if event in ('Quit', None):         # normally this is done IMMEDIATELY after the read
        break

window.close()

# All done!
sg.popup_auto_close('Done... this window auto closes')
