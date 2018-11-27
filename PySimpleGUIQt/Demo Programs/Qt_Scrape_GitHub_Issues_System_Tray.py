#!/usr/bin/env python
import PySimpleGUIQt as sg

import re
# Import requests (to download the page)
import requests

# Import BeautifulSoup (to parse what we download)
from bs4 import BeautifulSoup

# search github for total open issues and Issue Number of first issue
def get_num_issues():
    url = "https://github.com/MikeTheWatchGuy/PySimpleGUI/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc"
    # set the headers like we are a browser,
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    # download the page
    response = requests.get(url, headers=headers)
    # parse the downloaded homepage and grab all text,
    soup = BeautifulSoup(response.text, "lxml")
    # look for phrase "XXX Open"
    findopen = re.compile(r"\d+ Open")
    # get number of open issues
    number_open_string = findopen.search(str(soup)).group(0)
    num_open_issues = number_open_string[0:number_open_string.index(' ')]
    # find the first issue in the list by earing for "issue-id-XXXX"
    find_first_issue = re.compile(r'issue-id-\d+')
    first_issue_string = find_first_issue.search(str(soup)).group(0)
    first_issue = first_issue_string[9:]
    return num_open_issues, first_issue


def gui():
    sg.ChangeLookAndFeel('Topanga')

    sg.SetOptions(border_width=0)

    layout = [
            [sg.T('GitHub Issues Watcher' + 5 * ' ', click_submits=True, key='GitHub'),
            sg.Button('', size=(25,25),
                          image_data=red_x,
                          key='_quit_',button_color=(sg.LOOK_AND_FEEL_TABLE['Topanga']['TEXT'],sg.LOOK_AND_FEEL_TABLE['Topanga']['BACKGROUND']),
                          tooltip='Closes window')],
            [sg.T('', key='_status_', size=(12, 1))],
            [sg.T('', key='_numissues_', size=(20, 1))],
              ]

    window = sg.Window('Issue watcher',
                       no_titlebar=True,
                       grab_anywhere=True,
                       keep_on_top=True,
                       alpha_channel=.8,        # dim the lights a little
                       location=(2360,310),     # locate in upper right corner of screen
                       ).Layout(layout).Finalize()

    window.Refresh()
    status_elem = window.FindElement('_status_')
    issues_elem = window.FindElement('_numissues_')

    initial_issue_count, initial_first_issue = get_num_issues()
    seconds = 0
    poll_frequncy = 1000
    while True:
        event, values = window.Read(timeout=poll_frequncy)
        if event in ('_quit_', None):
            break
        if seconds % 60 == 0 or event.startswith('GitHub'):     # Every 60 seconds read GitHub
            status_elem.Update('Reading...')
            window.Refresh()
            issues, first_issue = get_num_issues()
            issues_elem.Update('{} Issues. {} is first issue'.format(issues, initial_first_issue))
            window.Refresh()
            # if something changed, then make a popup
            if issues != initial_issue_count or first_issue != initial_first_issue:
                sg.PopupNoWait('Issues changed on GitHub ', 'First issue # is {}'.format(first_issue), background_color='red', keep_on_top=True)
                initial_issue_count = issues
                initial_first_issue = first_issue
            status_elem.Update('')
        else:
            status_elem.Update('.' if seconds%2 else '')  # blink a '.' every 2 seconds so know still running

        seconds += poll_frequncy/1000
    window.Close()



def system_tray():

    menu_def = ['Root',
                ['E&xit']]
    tray = sg.SystemTray(data_base64=logo, tooltip='GitHub Issue Watcher')

    # tray.Hide()
    initial_issue_count, initial_first_issue = get_num_issues()
    # The Event Loop runs every 5000ms
    poll_frequncy = 5000
    seconds = 0
    while True:
        menu_item = tray.Read(timeout=5000)
        if menu_item == 'Exit':
            break
        if menu_item == 'Run GUI':
            gui()
        if seconds % 12 == 0:     # Every 60 seconds read GitHub
            issues, first_issue = get_num_issues()
            menu_def = ['root',
                        ['{} Issues'.format(issues), '{} First Issue'.format(first_issue), '---', '&Run GUI', '&Refresh',  'E&xit']]
            tray.Update(menu_def, tooltip='{} First Issue'.format(first_issue))
            # if something changed, then make a popup
            if issues != initial_issue_count or first_issue != initial_first_issue:
                sg.PopupNoWait('Issues changed on GitHub ', 'First issue # is {}'.format(first_issue), background_color='red', keep_on_top=True)
                initial_issue_count = issues
                initial_first_issue = first_issue
        if menu_item  in('Refresh', sg.EVENT_SYSTEM_TRAY_ICON_DOUBLE_CLICKED):
            issues, first_issue = get_num_issues()
            tray.ShowMessage('Issue', '{} Issues\n{} First Issue'.format(issues, first_issue), messageicon=sg.SYSTEM_TRAY_MESSAGE_ICON_INFORMATION, )
            tray.Update(data_base64=red_x)

        seconds += poll_frequncy/1000

