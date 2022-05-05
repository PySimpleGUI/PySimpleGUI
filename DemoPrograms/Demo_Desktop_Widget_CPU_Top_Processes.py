#!/usr/bin/env python
import PySimpleGUI as sg
import psutil
import operator

"""
    PSUTIL "Top" CPU Processes - Desktop Widget
    
    Creates a floating CPU utilization window running something similar to a "top" command.

    Use the spinner to adjust the number of seconds between readings of the CPU utilizaiton
    Rather than calling the threading module this program uses the PySimpleGUI perform_long_operation method.
        The result is similar.  The function is run as a thread... the call is simply wrapped.
            
    Copyright 2022 PySimpleGUI
"""

# global used to communicate with thread.
g_interval = 1      # how often to poll for CPU usage

def CPU_thread(window:sg.Window):

    while True:
        cpu_percent = psutil.cpu_percent(interval=g_interval)
        procs = psutil.process_iter()
        window.write_event_value('-CPU UPDATE FROM THREAD-', (cpu_percent, procs))


def main():
    global g_interval

    location =  sg.user_settings_get_entry('-location-', (None, None))

    # ----------------  Create Form  ----------------
    sg.theme('Black')

    layout = [[sg.Text(font=('Helvetica', 20), text_color=sg.YELLOWS[0], key='-CPU PERCENT-')],
              [sg.Text(size=(35, 12), font=('Courier New', 12), key='-PROCESSES-')],     # size will determine how many processes shown
              [sg.Text('Update every '), sg.Spin([x+1 for x in range(10)], 3, key='-SPIN-'), sg.T('seconds')]]

    window = sg.Window('Top CPU Processes', layout, no_titlebar=True, keep_on_top=True,location=location, use_default_focus=False, alpha_channel=.8, grab_anywhere=True, right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_VER_EXIT, enable_close_attempted_event=True)

    # start cpu measurement thread
    # using the PySimpleGUI call to start and manage the thread
    window.start_thread(lambda: CPU_thread(window), '-THREAD FINISHED-')
    g_interval = 1
    # Unusual construct of a Try around entire event loop... something is crashing, we need to find out what...
    try:
       # ----------------  main loop  ----------------
        while True:
            # --------- Read and update window --------
            event, values = window.read()
            # print(event, values)
            # --------- Do Button Operations --------
            if event in (sg.WIN_CLOSE_ATTEMPTED_EVENT, 'Exit'):
                sg.user_settings_set_entry('-location-', window.current_location())     # save window location before exiting
                break
            if event == 'Edit Me':
                sp = sg.execute_editor(__file__)
            elif event == 'Version':
                sg.popup_scrolled(__file__, sg.get_versions(), keep_on_top=True, location=window.current_location())
            elif event == '-CPU UPDATE FROM THREAD-':                   # indicates data from the thread has arrived
                cpu_percent, procs = values[event]                      # the thread sends a tuple
                if procs:
                    # --------- Create dictionary of top % CPU processes.  Format is name:cpu_percent --------
                    top = {}
                    for proc in procs:
                        try:
                            top[proc.name()] = proc.cpu_percent()
                        except Exception as e:
                            pass    # it's OK to get an exception here because processes come and go... one may have gone...
                            # sg.Print('*** GOT Exception looping through procs ***', c='white on red', font='_ 18')
                            # sg.Print('Exception = ', e, 'procs=', procs, 'proc', proc)

                    top_sorted = sorted(top.items(), key=operator.itemgetter(1), reverse=True)  # reverse sort to get highest CPU usage on top
                    if top_sorted:
                        top_sorted.pop(0)           # remove the idle process
                    display_string =  '\n'.join([f'{cpu/10:2.2f} {proc:23}' for proc, cpu in top_sorted])
                    # --------- Display timer and proceses in window --------
                    window['-CPU PERCENT-'].update(f'CPU {cpu_percent}')
                    window['-PROCESSES-'].update(display_string)
            # get the timeout from the spinner
            g_interval = int(values['-SPIN-'])
    except Exception as e:
        sg.Print('*** GOT Exception in event loop ***', c='white on red', font='_ 18')
        sg.Print('Exception = ', e, wait=True)      # IMPORTANT to add a wait/blocking so that the print pauses execution. Otherwise program continue and exits

    window.close()

if __name__ == '__main__':
    main()
