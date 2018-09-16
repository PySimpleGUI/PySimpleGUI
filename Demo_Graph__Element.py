import ping
from threading import Thread
import time
import PySimpleGUI as sg

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

    layout = [  [sg.T('Ping times to Google.com', font='Any 18')],
               [sg.Graph((300,300), (0,0), (100,500),background_color='white', key='graph')],
               [sg.Quit()]]

    form = sg.FlexForm('Canvas test', grab_anywhere=True)
    form.Layout(layout)

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
        form.FindElement('graph').DrawLine((prev_x, prev_y), (new_x, new_y), color='red')
        # form.FindElement('graph').DrawPoint((new_x, new_y), color='red')
        prev_x, prev_y = new_x, new_y
        if i >= 100:
            i = 0
            prev_x = prev_y = last_x = last_y = 0
            form.FindElement('graph').Erase()
        else: i += 4

    # tell thread we're done. wait for thread to exit
    g_exit = True
    thread.join()


if __name__ == '__main__':
    main()
    exit(69)