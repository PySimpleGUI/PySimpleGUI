#!/usr/bin/env python
import PySimpleGUI as sg
import time

'''
    Window that doesn't block
    good for applications with an loop that polls hardware
'''

def StatusOutputExample():
    # Create a text element that will be updated with status information on the GUI itself
    # Create the rows
    layout = [[sg.Text('Non-blocking GUI with updates')],
              [sg.Text('', size=(8, 2), font=('Helvetica', 20),
                    justification='center', key='output')],
              [sg.Button('LED On'), sg.Button('LED Off'), sg.Button('Quit')]]
    # Layout the rows of the Window and perform a read. Indicate the Window is non-blocking!
    window = sg.Window('Running Timer', layout, auto_size_text=True)

    #
    # Some place later in your code...
    # You need to perform a Read on your window every now and then or
    # else it won't refresh.
    #
    # your program's main loop
    i = 0
    while True:
        # This is the code that reads and updates your window
        event, values = window.read(timeout=10)
        window['output'].update('{:02d}:{:02d}.{:02d}'.format(
            (i // 100) // 60, (i // 100) % 60, i % 100))
        if event in ('Quit', None):
            break
        if event == 'LED On':
            print('Turning on the LED')
        elif event == 'LED Off':
            print('Turning off the LED')

        i += 1
        # Your code begins here

    # Broke out of main loop. Close the window.
    window.close()


def RemoteControlExample():

    layout = [[sg.Text('Robotics Remote Control')],
              [sg.Text(' '*10), sg.RealtimeButton('Forward')],
              [sg.RealtimeButton('Left'), sg.Text(' '*15),
               sg.RealtimeButton('Right')],
              [sg.Text(' '*10), sg.RealtimeButton('Reverse')],
              [sg.Text('')],
              [sg.Quit(button_color=('black', 'orange'))]
              ]

    window = sg.Window('Robotics Remote Control', layout,
                       auto_size_text=True, finalize=True)

    #
    # Some place later in your code...
    # You need to perform a ReadNonBlocking on your window every now and then or
    # else it won't refresh.
    #
    # your program's main loop
    while True:
        # This is the code that reads and updates your window
        event, values = window.read(timeout=0, timeout_key='timeout')
        if event != 'timeout':
            print(event)
        if event in ('Quit', None):
            break

    window.close()


def main():
    RemoteControlExample()
    StatusOutputExample()
    sg.popup('End of non-blocking demonstration')


if __name__ == '__main__':

    main()
