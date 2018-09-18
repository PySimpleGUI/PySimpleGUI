import ping
from threading import Thread
import time
import PySimpleGUI as sg


STEP_SIZE=1
SAMPLES = 6000
CANVAS_SIZE = (6000,500)

# globale used to communicate with thread.. yea yea... it's working fine
g_exit = False
g_response_time = None
def ping_thread(args):
    global g_exit, g_response_time
    while not g_exit:
        g_response_time = ping.quiet_ping('google.com', timeout=1000)

def main():
    global g_exit, g_response_time

    # start ping measurement thread
    thread = Thread(target=ping_thread, args=(None,))
    thread.start()

    sg.ChangeLookAndFeel('Black')
    sg.SetOptions(element_padding=(0,0))

    layout = [  [sg.T('Ping times to Google.com', font='Any 12'), sg.Quit(pad=((100,0), 0), button_color=('white', 'black'))],
               [sg.Graph(CANVAS_SIZE, (0,0), (SAMPLES,500),background_color='black', key='graph')],]

    form = sg.FlexForm('Canvas test', grab_anywhere=True, background_color='black', no_titlebar=False, use_default_focus=False)
    form.Layout(layout)

    form.Finalize()
    graph = form.FindElement('graph')

    prev_response_time = None
    i=0
    prev_x, prev_y  = 0, 0
    while True:
        time.sleep(.2)

        button, values = form.ReadNonBlocking()
        if button == 'Quit' or values is None:
            break
        if g_response_time is None or prev_response_time == g_response_time:
            continue
        new_x, new_y = i, g_response_time[0]
        prev_response_time = g_response_time
        if i >= SAMPLES:
            graph.Move(-STEP_SIZE,0)
            prev_x = prev_x - STEP_SIZE
        graph.DrawLine((prev_x, prev_y), (new_x, new_y), color='white')
        # form.FindElement('graph').DrawPoint((new_x, new_y), color='red')
        prev_x, prev_y = new_x, new_y
        i += STEP_SIZE if i < SAMPLES else 0

    # tell thread we're done. wait for thread to exit
    g_exit = True
    thread.join()


if __name__ == '__main__':
    main()
    exit(69)