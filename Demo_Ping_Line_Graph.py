import ping
from threading import Thread
import time
import PySimpleGUI as sg

# set coordinate system
canvas_right = 300
canvas_left = 0
canvas_top = 0
canvas_bottom = 300
# define the coordinates you'll use for your graph
x_right = 100
x_left = 0
y_bottom = 0
y_top = 500

# globale used to communicate with thread.. yea yea... it's working fine
g_exit = False
g_response_time = None

def ping_thread(args):
    global g_exit, g_response_time

    while not g_exit:
        g_response_time = ping.quiet_ping('google.com', timeout=1000)


def convert_xy_to_canvas_xy(x_in,y_in):
    scale_x = (canvas_right - canvas_left) / (x_right - x_left)
    scale_y = (canvas_top - canvas_bottom) / (y_top - y_bottom)
    new_x = canvas_left + scale_x * (x_in - x_left)
    new_y = canvas_bottom + scale_y * (y_in - y_bottom)
    return new_x, new_y



# start ping measurement thread
thread = Thread(target=ping_thread, args=(None,))
thread.start()

layout = [  [sg.T('Ping times to Google.com', font='Any 18')],
           [sg.Canvas(size=(canvas_right, canvas_bottom), background_color='white', key='canvas')],
           [sg.Quit()]
           ]

form = sg.FlexForm('Canvas test', grab_anywhere=True)
form.Layout(layout)
form.Finalize()

canvas = form.FindElement('canvas').TKCanvas

prev_response_time = None
i=0
prev_x, prev_y  = canvas_left, canvas_bottom
while True:
    time.sleep(.2)

    button, values = form.ReadNonBlocking()
    if button == 'Quit' or values is None:
        break

    if g_response_time is None or prev_response_time == g_response_time:
        continue
    new_x, new_y = convert_xy_to_canvas_xy(i, g_response_time[0])
    prev_response_time = g_response_time
    canvas.create_line(prev_x, prev_y, new_x, new_y, width=1, fill='black')
    prev_x, prev_y = new_x, new_y
    if i >= x_right:
        i = 0
        prev_x = prev_y = last_x = last_y = 0
    else: i += 1

# tell thread we're done. wait for thread to exit
g_exit = True
thread.join()


exit(69)