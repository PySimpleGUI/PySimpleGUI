#!/usr/bin/env python
import PySimpleGUI as sg
import os
import signal
import psutil
import operator
import sys

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


def show_list_by_name(python_only=False):
    disp_data = get_all_procs()
    disp_data = sorted(disp_data, key=operator.itemgetter(3), reverse=False)
    display_list = []
    for process in disp_data:
        if not python_only or (python_only and 'python' in process[2].lower()):
            display_list.append('{:5d} {:5.2f} {} {}\n'.format(process[0], process[1], process[2], process[3]))
    return display_list


def show_list_by_cpu(python_only=False):
    disp_data = get_all_procs()
    disp_data = sorted(disp_data, key=operator.itemgetter(1), reverse=True)

    display_list = []
    for process in disp_data:
        if not python_only or (python_only and 'python' in process[2].lower()):
            display_list.append('{:5d} {:5.2f} {} {}\n'.format(process[0], process[1], process[2], process[3]))
    return display_list


def make_window():
    layout = [[sg.Text('Python Process Killer - Choose one or more processes',
                       size=(45, 1), font=('Helvetica', 15), text_color='yellow')],
              [sg.Listbox(values=[' '], size=(130, 30), select_mode=sg.SELECT_MODE_EXTENDED, font=('Courier', 10), key='-PROCESSES-', expand_x=True, expand_y=True)],
              [sg.Text('Click refresh once or twice.. once for list, second to get CPU usage')],
              [sg.Text('Filter by typing name', font='ANY 14'), sg.Input(size=(15, 1), font='any 14', key='-FILTER-', enable_events=True),
               sg.Checkbox('Show only Python processes', default=True, enable_events=True, key='-PYTHON ONLY-')],
              [sg.Button('Sort by Name', ),
               sg.Button('Sort by % CPU', button_color=('white', 'DarkOrange2')),
               sg.Button('Show Open Files', button_color=('white', 'dark green')),
               sg.Button('Kill Selected', button_color=('white', 'red'), bind_return_key=True),
               sg.Button('Kill All', button_color='red on white'),
               sg.Button('Kill All & Exit', button_color='red on white'),
               sg.Exit(button_color=('white', 'sea green')), sg.Sizegrip()]]

    window = sg.Window('Python Process Killer', layout,
                       keep_on_top=True,
                       auto_size_buttons=False,
                       default_button_element_size=(12, 1),
                       return_keyboard_events=True,
                       resizable=True,
                        right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_EXIT,
                       finalize=True)
    window.bind('<Delete>', 'Kill Selected')
    window.set_min_size(window.size)
    return window

def kill_all(python_only=True):
    processes_to_kill = show_list_by_name(python_only=python_only)
    for proc in processes_to_kill:
        pid = int(proc[0:5])
        try:
            kill_proc(pid=pid)
            # kill_proc_tree(pid=pid)
        except Exception as e:
            pass

def main(silent=False):
    if silent:
        kill_all(python_only=True)
        sg.popup_auto_close('Killed everything....', 'This window autocloses')
        sys.exit()
    # ----------------  Create Form  ----------------
    sg.theme('Dark Grey 9')
    sg.set_options(icon=icon)

    window = make_window()
    current_display_list = display_list = show_list_by_name(window['-PYTHON ONLY-'].get())
    window['-PROCESSES-'].update(display_list)
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
            window['-PROCESSES-'].update(show_list_by_name(values['-PYTHON ONLY-']))
            name_sorted = True
        elif event.startswith('Kill'):
            if event.startswith('Kill All'):
                processes_to_kill = show_list_by_name(values['-PYTHON ONLY-'])
            else:
                processes_to_kill = values['-PROCESSES-']
            for proc in processes_to_kill:
                pid = int(proc[0:5])
                try:
                    kill_proc(pid=pid)
                    # kill_proc_tree(pid=pid)
                except Exception as e:
                    if event.endswith('Selected'):      # only show the error if trying to kill only 1 process
                        sg.popup_no_wait('Error killing process', e, auto_close_duration=2, auto_close=True, keep_on_top=True)
            current_display_list = show_list_by_name(values['-PYTHON ONLY-']) if name_sorted else show_list_by_cpu(values['-PYTHON ONLY-'])
            window['-PROCESSES-'].update(current_display_list)
            if event.endswith('Exit'):
                break
        elif event == 'Sort by % CPU':
            window['-PROCESSES-'].update(show_list_by_cpu(values['-PYTHON ONLY-']))
            name_sorted = False
        elif event == 'Show Open Files':
            for proc in values['-PROCESSES-']:
                pid = int(proc[0:5])
                parent = psutil.Process(pid)
                file_list = parent.open_files()
                out = ''
                for f in file_list:
                    out += f'{f}\n'
                sg.popup_scrolled(out, non_blocking=True, keep_on_top=True,size=(100,30))
        elif event == '-PYTHON ONLY-':          # if checkbox changed
            current_display_list = show_list_by_name(values['-PYTHON ONLY-']) if name_sorted else show_list_by_cpu(values['-PYTHON ONLY-'])
            window['-PROCESSES-'].update(current_display_list)
        elif event == '-FILTER-':  # was a typed character
            # display_list = window['-PROCESSES-'].get_list_values()
            display_list = current_display_list
            if display_list is not None:
                new_output = []
                for line in display_list:
                    if values['-FILTER-'] in line.lower():
                        new_output.append(line)
                window['-PROCESSES-'].update(new_output)
        elif event == 'Edit Me':
            sg.execute_editor(__file__)
    window.close()


