#!/usr/bin/env python
import PySimpleGUIWx as sg
import subprocess
import re
# Import requests (to download the page)
import requests
import datetime
import time

# Import BeautifulSoup (to parse what we download)
from bs4 import BeautifulSoup

# CCNSTANTS - CHANGE THESE TO MATCH YOUR SYSTEM
CHROME = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
DISCORD = r"C:\Users\mike\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Discord Inc\Discord.lnk"
VIEW_ISSUES_URL = r'https://github.com/MikeTheWatchGuy/PySimpleGUI/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc'
PULL_REQUEST_URL = r'https://github.com/MikeTheWatchGuy/PySimpleGUI/compare/master...Dev-latest'
ANNOUCEMENTS = r'https://github.com/MikeTheWatchGuy/PySimpleGUI/issues/142'
TRAFFIC = r'https://github.com/MikeTheWatchGuy/PySimpleGUI/graphs/traffic'
SEARCH = r'https://github.com/search?o=desc&q=pysimplegui&s=indexed&type=Code'
PYPI_STATS = r'https://pepy.tech/project/pysimplegui'
ICON_FILE = r'C:\Python\PycharmProjects\GooeyGUI\default_icon.ico'

# search github for total open issues and Issue Number of first issue
def get_num_issues():
    url = "https://github.com/MikeTheWatchGuy/PySimpleGUI/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc"
    # set the headers like we are a browser,
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    # download the page
    requests.adapters.DEFAULT_RETRIES = 25
    try:
        response = requests.get(url, headers=headers)
    except:
        return 0,0
    # parse the downloaded homepage and grab all text,
    soup = BeautifulSoup(response.text, "lxml")
    # look for phrase "XXX Open"
    # print(soup)
    findopen = re.compile(r"\d+ Open")
    # get number of open issues
    number_open_string = findopen.search(str(soup)).group()
    num_open_issues = number_open_string[0:number_open_string.index(' ')]
    # find the first issue in the list by earing for "issue-id-XXXX"
    soup = str(soup).replace('\n', '')
    find_first_issue = re.compile(r'#\d+\s+opened')
    first_issue_string = find_first_issue.search(str(soup)).group()
    first_issue = first_issue_string[1:first_issue_string.find(' ')]
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
            if issues == 0 and first_issue == 0:
                print('Read error', time.time())
                continue
            issues_elem.Update('{} Issues. {} is first issue'.format(issues, first_issue))
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
    tray = sg.SystemTray(menu=menu_def, data_base64=logo, tooltip='GitHub Issue Watcher')
    # tray = SystemTray(menu=menu_def, filename= ICON_FILE, tooltip='GitHub Issue Watcher')

    # tray.Hide()
    initial_issue_count, initial_first_issue = get_num_issues()
    tray.ShowMessage('Starting up...', '{} Issues\n{} First Issue'.format(initial_issue_count, initial_first_issue),
                     messageicon=sg.SYSTEM_TRAY_MESSAGE_ICON_CRITICAL, )
    issues = first_issue = 0
    # The Event Loop runs every 5000ms
    poll_frequncy = 5000
    seconds = 0
    print('Starting', datetime.datetime.now())
    while True:
        menu_item = tray.Read(timeout=poll_frequncy)
        if menu_item == 'Exit':
            break
        if menu_item == 'Run GUI':
            tray.Update(data_base64=red_x)
            gui()
            tray.Update(data_base64=logo)
        elif menu_item.startswith('View Issues'):
            sg.PopupNoWait('Refreshing issue data...', auto_close=True, auto_close_duration=3)
            issues, first_issue = get_num_issues()
            tray.ShowMessage('Refreshed', '{} Issues\n{} First Issue'.format(issues, first_issue), messageicon=sg.SYSTEM_TRAY_MESSAGE_ICON_INFORMATION, )
            sp = subprocess.Popen([CHROME, VIEW_ISSUES_URL], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        elif menu_item  in('Refresh', sg.EVENT_SYSTEM_TRAY_ICON_DOUBLE_CLICKED):
            tray.ShowMessage('Refreshing', 'Old values are\n{} Issues\n{} First Issue'.format(issues, first_issue), messageicon=sg.SYSTEM_TRAY_MESSAGE_ICON_NOICON )
            tray.Update(data_base64=red_x)
            issues, first_issue = get_num_issues()
            tray.ShowMessage('Refreshed', '{} Issues\n{} First Issue'.format(issues, first_issue), messageicon=sg.SYSTEM_TRAY_MESSAGE_ICON_CRITICAL, )
            tray.Update(data_base64=logo)
        # elif menu_item == sg.EVENT_SYSTEM_TRAY_ICON_ACTIVATED:
        #     tray.ShowMessage('Last check', '{} Issues\n{} First Issue'.format(issues, first_issue), messageicon=sg.SYSTEM_TRAY_MESSAGE_ICON_INFORMATION, )
        elif menu_item == sg.EVENT_SYSTEM_TRAY_MESSAGE_CLICKED :
            tray.Update(data_base64=logo)
            sp = subprocess.Popen([CHROME, VIEW_ISSUES_URL], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        elif  menu_item.startswith('Pull'):
            sp = subprocess.Popen([CHROME, PULL_REQUEST_URL], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        elif  menu_item.startswith('Announcements'):
            sp = subprocess.Popen([CHROME, ANNOUCEMENTS], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        elif  menu_item.startswith('Traffic'):
            sp = subprocess.Popen([CHROME, TRAFFIC], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        elif  menu_item.startswith('Search'):
            sp = subprocess.Popen([CHROME, SEARCH], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        elif  menu_item.startswith('Discord'):
            sp = subprocess.Popen([DISCORD, r''], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        elif  menu_item.startswith('PyPI'):
            sp = subprocess.Popen([CHROME, PYPI_STATS], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


        if seconds % 12 == 0:     # Every 60 seconds read GitHub
            issues, first_issue = get_num_issues()
            if issues != 0:
                menu_def = ['root',
                            ['{} Issues'.format(issues), '{} First Issue'.format(first_issue), '---','&View Issues Online', '&Pull Request','---', 'Announcements', 'Traffic', 'PyPI Stats', 'Search for Project' , '&Discord', '---','&Run GUI', '&Refresh',  'E&xit']]
                tray.Update(menu_def, tooltip='{} First Issue'.format(first_issue))
                # if something changed, then make a popup
                if issues != initial_issue_count or first_issue != initial_first_issue:
                    sg.PopupNonBlocking('Issues changed on GitHub ', 'First issue # is {}'.format(first_issue), background_color='red', keep_on_top=True, grab_anywhere=True)
                    initial_issue_count = issues
                    initial_first_issue = first_issue
                    tray.Update(data_base64=logo32x32red)
                    tray.ShowMessage('Issues changes!', '{} Issues\n{} First Issue'.format(issues, first_issue), messageicon=sg.SYSTEM_TRAY_MESSAGE_ICON_CRITICAL, )

            else:

                sg.PopupNonBlocking('Update error at: ',  datetime.datetime.now(),
                                    background_color='red', keep_on_top=True, grab_anywhere=True)
                print('Update failed', datetime.datetime.now())

        seconds += poll_frequncy/1000

red_x = b"R0lGODlhEAAQAPeQAIsAAI0AAI4AAI8AAJIAAJUAAJQCApkAAJoAAJ4AAJkJCaAAAKYAAKcAAKcCAKcDA6cGAKgAAKsAAKsCAKwAAK0AAK8AAK4CAK8DAqUJAKULAKwLALAAALEAALIAALMAALMDALQAALUAALYAALcEALoAALsAALsCALwAAL8AALkJAL4NAL8NAKoTAKwbAbEQALMVAL0QAL0RAKsREaodHbkQELMsALg2ALk3ALs+ALE2FbgpKbA1Nbc1Nb44N8AAAMIWAMsvAMUgDMcxAKVABb9NBbVJErFYEq1iMrtoMr5kP8BKAMFLAMxKANBBANFCANJFANFEB9JKAMFcANFZANZcANpfAMJUEMZVEc5hAM5pAMluBdRsANR8AM9YOrdERMpIQs1UVMR5WNt8X8VgYMdlZcxtYtx4YNF/btp9eraNf9qXXNCCZsyLeNSLd8SSecySf82kd9qqc9uBgdyBgd+EhN6JgtSIiNuJieGHhOGLg+GKhOKamty1ste4sNO+ueenp+inp+HHrebGrefKuOPTzejWzera1O7b1vLb2/bl4vTu7fbw7ffx7vnz8f///wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAJAALAAAAAAQABAAAAjUACEJHEiwYEEABniQKfNFgQCDkATQwAMokEU+PQgUFDAjjR09e/LUmUNnh8aBCcCgUeRmzBkzie6EeQBAoAAMXuA8ciRGCaJHfXzUMCAQgYooWN48anTokR8dQk4sELggBhQrU9Q8evSHiJQgLCIIfMDCSZUjhbYuQkLFCRAMAiOQGGLE0CNBcZYmaRIDLqQFGF60eTRoSxc5jwjhACFWIAgMLtgUocJFy5orL0IQRHAiQgsbRZYswbEhBIiCCH6EiJAhAwQMKU5DjHCi9gnZEHMTDAgAOw=="


logo = b'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'

logo32x32red = b'R0lGODlhIQAgAPcAAAAAADBpmDBqmTFqmjJrmzJsnDNtnTRrmTZtmzZumzRtnTdunDRunTRunjVvnzdwnzhwnjlxnzVwoDZxoTdyojhzozl0ozh0pDp1pjp2pjp2pzx0oj12pD52pTt3qD54pjt4qDx4qDx5qTx5qj16qj57qz57rD58rT98rkB4pkJ7q0J9rEB9rkF+rkB+r0d9qkZ/rEl7o0h8p0x9pk5/p0l+qUB+sEyBrE2Crk2Er0KAsUKAskSCtEeEtUWEtkaGuEiHuEiHukiIu0qKu0mJvEmKvEqLvk2Nv1GErVGFr1SFrVGHslaHsFCItFSIs1COvlaPvFiJsVyRuWCNsWSPsWeQs2SQtGaRtW+Wt2qVuGmZv3GYuHSdv3ievXyfvV2XxGWZwmScx2mfyXafwHikyP9gWP5pYJmdt6GbrqakuamgsayovYClw4Ory4SszI+vyoSv0JGvx5SzzJi0y5m2zp++16C6z6a/05/A2qHC3aXB2K3I3brP4MKxvsLU48LV5c3a5QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAP8ALAAAAAAhACAAAAj/AP8JHEiwoMGDCA1uoYIFYZmHZhIe9HIggEUBdgo+3FhGIsEqAiyKXDBnIEeOHgHFEMkyQII4/07KTEijpU01MWWiNDhDgM+fNhHg1Llz4BQCBAYoXar0p4ABaHISJXjnQYMIBbJq1YoUKYQ+UnUOVLJBoBUGaCMoMMB2a4EuYWcKlCBnoAMHMv5lacC3bwMGV+LK5cBEIJ0JKQTWkMC4MeM3gk8KZGPhRpTKApFQoDChs2cOAoluHDjmwoUX//wkMX2hgmvXHUKL7kiQSw6BOFjrvvBBtuiETjQI15ABg/EQvqce5JMjhHPnIEB4UJFcLsIlJEiM2L5dBIzq1gv+p2liwkSJ8+hXgN85mqAUFPBPyJffYj1KyQL12HDB3wWL/yxoEdl9+P1Thw4I6mDDggu2MSBt7eUkUB07VGihhW48GJZJtO3RAw8ggmghGQ/+NhAYPqToQ4g8QFGicgMBoeKMPqTxYoEE/aDjjjuecWOEBMExhBBBFFnkD0Cs8WNCeBRBhBBQRvmEfUAi9IURRWRZxJQciuWRQHmEccQRYhgU3pdofhkQADs='

system_tray()
