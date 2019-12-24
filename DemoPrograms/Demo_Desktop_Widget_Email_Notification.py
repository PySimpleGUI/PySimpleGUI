#!/usr/bin/env python
import PySimpleGUI as sg
import email
import imaplib
from datetime import datetime
import calendar

'''
    Usage of Notification in PSG
'''

IMAP_SERVER_GMAIL = 'imap.gmail.com'            # gmail server address
IMAP_SERVER_HOTMAIL = 'imap-mail.outlook.com'   # hotmail server address
################# Change these to match your email setup ################
LOGIN_EMAIL = 'you@mail.com'
LOGIN_PASSWORD = 'your email password'
# change to match your email service
IMAP_SERVER = IMAP_SERVER_GMAIL
MAX_EMAILS = 10


def gui():
    sg.theme('Topanga')
    sg.set_options(border_width=0, margins=(0, 0), element_padding=(4, 0))
    color = ('#282923', '#282923')
    layout = [[sg.Text('Email New Mail Notification' + 48 * ' '),
               sg.Button('', image_data=refresh,
                    button_color=color,
                    key='-refresh-',
                    tooltip='refreshes Email'),
               sg.Button('', image_data=red_x,
                    button_color=color,
                    key='-quit-',
                    tooltip='Closes window')],
              [sg.Text('', key='-status-', size=(25, 1))], ]

    for i in range(MAX_EMAILS):
        layout.append([sg.Text('', size=(20, 1), key='{}date'.format(i), font='Sans 8'),
                       sg.Text('', size=(45, 1), font='Sans 8', key='{}from'.format(i))])

    window = sg.Window('',
                       layout,
                       no_titlebar=True,
                       grab_anywhere=True,
                       keep_on_top=True,
                       alpha_channel=0,
                       finalize=True)

    # move the window to the upper right corner of the screen
    w, h = window.get_screen_dimensions()
    window.move(w - 410, 0)
    window.set_alpha(.9)
    window.refresh()

    status_elem = window['-status-']

    while True:
        status_elem.update('Reading...')
        window.refresh()
        read_mail(window)
        status_elem.update('')
        # return every 30 seconds
        event, values = window.read(timeout=30 * 1000)
        if event == '-quit-':
            break


def read_mail(window):
    """
    Reads late emails from IMAP server and displays them in the Window
    :param window: window to display emails in
    :return:
    """
    mail = imaplib.IMAP4_SSL(IMAP_SERVER)

    (retcode, capabilities) = mail.login(LOGIN_EMAIL, LOGIN_PASSWORD)
    mail.list()
    typ, data = mail.select('Inbox')
    n = 0
    now = datetime.now()
    # get messages from today
    search_string = '(SENTON {}-{}-{})'.format(now.day,
                                               calendar.month_abbr[now.month], now.year)
    (retcode, messages) = mail.search(None, search_string)
    if retcode == 'OK':
        # message numbers are separated by spaces, turn into list
        msg_list = messages[0].split()
        msg_list.sort(reverse=True)  # sort messages descending
        for n, message in enumerate(msg_list):
            if n >= MAX_EMAILS:
                break

            from_elem = window['{}from'.format(n)]
            date_elem = window['{}date'.format(n)]
            from_elem.update('')  # erase them so you know they're changing
            date_elem.update('')
            window.refresh()

            typ, data = mail.fetch(message, '(RFC822)')
            for response_part in data:
                if isinstance(response_part, tuple):

                    original = email.message_from_bytes(response_part[1])
                    date_str = original['Date'][:22]

                    from_elem.update(original['From'])
                    date_elem.update(date_str)
                    window.refresh()  # make the window changes show up right away


