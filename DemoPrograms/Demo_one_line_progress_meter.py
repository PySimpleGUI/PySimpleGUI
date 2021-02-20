"""
    Demo one_line_progress_meter

    Add 1 line of code, get a very nice graphical progress meter window

    As a software engineer, it's frustrating to know that there is a better way that
    are not being shown. Adding a progress meter to your loop does not require 2 lines
    of code. It can be done with 1.

    So many of the popular progress meter packages require multiple changes to your code.
    There are 2 varieties:
        * Add 2 lines of code
            1. Add - A setup outside your loop
            2. Add - A call to a meter update function inside inside your loop
        * Modify 1, add 1
            1. Modify - Your existing for statement to use an iterator made by the meter API
            2. Add - A call to the meter update function inside your loop

    The PySimpleGUI "One Line Progress Meter" requires you to:
        * Add - A call to the meter update funciton inside your loop


    Copyright 2021 PySimpleGUI.org
"""


import PySimpleGUI as sg
import time



# --------------------------------- BEFORE ---------------------------------
# Your EXISTING code may look like this

MAX=100     # the max number of items you'll process
for i in range(MAX):
    # Do your processing stuff here (simulated with this sleep)
    time.sleep(.1)
    print(f'Your old code simply looped through {i}')


# --------------------------------- AFTER ---------------------------------
# Now let's add a PySimpleGUI one line progress meter

MAX=100     # the max number of items you'll process
for i in range(MAX):
    # Here is your line of code
    sg.one_line_progress_meter('Some test', i+1, MAX)
    time.sleep(.1)
    print(f'Your new code still simply loops through, but you also get the nifty progress window {i}')

sg.popup('Done', 'As you can see, the bar auto disappeared', 'because it reached max value')

# --------------------------------- FANCY ---------------------------------
# What about that "Cancel" button?  Let's hook it up

MAX=100     # the max number of items you'll process
for i in range(MAX):
    # This time we're checking to see if the meter stopped. If it stopped early, then it was cancelled.
    if not sg.one_line_progress_meter('A Meter You Can Cancel', i+1, MAX, 'KEY', 'Try Clicking Cancel Button') and i+1 != MAX:
        sg.popup_auto_close('Cancelling your loop...')
        break
    time.sleep(.1)
    print(f'Your new code still simply loops through, but you also get the nifty progress window {i}')

sg.popup('Done with your loop!', 'About to exit program')