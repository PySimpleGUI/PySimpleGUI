import PySimpleGUI as sg
import textwrap
from multiprocessing import Process

'''
    Multiprocessing based Notification Window Demo Program
    
    The PySimpleGUI code for showing the windows themselves ovolved from code supplied by PySimpleGUI user ncotrb

    Displays a small informational window with an Icon and a message in the lower right corner of the display
    Option to fade in/out or immediatealy display.
    
    You can click on the notification window to speed things along.  The idea is that if you click while fading in, you should immediately see the info. If you click while info is displaying or while fading out, the window closes immediately.
    
    Note - In order to import and use these calls, you must make the call from a "main program".
    
    Copyright 2020 PySimpleGUI
    
'''


# -------------------------------------------------------------------
# fade in/out info and default window alpha
WIN_MARGIN = 60

# colors
WIN_COLOR = "#282828"
TEXT_COLOR = "#ffffff"

DEFAULT_DISPLAY_DURATION_IN_MILLISECONDS = 3000     # how long to display the window
DEFAULT_FADE_IN_DURATION = 2000                     # how long to fade in / fade out the window

# Base64 Images to use as icons in the window
image64_error = b'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAA3NCSVQICAjb4U/gAAAACXBIWXMAAADlAAAA5QGP5Zs8AAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAIpQTFRF////20lt30Bg30pg4FJc409g4FBe4E9f4U9f4U9g4U9f4E9g31Bf4E9f4E9f4E9f4E9f4E9f4FFh4Vdm4lhn42Bv5GNx5W575nJ/6HqH6HyI6YCM6YGM6YGN6oaR8Kev9MPI9cbM9snO9s3R+Nfb+dzg+d/i++vt/O7v/fb3/vj5//z8//7+////KofnuQAAABF0Uk5TAAcIGBktSYSXmMHI2uPy8/XVqDFbAAAA8UlEQVQ4y4VT15LCMBBTQkgPYem9d9D//x4P2I7vILN68kj2WtsAhyDO8rKuyzyLA3wjSnvi0Eujf3KY9OUP+kno651CvlB0Gr1byQ9UXff+py5SmRhhIS0oPj4SaUUCAJHxP9+tLb/ezU0uEYDUsCc+l5/T8smTIVMgsPXZkvepiMj0Tm5txQLENu7gSF7HIuMreRxYNkbmHI0u5Hk4PJOXkSMz5I3nyY08HMjbpOFylF5WswdJPmYeVaL28968yNfGZ2r9gvqFalJNUy2UWmq1Wa7di/3Kxl3tF1671YHRR04dWn3s9cXRV09f3vb1fwPD7z9j1WgeRgAAAABJRU5ErkJggg=='

image64_success = b'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAA3NCSVQICAjb4U/gAAAACXBIWXMAAAEKAAABCgEWpLzLAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAHJQTFRF////ZsxmbbZJYL9gZrtVar9VZsJcbMRYaMZVasFYaL9XbMFbasRZaMFZacRXa8NYasFaasJaasFZasJaasNZasNYasJYasJZasJZasJZasJZasJZasJYasJZasJZasJZasJZasJaasJZasJZasJZasJZ2IAizQAAACV0Uk5TAAUHCA8YGRobHSwtPEJJUVtghJeYrbDByNjZ2tvj6vLz9fb3/CyrN0oAAADnSURBVDjLjZPbWoUgFIQnbNPBIgNKiwwo5v1fsQvMvUXI5oqPf4DFOgCrhLKjC8GNVgnsJY3nKm9kgTsduVHU3SU/TdxpOp15P7OiuV/PVzk5L3d0ExuachyaTWkAkLFtiBKAqZHPh/yuAYSv8R7XE0l6AVXnwBNJUsE2+GMOzWL8k3OEW7a/q5wOIS9e7t5qnGExvF5Bvlc4w/LEM4Abt+d0S5BpAHD7seMcf7+ZHfclp10TlYZc2y2nOqc6OwruxUWx0rDjNJtyp6HkUW4bJn0VWdf/a7nDpj1u++PBOR694+Ftj/8PKNdnDLn/V8YAAAAASUVORK5CYII='

# -------------------------------------------------------------------

