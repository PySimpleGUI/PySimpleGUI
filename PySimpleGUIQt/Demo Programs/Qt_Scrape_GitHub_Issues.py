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
            [sg.T('', key='_numissues_', size=(18, 1))],
              ]

    window = sg.Window('Issue watcher',
                       no_titlebar=True,
                       grab_anywhere=True,
                       keep_on_top=True,
                       alpha_channel=.8,        # dim the lights a little
                       location=(2360,310),     # locate in upper right corner of screen
                       element_padding=(0,0)
                       ).Layout(layout).Finalize()

    window.Refresh()
    status_elem = window.FindElement('_status_')
    issues_elem = window.FindElement('_numissues_')

    initial_issue_count, initial_first_issue = get_num_issues()
    # The Event Loop runs every 5000ms
    poll_frequncy = 5000
    seconds = 0
    while True:
        # read with a 5 second timeout
        event, values = window.Read(timeout=poll_frequncy)
        # print(event, values)
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

red_x = b"R0lGODlhEAAQAPeQAIsAAI0AAI4AAI8AAJIAAJUAAJQCApkAAJoAAJ4AAJkJCaAAAKYAAKcAAKcCAKcDA6cGAKgAAKsAAKsCAKwAAK0AAK8AAK4CAK8DAqUJAKULAKwLALAAALEAALIAALMAALMDALQAALUAALYAALcEALoAALsAALsCALwAAL8AALkJAL4NAL8NAKoTAKwbAbEQALMVAL0QAL0RAKsREaodHbkQELMsALg2ALk3ALs+ALE2FbgpKbA1Nbc1Nb44N8AAAMIWAMsvAMUgDMcxAKVABb9NBbVJErFYEq1iMrtoMr5kP8BKAMFLAMxKANBBANFCANJFANFEB9JKAMFcANFZANZcANpfAMJUEMZVEc5hAM5pAMluBdRsANR8AM9YOrdERMpIQs1UVMR5WNt8X8VgYMdlZcxtYtx4YNF/btp9eraNf9qXXNCCZsyLeNSLd8SSecySf82kd9qqc9uBgdyBgd+EhN6JgtSIiNuJieGHhOGLg+GKhOKamty1ste4sNO+ueenp+inp+HHrebGrefKuOPTzejWzera1O7b1vLb2/bl4vTu7fbw7ffx7vnz8f///wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAJAALAAAAAAQABAAAAjUACEJHEiwYEEABniQKfNFgQCDkATQwAMokEU+PQgUFDAjjR09e/LUmUNnh8aBCcCgUeRmzBkzie6EeQBAoAAMXuA8ciRGCaJHfXzUMCAQgYooWN48anTokR8dQk4sELggBhQrU9Q8evSHiJQgLCIIfMDCSZUjhbYuQkLFCRAMAiOQGGLE0CNBcZYmaRIDLqQFGF60eTRoSxc5jwjhACFWIAgMLtgUocJFy5orL0IQRHAiQgsbRZYswbEhBIiCCH6EiJAhAwQMKU5DjHCi9gnZEHMTDAgAOw=="


gui()
