#!/usr/bin/env python
import sys
import PySimpleGUI as sg


# Robotics design pattern
# Uses Realtime Buttons to simulate the controls for a robot
# Rather than sending a single click when a button is clicked, Realtime Buttons
#       send button presses continuously while the button is pressed down.
# Two examples, one using fancy graphics, one plain.

def RemoteControlExample():
    # Make a form, but don't use context manager
    sg.set_options(element_padding=(0,0))
    back = '#eeeeee'

    sg.set_options(border_width=0,
        button_color=('black', back),
        background_color=back,
        element_background_color=back,
        text_element_background_color=back)

    mypad = ((50,0),0)
    layout = [[sg.Text('Robotics Remote Control')],
                 [sg.Text('', justification='center', size=(19,1), key='status')],
                 [ sg.RealtimeButton('', key='Forward', pad=mypad)],
                 [ sg.RealtimeButton('', key='Left', ),
                   sg.RealtimeButton('', key='Right', pad=mypad)],
                 [ sg.RealtimeButton('', key='Reverse', pad=mypad)],
                 [sg.Text('')],
                 [sg.Quit(button_color=('black', 'orange'))]]

    window = sg.Window('Robotics Remote Control', layout, grab_anywhere=False)

    #
    # Some place later in your code...
    # You need to perform a ReadNonBlocking on your form every now and then or
    # else it won't refresh.
    #
    # your program's main loop
    while True:
        # This is the code that reads and updates your window
        event, values = window.read(timeout=0, timeout_key='timeout')
        if event is not None:
            window['status'].update(event)
        elif event != 'timeout':
            window['status'].update('')
        # if user clicked quit button OR closed the form using the X, then break out of loop
        if event == 'Quit' or values is None:
            break

    window.close()


def RemoteControlExample_NoGraphics():
    # Make a form, but don't use context manager

    layout = [[sg.Text('Robotics Remote Control', justification='center')],
                 [sg.Text('', justification='center', size=(19,1), key='status')],
                 [sg.Text(' '*8), sg.RealtimeButton('Forward')],
                 [ sg.RealtimeButton('Left'), sg.Text('              '), sg.RealtimeButton('Right')],
                 [sg.Text(' '*8), sg.RealtimeButton('Reverse')],
                 [sg.Text('')],
                 [sg.Quit(button_color=('black', 'orange'))]]
    # Display form to user
    window = sg.Window('Robotics Remote Control', layout, grab_anywhere=False)

    #
    # Some place later in your code...
    # You need to perform a Read on your form every now and then or
    # else it won't refresh.
    # Notice how the timeout is 100ms. You don't have to use a timeout = 0 for all of your hardware
    # applications.  Leave some CPU for other threads or for your GUI.  The longer you are in the GUI, the more
    # responsive the GUI itself will be  Match your timeout with your hardware's capabilities
    #
    # your program's main loop
    while True :
        # This is the code that reads and updates your window
        event, values = window.read(timeout=100, timeout_key='timeout')
        # print(event, values)
        if event != 'timeout':
            window['status'].update(event)
        else:
            window['status'].update('')
        # if user clicked quit button OR closed the form using the X, then break out of loop
        if event in (None, 'Quit'):
            break

    window.close()

# ------------------------------------- main -------------------------------------
def main():
    RemoteControlExample_NoGraphics()
    # Uncomment to get the fancy graphics version.  Be sure and download the button images!
    RemoteControlExample()
    # sg.popup('End of non-blocking demonstration')

if __name__ == '__main__':

    main()
