#!/usr/bin/env python
from PySimpleGUIWx import SystemTray
from PySimpleGUIWx import EVENT_SYSTEM_TRAY_ICON_DOUBLE_CLICKED
from PySimpleGUIWx import EVENT_SYSTEM_TRAY_ICON_ACTIVATED
from PySimpleGUIWx import EVENT_SYSTEM_TRAY_ICON_RIGHT_CLICK
from PySimpleGUIWx import EVENT_SYSTEM_TRAY_MESSAGE_CLICKED
import PySimpleGUIWx as sgwx
import PySimpleGUI as sg

import subprocess
import time
import re
# Import requests (to download the page)
import requests
import datetime

# Import BeautifulSoup (to parse what we download)
from bs4 import BeautifulSoup

# CCNSTANTS - CHANGE THESE TO MATCH YOUR SYSTEM
CHROME = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
DISCORD = r"C:\Users\mike\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Discord Inc\Discord.lnk"
VIEW_ISSUES_URL = r'https://github.com/MikeTheWatchGuy/PySimpleGUI/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc'
PULL_REQUEST_URL = r'https://github.com/MikeTheWatchGuy/PySimpleGUI/compare/master...Dev-latest'

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
            if issues == 0 and first_issue == 0:
                print('Read error', time.time())
                continue
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
    tray = SystemTray(menu=menu_def, data_base64=logo, tooltip='GitHub Issue Watcher')
    # tray = SystemTray(menu=menu_def, filename= ICON_FILE, tooltip='GitHub Issue Watcher')

    # tray.Hide()
    initial_issue_count, initial_first_issue = get_num_issues()
    issues = first_issue = 0
    # The Event Loop runs every 5000ms
    poll_frequncy = 5000
    seconds = 0
    print('Starting', datetime.datetime.now())

    while True:
        menu_item = tray.Read(timeout=2000)
        if menu_item == 'Exit':
            break
        if menu_item == 'Run GUI':
            tray.Update(data_base64=red_x)
            gui()
            tray.Update(data_base64=logo)
        elif menu_item == EVENT_SYSTEM_TRAY_ICON_ACTIVATED:
            tray.ShowMessage('Issue', '{} Issues\n{} First Issue'.format(issues, first_issue), messageicon=sgwx.SYSTEM_TRAY_MESSAGE_ICON_INFORMATION, )

        if seconds % 12 == 0:     # Every 60 seconds read GitHub
            issues, first_issue = get_num_issues()
            if issues != 0:
                menu_def = ['root',
                            ['{} Issues'.format(issues), '{} First Issue'.format(first_issue), '---','&View Issues Online', '&Pull Request','&Discord', '---','&Run GUI', '&Refresh',  'E&xit']]
                tray.Update(menu_def, tooltip='{} First Issue'.format(first_issue))
                # if something changed, then make a popup
                if issues != initial_issue_count or first_issue != initial_first_issue:
                    sg.Popup('Issues changed on GitHub ', 'First issue # is {}'.format(first_issue), background_color='red', keep_on_top=True)
                    initial_issue_count = issues
                    initial_first_issue = first_issue
            else:
                print('Update failed', datetime.datetime.now())
        if menu_item  in('Refresh', EVENT_SYSTEM_TRAY_ICON_DOUBLE_CLICKED):
            issues, first_issue = get_num_issues()
            tray.ShowMessage('Issue', '{} Issues\n{} First Issue'.format(issues, first_issue), messageicon=sgwx.SYSTEM_TRAY_MESSAGE_ICON_INFORMATION, )
            sp = subprocess.Popen([CHROME, VIEW_ISSUES_URL], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        elif menu_item == EVENT_SYSTEM_TRAY_MESSAGE_CLICKED or menu_item.startswith('View Issues'):
            sp = subprocess.Popen([CHROME, VIEW_ISSUES_URL], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        elif  menu_item.startswith('Pull'):
            sp = subprocess.Popen([CHROME, PULL_REQUEST_URL], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        elif  menu_item.startswith('Discord'):
            sp = subprocess.Popen([DISCORD, r''], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        seconds += poll_frequncy/1000

red_x = b"R0lGODlhEAAQAPeQAIsAAI0AAI4AAI8AAJIAAJUAAJQCApkAAJoAAJ4AAJkJCaAAAKYAAKcAAKcCAKcDA6cGAKgAAKsAAKsCAKwAAK0AAK8AAK4CAK8DAqUJAKULAKwLALAAALEAALIAALMAALMDALQAALUAALYAALcEALoAALsAALsCALwAAL8AALkJAL4NAL8NAKoTAKwbAbEQALMVAL0QAL0RAKsREaodHbkQELMsALg2ALk3ALs+ALE2FbgpKbA1Nbc1Nb44N8AAAMIWAMsvAMUgDMcxAKVABb9NBbVJErFYEq1iMrtoMr5kP8BKAMFLAMxKANBBANFCANJFANFEB9JKAMFcANFZANZcANpfAMJUEMZVEc5hAM5pAMluBdRsANR8AM9YOrdERMpIQs1UVMR5WNt8X8VgYMdlZcxtYtx4YNF/btp9eraNf9qXXNCCZsyLeNSLd8SSecySf82kd9qqc9uBgdyBgd+EhN6JgtSIiNuJieGHhOGLg+GKhOKamty1ste4sNO+ueenp+inp+HHrebGrefKuOPTzejWzera1O7b1vLb2/bl4vTu7fbw7ffx7vnz8f///wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAJAALAAAAAAQABAAAAjUACEJHEiwYEEABniQKfNFgQCDkATQwAMokEU+PQgUFDAjjR09e/LUmUNnh8aBCcCgUeRmzBkzie6EeQBAoAAMXuA8ciRGCaJHfXzUMCAQgYooWN48anTokR8dQk4sELggBhQrU9Q8evSHiJQgLCIIfMDCSZUjhbYuQkLFCRAMAiOQGGLE0CNBcZYmaRIDLqQFGF60eTRoSxc5jwjhACFWIAgMLtgUocJFy5orL0IQRHAiQgsbRZYswbEhBIiCCH6EiJAhAwQMKU5DjHCi9gnZEHMTDAgAOw=="


logo = b'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'


system_tray()
