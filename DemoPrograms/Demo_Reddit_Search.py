import PySimpleGUI as sg
import praw  # The Reddit APIs
from webbrowser import open_new_tab

"""
    Demo Reddit Searcher

    Will search through a list of subreddits for a string of your choice.  You can search only the
    posts or the posts and comments.  When a match is found the title will be displayed in the window.
    The post details are displayed in a popup window or launched a browser tab to the post on Reddit.

    NOTE - you must register with Reddit as a developer. Instructions on doing that are below

    Copyright 2020 PySimpleGUI
"""

# To use the Reddit APIs you will need to sign up by visiting this site:
# https://www.reddit.com/prefs/apps/
# You will receive a client_id and client_secret string that you can
# enter below along with your normal Reddit ID & Password
reddit_praw_parameters = {'client_id': ' YOU MUST REGISTER ',  # get from Reddit PRAW signup
                          'client_secret': '  YOU MUST REGISTER ',  # get from Reddit PRAW signup
                          'user_agent': 'YourRedditID',  # same as user name on Reddit
                          'username': 'YourRedditID',  # same as user name on Reddit
                          'password': 'YourRedditPassword'}  # your Reddit password

# The list of subreddits to search
sub_names = ('Python', 'learnpython', 'learnprogramming', 'PySimpleGUI', 'AskProgramming', 'Coding', 'Programming')

sg.theme('Dark Red')

if reddit_praw_parameters['username'] == 'YourRedditID':
    sg.popup_error('You must register with Reddit to get credentials first',
                   'Modify the reddit_praw_parameters dictionary with the details',
                   r'Go here to register: https://www.reddit.com/prefs/apps/')
    exit()

layout = [[sg.Text('Reddit Reader')],
          [sg.Listbox(sub_names, size=(25, 7), select_mode=sg.SELECT_MODE_MULTIPLE, key='-SUBS-')],
          [sg.Text('Search for:'), sg.Input(key='-SEARCH STRING-')],
          [sg.Checkbox('Look in Comments', key='-COMMENTS-')],
          [sg.Checkbox('Show finds in browser', key='-BROWSER-')],
          [sg.Text('Limit: '), sg.Spin(list(range(100, 5000)), size=(4, 1), key='-LIMIT-')],
          [sg.Text('Now Reading Sub:'), sg.Text(size=(25, 1), key='-OUT SUB-')],
          [sg.Text('Now Reading Post:'), sg.Text(size=(40, 1), key='-OUT POST-')],
          [sg.Text('Posts Read:'), sg.Text(size=(25, 1), key='-NUM POSTS-')],
          [sg.Multiline(size=(60, 10), key='-MLINE-')],
          [sg.ProgressBar(100, orientation='horizontal', size=(30, 20), key='-PROG-')],
          [sg.Button('Start Scrape'), sg.Button('Exit')], ]

window = sg.Window('Reddit Reader', layout)

reddit = praw.Reddit(**reddit_praw_parameters)

while True:  # Event Loop
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    subs_to_read = values['-SUBS-']
    search_string = values['-SEARCH STRING-']
    if event.startswith('Start'):
        for sub in subs_to_read:
            window['-OUT SUB-'].update(sub)
            subreddit = reddit.subreddit(sub)
            submissions = subreddit.new(limit=int(values['-LIMIT-']))
            num_submissions = int(values['-LIMIT-'])
            for num, submission in enumerate(submissions):
                opened = False
                text = ''.join([t for t in submission.selftext if ord(t) in range(65536)])
                window['-PROG-'].update_bar(100 * (num + 1) // num_submissions)
                title = ''.join([t for t in submission.title if ord(t) in range(65536)])
                window['-NUM POSTS-'].update(num)
                window.refresh()
                if search_string in text:
                    opened = True
                    window['-MLINE-'].update(str(title) + '\n', append=True, autoscroll=True)
                    if values['-BROWSER-']:
                        open_new_tab(submission.url)
                    else:
                        sg.popup_scrolled(f'Found {search_string} in post', submission.url, f'\nTITLE: {title}', str(text), title=title, non_blocking=True)
                window['-OUT POST-'].update(str(title))
                if values['-COMMENTS-']:  # if should also search comments
                    comments = submission.comments
                    for comment in comments:
                        if search_string in comment.body:
                            window['-MLINE-'].update(str(title) + '\n', append=True, autoscroll=True)
                            comment = ''.join([t for t in comment.body if ord(t) in range(65536)])
                            if values['-BROWSER-']:
                                if not opened:
                                    open_new_tab(submission.url)
                                    opened = True
                            else:
                                sg.popup_scrolled(f'Found {search_string} in comment', submission.url, f'\nTITLE: {title}', comment, title=title,
                                                  non_blocking=True)
                            window.refresh()
                event, values = window.read(timeout=0)
                if event in (sg.WIN_CLOSED, 'Exit'):
                    break
            if event in (sg.WIN_CLOSED, 'Exit'):
                window['-OUT SUB-'].update('*** Aborted ***')
                break
            else:
                window['-OUT SUB-'].update('*** Done! ***')
        if event == sg.WIN_CLOSED:
            break
window.close()

