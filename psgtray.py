import pystray, io, base64, threading, time
from PIL import Image
import PySimpleGUI as sg

"""
    A System Tray Icon implementation that can work with the tkinter port of PySimpleGUI!

    To use, add this import to your code:
    from psgtray import SystemTray
    
    Make sure the psgtray.py file is in the same folder as your app or is on your Python path

    Because this code is entirely in the user's space it's possible to use the pystray package
    to implement the system tray icon feature.  You need to install pystray and PIL.
    
    As of this date, the latest version of pystray is 0.17.3
    
    This code works well under Windows.
    
    On Linux there are some challenges.  Some changes were
    needed in order to get pystray to run as a thread using gtk as the backend.
    The separator '---' caused problems so it is now ignored.  Unknown why it caused the
    menu to not show at all, but it does.

    A sample bit of code is at the bottom for your reference.
    
    Your window will receive events from the system tray thread.
    
    In addition to the init, these are the class methods available:
        change_icon
        hide_icon
        show_icon
        set_tooltip
        notify
        
    In your code, you will receive events from tray with key SystemTray.key
    The value will be the choice made or a click event.  This is the magic statement:
        window.write_event_value(tray.key, item.text)
        
    Extra Special thanks to FireDM for the design pattern that made this work.
    (https://github.com/firedm/FireDM)
    Copyright 2021 PySimpleGUI
"""


class SystemTray:
    DOUBLE_CLICK_THRESHOLD = 500  # time in milliseconds to determine double clicks
    DEFAULT_KEY = '-TRAY-'          # the default key that will be used to send events to your window
    key_counter = 0

    def __init__(self, menu=None, icon=None, tooltip='', single_click_events=False, window=None, key=DEFAULT_KEY):
        """
        A System Tray Icon

        Initializing the object is all that is required to make the tray icon and start the thread.

        :param menu: The PySimpleGUI menu data structure
        :type menu: List[List[Tuple[str, List[str]]]
        :param icon: Icon to show in the system tray.  Can be a file or a BASE64 byte string
        :type icon: str | bytes
        :param tooltip: Tooltip that is shown when mouse hovers over the system tray icon
        :type tooltip: str
        :param single_click_events: If True then both single click and double click events will be generated
        :type single_click_events: bool
        :param window: The window where the events will be sent using window.write_event_value
        :type window: sg.Window
        """
        self.title = tooltip
        self.tray_icon = None  # type: pystray.Icon
        self.window = window
        self.tooltip = tooltip
        self.menu_items = self._convert_psg_menu_to_tray(menu[1])
        self.key = key if SystemTray.key_counter == 0 else key+str(SystemTray.key_counter)
        SystemTray.key_counter += 1
        self.double_click_timer = 0
        self.single_click_events_enabled = single_click_events
        if icon is None:
            self.icon = sg.DEFAULT_BASE64_ICON
        else:
            self.icon = icon

        self.thread_started = False
        self.thread = threading.Thread(target=self._pystray_thread, daemon=True)
        self.thread.start()
        while not self.thread_started:      # wait for the thread to begin
            time.sleep(.2)
        time.sleep(.2)                      # one more slight delay to allow things to actually get running

    def change_icon(self, icon=None):
        """
        Change the icon shown in the tray to a file or a BASE64 byte string.
        :param icon: The icon to change to
        :type icon: str | bytes
        """
        if icon is not None:
            self.tray_icon.icon = self._create_image(icon)

    def hide_icon(self):
        """
        Hides the icon
        """
        self.tray_icon.visible = False

    def show_icon(self):
        """
        Shows a previously hidden icon
        """
        self.tray_icon.visible = True

    def set_tooltip(self, tooltip):
        """
        Set the tooltip that is shown when hovering over the icon in the system tray
        """
        self.tray_icon.title = tooltip

    def show_message(self, title=None, message=None):
        """
        Show a notification message balloon in the system tray
        :param title: Title that is shown at the top of the balloon
        :type title: str
        :param message: Main message to be displayed
        :type message: str
        """
        self.tray_icon.notify(title=str(title) if title is not None else '', message=str(message) if message is not None else '')

    def close(self):
        """
        Whlie not required, calling close will remove the icon from the tray right away.
        """
        self.tray_icon.visible = False      # hiding will close any message bubbles that may hold up the removal of icon from tray
        self.tray_icon.stop()

    # --------------------------- The methods below this point are not meant to be user callable ---------------------------
    def _on_clicked(self, icon, item: pystray.MenuItem):
        self.window.write_event_value(self.key, item.text)

    def _convert_psg_menu_to_tray(self, psg_menu):
        menu_items = []
        i = 0
        if isinstance(psg_menu, list):
            while i < len(psg_menu):
                item = psg_menu[i]
                look_ahead = item
                if i != (len(psg_menu) - 1):
                    look_ahead = psg_menu[i + 1]
                if not isinstance(item, list) and not isinstance(look_ahead, list):
                    disabled = False
                    if item == sg.MENU_SEPARATOR_LINE:
                        item = pystray.Menu.SEPARATOR
                    elif item.startswith(sg.MENU_DISABLED_CHARACTER):
                        disabled = True
                        item = item[1:]
                    if not (item == pystray.Menu.SEPARATOR and sg.running_linux()):
                        menu_items.append(pystray.MenuItem(item, self._on_clicked, enabled=not disabled, default=False))
                elif look_ahead != item:
                    if isinstance(look_ahead, list):
                        if menu_items is None:
                            menu_items = pystray.MenuItem(item, pystray.Menu(*self._convert_psg_menu_to_tray(look_ahead)))
                        else:
                            menu_items.append(pystray.MenuItem(item, pystray.Menu(*self._convert_psg_menu_to_tray(look_ahead))))
                i += 1
        # important item - this is where clicking the icon itself will go
        menu_items.append(pystray.MenuItem('default', self._default_action_callback, enabled=True, default=True, visible=False))

        return menu_items

    def _default_action_callback(self):
        delta = (time.time() - self.double_click_timer) * 1000
        if delta < self.DOUBLE_CLICK_THRESHOLD:  # if last click was recent, then this click is a double-click
            self.window.write_event_value(self.key, sg.EVENT_SYSTEM_TRAY_ICON_DOUBLE_CLICKED)
            self.double_click_timer = 0
        else:
            if self.single_click_events_enabled:
                self.window.write_event_value(self.key, sg.EVENT_SYSTEM_TRAY_ICON_ACTIVATED)
            self.double_click_timer = time.time()

    def _pystray_thread(self):
        self.tray_icon = pystray.Icon(self.title, self._create_image(self.icon))
        self.tray_icon.default_action = self._default_action_callback
        self.tray_icon.menu = pystray.Menu(*self.menu_items)
        self.tray_icon.title = self.tooltip  # tooltip for the icon
        self.thread_started = True
        self.tray_icon.run()

    def _create_image(self, icon):
        if isinstance(icon, bytes):
            buffer = io.BytesIO(base64.b64decode(icon))
            img = Image.open(buffer)
        elif isinstance(icon, str):
            img = Image.open(icon)
        else:
            img = None
        return img


