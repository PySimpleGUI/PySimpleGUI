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
    Utility to show running processes, CPU usage and provides way to kill processes.
    Based on psutil package that is easily installed using pip
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
    # sg.ChangeLookAndFeel('Topanga')

    layout = [[sg.Text('Process Killer - Choose one or more processes',
                       size=(45,1), font=('Helvetica', 15), text_color='red')],
              [sg.Listbox(values=[' '], size=(50, 30), select_mode=sg.SELECT_MODE_EXTENDED,  font=('Courier', 12), key='_processes_')],
              [sg.Text('Click refresh once or twice.. once for list, second to get CPU usage')],
              [sg.T('Filter by typing name', font='ANY 14'), sg.In(size=(15,1), font='any 14', key='_filter_')],
              [sg.Button('Sort by Name', ),
               sg.Button('Sort by % CPU', button_color=('white', 'DarkOrange2')),
               sg.Button('Kill', button_color=('white','red'), bind_return_key=True),
               sg.Exit(button_color=('white', 'sea green'))]]

    window = sg.Window('Process Killer',
                       keep_on_top=True,
                       auto_size_buttons=False,
                       default_button_element_size=(12,1),
                       return_keyboard_events=True,
                       ).Layout(layout)

    display_list = None
    # ----------------  main loop  ----------------
    while (True):
        # --------- Read and update window --------
        event, values = window.Read()
        if event is None or event == 'Exit':
            break

        # skip mouse, control key and shift key events entirely
        if 'Mouse' in event or 'Control' in event or 'Shift' in event:
            continue

        # --------- Do Button Operations --------
        if event == 'Sort by Name':
            psutil.cpu_percent(interval=1)
            procs = psutil.process_iter()
            all_procs = [[proc.cpu_percent(), proc.name(), proc.pid] for proc in procs]
            sorted_by_cpu_procs = sorted(all_procs, key=operator.itemgetter(1), reverse=False)
            display_list = []
            for process in sorted_by_cpu_procs:
                display_list.append('{:5d} {:5.2f} {}\n'.format(process[2], process[0]/10, process[1]))
            window.FindElement('_processes_').Update(display_list)
        elif event == 'Kill':
            processes_to_kill = values['_processes_']
            for proc in processes_to_kill:
                pid = int(proc[0:5])
                if sg.PopupYesNo('About to kill {} {}'.format(pid, proc[12:]), keep_on_top=True) == 'Yes':
                    try:
                        kill_proc_tree(pid=pid)
                    except:
                        sg.PopupAutoClose('Error killing process', auto_close_duration=1)
        elif event == 'Sort by % CPU':
            psutil.cpu_percent(interval=1)
            procs = psutil.process_iter()
            all_procs = [[proc.cpu_percent(), proc.name(), proc.pid] for proc in procs]
            sorted_by_cpu_procs = sorted(all_procs, key=operator.itemgetter(0), reverse=True)
            display_list = []
            for process in sorted_by_cpu_procs:
                display_list.append('{:5d} {:5.2f} {}\n'.format(process[2], process[0]/10, process[1]))
            window.FindElement('_processes_').Update(display_list)
        else:                   # was a typed character
            if display_list is not None:
                new_output = []
                for line in display_list:
                    if values['_filter_'] in line.lower():
                        new_output.append(line)
                window.FindElement('_processes_').Update(new_output)


if __name__ == "__main__":
    main()
    sys.exit(0)