def _display_notification(title, message, icon=image64_success, display_duration_in_ms=DEFAULT_DISPLAY_DURATION_IN_MILLISECONDS, fade_in_duration=DEFAULT_FADE_IN_DURATION, alpha=0.9, location=None):
    """
    The PROCESS that is started when a toaster message is to be displayed.
    Note that this is not a user callable function.
    It does the actual work of creating and showing the window on the screen

    Displays a "notification window", usually in the bottom right corner of your display.  Has an icon, a title, and a message
    The window will slowly fade in and out if desired.  Clicking on the window will cause it to move through the end the current "phase". For example, if the window was fading in and it was clicked, then it would immediately stop fading in and instead be fully visible.  It's a way for the user to quickly dismiss the window.
    :param title: (str) Text to be shown at the top of the window in a larger font
    :param message: (str) Text message that makes up the majority of the window
    :param icon: (base64) A base64 encoded PNG/GIF image that will be displayed in the window
    :param display_duration_in_ms: (int) Number of milliseconds to show the window
    :param fade_in_duration: (int) Number of milliseconds to fade window in and out
    :param alpha: (float) Alpha channel. 0 - invisible 1 - fully visible
    :param location: Tuple[int, int] Location on the screen to display the window
    :return: (Any) The Process ID returned from calling multiprocessing.Process
    """
    # Compute location and size of the window
    message = textwrap.fill(message, 50)
    win_msg_lines = message.count("\n") + 1

    screen_res_x, screen_res_y = sg.Window.get_screen_size()
    win_margin = WIN_MARGIN  # distance from screen edges
    win_width, win_height = 364, 66 + (14.8 * win_msg_lines)

    layout = [[sg.Graph(canvas_size=(win_width, win_height), graph_bottom_left=(0, win_height), graph_top_right=(win_width, 0), key="-GRAPH-", background_color=WIN_COLOR, enable_events=True)]]

    win_location = location if location is not None else (screen_res_x - win_width - win_margin, screen_res_y - win_height - win_margin)
    window = sg.Window(title, layout, background_color=WIN_COLOR, no_titlebar=True,
                       location=win_location, keep_on_top=True, alpha_channel=0, margins=(0,0), element_padding=(0,0), grab_anywhere=True, finalize=True)

    window["-GRAPH-"].draw_rectangle((win_width, win_height), (-win_width, -win_height), fill_color=WIN_COLOR, line_color=WIN_COLOR)
    window["-GRAPH-"].draw_image(data=icon, location=(20, 20))
    window["-GRAPH-"].draw_text(title, location=(64, 20), color=TEXT_COLOR, font=("Arial", 12, "bold"), text_location=sg.TEXT_LOCATION_TOP_LEFT)
    window["-GRAPH-"].draw_text(message, location=(64, 44), color=TEXT_COLOR, font=("Arial", 9), text_location=sg.TEXT_LOCATION_TOP_LEFT)
    window["-GRAPH-"].set_cursor('hand2')

    if fade_in_duration:
        for i in range(1,int(alpha*100)):               # fade in
            window.set_alpha(i/100)
            event, values = window.read(timeout=fade_in_duration // 100)
            if event != sg.TIMEOUT_KEY:
                window.set_alpha(1)
                break
        event, values = window(timeout=display_duration_in_ms)
        if event == sg.TIMEOUT_KEY:
            for i in range(int(alpha*100),1,-1):       # fade out
                window.set_alpha(i/100)
                event, values = window.read(timeout=fade_in_duration // 100)
                if event != sg.TIMEOUT_KEY:
                    break
    else:
        window.set_alpha(alpha)
        event, values = window(timeout=display_duration_in_ms)

    window.close()


def display_notification(title, message, icon=image64_success, display_duration_in_ms=DEFAULT_DISPLAY_DURATION_IN_MILLISECONDS, fade_in_duration=DEFAULT_FADE_IN_DURATION, alpha=0.9, location=None):
    """
    Displays a "notification window", usually in the bottom right corner of your display.  Has an icon, a title, and a message
    The window will slowly fade in and out if desired.  Clicking on the window will cause it to move through the end the current "phase". For example, if the window was fading in and it was clicked, then it would immediately stop fading in and instead be fully visible.  It's a way for the user to quickly dismiss the window.
    :param title: (str) Text to be shown at the top of the window in a larger font
    :param message: (str) Text message that makes up the majority of the window
    :param icon: (base64) A base64 encoded PNG/GIF image that will be displayed in the window
    :param display_duration_in_ms: (int) Number of milliseconds to show the window
    :param fade_in_duration: (int) Number of milliseconds to fade window in and out
    :param alpha: (float) Alpha channel. 0 - invisible 1 - fully visible
    :param location: Tuple[int, int] Location on the screen to display the window
    :return: (Any) The Process ID returned from calling multiprocessing.Process
    """
    proc = Process(target=_display_notification, args=(title, message, icon, display_duration_in_ms, fade_in_duration, alpha, location))
    proc.start()
    return proc

if __name__ == '__main__':
    proc2 = display_notification('Normal Location', 'This is my notification!')
    proc3 = display_notification('Upper Left', 'This one does not fade in!', icon=image64_error, location=(0,0), fade_in_duration=0)

    proc3.join()
    proc2.join()
    print('*** Successfully joined process ***')