if __name__ == "__main__":
    icon = b'iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAFLklEQVR4nO2ZW2xURRjHfzNnz9meXnYplHKtIhKEAgoEabUgKARBQTQ8+mLi5dXERIJPhMREownhyQfii8+aKKCCRIPRQiGEi3IRuSXc5dbSbbvdc5vxYUvAsmfP6bKtmuwvOS87s9/3/We++WbOHKhQoUKFChVKR4Q1fP3T3k1Jy5rluu5IxhOKZVk4rnvitWVtGwu1J4r8d0WyqqpVyFCtI4plJXFcdxIwVCHacZwcrutiGgkMwwCthynMEIQgCAK8wEdrDWgnrGuxGcl3MAz2nDzM2WuXQBpljTMSFTBtQhNLm+dFdo0WIg32nztJ+5H9YJoxnOv8yhNlSEnPY9G8VpbPXoCKijOOPdNIgGlFC9EaWVuNdj2065VBjMj7joF8SE/30BohJaPfWEl1SzP4QdlMx6F8QrwAu2Um1S3NpFa1IOvrQEUlRPkoj5BAYTSkSa9dBFpjNjVSt3wBBP83IVqTerkVs6kR/1Y32vWoXTYf89HxI5ZiDy/ED0g2T6H2hfmo3iy3t+6g/+hZEmPSpNY8C4aEEdh+4pUEpfIjKwbp1hphJxm17jlkrU33tnaco2fQjkvVrClUL5xJtuME/Yf+BLOAq0AV32T9IPY6ixaiNUZDmsRjExCJQd0Dhf30DJLNU3AvXKfn+wNgmbhnr9C75wjptYtJvdJG7tRFtOP+sxwrTWJcPcJOhorRvo9RX5dvjyjlkUK06zNq3VIaGtqwVAFjIi8os2Mvwa07YJkQKHp+OIg9fzrJJ5qoXfIUPd/tB2vAnR+QmNhA44bXSTSkQlPPRVF7zkVnfEgW38OiZ0QIgkwfvt+L1AWEGAbOmUtk9528lz6GJLjZRebbDsa8vZq6lS1kD58muHEnv2akIL22DbNxFH5nBt3vFjyH+1qheo1YG2ukEGEluPPlz9w+dhASBUZFgA5UPpfvd2gmyHYcp6a1GXv+dFKrWun6Yhe4PvbCGdS0ziLI9HFry1e456+CUeAc53v0zFmAeGlqZL2IV7UChfZ8tF/g8fyB89WgURMCnfPo3taO6slSu/hJrOlNiJok6VcXI+wkPT8ewjl1Ea11cdsxiCfk7iEw9An5nylxTl2k95ffkHU2qdXPkFrThvX4JJzzV+nZfRASRnHbMYlXfktGAJqeXQew507LP3Omol2PzPZ2VGcmXxzKQPnOWmEYEv9aJ5mdBxBCICyT/sOnyR74o/DeUiLDLwTANOj79XdyZy6j+vrp/qY9vxmW451lgGFOrQGEQGdzZLbvw5rcgHfhr/zaKCMjIwTATJA7do7c8fNlFwExhfhBAJ5X5PIoJnePInFTyvPyvmMQKcT1fdYtXMLzM+bCSF8NKc3oVBrX90lEFIZIIUorpjVOQo5vKlt8Q0Epha+iZyVeaqkAYhj7NwkXIrBtuxpZ6AwUhdZ4IVetpmWVVHaTVhLHdeyw9mIzsrk/29fk+N6Qneb6c2Nvdna/jxgUsdZ67Oj0p1V21c2h2lS+D3AprH1YVu9b6z+eXD+u/mIhIV3Xux75/JMNl8vtc1j2kXGNdSKQ8sEU0ppxjXXDMnglG/1gy2ezlTJbpSFNNei9WgjRiNYbC80IQmzSWt+4/2cpJSpQnonu+PC9d06UEk9JQtZv3jpLCHYnq+yJd0+4g+MtttgH67trw8nlrkgpV3z07psnhxpTSaklpFhRU5ua6DoOhFwvJ0LuibXWA58IHrBKTV1qUl9v5kVgZIRIoS/5nrvT90I/V5SElAIpdGhlqlChQoUK/zn+BhjXF7IsC7cbAAAAAElFTkSuQmCC'

    if len(sys.argv) == 2 and sys.argv[1] == 'silent':
        main(silent=True)
    else:
        main(silent=False)