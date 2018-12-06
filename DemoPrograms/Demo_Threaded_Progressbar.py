#! /usr/bin/env python
#  -*- coding: utf-8 -*-

"""
Quick and dirty threading example for PySimpleGUI progress bar executing class methods
Written in 2018 by Orsiris de Jong, www.netpower.fr, works with Python 3+
"""

from threading import Thread
from concurrent.futures import Future
from time import time, sleep
import PySimpleGUI as sg

# Helper functions for threading class functions with return values using future from https://stackoverflow.com/a/19846691/2635443
def call_with_future(fn, future, args, kwargs):
    try:
        result = fn(*args, **kwargs)
        future.set_result(result)
    except Exception as exc:
        future.set_exception(exc)

def threaded(fn):
    def wrapper(*args, **kwargs):
        future = Future()
        Thread(target=call_with_future, args=(fn, future, args, kwargs)).start()
        return future
    return wrapper

# Some fancy class which functions should be threaded or not using decorator
class SomeFancyClass:
    def __init__(self):
        self.somevar = 'Some initial class variable'

    # Adding this decoroator to thread the function below
    @threaded
    def func_to_be_threaded(self):
        print(self.somevar)
        sleep(7)
        self.somevar = 'New value'
        return('Return from func_to_be_threaded is ' + self.somevar)


    @threaded
    def another_thread_function(self):
        print(self.somevar)
        sleep(3)
        return ('Return from another_thread_function is ' + self.somevar)

    def non_threaded_function(self):
        print('waiting')
        sleep(5)
        print('finished waiting')

# The main progress bar method
def progressbar(myClass):
    maxwait = 10  # Wait for 10 seconds max with the progress bar before asking to cancel
    progress = 0
    startTime = 0
    currentTime = 0

    function_one = None
    function_two = None
    function_one_done = False
    function_two_done = False

    # layout of the progress bar window
    layout = [[sg.Text('Launching threads')],
              [sg.ProgressBar(100, orientation='h', size=(20, 20), key='progressbar')],
              [sg.Cancel()]]

    # create the progress bar
    window = sg.Window('Init', text_justification='center').Layout(layout)

    startTime = time()

    while True:
        event, values = window.Read(timeout=300)
        if event == 'Cancel' or event is None:
            if function_one != None:
                function_one.cancel()
            if function_two != None:
                function_two.cancel()
            window.Close()
            exit()

        if function_one == None:
            # Launch first threaded function
            function_one = myClass.func_to_be_threaded()

        if function_two == None:
            # Launch second threaded function
            function_two = myClass.another_thread_function()

        print('function_one is done: ' + str(function_one.done()))
        print('function_two is done: ' + str(function_two.done()))

        if function_one.done() == True and function_one_done == False:
            function_one_done = True
            print(function_one.result())
            progress += 70

        if function_two.done() == True and function_two_done == False:
            function_two_done = True
            print(function_two.result())
            progress += 30

        window.FindElement('progressbar').UpdateBar(progress)

        currentTime = time()
        if (currentTime - startTime) > maxwait:
            action = sg.Popup('Seems that it takes too long, shall we continue the program',custom_text=('No', 'Yes'))
            if action == 'No':
                function_one.cancel()
                function_two.cancel()
                break
            elif action == 'Yes':
                startTime = time() # Lets give another 10 seconds or check if functions must be stopped
                """
                TODO: We could relaunch the functions with
                function_one.cancel()
                if function_one.cancelled():
                    function_one = myClass.func_to_be_threaded()
                """

        if progress >= 100:
            sg.Popup('Execution finished')
            break
    window.Close()

def main():
    myClass = SomeFancyClass()
    progressbar(myClass)


if __name__ == '__main__':
    main()    
