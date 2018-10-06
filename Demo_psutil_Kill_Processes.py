#!/usr/bin/env python
import sys
import sys
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg
import os
import signal
import psutil
import operator


"""
"""




def kill_proc_tree(pid, sig=signal.SIGTERM, include_parent=True,
                   timeout=None, on_terminate=None):
    """Kill a process tree (including grandchildren) with signal
    "sig" and return a (gone, still_alive) tuple.
    "on_terminate", if specified, is a callabck function which is
    called as soon as a child terminates.
    """
    if pid == os.getpid():
        raise RuntimeError("I refuse to kill myself")
    parent = psutil.Process(pid)
    children = parent.children(recursive=True)
    if include_parent:
        children.append(parent)
    for p in children:
        p.send_signal(sig)
    gone, alive = psutil.wait_procs(children, timeout=timeout,
                                    callback=on_terminate)
    return (gone, alive)


def main():

    # ----------------  Create Form  ----------------
    # sg.ChangeLookAndFeel('Dark')
    layout = [[sg.Text('Process Killer - Choose one or more processes',
                       size=(45,1), font=('Helvetica', 15))],
                 [sg.Listbox(values=[], size=(50, 30), select_mode=sg.SELECT_MODE_EXTENDED,  font=('Courier', 12), key='_processes_')],
              [sg.Text('Click refresh once or twice.. once for list, second to get CPU usage')],
                [sg.RButton('Refresh'), sg.RButton('Kill', button_color=('white','red')),
                 sg.Exit(button_color=('white', 'firebrick4'))]]

    window = sg.Window('Process Killer',
                       keep_on_top=True,
                       auto_size_buttons=False,
                       default_button_element_size=(9,1),
                       grab_anywhere=False).Layout(layout)


    # ----------------  main loop  ----------------
    while (True):
        # --------- Read and update window --------
        button, values = window.Read()

        # --------- Do Button Operations --------
        if values is None or button == 'Exit':
            break

        if button == 'Refresh':
            psutil.cpu_percent(interval=1)
            procs = psutil.process_iter()
            top = {proc.name(): (proc.cpu_percent(), proc.pid) for proc in procs}

            # cpu_percent = psutil.cpu_percent(interval=interval)       # if don't wan to use a task

            display_string = ''
            # --------- Create list of top % CPU porocesses --------

            top_sorted = sorted(top.items(), key=operator.itemgetter(0), reverse=False)
            if top_sorted:
                top_sorted.pop(0)
            display_string = []
            for proc, pair in top_sorted:
                cpu, pid = pair
                display_string.append('{:5d} {:5.2f}  {}\n'.format(pid, cpu/10, proc))

            window.FindElement('_processes_').Update(display_string)

        if button == 'Kill':
            processes_to_kill = values['_processes_']
            for proc in processes_to_kill:
                pid = int(proc[0:5])
                if sg.PopupYesNo('About to kill {} {}'.format(pid, proc[13:]), keep_on_top=True) == 'Yes':
                    kill_proc_tree(pid=pid)


if __name__ == "__main__":
    main()