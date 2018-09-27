#!/usr/bin/env python
import sys
if sys.version_info[0] < 3:
    import PySimpleGUI27 as sg
else:
    import PySimpleGUI as sg

# Robotics design pattern
# Uses Realtime Buttons to simulate the controls for a robot
# Rather than sending a single click when a button is clicked, Realtime Buttons
#       send button presses continuously while the button is pressed down.
# Two examples, one using fancy graphics, one plain.

def RemoteControlExample():
    # Make a form, but don't use context manager
    sg.SetOptions(element_padding=(0,0))
    back ='#eeeeee'
    image_forward = 'ButtonGraphics/RobotForward.png'
    image_backward = 'ButtonGraphics/RobotBack.png'
    image_left = 'ButtonGraphics/RobotLeft.png'
    image_right = 'ButtonGraphics/RobotRight.png'

    sg.SetOptions(border_width=0, button_color=('black', back), background_color=back, element_background_color=back, text_element_background_color=back)

    layout = [[sg.Text('Robotics Remote Control')],
                 [sg.T('', justification='center', size=(19,1), key='status')],
                 [ sg.RealtimeButton('Forward', image_filename=image_forward, pad=((50,0),0))],
                 [ sg.RealtimeButton('Left', image_filename=image_left), sg.RealtimeButton('Right', image_filename=image_right, pad=((50,0), 0))],
                 [ sg.RealtimeButton('Reverse', image_filename=image_backward, pad=((50,0),0))],
                 [sg.T('')],
                 [sg.Quit(button_color=('black', 'orange'))]]

    window = sg.Window('Robotics Remote Control', auto_size_text=True, grab_anywhere=False).Layout(layout)

    #
    # Some place later in your code...
    # You need to perform a ReadNonBlocking on your form every now and then or
    # else it won't refresh.
    #
    # your program's main loop
    while (True):
        # This is the code that reads and updates your window
        button, values = window.ReadNonBlocking()
        if button is not None:
            window.FindElement('status').Update(button)
        else:
            window.FindElement('status').Update('')
        # if user clicked quit button OR closed the form using the X, then break out of loop
        if button == 'Quit' or values is None:
            break

    window.CloseNonBlocking()


def RemoteControlExample_NoGraphics():
    # Make a form, but don't use context manager

    layout = [[sg.Text('Robotics Remote Control', justification='center')],
                 [sg.T('', justification='center', size=(19,1), key='status')],
                 [sg.T(' '*8), sg.RealtimeButton('Forward')],
                 [ sg.RealtimeButton('Left'), sg.T('              '), sg.RealtimeButton('Right')],
                 [sg.T(' '*8), sg.RealtimeButton('Reverse')],
                 [sg.T('')],
                 [sg.Quit(button_color=('black', 'orange'))]]
    # Display form to user
    window = sg.Window('Robotics Remote Control', auto_size_text=True, grab_anywhere=False).Layout(layout)

    #
    # Some place later in your code...
    # You need to perform a ReadNonBlocking on your form every now and then or
    # else it won't refresh.
    #
    # your program's main loop
    while (True):
        # This is the code that reads and updates your window
        button, values = window.ReadNonBlocking()
        if button is not None:
            window.FindElement('status').Update(button)
        else:
            window.FindElement('status').Update('')
        # if user clicked quit button OR closed the form using the X, then break out of loop
        if button == 'Quit' or values is None:
            break

    window.CloseNonBlocking()




# ------------------------------------- main -------------------------------------
def main():
    RemoteControlExample_NoGraphics()
    # Uncomment to get the fancy graphics version.  Be sure and download the button images!
    RemoteControlExample()
    # sg.Popup('End of non-blocking demonstration')

if __name__ == '__main__':

    main()
