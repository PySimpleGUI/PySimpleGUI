import PySimpleGUI as sg
import time
import psutil

"""
    PSUTIL Desktop Widget
    Creates a floating CPU utilization window that is always on top of other windows
    You move it by grabbing anywhere on the window
    Good example of how to do a non-blocking, polling program using PySimpleGUI
    Use the spinner to adjust the number of seconds between readings of the CPU utilizaiton

    NOTE - you will get a warning message printed when you exit using exit button.
    It will look something like:
            invalid command name "1616802625480StopMove"
"""

# ----------------  Create Form  ----------------
sg.ChangeLookAndFeel('Black')
form_rows = [[sg.Text('')],
             [sg.Text('', size=(8, 2), font=('Helvetica', 20), justification='center', key='text')],
             [sg.Exit(button_color=('white', 'firebrick4'), pad=((15,0), 0)), sg.Spin([x+1 for x in range(10)], 1, key='spin')]]
# Layout the rows of the form and perform a read. Indicate the form is non-blocking!
form = sg.FlexForm('Running Timer', no_titlebar=True, auto_size_buttons=False, keep_on_top=True, grab_anywhere=True)
form.Layout(form_rows)

# ----------------  main loop  ----------------
while (True):
    # --------- Read and update window --------
    button, values = form.ReadNonBlocking()

    # --------- Do Button Operations --------
    if values is None or button == 'Exit':
        break
    try:
        interval = int(values['spin'])
    except:
        interval = 1

    cpu_percent = psutil.cpu_percent(interval=interval)

    # --------- Display timer in window --------

    form.FindElement('text').Update(f'CPU {cpu_percent:02.0f}%')


# --------- After loop --------

# Broke out of main loop. Close the window.
form.CloseNonBlockingForm()
