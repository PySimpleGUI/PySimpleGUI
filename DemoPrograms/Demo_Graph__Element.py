import PySimpleGUI as sg
from threading import Thread
import ping
import time

# Yet another usage of Graph element.

STEP_SIZE = 1
SAMPLES = 6000
CANVAS_SIZE = (6000, 500)

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

    sg.change_look_and_feel('Black')
    sg.set_options(element_padding=(0, 0))

    layout = [[sg.Text('Ping times to Google.com', font='Any 12'),
                sg.Quit(pad=((100, 0), 0), button_color=('white', 'black'))],
              [sg.Graph(CANVAS_SIZE, (0, 0), (SAMPLES, 500),
                        background_color='black', key='graph')]
              ]

    form = sg.FlexForm('Canvas test', layout, grab_anywhere=True, background_color='black',
                       no_titlebar=False, use_default_focus=False, finalize=True)
    graph = form['graph']

    prev_response_time = None
    i = 0
    prev_x, prev_y = 0, 0
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
            graph.move(-STEP_SIZE, 0)
            prev_x = prev_x - STEP_SIZE
        graph.draw_line((prev_x, prev_y), (new_x, new_y), color='white')
        # form['graph'].draw_point((new_x, new_y), color='red')
        prev_x, prev_y = new_x, new_y
        i += STEP_SIZE if i < SAMPLES else 0

    # tell thread we're done. wait for thread to exit
    g_exit = True
    thread.join()


if __name__ == '__main__':
    main()
    