# MM""""""""`M                                       dP
# MM  mmmmmmmM                                       88
# M`      MMMM dP.  .dP .d8888b. 88d8b.d8b. 88d888b. 88 .d8888b.
# MM  MMMMMMMM  `8bd8'  88'  `88 88'`88'`88 88'  `88 88 88ooood8
# MM  MMMMMMMM  .d88b.  88.  .88 88  88  88 88.  .88 88 88.  ...
# MM        .M dP'  `dP `88888P8 dP  dP  dP 88Y888P' dP `88888P'
# MMMMMMMMMMMM                              88
#                                           dP
# M""MMMMM""M
# M  MMMMM  M
# M  MMMMM  M .d8888b. .d8888b.
# M  MMMMM  M Y8ooooo. 88ooood8
# M  `MMM'  M       88 88.  ...
# Mb       dM `88888P' `88888P'
# MMMMMMMMMMM


def main():
    # This example shows using TWO tray icons together

    menu = ['', ['Show Window', 'Hide Window', '---', '!Disabled Item', 'Change Icon', ['Happy', 'Sad', 'Plain'], 'Exit']]
    tooltip = 'Tooltip'

    layout = [[sg.Text('My PySimpleGUI Window with a Tray Icon - X will minimize to tray')],
              [sg.Text('Note - you are running a file that is meant to be imported')],
              [sg.T('Change Icon Tooltip:'), sg.Input(tooltip, key='-IN-', s=(20,1)), sg.B('Change Tooltip')],
              [sg.Multiline(size=(60,10), reroute_stdout=False, reroute_cprint=True, write_only=True, key='-OUT-')],
              [sg.Button('Go'), sg.B('Hide Icon'), sg.B('Show Icon'), sg.B('Hide Window'), sg.B('Close Tray'), sg.Button('Exit')]]

    window = sg.Window('Window Title', layout, finalize=True, enable_close_attempted_event=True)


    tray1 = SystemTray(menu, single_click_events=False, window=window, tooltip=tooltip, icon=sg.DEFAULT_BASE64_ICON)
    tray2 = SystemTray(menu, single_click_events=False, window=window, tooltip=tooltip, icon=sg.EMOJI_BASE64_HAPPY_JOY)
    time.sleep(.5)      # wait just a little bit since TWO are being started at once
    tray2.show_message('Started', 'Both tray icons started')

    while True:
        event, values = window.read()
        print(event, values)
        # IMPORTANT step. It's not required, but convenient.
        # if it's a tray event, change the event variable to be whatever the tray sent
        # This will make your event loop homogeneous with event conditionals all using the same event variable
        if event in (tray1.key, tray2.key):
            sg.cprint(f'System Tray Event = ', values[event], c='white on red')
            tray = tray1 if event == tray1.key else tray2
            event = values[event]       # use the System Tray's event as if was from the window
        else:
            tray = tray1                # if wasn't a tray event, there's still a tray varaible used, so default to "first" tray created

        if event in (sg.WIN_CLOSED, 'Exit'):
            break

        sg.cprint(event, values)
        tray.show_message(title=event, message=values)
        tray.set_tooltip(values['-IN-'])

        if event in ('Show Window', sg.EVENT_SYSTEM_TRAY_ICON_DOUBLE_CLICKED):
            window.un_hide()
            window.bring_to_front()
        elif event in ('Hide Window', sg.WIN_CLOSE_ATTEMPTED_EVENT):
            window.hide()
            tray.show_icon()        # if hiding window, better make sure the icon is visible
            # tray.notify('System Tray Item Chosen', f'You chose {event}')
        elif event == 'Happy':
            tray.change_icon(sg.EMOJI_BASE64_HAPPY_JOY)
        elif event == 'Sad':
            tray.change_icon(sg.EMOJI_BASE64_FRUSTRATED)
        elif event == 'Plain':
            tray.change_icon(sg.DEFAULT_BASE64_ICON)
        elif event == 'Hide Icon':
            tray.hide_icon()
        elif event == 'Show Icon':
            tray.show_icon()
        elif event == 'Close Tray':
            tray.close()
        elif event == 'Change Tooltip':
            tray.set_tooltip(values['-IN-'])

    tray1.close()
    tray2.close()
    window.close()


if __name__ == '__main__':
    # Normally this file is not "run"
    main()