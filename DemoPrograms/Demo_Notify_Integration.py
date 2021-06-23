import PySimpleGUI as sg
from notifypy import Notify
import tempfile
import base64
import os

"""
    Demo of Notification integration with PySimpleGUI
    
    You will need to install the py-notifypy package (note spelling!):
        pip install notify-py

    Displays an OS created notification
    
    There are more options than those in this Demo... like all PySimpleGUI Demo Programs
        the demo is meant to give you a starting point
    
    For more info about the notifypy package, visit the project's GitHub
    https://github.com/ms7m/notify-py
    
    To show a notification, call the function provided: notify_popout
    
    If you use a base64 icon, then a temp file will be created. If you wish to cleanup these
    temp files (an optional step), then include this line of code when you close the window:
    [os.remove(file) for file in notify_popout.temp_files] if hasattr(notify_popout, 'temp_files') else None
    
    Copyright 2021 PySimpleGUI
"""


def notify_popout(title=None, message=None, icon=sg.DEFAULT_BASE64_ICON, app_name=None):
    """
    Show a notification popout window

    :param title: Title shown in the notification
    :param message: Message shown in the notification
    :param icon: Icon shown in the notification - defaults to PySimpleGUI icon. Should be a PNG file
    :param app_name: Application name shown in the notification
    """
    if not hasattr(notify_popout, 'temp_files'):
        notify_popout.temp_files = []

    notification = Notify()
    notification.title = title
    notification.message = message
    tmp = None
    if isinstance(icon, bytes):
        with tempfile.TemporaryFile(suffix='.png', delete=False) as tmp:
            tmp.write(base64.b64decode(icon))
            tmp.close()
        notification.icon = tmp.name
    elif icon is not None:
        notification.icon = icon
    if app_name is not None:
        notification.application_name = app_name
    notification.send(block=False)
    if tmp is not None:
        notify_popout.temp_files.append(tmp.name)


def main():
    """
    A little test application that demonstrates calling the notify_popout function
    """

    layout = [  [sg.Text('My Window')],
                [sg.T('Notification message:'), sg.Input(key='-IN-')],
                [sg.B('Show Notification', bind_return_key=True), sg.Button('Exit')]  ]

    window = sg.Window('My PySimpleGUI Application', layout)

    while True:             # Event Loop
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == 'Show Notification':
            notify_popout(title=window.Title,  message=values['-IN-'], app_name=window.Title)

    window.close()
    # enjoy the anti-pattern that cleans up the temp files
    [os.remove(file) for file in notify_popout.temp_files] if hasattr(notify_popout, 'temp_files') else None


if __name__ == '__main__':
    main()
