#!/usr/bin/env python
import sys
import sys
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg
import psutil
import time
from threading import Thread
import operator


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

# globale used to communicate with thread.. yea yea... it's working fine
g_interval = 1
g_cpu_percent = 0
g_procs = None
g_exit = False

def CPU_thread(args):
    global g_interval, g_cpu_percent, g_procs, g_exit

    while not g_exit:
        try:
            g_cpu_percent = psutil.cpu_percent(interval=g_interval)
            g_procs = psutil.process_iter()
        except:
            pass


def main():
    global g_interval,  g_procs, g_exit

    # ----------------  Create Form  ----------------
    sg.ChangeLookAndFeel('Black')
    layout = [[sg.Text('', size=(8,1), font=('Helvetica', 20),text_color=sg.YELLOWS[0], justification='center', key='text')],
                 [sg.Text('', size=(30, 8), font=('Courier New', 12),text_color='white', justification='left', key='processes')],
                 [sg.Exit(button_color=('white', 'firebrick4'), pad=((15,0), 0)), sg.Spin([x+1 for x in range(10)], 1, key='spin')],]

    window = sg.Window('CPU Utilization', no_titlebar=True, auto_size_buttons=False,
                       keep_on_top=True, grab_anywhere=True).Layout(layout)

    # start cpu measurement thread
    thread = Thread(target=CPU_thread,args=(None,))
    thread.start()
    # ----------------  main loop  ----------------
    while (True):
        # --------- Read and update window --------
        button, values = window.ReadNonBlocking()

        # --------- Do Button Operations --------
        if values is None or button == 'Exit':
            break
        try:
            g_interval = int(values['spin'])
        except:
            g_interval = 1

        # cpu_percent = psutil.cpu_percent(interval=interval)       # if don't wan to use a task
        cpu_percent = g_cpu_percent

        # let the GUI run ever 700ms regardless of CPU polling time. makes window be more responsive
        time.sleep(.7)

        display_string = ''
        if g_procs:
            # --------- Create list of top % CPU porocesses --------
            try:
                top = {proc.name() : proc.cpu_percent() for proc in g_procs}
            except: pass


            top_sorted = sorted(top.items(), key=operator.itemgetter(1), reverse=True)
            if top_sorted:
                top_sorted.pop(0)
            display_string = ''
            for proc, cpu in top_sorted:
                display_string += '{:2.2f} {}\n'.format(cpu/10, proc)


        # --------- Display timer in window --------
        window.FindElement('text').Update('CPU {}'.format(cpu_percent))
        window.FindElement('processes').Update(display_string)

    # Broke out of main loop. Close the window.
    window.CloseNonBlocking()
    g_exit = True
    thread.join()

if __name__ == "__main__":
    main()