red_x = "R0lGODlhEAAQAPeQAIsAAI0AAI4AAI8AAJIAAJUAAJQCApkAAJoAAJ4AAJkJCaAAAKYAAKcAAKcCAKcDA6cGAKgAAKsAAKsCAKwAAK0AAK8AAK4CAK8DAqUJAKULAKwLALAAALEAALIAALMAALMDALQAALUAALYAALcEALoAALsAALsCALwAAL8AALkJAL4NAL8NAKoTAKwbAbEQALMVAL0QAL0RAKsREaodHbkQELMsALg2ALk3ALs+ALE2FbgpKbA1Nbc1Nb44N8AAAMIWAMsvAMUgDMcxAKVABb9NBbVJErFYEq1iMrtoMr5kP8BKAMFLAMxKANBBANFCANJFANFEB9JKAMFcANFZANZcANpfAMJUEMZVEc5hAM5pAMluBdRsANR8AM9YOrdERMpIQs1UVMR5WNt8X8VgYMdlZcxtYtx4YNF/btp9eraNf9qXXNCCZsyLeNSLd8SSecySf82kd9qqc9uBgdyBgd+EhN6JgtSIiNuJieGHhOGLg+GKhOKamty1ste4sNO+ueenp+inp+HHrebGrefKuOPTzejWzera1O7b1vLb2/bl4vTu7fbw7ffx7vnz8f///wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAJAALAAAAAAQABAAAAjUACEJHEiwYEEABniQKfNFgQCDkATQwAMokEU+PQgUFDAjjR09e/LUmUNnh8aBCcCgUeRmzBkzie6EeQBAoAAMXuA8ciRGCaJHfXzUMCAQgYooWN48anTokR8dQk4sELggBhQrU9Q8evSHiJQgLCIIfMDCSZUjhbYuQkLFCRAMAiOQGGLE0CNBcZYmaRIDLqQFGF60eTRoSxc5jwjhACFWIAgMLtgUocJFy5orL0IQRHAiQgsbRZYswbEhBIiCCH6EiJAhAwQMKU5DjHCi9gnZEHMTDAgAOw=="
refresh = 'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAACb0lEQVR4XpVTXUiTbxT/vePdFuF0BTFW9ufVvMlu+iACka6CQY1gQVdtEmTMpSKzzJT/RTdCRHhT4F0Us8LGVqlo1lZaFslWQWBkN+tDkpSpbfNz797T8zy6DbUbf/Dbec7vfOycMwa0DBJjM7Ko72mBtz+KplCS6Ronf3NNxNZBt2qv4dJzL0uKwGRqU/6zHDqyd1dBk32/xMnfXOMxkVPXXYlVSLjykk4fKIb/4zgUSxEO7zRBKd4Bjm/jU9ys8f2fJoCFhRiWl6pw6+Qw0BymhlfT5Lg/xmycHA++ktL+nsRqrUOrdpBpH6hhKC7yhObti0CgKUTu0KTgcd8X4j4aB2bYvj7UPqkQrO/1cU25ESV3eJJO8LzLIQ11/CYXn5Grf4KqGF19E3Ts9iixe2QPm0dtt5PtP6NcHxF5ZVfDhIbeqMQ6E0hcI4ec327jah513T4YDM5TR/dh8vc0hkfHUxI2gwuPKyDLb2wV5cIdePuZZGwWmQxSSyqICFBVyKgJJkFaQW4Hna4THQ4X/gUiD2+QXEwjNZsASJvTgWgMqoY95WWw7raAJdjheeTEeniCTqgZu2IxswnSmGI3gEZjMiQpAMocTC2nJcm4hU9gRjp9E+6Ajb07wKFpHqRVOzKqedFUhOX4HyRnEwSjMQCB8/4IqnxU2DYiaGnsIe7n2UlK61MWe0dbW18Ijdfk/wuy7IXeEEvEvmM+kcRM4XYYSkohW62ChtIS/NKbWGwO8z9+Anp9TNSsQU2wEtVdEZy5o7Gfi7Z5ewj/vxbkPs51kYhVP4zAw3I3IN+ohSVFcfZeEs67Gid/c03E1uEv5QpTFzvZK5EAAAAASUVORK5CYII='
gui()
