#!/usr/bin/env python
import PySimpleGUI as sg

"""
    Demo - State Machine using timers

    State Machines are very useful when you need to perform a series of operations that you
    cannot do all at once due to a time constraint. Particularly problematic are operations
    where you would normally use "sleeps" as part of the sequence.

    In this Demo Program, we're going to use the PySimpleGUI Timer API calls to provide our
    sleep-like behavior.

    The sequence of operations we're going to run are:
        User clicks a "Send" Button to start the sequence:
            1. A "Status Window" is shown that says "Sending" and Disable SEND button
            2. Sleep for 3 seconds
            3. Close the "Status Window"
            4. Sleep for 2 seconds
            5. Enable SEND button and Go to state 1

    Control of the state machine will be through the PySimpleGUI events.  This will enable you to use threads
    for any of these states and have the threads communicate the state transitions using the same write_event_value used
    in this example.

    Copyright 2024 PySimpleSoft Inc.
"""


class State:
    stopped = 'stopped'
    start = 'start'
    delay_3_sec = 'delay 3 seconds'
    close_win = 'close win'
    delay_2_sec = 'delay 2 seconds'
    enable_send = 'enable send'


TIMER1 = 3000
TIMER2 = 2000
NEXT_STATE = '-NEXT-'


def make_send_window():
    layout = [[sg.Text('Send Window')],
              [sg.Text('State:'), sg.Text(key='-STATE-')]]

    # Create window a little lower on screen so windows don't overlap
    window = sg.Window('Send Window', layout, finalize=True, relative_location=(0, 150))
    return window


def main():
    layout = [[sg.Text('State Machine Example', font='_ 14')],
              [sg.Text('Click Send to begin sequence')],
              [sg.Text('State:'), sg.Text(key='-STATE-')],
              [sg.Button('Send', key='-SEND-'), sg.Button('Exit')]]

    window = sg.Window('State Machine Example', layout, font='Any 12')

    window_send = None
    state = State.stopped

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break

        if event == '-SEND-':
            state = State.start
        elif event == NEXT_STATE:
            state = values[event]

        window['-STATE-'].update(state)
        if window_send:
            window_send.refresh()

        # ----- STATE MACHINE PROCESSING -----
        if state == State.start:
            window['-SEND-'].update(disabled=True)
            window_send = make_send_window()
            window.write_event_value(NEXT_STATE, State.delay_3_sec)
        elif event == sg.TIMER_KEY and state == State.delay_3_sec:      # be sure the if with the timer check AND state is above if with only state
            window.write_event_value(NEXT_STATE, State.close_win)
        elif state == State.delay_3_sec:
            window.timer_start(TIMER1, repeating=False)
        elif state == State.close_win:
            window_send.close()
            window_send = None
            window.write_event_value(NEXT_STATE, State.delay_2_sec)
        elif event == sg.TIMER_KEY and state == State.delay_2_sec:
            window.write_event_value(NEXT_STATE, State.enable_send)
        elif state == State.delay_2_sec:
            window.timer_start(TIMER2, repeating=False)
        elif state == State.enable_send:
            window['-SEND-'].update(disabled=False)
            window.write_event_value(NEXT_STATE, State.stopped)

    window.close()


if __name__ == '__main__':
    main()
