import PySimpleGUI as sg
import time
import threading

"""
    Demo - Multi-threaded - Show Windows and perform other PySimpleGUI calls in what appread to be from a thread
    
    Just so that it's clear, you CANNOT make PySimpleGUI calls directly from a thread.  There is ONE exception to this
    rule.  A thread may call  window.write_event_values which enables it to communicate to a window through the window.read calls.

    The main GUI will not be visible on your screen nor on your taskbar despite running in the background.  The calls you 
    make, such as popup, or even Window.read will create windows that your user will see.
    
    The basic function that you'll use in your thread has this format:
        make_delegate_call(lambda: sg.popup('This is a popup', i, auto_close=True, auto_close_duration=2, keep_on_top=True, non_blocking=True))

    Everything after the "lambda" looks exactly like a PySimpleGUI call.
    If you want to display an entire window, then the suggestion is to put it into a function and pass the function to make_delegate_call
    
    Note - the behavior of variables may be a bit of a surprise as they are not evaluated until the mainthread processes the event.  This means
    in the example below that the counter variable being passed to the popup will not appear to be counting correctly.  This is because the
    value shown will be the value at the time the popup is DISPLAYED, not the value when the make_delegate_call was made. 
    
    Copyright 2022 PySimpleGUI
"""


# Design decision was to make the window a global.  You can just as easily pass it to your function after initizing your window
# But there becomes a problem then of wheere do you place the thread startup code.  Using this global decouples them so that
# the thread is not started in the function that makes and executes the GUI

window:sg.Window = None

# M""MMMM""M
# M. `MM' .M
# MM.    .MM .d8888b. dP    dP 88d888b.
# MMMb  dMMM 88'  `88 88    88 88'  `88
# MMMM  MMMM 88.  .88 88.  .88 88
# MMMM  MMMM `88888P' `88888P' dP
# MMMMMMMMMM
#
# M""""""""M dP                                        dP
# Mmmm  mmmM 88                                        88
# MMMM  MMMM 88d888b. 88d888b. .d8888b. .d8888b. .d888b88
# MMMM  MMMM 88'  `88 88'  `88 88ooood8 88'  `88 88'  `88
# MMMM  MMMM 88    88 88       88.  ... 88.  .88 88.  .88
# MMMM  MMMM dP    dP dP       `88888P' `88888P8 `88888P8
# MMMMMMMMMM

def the_thread():
    """
    This is code that is unique to your application.  It wants to "make calls to PySimpleGUI", but it cannot directly do so.
    Instead it will send the request to make the call to the mainthread that is running the GUI.

    :return:
    """

    # Wait for the GUI to start running
    while window is None:
        time.sleep(.2)

    for i in range(5):
        time.sleep(.2)
        make_delegate_call(lambda: sg.popup('This is a popup', i, relative_location=(0, -300), auto_close=True, auto_close_duration=2, keep_on_top=True, non_blocking=True))
        make_delegate_call(lambda: sg.popup_scrolled(__file__, sg.get_versions(), auto_close=True, auto_close_duration=1.5, non_blocking=True))

    make_delegate_call(lambda: sg.popup('One last popup before exiting...', relative_location=(-200, -200)))

    # when finished and ready to stop, tell the main GUI to exit
    window.write_event_value('-THREAD EXIT-', None)


# -------------------------------------------------------------------------------------------------------- #

# The remainder of the code is part of the overall design pattern.  You should copy this code
# and use it as the basis for creating this time of delegated PySimpleGUI calls


# M""""""'YMM                   oo
# M  mmmm. `M
# M  MMMMM  M .d8888b. .d8888b. dP .d8888b. 88d888b.
# M  MMMMM  M 88ooood8 Y8ooooo. 88 88'  `88 88'  `88
# M  MMMM' .M 88.  ...       88 88 88.  .88 88    88
# M       .MM `88888P' `88888P' dP `8888P88 dP    dP
# MMMMMMMMMMM                           .88
#                                   d8888P
# MM"""""""`YM            dP     dP
# MM  mmmmm  M            88     88
# M'        .M .d8888b. d8888P d8888P .d8888b. 88d888b. 88d888b.
# MM  MMMMMMMM 88'  `88   88     88   88ooood8 88'  `88 88'  `88
# MM  MMMMMMMM 88.  .88   88     88   88.  ... 88       88    88
# MM  MMMMMMMM `88888P8   dP     dP   `88888P' dP       dP    dP
# MMMMMMMMMMMM

def make_delegate_call(func):
    """
    Make a delegate call to PySimpleGUI.

    :param func:    A lambda expression most likely.  It's a function that will be called by the mainthread that's executing the GUI
    :return:
    """
    if window is not None:
        window.write_event_value('-THREAD DELEGATE-', func)


#                     oo
#
# 88d8b.d8b. .d8888b. dP 88d888b.
# 88'`88'`88 88'  `88 88 88'  `88
# 88  88  88 88.  .88 88 88    88
# dP  dP  dP `88888P8 dP dP    dP

def main():
    global window

    # create a window.  A key is needed so that the values dictionary will return the thread's value as a key
    layout = [[sg.Text('', k='-T-')]]

    # set the window to be both invisible and have no taskbar icon
    window = sg.Window('Invisible window', layout, no_titlebar=True, alpha_channel=0, finalize=True, font='_ 1', margins=(0,0), element_padding=(0,0))
    window.hide()

    while True:
        event, values = window.read()
        if event in ('Exit', sg.WIN_CLOSED):
            break
        # if the event is from the thread, then the value is the function that should be called
        if event == '-THREAD DELEGATE-':
            try:
                values[event]()
            except Exception as e:
                sg.popup_error_with_traceback('Error calling your function passed to GUI', event, values, e)
        elif event == '-THREAD EXIT-':
            break
    window.close()


# MP""""""`MM   dP                       dP
# M  mmmmm..M   88                       88
# M.      `YM d8888P .d8888b. 88d888b. d8888P dP    dP 88d888b.
# MMMMMMM.  M   88   88'  `88 88'  `88   88   88    88 88'  `88
# M. .MMM'  M   88   88.  .88 88         88   88.  .88 88.  .88
# Mb.     .dM   dP   `88888P8 dP         dP   `88888P' 88Y888P'
# MMMMMMMMMMM                                          88
#                                                      dP

if __name__ == '__main__':
    # first your thread will be started
    threading.Thread(target=the_thread, daemon=True).start()
    # then startup the main GUI
    main()
