import threading
import time
import PySimpleGUI as sg

"""
    Threaded Demo - Multiwindow Version

    This demo uses the write_event_value method in a multi-window environment.  Instead of window.read() returning the event to
    the user, the call to read_all_windows is used which will return both the window that had the event along with the event.

    Copyright 2020 PySimpleGUI.org
"""

THREAD_EVENT = '-THREAD-'
PROGRESS_EVENT = '-PROGRESS-'

cp = sg.cprint


def the_thread(window, window_prog):
    """
    The thread that communicates with the application through the window's events.

    Once a second wakes and sends a new event and associated value to a window for 10 seconds.

    Note that WHICH window the message is sent to doesn't really matter because the code
    in the event loop is calling read_all_windows.  This means that any window with an event
    will cause the call to return.
    """
    for i in range(10):
        time.sleep(1)
        window.write_event_value(THREAD_EVENT, (threading.current_thread().name, i))  # Data sent is a tuple of thread name and counter
        window_prog.write_event_value(PROGRESS_EVENT, i)  # Send a message that the progress bar should be updated


def make_progbar_window():
    layout = [[sg.Text('Progress Bar')],
              [sg.ProgressBar(10, orientation='h', size=(15, 20), k='-PROG-')]]
    return sg.Window('Progress Bar', layout, finalize=True, location=(800, 800))


def make_main_window():
    layout = [[sg.Text('Output Area - cprint\'s route to here', font='Any 15')],
              [sg.Multiline(size=(65, 20), key='-ML-', autoscroll=True, reroute_stdout=True, write_only=True, reroute_cprint=True)],
              [sg.T('Input so you can see data in your dictionary')],
              [sg.Input(key='-IN-', size=(30, 1))],
              [sg.B('Start A Thread'), sg.B('Dummy'), sg.Button('Exit')]]

    return sg.Window('Window Main', layout, finalize=True)


def main():
    """
    The demo will display in the multiline info about the event and values dictionary as it is being
    returned from window.read()
    Every time "Start" is clicked a new thread is started
    Try clicking "Dummy" to see that the window is active while the thread stuff is happening in the background
    """

    main_window = make_main_window()
    window_prog = make_progbar_window()

    while True:  # Event Loop
        window, event, values = sg.read_all_windows()
        print(window.Title, event, values)

        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event.startswith('Start'):
            threading.Thread(target=the_thread, args=(main_window, window_prog), daemon=True).start()
        if event == THREAD_EVENT:
            cp(f'Thread Event ', colors='white on blue', end='')
            cp(f'{values[THREAD_EVENT]}', colors='white on red')
        if event == PROGRESS_EVENT:
            cp(f'Progress Event from thread ', colors='white on purple', end='')
            cp(f'{values[PROGRESS_EVENT]}', colors='white on red')
            window_prog['-PROG-'].update(values[event] % 10 + 1)  # type: sg.ProgressBar.update()
        if event == 'Dummy':
            window.write_event_value('-DUMMY-', 'pressed')
        if event == '-DUMMY-':
            cp("Dummy pressed")

    window.close()


if __name__ == '__main__':
    main()