#!/usr/bin/env python
import sys
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg
from time import sleep


"""
    Demonstration of simple and multiple OneLineProgressMeter's as well as the Progress Meter Element
    
    There are 4 demos
    1. Manually updated progress bar
    2. Custom progress bar built into your window, updated in a loop
    3. OneLineProgressMeters, nested meters showing how 2 can be run at the same time.
    4. An "iterable" style progress meter - a wrapper for OneLineProgressMeters
    
    If the software determined that a meter should be cancelled early, 
        calling OneLineProgresMeterCancel(key) will cancel the meter with the matching key
"""



"""
    The simple case is that you want to add a single meter to your code.  The one-line solution.
    This demo function shows 3 different OneLineProgressMeter tests
        1. A horizontal with red and white bar colors
        2. A vertical bar with default colors
        3. A test showing 2 running at the same time 
"""

def demo_one_line_progress_meter():
    # Display a progress meter. Allow user to break out of loop using cancel button
    for i in range(10000):
        if not sg.OneLineProgressMeter('My 1-line progress meter', i+1, 10000, 'meter key','MY MESSAGE1', 'MY MESSAGE 2', orientation='h', bar_color=('white', 'red')):
            print('Hit the break')
            break
    for i in range(10000):
        if not sg.OneLineProgressMeter('My 1-line progress meter', i+1, 10000, 'meter key', 'MY MESSAGE1', 'MY MESSAGE 2',orientation='v' ):
            print('Hit the break')
            break

    layout = [
                [sg.T('One-Line Progress Meter Demo', font=('Any 18'))],
                [sg.T('Outer Loop Count', size=(15,1), justification='r'), sg.In(default_text='100', size=(5,1), key='CountOuter', do_not_clear=True),
                 sg.T('Delay'), sg.In(default_text='10', key='TimeOuter', size=(5,1), do_not_clear=True), sg.T('ms')],
                [sg.T('Inner Loop Count', size=(15,1), justification='r'), sg.In(default_text='100', size=(5,1), key='CountInner', do_not_clear=True) ,
                 sg.T('Delay'), sg.In(default_text='10', key='TimeInner', size=(5,1), do_not_clear=True), sg.T('ms')],
                [sg.Button('Show', pad=((0,0), 3), bind_return_key=True), sg.T('me the meters!')]
              ]

    window = sg.Window('One-Line Progress Meter Demo').Layout(layout)

    while True:
        event, values = window.Read()
        if event is None:
            break
        if event == 'Show':
            max_outer = int(values['CountOuter'])
            max_inner = int(values['CountInner'])
            delay_inner = int(values['TimeInner'])
            delay_outer = int(values['TimeOuter'])
            for i in range(max_outer):
                if not sg.OneLineProgressMeter('Outer Loop', i+1, max_outer, 'outer'):
                    break
                sleep(delay_outer/1000)
                for j in range(max_inner):
                    if not sg.OneLineProgressMeter('Inner Loop', j+1, max_inner, 'inner'):
                        break
                    sleep(delay_inner/1000)


'''
    Manually Updated Test
    Here is an example for when you want to "sprinkle" progress bar updates in multiple
    places within your source code and you're not running an event loop.
    Note that UpdateBar is special compared to other Update methods. It also refreshes
    the containing window and checks for window closure events
    The sleep calls are here only for demonstration purposes.  You should NOT be adding
    these kinds of sleeps to a GUI based program normally.
'''

def manually_updated_meter_test():
    # layout the form
    layout = [[sg.Text('This meter is manually updated 4 times')],
              [sg.ProgressBar(max_value=10, orientation='h', size=(20,20), key='progress')]]

    # create the form`
    window = sg.Window('Custom Progress Meter', layout).Finalize()  # must finalize since not running an event loop

    progress_bar = window.FindElement('progress')                   # Get the element to make updating easier

    # -------------------- Your Program Code --------------------
    # Spot #1 to indicate progress
    progress_bar.UpdateBar(1)         # show 10% complete
    sleep(2)

    # more of your code.... perhaps pages and pages of code.
    # Spot #2 to indicate progress
    progress_bar.UpdateBar(2)         # show 20% complete
    sleep(2)

    # more of your code.... perhaps pages and pages of code.
    # Spot #3 to indicate progress
    progress_bar.UpdateBar(6)         # show 60% complete
    sleep(2)

    # more of your code.... perhaps pages and pages of code.
    # Spot #4 to indicate progress
    progress_bar.UpdateBar(9)         # show 90% complete
    sleep(2)
    window.Close()


'''
    This function shows how to create a custom window with a custom progress bar and then
    how to update the bar to indicate progress is being made
'''

def custom_meter_example():
    # layout the form
    layout = [[sg.Text('A typical custom progress meter')],
              [sg.ProgressBar(1, orientation='h', size=(20,20), key='progress')],
              [sg.Cancel()]]

    # create the form`
    window = sg.Window('Custom Progress Meter').Layout(layout)
    progress_bar = window.FindElement('progress')
    # loop that would normally do something useful
    for i in range(10000):
        # check to see if the cancel button was clicked and exit loop if clicked
        event, values = window.Read(timeout=0)
        if event == 'Cancel' or event == None:
            break
        # update bar with loop value +1 so that bar eventually reaches the maximum
        progress_bar.UpdateBar(i+1, 10000)
    # done with loop... need to destroy the window as it's still open
    window.Close()


'''
    A Wrapper for OneLineProgressMeter that combines your iterable with a progress meter into a single interface.  Two functions are provided  
    progess_bar - The basic wrapper
    progress_bar_range - A "convienence function" if you wanted to specify like a range
'''


def progress_bar(key, iterable, *args, title='', **kwargs):
    """
    Takes your iterable and adds a progress meter onto it
    :param key: Progress Meter key
    :param iterable: your iterable
    :param args: To be shown in one line progress meter
    :param title: Title shown in meter window
    :param kwargs: Other arguments to pass to OneLineProgressMeter
    :return:
    """
    sg.OneLineProgressMeter(title, 0, len(iterable), key, *args, **kwargs)
    for i, val in enumerate(iterable):
        yield val
        if not sg.OneLineProgressMeter(title, i+1, len(iterable), key, *args, **kwargs):
            break


def progress_bar_range(key, start, stop=None, step=1, *args, **kwargs):
    """
    Acts like the range() function but with a progress meter built-into it
    :param key: progess meter's key
    :param start: low end of the range
    :param stop: Uppder end of range
    :param step:
    :param args:
    :param kwargs:
    :return:
    """
    return progress_bar(key, range(start, stop, step), *args, **kwargs)


# -------------------- Demo Usage --------------------
def demo_iterable_progress_bar():
    my_list = list(range(1000))  # start with a list of 100 integers as the user's list

    # first form takes an iterable and a key and will return a value from your iterable
    # and bump the progress meter at the same time
    for value in progress_bar('bar1', my_list, ):
        # do something useful with value, a value from your list.
        print(value)

    # Since the progress_bar is an iterator, you can use it within a list comprehension
    my_list = [x for x in progress_bar('bar1', my_list)]



demo_iterable_progress_bar()
manually_updated_meter_test()
custom_meter_example()
demo_one_line_progress_meter()