red_x = b"R0lGODlhEAAQAPeQAIsAAI0AAI4AAI8AAJIAAJUAAJQCApkAAJoAAJ4AAJkJCaAAAKYAAKcAAKcCAKcDA6cGAKgAAKsAAKsCAKwAAK0AAK8AAK4CAK8DAqUJAKULAKwLALAAALEAALIAALMAALMDALQAALUAALYAALcEALoAALsAALsCALwAAL8AALkJAL4NAL8NAKoTAKwbAbEQALMVAL0QAL0RAKsREaodHbkQELMsALg2ALk3ALs+ALE2FbgpKbA1Nbc1Nb44N8AAAMIWAMsvAMUgDMcxAKVABb9NBbVJErFYEq1iMrtoMr5kP8BKAMFLAMxKANBBANFCANJFANFEB9JKAMFcANFZANZcANpfAMJUEMZVEc5hAM5pAMluBdRsANR8AM9YOrdERMpIQs1UVMR5WNt8X8VgYMdlZcxtYtx4YNF/btp9eraNf9qXXNCCZsyLeNSLd8SSecySf82kd9qqc9uBgdyBgd+EhN6JgtSIiNuJieGHhOGLg+GKhOKamty1ste4sNO+ueenp+inp+HHrebGrefKuOPTzejWzera1O7b1vLb2/bl4vTu7fbw7ffx7vnz8f///wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAJAALAAAAAAQABAAAAjUACEJHEiwYEEABniQKfNFgQCDkATQwAMokEU+PQgUFDAjjR09e/LUmUNnh8aBCcCgUeRmzBkzie6EeQBAoAAMXuA8ciRGCaJHfXzUMCAQgYooWN48anTokR8dQk4sELggBhQrU9Q8evSHiJQgLCIIfMDCSZUjhbYuQkLFCRAMAiOQGGLE0CNBcZYmaRIDLqQFGF60eTRoSxc5jwjhACFWIAgMLtgUocJFy5orL0IQRHAiQgsbRZYswbEhBIiCCH6EiJAhAwQMKU5DjHCi9gnZEHMTDAgAOw=="


