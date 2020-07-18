import subprocess
import PySimpleGUI as sg
import threading


"""
    Demo - Run a shell command while displaying an animated GIF to inform the user the 
    program is still running.
    If you have a GUI and you start a subprocess to run a shell command, the GUI essentually
    locks up and often the operation system will off to terminate the program for you.

    This demo fixes this situation by running the subprocess as a Thread.   This enables
    the subproces to run async to the main program.  The main program then simply runs a loop,
    waiting for the thread to complete running. 

    The output from the subprocess is saved and displayed in a scrolled popup.
"""


def process_thread():
    global proc
    proc = subprocess.run('pip list', shell=True, stdout=subprocess.PIPE)


def main():
    thread = threading.Thread(target=process_thread, daemon=True)
    thread.start()

    while True:
        sg.popup_animated(sg.DEFAULT_BASE64_LOADING_GIF, 'Loading list of packages', time_between_frames=100)
        thread.join(timeout=.1)
        if not thread.is_alive():
            break
    sg.popup_animated(None)

    output = proc.__str__().replace('\\r\\n', '\n')
    sg.popup_scrolled(output, font='Courier 10')


if __name__ == '__main__':
    main()
