#!/usr/bin/env python
import PySimpleGUI as sg
import os
import signal
import psutil
import operator

CONFIRM_KILLS = False

"""
    Task killer program focused on Python only programs
    
    While there is another demo program that handles all running processes, this specific
    demo is for Python oriented processes only.  It is based on the original, more general
    purpose task killer demo.
    
    In addition to filtering out all but Python programs, it also displays the command line used
    to launch the program.  This is particularly good for programs that have no titlebar or
    are running in the background or system tray.

    Copyright 2020 PySimpleGUI.org
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


def kill_proc(pid, sig=signal.SIGTERM, include_parent=True,
                   timeout=None, on_terminate=None):
    """Kill a process tree (including grandchildren) with signal
    "sig" and return a (gone, still_alive) tuple.
    "on_terminate", if specified, is a callabck function which is
    called as soon as a child terminates.
    """
    if pid == os.getpid():
        raise RuntimeError("I refuse to kill myself")
    parent = psutil.Process(pid)
    parent.send_signal(sig)


def get_all_procs():
    psutil.cpu_percent(interval=.1)
    procs = psutil.process_iter()
    all_procs = []
    for proc in procs:
        try:
            all_procs.append([proc.cpu_percent(), proc.name(), proc.pid, proc.cmdline()])
        except: pass

    disp_data = []
    for process in all_procs:
        try:
            name = process[3][1]
        except:
            name = ''
        disp_data.append([process[2], process[0]/10, process[1], name])
    return disp_data


def show_list_by_name():
    disp_data = get_all_procs()
    disp_data = sorted(disp_data, key=operator.itemgetter(3), reverse=False)
    display_list = []
    for process in disp_data:
        if 'python' in process[2].lower():
            display_list.append('{:5d} {:5.2f} {} {}\n'.format(process[0], process[1], process[2], process[3]))
    return display_list


def show_list_by_cpu():
    disp_data = get_all_procs()
    disp_data = sorted(disp_data, key=operator.itemgetter(1), reverse=True)

    display_list = []
    for process in disp_data:
        if 'python' in process[2].lower():
            display_list.append('{:5d} {:5.2f} {} {}\n'.format(process[0], process[1], process[2], process[3]))
    return display_list


def main():
    # ----------------  Create Form  ----------------
    # sg.theme('Topanga')

    layout = [[sg.Text('Python Process Killer - Choose one or more processes',
                       size=(45, 1), font=('Helvetica', 15), text_color='yellow')],
              [sg.Listbox(values=[' '], size=(100, 20), select_mode=sg.SELECT_MODE_EXTENDED, font=('Courier', 10), key='-processes-')],
              [sg.Text('Click refresh once or twice.. once for list, second to get CPU usage')],
              [sg.Text('Filter by typing name', font='ANY 14'), sg.Input(size=(15, 1), font='any 14', key='-filter-')],
              [sg.Button('Sort by Name', ),
               sg.Button('Sort by % CPU', button_color=('white', 'DarkOrange2')),
               sg.Button('Kill', button_color=('white', 'red'), bind_return_key=True),
               sg.Button('Kill All', button_color='red on white', bind_return_key=True),
               sg.Exit(button_color=('white', 'sea green'))]]

    window = sg.Window('Python Process Killer', layout,
                       keep_on_top=True,
                       auto_size_buttons=False,
                       default_button_element_size=(12, 1),
                       return_keyboard_events=True,
                       finalize=True)

    display_list = show_list_by_name()
    window['-processes-'].update(display_list)
    name_sorted = True
    # ----------------  main loop  ----------------
    while True:
        # --------- Read and update window --------
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break

        # skip mouse, control key and shift key events entirely
        if 'Mouse' in event or 'Control' in event or 'Shift' in event:
            continue

        # --------- Do Button Operations --------
        if event == 'Sort by Name':
            window['-processes-'].update(show_list_by_name())
            name_sorted = True
        elif event.startswith('Kill'):
            if event.endswith('All'):
                processes_to_kill = show_list_by_name()
            else:
                processes_to_kill = values['-processes-']
            for proc in processes_to_kill:
                pid = int(proc[0:5])
                try:
                    kill_proc(pid=pid)
                    # kill_proc_tree(pid=pid)
                except Exception as e:
                    sg.popup_no_wait('Error killing process', e, auto_close_duration=2, auto_close=True, keep_on_top=True)
            window['-processes-'].update(show_list_by_name() if name_sorted else show_list_by_cpu())
        elif event == 'Sort by % CPU':
            window['-processes-'].update(show_list_by_cpu())
            name_sorted = False
        else:  # was a typed character
            if display_list is not None:
                new_output = []
                for line in display_list:
                    if values['-filter-'] in line.lower():
                        new_output.append(line)
                window['-processes-'].update(new_output)
    window.close()


if __name__ == "__main__":
    main()
