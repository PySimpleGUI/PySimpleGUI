import PySimpleGUI as sg
import queue
import logging
import threading
import time

"""
    This code originated in this project:
    https://github.com/john144/MultiThreading
    Thanks to John for writing this in the early days of PySimpleGUI
    Demo program showing one way that a threaded application can function with PySimpleGUI
    Events are sent from the ThreadedApp thread to the main thread, the GUI, by using a queue
"""

logger = logging.getLogger('mymain')


def externalFunction():
    logger.info('Hello from external app')
    logger.info('External app sleeping 5 seconds')
    time.sleep(5)
    logger.info('External app waking up and exiting')


class ThreadedApp(threading.Thread):
    def __init__(self):
        super().__init__()
        self._stop_event = threading.Event()

    def run(self):
        externalFunction()

    def stop(self):
        self._stop_event.set()


class QueueHandler(logging.Handler):
    def __init__(self, log_queue):
        super().__init__()
        self.log_queue = log_queue

    def emit(self, record):
        self.log_queue.put(record)


def main():

    layout = [
            [sg.Multiline(size=(50, 15), key='-LOG-')],
            [sg.Button('Start', bind_return_key=True, key='-START-'), sg.Button('Exit')]
        ]

    window = sg.Window('Log window', layout,
            default_element_size=(30, 2),
            font=('Helvetica', ' 10'),
            default_button_element_size=(8, 2),)

    appStarted = False

    # Setup logging and start app
    logging.basicConfig(level=logging.DEBUG)
    log_queue = queue.Queue()
    queue_handler = QueueHandler(log_queue)
    logger.addHandler(queue_handler)
    threadedApp = ThreadedApp()

    # Loop taking in user input and querying queue
    while True:
        # Wake every 100ms and look for work
        event, values = window.read(timeout=100)

        if event == '-START-':
            if appStarted is False:
                threadedApp.start()
                logger.debug('App started')
                window['-START-'].update(disabled=True)
                appStarted = True
        elif event in  (None, 'Exit'):
            break

        # Poll queue
        try:
            record = log_queue.get(block=False)
        except queue.Empty:
            pass
        else:
            msg = queue_handler.format(record)
            window['-LOG-'].update(msg+'\n', append=True)

    window.close()


if __name__ == '__main__':
    main()