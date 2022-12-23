import PySimpleGUI as sg
import time

"""
    Demo Program - Periodic Timer Event

    How to use a thread to generate an event every x seconds

    One method of getting periodic timer event that's more predictable than using window.read(timeout=x)
    The problem with using a timeout with window.read is that if any event happens prior to the timer
    expiring, the timer event will not happen.  The timeout parameter is not designed to provide a "heartbeat"
    type of timer but rather to guarantee you will get an event within that amount of time, be it a
    user-caused event or a timeout.

    Copyright 2022 PySimpleGUI
"""

timer_running = {}


def timer_status_change(timer_id, start=None, stop=None, delete=None):
    """
    Encapsulates/manages the timers dictionary

    :param timer_id: ID of timer to change status
    :type timer_id: int
    :param start:   Set to True when timer is started
    :type start:    bool
    :param stop:    Set to True when timer is stopped
    :type stop:     bool
    :param delete:  Set to True to delete a timer
    :type delete    bool
    """
    global timer_running

    if start:
        timer_running[timer_id] = True
    if stop:
        timer_running[timer_id] = False
    if delete:
        del timer_running[timer_id]


def timer_is_running(timer_id):
    """

    :param timer_id:    The timer ID to check
    :type timer_id:     int
    :return:            True if the timer is running
    :rtype:             bool
    """
    if timer_running[timer_id]:
        return True
    return False



def periodic_timer_thread(window, interval, timer_id):
    """
    Thread that sends messages to the GUI after some interval of time

    :param window:   Window the events will be sent to
    :type window:    sg.Window
    :param interval: How frequently to send an event
    :type interval:  float
    :param timer_id: A timer identifier
    :type timer_id:  int
    """


    while True:
        time.sleep(interval)                # sleep until time to send a timer event
        window.write_event_value(('-THREAD-', '-TIMER EVENT-'), timer_id)
        if not timer_is_running(timer_id):  # If timer has been stopped, delete it and return from thread
            timer_status_change(timer_id, delete=True)
            return


def main():
    layout = [[sg.Text('Window with periodic time events')],
              [sg.Text(key='-MESSAGE-')],
              [sg.Text('Timer Status:'), sg.Text(key='-TIMER STATUS-')],
              [sg.Text('Duration:'), sg.In(s=3, key='-DURATION-'), sg.Button('Start')],
              [sg.Text('Timer ID:'), sg.In(s=3, key='-STOP ID-'), sg.Button('Stop'),],
              [ sg.Button('Dummy'), sg.Button('Exit')], ]

    window = sg.Window('Blinking LED Window', layout)

    timer_counter = 0
    # --------------------- EVENT LOOP ---------------------
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        window['-MESSAGE-'].update(f'{event} {values}')
        window['-TIMER STATUS-'].update(f'{timer_running}')
        if event == 'Start':
            if values['-DURATION-']:
                timer_status_change(timer_counter, start=True)
                window.start_thread(lambda: periodic_timer_thread(window, float(values['-DURATION-']), timer_counter), ('-THREAD-', '-THREAD ENDED-'))
                timer_counter += 1
            else:
                window['-MESSAGE-'].update('Please enter a numeric duration')
        elif event == 'Stop':
            if values['-STOP ID-']:
                timer_status_change(int(values['-STOP ID-']), stop=True)

    window.close()

if __name__ == '__main__':
    main()