logo = b'iVBORw0KGgoAAAANSUhEUgAAADIAAAAtCAMAAADbYcjNAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAMAUExURQAAADBpmDFqmDBqmTFqmjJrmzJsmzJsnDNtnTRrmjVtmjZsmzRunTRunjVvnzdwnjVwnzpxnzVwoDZxoTdyojlyoThzozhzpDh0pDp1pjp2pj51ozt3qDt4qDx4qDx5qj16qj57rD58rT98rkF1oEB4pUB4pkR6pkJ6qEN8q0B9rUB9rkB+rkV7qUZ8qUp9p0x+p0h/rEB+sEeArkqArEqBr0uCrkKAsUKAskOCs0OCtESCtEWEtkaFuEaGuE2FsUiHukiIukmJvEmKvEqLvkuMvk2KuUyLvEyMv1OErVWDqlWHr1qHrVaIsVCMvFSPvV2LsViOuVSQvmyUtmyXuXKbvXefv3ugv06NwE6OwFmUwl2XxGScyGmbw22hynikxnmmyv/UO//UPP/VPf/UPv/VP//UQP/VQf/VQv/WQP/WQf/WQv/WQ//XRP/WRf/WSf/YRf/YRv/YR//YSP/ZSf/ZSv/aS//aTP/aTf/bTv/YUf/ZUv/bUP/cUP/cUv/dVP/dVv/eVv/bW//dWf/cWv/eWP/fWv/dXf/fXf/eXv/cYP/fYP/dZP/dZv/eZf/fZv/eaP/gW//gXP/gXv/gYP/iYf/iYv/hZP/jZP/iZv/kZv/jaf/ja//kaP/lav/kbP/lb//mbP/mbv/ncP/mcv/iff/ocv/odP/odv/oeP/of//qf4GnxYOox4SoxYSpx4asyo+ux4isyouuyouvzIyuyYyvy4yvzI6wy46wzIyz0pCuyJSxyZWyy5u3zZ24zpW30pG52J250J+60aC60KS90aDC3a3E163F2K3F2bPI2bvO3rzP3qvJ4LHN4rnR5P/qgf/qgv/qiP/sif/sjf/sj//olf/ql//ulv/omf/qnv/tnP/qoP/ro//qpP/sov/upf/tqP/uqP/vrf/vrv/us//wpP/wpv/xrf/wsP/wsv/ys//xtP/ytf/ytv/zuf/zuv/0vP/0vsDS38XZ6cnb6f/xw//zwv/yxf/1w//zyP/1yf/2zP/3z//30wAAAM55ho4AAAEAdFJOU////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////wBT9wclAAAACXBIWXMAABcQAAAXEAEYYRHbAAAAGHRFWHRTb2Z0d2FyZQBwYWludC5uZXQgNC4xLjFjKpxLAAADnElEQVRIS62OeVhUZRSHw6IosQzGBgoIszKXqGylghKwbHErNVPbEFQQTXYogzZtt2SmiSEHnBHJPdM2Ldv3xbW91Pay0tT29dc53znfvTP809Pz9P7x3Xvu8773fHvhP/M/JBce0GX/8/WduX3ipDt/1nclNrk4TnhR5y1FVzHX/KqzISY5Uou4uLVm/sgEzF1mFqKTruozL9D8gfrM1aIwbvJaF7WFJ4FJqgtb1XOTN1R1eBqYrLbwvpo2+SF2B/NEbFNY+IWoNum6t0UD4imgTO3CCROKiqaJqsnx8fHx+7ho/RBALsnFxcUlJSWlNxpXkkv2I/a1uPnLWEA626WlU6aUlf3uJomJiccdlJDAoQvFBwPsklw2deq06dNnO8nIbj3oHE4hkWDQ7HVcSzLb5eXlFRWVTtKj+/P8OJDojfO6Wahfi3uMW1FZWVVVVV39jk2Skl6RR9JhwOjunDJUPYfZ1q6uqampvcUmWZ4sOpcnJ9Pj8WQqHYAZ4tbW1tXV19ffbJNXPZ6sUUM8nqOBRzweT7LDBQDZdcYmZlz3rk2wNCUlxes9iXYcwlBmOAq4W12moeE2liXBg9QcA6yiB+P1eqk8FtgmdoOh8SbjaoJlqacAj6ZqYqBffCJyo+GGO0S1CVYDKw8VUg0nAJ87NnOrmk4CPJYmSNeHdjQ2Xm/kmcx9qkUlKzKU9PT0tLSTaYeVZ84i/KpFJQ9nZmYermRknAh8qu6sOU1EUDXCJit6UuJwFu1gm+WmJp/PR7f6xr9NVE2eOYLoaeEdVvb5/H7/XOC7QCDwoXE16d+L4IzpC3xmZLb99wYC9wPbm5mP2ZVkRH9DP0OvK/CLcUkmmpvn0Y5gsKWlJRRykwEOXAJBI5NNBNtoRyhEJxa3bnKS005ltBoAqGz+3E47Qq2tO9gLR+jQJAbaItdgWhdje1tbOPwHe5GFdEhyuiE7O1sTkQ1t4fZwOBKJbCTt6/lfOsllZ0TzE9rZpV8bORKZz2z46q2ODpYlwZmCJFfiTyuL3WHZzK4ma7QRgJ2dZcG4mmBoriEnJ4eSc4BvO9vMe0a1CQZKIwwDdqkWxRIxnWT9QOJsITd3KN1NRRc1nQTrzs3L40y4CNitprLwbxXdBD/mM3nCWPoQs+cBkYioBLi8oMBk+flcAHtUJ942HwwxCd4cM2hQATFO5+81WPSbfmBiE+Cl8ZcOHvusDsBfG+hKm/foJHRO/hXgH831bVAP1oP5AAAAAElFTkSuQmCC'


system_tray()
