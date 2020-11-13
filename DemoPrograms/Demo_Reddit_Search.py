import PySimpleGUI as sg
import praw  # The Reddit APIs
from webbrowser import open_new_tab

"""
    Demo Reddit Searcher

    Will search through a list of subreddits for a string(s) of your choice.  You can search only the
    posts or the posts and comments.  When a match is found the title will be displayed in the window.
    Two progress meters show the current progress.
    Once completed, a listbox is populared with he responses.  Click on the titles and a brower tab
    is opened to the topic.

    NOTE - you must register with Reddit as a developer. https://www.reddit.com/prefs/apps/ 
    You can set these credentials using the "Settings Window".

    Copyright 2020 PySimpleGUI
"""

settings = sg.UserSettings()

def make_search_row(item_number):
    search_layout = [sg.Combo(sorted(settings.get('-search string-', [])), settings['-last search-'], size=(45,1), k=('-SEARCH STRING-', item_number)),
        # sg.In(key=('-SEARCH STRING-', item_number)),
                     sg.CB('Require', key=('-SEARCH REQUIRED-', item_number))]
    return search_layout

def settings_window():
    def input_line(text, key, default):
        return [sg.T(text, size=(15,1), justification='r'), sg.In(default, size=(20,1), k=key)]

    layout = [[sg.T('Reddit PRAW Settings', font='default 15')],
              [sg.T('Note - You must register with Reddit to obtain PRAW credentials')],
              input_line('Client ID', '-CLIENT ID-', settings['client_id']),
              input_line('Client Secret', '-CLIENT SECRET-', settings['client_secret']),
              input_line('User Agent', '-USER AGENT-', settings['user_agent']),
              input_line('Username', '-USERNAME-', settings['username']),
              input_line('Password', '-PASSWORD-', settings['password']),
              [sg.CB('Clear Search History', k='-CLEAR HISTORY-')],
              ]
    layout += [[sg.Ok(), sg.Cancel()]]

    event, values = sg.Window('Reddit Reader Settings', layout).read(close=True)

    if event == 'Ok':
        settings['client_id'] = values['-CLIENT ID-']
        settings['client_secret'] = values['-CLIENT SECRET-']
        settings['user_agent'] = values['-USER AGENT-']
        settings['username'] = values['-USERNAME-']
        settings['password'] = values['-PASSWORD-']
        if values['-CLEAR HISTORY-']:
            settings['-search string-'] = []
        return True

    return False


