import PySimpleGUI as sg
from psgtray import SystemTray

"""
    A System Tray Icon using pystray - No visible window version

    Import the SystemTray object with this line of code:
    from psgtray import SystemTray

    Key for the system tray icon is: 
        tray = SystemTray()
        tray.key

    values[key] contains the menu item chosen.

    One trick employed here is to change the window's event to be the event from the System Tray.

    This demo program keeps the Window hidden all the time so that it's a pure "System Tray" application.
    Because the PySimpleGUI architecture implemented the tray icon using the psgtray package combined with the
    overall window event loop, a Window object is still required.  The point of this demo is to show that this
    window does not need to ever appear to the user.

    Copyright PySimpleGUI 2022
"""


def main():
    menu = ['', ['---', '!Disabled Item', 'Change Icon', ['Happy', 'Sad', 'Plain'], 'Exit']]
    tooltip = 'Tooltip'

    layout = [[sg.T('Empty Window', key='-T-')]]

    window = sg.Window('Window Title', layout, finalize=True, enable_close_attempted_event=True, alpha_channel=0)
    window.hide()

    tray = SystemTray(menu, single_click_events=False, window=window, tooltip=tooltip, icon=sg.DEFAULT_BASE64_ICON, key='-TRAY-')
    tray.show_message('System Tray', 'System Tray Icon Started!')
    print(sg.get_versions())
    while True:
        event, values = window.read()
        # IMPORTANT step. It's not required, but convenient. Set event to value from tray
        # if it's a tray event, change the event variable to be whatever the tray sent
        if event == tray.key:
            event = values[event]  # use the System Tray's event as if was from the window

        if event in (sg.WIN_CLOSED, 'Exit'):
            break

        tray.show_message(title=event, message=values)

        if event == 'Happy':
            tray.change_icon(sg.EMOJI_BASE64_HAPPY_JOY)
        elif event == 'Sad':
            tray.change_icon(sg.EMOJI_BASE64_FRUSTRATED)
        elif event == 'Plain':
            tray.change_icon(sg.DEFAULT_BASE64_ICON)
        elif event == 'Hide Icon':
            tray.hide_icon()
        elif event == 'Show Icon':
            tray.show_icon()
        elif event == 'Change Tooltip':
            tray.set_tooltip(values['-IN-'])

    tray.close()  # optional but without a close, the icon may "linger" until moused over
    window.close()


if __name__ == '__main__':
    main()