def main():
    while True:
        # reddit_praw_parameters = settings.get_dict()
        reddit_praw_parameters = {'client_id' : settings['client_id'], 'client_secret':settings['client_secret'],
                                  'user_agent' : settings['user_agent'], 'username' : settings['username'], 'password': settings['password']}
        try:
            reddit = praw.Reddit(**reddit_praw_parameters)
            break
        except Exception as e:
            sg.popup('Problem with your settings file', e)
            if not settings_window():
                sg.popup_error('Must set settings before can continue')
                exit()

    # Read your Reddit PRAW configuration from a json file
    # try:
    #     with open(path.join(path.dirname(__file__), r'praw.cfg'), 'r') as f:
    #         reddit_praw_parameters = load(f)
    # except:
    #     sg.popup_error('Failed loading the Reddit API login credential file.', 'The File should be named:', path.join(path.dirname(__file__), r'praw.cfg'))
    #     exit()
    # To use the Reddit APIs you will need to sign up by visiting this site:
    # https://www.reddit.com/prefs/apps/
    # You will receive a client_id and client_secret string that you can
    # enter along with your normal Reddit ID & Password and save into a file named praw.cfg

    sub_names = ('Python', 'learnpython', 'learnprogramming', 'PySimpleGUI', 'madeinpython', 'AskProgramming', 'Coding', 'Programming', 'learnmachinelearning', 'MLQuestions', 'datascience', 'MachineLearning', 'pythontips', 'pystats', 'pythoncoding', 'pythondev', 'scipy')

    sg.theme('Dark Red')
    num_searches = 1
    search_layout =  [[sg.B('+'), sg.T('Add term')]]
    search_layout += [make_search_row(i) for i in range(num_searches)]
    layout = [[sg.Text('Reddit Searcher', font='Any 18')],
              [sg.Frame('Choose Subs',
                  [[sg.Listbox(sub_names, size=(25, 7), select_mode=sg.SELECT_MODE_MULTIPLE, key='-SUBS-')]]),
              sg.Frame('Options',
                        [[sg.Checkbox('Look in Comments', True, key='-COMMENTS-')],
                         [sg.Checkbox('Show finds in browser', key='-BROWSER-')],
                         [sg.Checkbox('Show popup', key='-POPUP-')],
                         [sg.Text('Limit: '), sg.Spin(list(range(200, 5000)), size=(4, 1), key='-LIMIT-')]])],
              [sg.Frame('Search Terms', search_layout, key='-SEARCH FRAME-' )],
              [sg.Frame('Status',[
                  [sg.Text('Reading Sub:'), sg.Text(size=(25, 1), key='-OUT SUB-')],
                  [sg.Text('Reading Post:'), sg.Text(size=(40, 1), key='-OUT POST-')],
                  [sg.Text('Posts Read:'), sg.Text(size=(25, 1), key='-NUM POSTS-')],
                  [sg.T('Sub Progress', size=(12,1)), sg.ProgressBar(100, orientation='horizontal', size=(30, 20), key='-PROG-')],
                  [sg.T('Overall Progress', size=(12,1)),sg.ProgressBar(100, orientation='horizontal', size=(30, 20), key='-PROG-TOTAL-')],])],
                [sg.Frame('Results (Click to Lauch in Browser)',
                  [[sg.Listbox([], size=(60,10), key='-LISTBOX-', enable_events=True)]])],
              [sg.Button('Start Search', bind_return_key=True), sg.B('Settings'), sg.Button('Exit')], ]

    window = sg.Window('Reddit Reader', layout, icon=reddit_icon, use_default_focus=False)

    results = {}
    while True:  # Event Loop
        event, values = window.read()
        if event in (None, 'Exit'):
            break
        if event == 'Settings':
            if settings_window():
                reddit = praw.Reddit(**reddit_praw_parameters)

        subs_to_read = values['-SUBS-']
        if event.startswith('Start'):
            window['-LISTBOX-'].update([''])
            results = {}
            search_list = []    # make a list of tuples (search term, bool required)
            for v in values:
                if isinstance(v, tuple):     # if value is a tuple
                    if v[0] == '-SEARCH STRING-':
                        search_list.append((values[v].lower(), values[('-SEARCH REQUIRED-', v[1])]))
                        settings['-search string-'] = list(set(settings.get('-search string-', []) + [values['-SEARCH STRING-', v[1]], ]))
            settings['-last search-'] = search_list[0][0]
            print('last search = ', settings['-last search-'])
            print('Search list = ', search_list)
            # Loop through the subs
            for sub_count, sub in enumerate(subs_to_read):
                window['-OUT SUB-'].update(sub)
                subreddit = reddit.subreddit(sub)
                submissions = subreddit.new(limit=int(values['-LIMIT-']))
                num_submissions = int(values['-LIMIT-'])
                # Loop through submissions
                for num, submission in enumerate(submissions):
                    opened = False
                    text = ''.join([t.lower() for t in submission.selftext if ord(t) in range(65536)])
                    window['-PROG-'].update_bar(100 * (num + 1) // num_submissions)
                    title = ''.join([t for t in submission.title if ord(t) in range(65536)])
                    window['-NUM POSTS-'].update(num)
                    window.refresh()
                    found = False
                    for search_item in search_list:
                        if search_item[0] and search_item[0] in text:
                            found = True
                        elif search_item[1]:
                            found = False
                            break
                    if found:
                        opened = True
                        results[title] = submission.url
                        window['-LISTBOX-'].update(list(results.keys()))
                        if values['-BROWSER-']:
                            open_new_tab(submission.url)
                        elif values['-POPUP-']:
                            sg.popup_scrolled(f'Search found', submission.url, f'\nTITLE: {title}', str(text), title=title, non_blocking=True)
                    window['-OUT POST-'].update(str(title))
                    if values['-COMMENTS-']:  # if should also search comments
                        for comment in submission.comments:
                            found = False
                            for search_item in search_list:
                                try:
                                    if search_item[0] and search_item[0] in comment.body.lower():
                                        found = True
                                    elif search_item[1]:
                                        found = False
                                        break
                                except Exception as e:
                                    print(f'Exception searching the comments:\n{e}')
                            if found:
                                results[title] = submission.url
                                window['-LISTBOX-'].update(list(results.keys()))
                                comment_text = ''.join([t for t in comment.body if ord(t) in range(65536)])
                                if values['-BROWSER-'] and not opened:
                                    open_new_tab(submission.url)
                                    opened = True
                                elif values['-POPUP-']:
                                    sg.popup_scrolled(f'Search found in comment', submission.url, f'\nTITLE: {title}', comment_text, title=title, non_blocking=True)
                                window.refresh()
                    event, values = window.read(timeout=0)
                    if event == '-LISTBOX-':            # experimental - see if clicked on an item in the list while it's still being built
                        url = results.get(values['-LISTBOX-'][0])
                        if url: open_new_tab(url)
                    if event in (None, 'Exit'):
                        break
                # Done processing the single sub, so update the total progress bar
                window['-PROG-TOTAL-'].update_bar(100 * (sub_count + 1) // len(subs_to_read))
                if event in (None, 'Exit'):
                    window['-OUT SUB-'].update('*** Aborted ***')
                    break
                else:
                    window['-OUT SUB-'].update('*** Done with this sub ***')
            else:   # if made it through the loop, then show a popup saying completed
                window['-OUT SUB-'].update('*** DONE with all subs ***')
            if event is None:
                break
        if event == '+':
            window.extend_layout(window['-SEARCH FRAME-'], [make_search_row(num_searches)])
            num_searches += 1
        if event == '-LISTBOX-':
            url = results.get(values['-LISTBOX-'][0])
            if url: open_new_tab(url)


    window.close()

if __name__ == '__main__':
    reddit_icon = b'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAKjUlEQVR42qWXCXBUVRaGz31b7+m9sxGWsOuIFrIpxSIim4gii6AgYIgwiKIUIkvGUUdZhHJBRXEQFEpENiUoq4MMiA4ICIqExAESkpCtl3S/Xl+/d++cl8GacQgTx7lVt7pev773fPec/5x7msBvHA8VvsDd0MFMD31zqSch4v77RvT7Q0wO2PDV84yxGCHkZcFgWBoOheC5oievuw/5LcafWPRniIT88F1JBNrkknOSwFk0Vavs27P9rR6PRzGZDPLlisosr88rpFIKN6PgAfp/Aby47E1StGA2+/l53nMfgKqqUFMfNSXk2iuyHFzeuX1r7cbOeS9PnjRevnCpwvblwcONFpvVJfACXzhtnPo/A7y3cRsUTB4LC4qWQUSWoWePHty0yaPpM0VLiMZn8YlkikXl0PBgMLxu1+blPn3NilfeXWg0Gpak02pK07TnHU7XUo4jfMGUMZr+ftnKd2DBvJnXB1izdjMAYzCjcGKzUK+uep9UVpezuOoEjXJQW1t9wCCZIhofH/PJuuUtenLYqGmwt3j99QFOnPyh6TPDaReLd+1/DBjMppTmSZLk93jcT4cC4U3llRdvSSjGNhyoliv18gtuh+VLu8X6aTKtNKiKcHzKlKH3HTv27VuKovgoZVFJEte2bp399Nj7hkPBzAXw3jvLrg8wf9HLBD3Abryh40Q5FtuU3749ROWoGgoFBUZp+nxJ6Smr1dwVw2rhOI6njADHASMENKCQSKVSf3d7M29xOOzE5XKnDQaDeO7cj0AIN7Zjh/ztuJbc0b8nuy6APtA+efWN9VUTxo3OMZqkeCwWN2zZVsyjJzRisfKgqcApisbxAsX46usJ1ShjkihQngeIx6nb5YIhgwcwTVO4tKqSncX7vx85fODNdrud83ldtFmAnZ//FZx2IyRTCobibN3IkUN81VVXtEvllbxkMFLgRSZeLKWq2cqlPT7C0zSu5glBYiqKwIcamdToZ2q7ToQSRrRUkuvW7aa0zWoQPy3eV+VwZOQZjSaCgmzeAx9v3weXL1fyKia0mlZrc1vlZsqRKNx0YxcaQVfn7NoAmaveJqxjW/iu6CUIizYQ0Rv6qQ1aCrovXwSGM6UQmPUIqxhdCOlohKuvbwCP2508X1qmdurU0YZh4y6WX6IL5s64FuCjrXsgOycTunRuz2/cuLXK5XRmjRo1VLlS4+frgo2k17MPgT3LSWgwAMdmLoGAPQ+4VAw0yQzWQBX027IEBJBYNCyTo3NeZ627dIG8LKe6eWuxhNuXF04b3+5KbSOs37gJFj8961qAA4e+JYFAmE0YMxg+23uUDb2rN43H07SiooaTCQee7VtI5sk9JN5rEA2NL+CAqqBqGE5KQWEcuA4Vg+PzzayqXR9SP3U6y7aZads2mcxkFMieA8f5kcP6krUbdoHXYyf3jujPrgE4evwsJ8sxOuzO3k0Adw7opfhDUSEYioAk8mD0esCQkInB5QQDip6pGsFdGNUYUTTGoiojCX+QxSURtHAEs4NnrXK9zOe20r0Hjok6QPHurwATgx96Z2/tGoB9B49zKSVJRw3r3wTQuXMHNZFIEAwbybBZwWYxELvdzAijJK2kAQ+tZwwQPRV5gqkmQCShgb+2gUUTScCUZCg6PLGDnT5zTtABNm87AGazkRs1oh+9BmDHroMQjXPw8AMDmwAwZRgvcGmT0Shk2CzgdtnB31ADsiyTnJxsEAUeeJ5HHsb0zKmtrwfgJGYy2SAcjrCUogB6R09VHp85HQDDDFVVVTBt0uhrNfDJZ19CUuHIxPsHsJ17jzzCA/ee2WJOioIgSAaRs1ms7IeSEnjj7beIHG4kAhoXBLFpbSgYYC6vj82Y/ijp2qkTjcbimJ2oDixeqWTCFIvHnpw4dvjrxXsOk3A4zCZPuKd5AH8sFwof6ASHjp+FyosVK0wm4zyrxaqiixmC8G63W9+XO/TVEThX+hNEE/opFeiSnw8D+/cHgRNYOBJGy1g3NUpSSoqPRqNrAnV1s0Sjkc15bAr7YNNOmPLgvc1XwtUf1cCsidmw45O9xOtzE38wMjMWTy7DMJgFLDa6HowGCRx2B6TVNNE1IooSlmLCGsMhUBSVYQ3BoFCGGkikkqnlWE5WNEZiahJ1oagKzCyYcP27QB9z5q+AkpLznMVsomVlZb1ycvMO9OrZzWqzmYnZbAKr2QKEE0AQCOFR6dgXECy3aFODaDSGuuG5mtoGwBkrv+zveaWqvMTltHAF0yZTXiC/iH+zAOOnLoTa6stoQMjIzcs/JkfjHRoDVVPHjR62MpVOZ+Ezyh+wBmAqUta0A483En6i6o3E63HC+bKKxWUXrrwkCfyxgsl333bw28tsRdHD0Ny4FmDKfC4elymW4bE5uW23EtH21KY1819bt3E7y8nOgWQyQdPpNEklFUilU2hcwNyW8OSCiskohSONMH3KODJq/JzVTpfn9+3yc+/2B2O7g/46btPaF2mLAJMKn8XcZ6y6snqV05M5mxL7zTs+WPCDDtD39ttRjDwTRQFrACXJpEJi8TjTRYe9nybLUbGqupIUPDyWjJn0zCDUzF/q66pfwDV/xFDxh/Zt1FoEGDyygFNTCRpPJKZm5eavb53fde6bS6e/qgMMHNAfq6Ko2axGXEkIhoFoqDkEAUy9NHrNcPbcWdABJkxbvAZTrvDShfLu2JScFkSJnPr6Y9YiQO9+94PT1wa3ByHQUPuh1+sd123QyD92tMnPowfAajFqVquRcOhvVWPYnFKWSKSwb4xR7B35kpIScvRYyapQSH4iEAy92apN+8exZsHZ06fg1NdbWtbAbQPGgWT2gWTASicabMloeK1J4sePuucO6NPnVtWRkUFcTisRUdFoH5QUJTKqPxAKswSG4/iJM8LBwydASapvf3X4yJNt27dVbLYM0PDHJ4582DJAv8EPAm9wgygy4AwZUPLjWS4vy/aU0+laOXvGgyw3t5Xm9WRwVotB718hkVShwR+CxnCUVldWCB/v2A+nvzvzWDgSWe31uHUvMW9mNnz9xfu/Lgv00WvAZHC4HND9hi4gGVWipRNMNFjuatsmb0t+fr61VW4287it2BMyjH2K1NUHtCD2DJcuXox8+NG2CdGIvN/qcGEtEemlcj8YjEY4/c22Xw+gj5UbyuBPc++AhfPnQ2lZLfgy7V7s+YszM319unbtqvTo/ju8DjhS39DISn+6oGHDKkaj8uG6Gv7uVa/NjM59dgPs3rYazp/7G/y30RwAShz0LsZiMpkNiURcW7ryXR2/V9Nb3e+o0B63dlPzWrWilVXV5OTJ70XMxH9uiO/wEjpfU12xaN3aVd9jVyvj1ymcMZxqSwC6YdPVqf/RNC9/Ze3RoXcNsPi87qbN9R6g3h+EffsP4d2gG2MwbMhA8Pm8VEmlsT/lhPqGAOz/4nBs4bzCvppGE1eNh3EqOLWr87oA/FUAe0aGQ1z83MoTQwb3txHyy5/u3nuQRsKNpRl2R+cRwwZx//5Oh0QA+fmiJ3rE4/HYVcP6TLQEwF+d8DPEi8tXP4633Kymqs/+VUfwYnpj4bxHl2B4FsXjicd/6VcCBkl4q+iZWauvGv15wn8C/ANa6jpsf0TMOwAAAABJRU5ErkJggg=='

    main()