import os.path
import subprocess
import sys
import mmap, re

import PySimpleGUI as sg

"""
    PySimpleGUI Code Finder & Launcher

    Use to filter and search your source code tree.
        Then run or edit your files

    Filter the list of :
        * Search using filename
        * Searching within the demo program's source code (like grep)
    
    The basic file operations are
        * Edit a file in your editor
        * Run a file
        * Filter file list
        * Search in files
    
    Additional operations
        * Edit this file in editor
        
    Keeps a "history" of the previously chosen folders to easy switching between projects
                
    Copyright 2021 PySimpleGUI.org
"""



def get_file_list_dict():
    """
    Returns dictionary of files
    Key is short filename
    Value is the full filename and path

    :return: Dictionary of demo files
    :rtype: Dict[str:str]
    """

    demo_path = get_demo_path()
    demo_files_dict = {}
    for dirname, dirnames, filenames in os.walk(demo_path):
        for filename in filenames:
            if filename.endswith('.py') or filename.endswith('.pyw'):
                fname_full = os.path.join(dirname, filename)
                if filename not in demo_files_dict.keys():
                    demo_files_dict[filename] = fname_full
                else:
                    # print(f'duplicate filename found {filename} path {dirname}')
                    demo_files_dict[f'{filename}_1'] = fname_full

    return demo_files_dict


def get_file_list():
    """
    Returns list of filenames of files to display
    No path is shown, only the short filename

    :return: List of filenames
    :rtype: List[str]
    """
    return list(get_file_list_dict().keys())


def get_demo_path():
    """
    Get the top-level folder path
    :return: Path to list of files using the user settings for this file.  Returns folder of this file if not found
    :rtype: str
    """
    demo_path = sg.user_settings_get_entry('-demos folder-', os.path.dirname(__file__))

    return demo_path



def get_editor():
    """
    Get the path to the editor based on user settings or on PySimpleGUI's global settings

    :return: Path to the editor
    :rtype: str
    """
    try:    # in case running with old version of PySimpleGUI that doesn't have a global PSG settings path
        global_editor = sg.pysimplegui_user_settings.get('-editor program-')
    except:
        global_editor = ''

    return sg.user_settings_get_entry('-editor program-', global_editor)


def get_theme():
    """
    Get the theme to use for the program
    Value is in this program's user settings. If none set, then use PySimpleGUI's global default theme
    :return: The theme
    :rtype: str
    """
    # First get the current global theme for PySimpleGUI to use if none has been set for this program
    try:
        global_theme = sg.theme_global()
    except:
        global_theme = sg.OFFICIAL_PYSIMPLEGUI_THEME
    # Get theme from user settings for this program.  Use global theme if no entry found
    return sg.user_settings_get_entry('-theme-', global_theme)



def find_in_file(string):
    """
    Search through the demo files for a string.
    The case of the string and the file contents are ignored

    :param string: String to search for
    :return: List of files containing the string
    :rtype: List[str]
    """

    # So you face a prediciment here. You wish to read files, both small and large; however the bigger the file/bigger the list, the longer to read the file.
    # This probably isn't what you want, right?
    # Well, we can't use a direct command line to run grep and parse. But it is an option. The user may not have it.
    # We could check if grep exists and if not use our method; but it isn't the best way.
    # So using background knowldge, we know that grep is *very* fast.
    #
    # Why?
    # Grep reads a *ton* of files into memory then searches through the memory to find the string or regex/pattern corresponding to the file.
    # How can we load a file into memory on python as fast as grep whilst keeping it universal?
    # memory mapping (mmap).
    # We can't load a lot of files into memory as we may face issues with watchdog on other operating systems. So we load one file at a time and search though there.
    # This will allow the fastest searching and loading of a file without sacrificing read times.
    # 2.8 seconds on the highend for both small and large files in memory.
    # We also don't have to iterate over lines this way.
    file_list_dict = get_file_list_dict()
    file_list = []


    for file in file_list_dict:
        try:
            full_filename = file_list_dict[file]

            with open(full_filename, 'rb', 0) as f, mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as s:
                if re.search(br'(?i)' + bytes(re.escape(string.lower()), 'utf-8'), s):
                    #                         ^^^^^^^^^-----------------------------------> re.escape
                    #                         (In case the user types ( or any other character that can be treated like a regex)
                    file_list.append(file)
        except ValueError:
            pass    # caused by an empty file so no problem skipping it
        except Exception as e:
            print(f'{file}', e)

    return list(set(file_list))


def settings_window():
    """
    Show the settings window.
    This is where the folder paths and program paths are set.
    Returns True if settings were changed

    :return: True if settings were changed
    :rtype: (bool)
    """

    editor_program = get_editor()

    layout = [[sg.T('Program Settings', font='DEFAIULT 18')],
              [sg.T('Path to Tree', size=(20,1)),
                 sg.Combo(sg.user_settings_get_entry('-folder names-', []), default_value=sg.user_settings_get_entry('-demos folder-', ''), size=(50, 1), key='-FOLDERNAME-'),
                 sg.FolderBrowse('Folder Browse', target='-FOLDERNAME-'), sg.B('Clear History')],
              [sg.T('Editor Program', size=(20,1)), sg.In(sg.user_settings_get_entry('-editor program-', editor_program),k='-EDITOR PROGRAM-'), sg.FileBrowse()],
              [sg.T(r"For PyCharm, Add this to your PyCharm main program's folder \bin\pycharm.bat")],
              [sg.Combo(['']+sg.theme_list(), sg.user_settings_get_entry('-theme-', None), k='-THEME-')],
              [sg.B('Ok', bind_return_key=True), sg.B('Cancel')],
              ]

    window = sg.Window('Settings', layout)

    settings_changed = False

    while True:
        event, values = window.read()
        if event in ('Cancel', sg.WIN_CLOSED):
            break
        if event == 'Ok':
            sg.user_settings_set_entry('-demos folder-', values['-FOLDERNAME-'])
            new_editor = editor_program if not values['-EDITOR PROGRAM-'] else values['-EDITOR PROGRAM-']
            sg.user_settings_set_entry('-editor program-', new_editor)
            new_theme = get_theme() if values['-THEME-'] == '' else values['-THEME-']
            sg.user_settings_set_entry('-theme-', new_theme)
            sg.user_settings_set_entry('-folder names-', list(set(sg.user_settings_get_entry('-folder names-', []) + [values['-FOLDERNAME-'], ])))
            settings_changed = True
            break
        elif event == 'Clear History':
            sg.user_settings_set_entry('-folder names-', [])
            sg.user_settings_set_entry('-last filename-', '')
            window['-FOLDERNAME-'].update(values=[], value='')

    window.close()
    return settings_changed


# --------------------------------- Create the window ---------------------------------
def make_window():
    """
    Creates the main window
    :return: The main window object
    :rtype: (Window)
    """

    theme = get_theme()
    if not theme:
        theme = sg.OFFICIAL_PYSIMPLEGUI_THEME
    sg.theme(theme)
    # First the window layout...2 columns

    find_tooltip = "Find in file\nEnter a string in box to search for string inside of the files.\nFile list will update with list of files string found inside."
    filter_tooltip = "Filter files\nEnter a string in box to narrow down the list of files.\nFile list will update with list of files with string in filename."

    ML_KEY = '-ML-'         # Multline's key

    left_col = [
        [sg.Listbox(values=get_file_list(), select_mode=sg.SELECT_MODE_EXTENDED, size=(50, 20), key='-DEMO LIST-')],
        [sg.Text('Filter:', tooltip=filter_tooltip), sg.Input(size=(25, 1), enable_events=True, key='-FILTER-', tooltip=filter_tooltip),
         sg.T(size=(20,1), k='-FILTER NUMBER-')],
        [sg.Button('Run'), sg.B('Edit'), sg.B('Clear')],
        [sg.Text('Find:', tooltip=find_tooltip), sg.Input(size=(25, 1), enable_events=True, key='-FIND-', tooltip=find_tooltip),
         sg.T(size=(20,1), k='-FIND NUMBER-')]]

    right_col = [
        [sg.Multiline(size=(70, 21), write_only=True, key=ML_KEY, reroute_stdout=True, echo_stdout_stderr=True)],
        [sg.Button('Edit Me (this program)'), sg.B('Settings'), sg.Button('Exit')],
        [sg.T('PySimpleGUI ver ' + sg.version.split(' ')[0] + '  tkinter ver ' + sg.tclversion_detailed, font='Default 8', pad=(0,0))],
    ]

    # ----- Full layout -----

    layout = [[sg.Text('PySimpleGUI Project File Searcher & Launcher', font='Any 20')],
              [sg.T('Click settings to set top of your tree or choose a previously chosen folder'),
               sg.Combo(sg.user_settings_get_entry('-folder names-', []), default_value=sg.user_settings_get_entry('-demos folder-', ''), size=(50, 1), key='-FOLDERNAME-', enable_events=True, readonly=True)],
              sg.vtop([sg.Column(left_col, element_justification='c'), sg.Col(right_col, element_justification='c') ])]

    # --------------------------------- Create Window ---------------------------------
    window = sg.Window('PSG Finder Launcher', layout, finalize=True, icon=icon)

    sg.cprint_set_output_destination(window, ML_KEY)
    return window
# --------------------------------- Main Program Layout ---------------------------------

def main():
    """
    The main program that contains the event loop.
    It will call the make_window function to create the window.
    """

    editor_program = get_editor()
    file_list_dict = get_file_list_dict()
    file_list = get_file_list()
    window = make_window()
    window['-FILTER NUMBER-'].update(f'{len(file_list)} files')

    while True:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, 'Exit'):
            break
        if event == 'Edit':
            for file in values['-DEMO LIST-']:
                sg.cprint(f'Editing using {editor_program}', text_color='white', background_color='red', end='')
                sg.cprint('')
                sg.cprint(f'{file_list_dict[file]}', text_color='white', background_color='purple')
                execute_command_subprocess(f'{editor_program}', f'"{file_list_dict[file]}"')
        elif event == 'Run':
            sg.cprint('Running....', c='white on green', end='')
            sg.cprint('')
            for file in values['-DEMO LIST-']:
                file_to_run = str(file_list_dict[file])
                sg.cprint(file_to_run,text_color='white', background_color='purple')
                execute_command_subprocess('python', f'{file_to_run}')
                # run_py(file_to_run)
        elif event.startswith('Edit Me'):
            sg.cprint(f'opening using {editor_program}\nThis file - {__file__}', text_color='white', background_color='green', end='')
            execute_command_subprocess(f'{editor_program}', f'"{__file__}"')
        elif event == '-FILTER-':
            new_list = [i for i in file_list if values['-FILTER-'].lower() in i.lower()]
            window['-DEMO LIST-'].update(new_list)
            window['-FILTER NUMBER-'].update(f'{len(new_list)} files')
            window['-FIND NUMBER-'].update('')
            window['-FIND-'].update('')
        elif event == '-FIND-':
            file_list = find_in_file(values['-FIND-'])
            window['-DEMO LIST-'].update(sorted(file_list))
            window['-FIND NUMBER-'].update(f'{len(file_list)} files')
            window['-FILTER NUMBER-'].update('')
            window['-FILTER-'].update('')
        elif event == 'Settings':
            if settings_window() is True:
                window.close()
                window = make_window()
                editor_program = get_editor()
                file_list_dict = get_file_list_dict()
                file_list = get_file_list()
                window['-FILTER NUMBER-'].update(f'{len(file_list)} files')
        elif event == 'Clear':
            window['-FILTER-'].update('')
            window['-FILTER NUMBER-'].update(f'{len(file_list)} files')
            window['-FIND-'].update('')
            window['-DEMO LIST-'].update(file_list)
            window['-FIND NUMBER-'].update('')
        elif event == '-FOLDERNAME-':
            sg.user_settings_set_entry('-demos folder-', values['-FOLDERNAME-'])
            file_list_dict = get_file_list_dict()
            file_list = get_file_list()
            window['-DEMO LIST-'].update(values=file_list)
            window['-FILTER NUMBER-'].update(f'{len(file_list)} files')


    window.close()



def execute_command_subprocess(command, *args, wait=False):

    if sys.platform == 'linux':
        arg_string = ''
        for arg in args:
            arg_string += ' ' + str(arg)
        sp = subprocess.Popen(['python3' + arg_string, ], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    else:
        expanded_args = ' '.join(args)
        sp = subprocess.Popen([command, expanded_args], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if wait:
        out, err = sp.communicate()
        if out:
            print(out.decode("utf-8"))
        if err:
            print(err.decode("utf-8"))


if __name__ == '__main__':
    # https://www.vecteezy.com/free-vector/idea-bulb is where I got the icon

    icon = b'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAACXBIWXMAAAsSAAALEgHS3X78AAAK/2lUWHRYTUw6Y29tLmFkb2JlLnhtcAAAAAAAPD94cGFja2V0IGJlZ2luPSLvu78iIGlkPSJXNU0wTXBDZWhpSHpyZVN6TlRjemtjOWQiPz4NCjx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDUuMy1jMDA3IDEuMTM2ODgxLCAyMDEwLzA2LzEwLTE4OjExOjM1ICAgICAgICAiPg0KICA8cmRmOlJERiB4bWxuczpyZGY9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiPg0KICAgIDxyZGY6RGVzY3JpcHRpb24gcmRmOmFib3V0PSIiIHhtbG5zOnhtcE1NPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvbW0vIiB4bWxuczpzdEV2dD0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL3NUeXBlL1Jlc291cmNlRXZlbnQjIiB4bWxuczpkYz0iaHR0cDovL3B1cmwub3JnL2RjL2VsZW1lbnRzLzEuMS8iIHhtbG5zOnhtcD0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wLyIgeG1wTU06RG9jdW1lbnRJRD0iRUM4REZFNUEyMEM0QjcwMzFBMjNBRDA4NENCNzZCODAiIHhtcE1NOk9yaWdpbmFsRG9jdW1lbnRJRD0iRUM4REZFNUEyMEM0QjcwMzFBMjNBRDA4NENCNzZCODAiIHhtcE1NOkluc3RhbmNlSUQ9InhtcC5paWQ6OUVBNkIyNzA3NjYyRTkxMThDQzNFODdFN0ZEQTgwNTEiIGRjOmZvcm1hdD0iaW1hZ2UvanBlZyIgeG1wOlJhdGluZz0iNSIgeG1wOk1ldGFkYXRhRGF0ZT0iMjAxOS0wNC0xOVQxMjoxMTozOSswNDozMCI+DQogICAgICA8eG1wTU06SGlzdG9yeT4NCiAgICAgICAgPHJkZjpTZXE+DQogICAgICAgICAgPHJkZjpsaSBzdEV2dDphY3Rpb249InNhdmVkIiBzdEV2dDppbnN0YW5jZUlEPSJ4bXAuaWlkOkYwNjRBQzcwNzY2MkU5MTFBNkU1QzYwODhFRTUxMzM5IiBzdEV2dDp3aGVuPSIyMDE5LTA0LTE5VDEyOjExOjM5KzA0OjMwIiBzdEV2dDpzb2Z0d2FyZUFnZW50PSJBZG9iZSBQaG90b3Nob3AgQ2FtZXJhIFJhdyA3LjAiIHN0RXZ0OmNoYW5nZWQ9Ii9tZXRhZGF0YSIgLz4NCiAgICAgICAgICA8cmRmOmxpIHN0RXZ0OmFjdGlvbj0ic2F2ZWQiIHN0RXZ0Omluc3RhbmNlSUQ9InhtcC5paWQ6OUVBNkIyNzA3NjYyRTkxMThDQzNFODdFN0ZEQTgwNTEiIHN0RXZ0OndoZW49IjIwMTktMDQtMTlUMTI6MTE6MzkrMDQ6MzAiIHN0RXZ0OnNvZnR3YXJlQWdlbnQ9IkFkb2JlIFBob3Rvc2hvcCBDYW1lcmEgUmF3IDcuMCAoV2luZG93cykiIHN0RXZ0OmNoYW5nZWQ9Ii9tZXRhZGF0YSIgLz4NCiAgICAgICAgPC9yZGY6U2VxPg0KICAgICAgPC94bXBNTTpIaXN0b3J5Pg0KICAgICAgPGRjOnRpdGxlPg0KICAgICAgICA8cmRmOkFsdD4NCiAgICAgICAgICA8cmRmOmxpIHhtbDpsYW5nPSJ4LWRlZmF1bHQiPkJ1bGIgSWNvbiBEZXNpZ248L3JkZjpsaT4NCiAgICAgICAgPC9yZGY6QWx0Pg0KICAgICAgPC9kYzp0aXRsZT4NCiAgICAgIDxkYzpjcmVhdG9yPg0KICAgICAgICA8cmRmOlNlcT4NCiAgICAgICAgICA8cmRmOmxpPklZSUtPTjwvcmRmOmxpPg0KICAgICAgICA8L3JkZjpTZXE+DQogICAgICA8L2RjOmNyZWF0b3I+DQogICAgICA8ZGM6ZGVzY3JpcHRpb24+DQogICAgICAgIDxyZGY6QWx0Pg0KICAgICAgICAgIDxyZGY6bGkgeG1sOmxhbmc9IngtZGVmYXVsdCI+QnVsYiBJY29uIERlc2lnbg0KPC9yZGY6bGk+DQogICAgICAgIDwvcmRmOkFsdD4NCiAgICAgIDwvZGM6ZGVzY3JpcHRpb24+DQogICAgICA8ZGM6c3ViamVjdD4NCiAgICAgICAgPHJkZjpCYWc+DQogICAgICAgICAgPHJkZjpsaT5idWxiPC9yZGY6bGk+DQogICAgICAgICAgPHJkZjpsaT5lbmVyZ3k8L3JkZjpsaT4NCiAgICAgICAgICA8cmRmOmxpPmlkZWE8L3JkZjpsaT4NCiAgICAgICAgICA8cmRmOmxpPmxpZ2h0PC9yZGY6bGk+DQogICAgICAgICAgPHJkZjpsaT5saWdodGJ1bGI8L3JkZjpsaT4NCiAgICAgICAgICA8cmRmOmxpPmJ1bGIgaWNvbjwvcmRmOmxpPg0KICAgICAgICAgIDxyZGY6bGk+ZW5lcmd5IGljb248L3JkZjpsaT4NCiAgICAgICAgICA8cmRmOmxpPmlkZWEgaWNvbjwvcmRmOmxpPg0KICAgICAgICAgIDxyZGY6bGk+bGlnaHQgaWNvbjwvcmRmOmxpPg0KICAgICAgICAgIDxyZGY6bGk+bGlnaHRidWxiIGljb248L3JkZjpsaT4NCiAgICAgICAgICA8cmRmOmxpPmljb248L3JkZjpsaT4NCiAgICAgICAgICA8cmRmOmxpPmlsbHVzdHJhdGlvbjwvcmRmOmxpPg0KICAgICAgICAgIDxyZGY6bGk+ZGVzaWduPC9yZGY6bGk+DQogICAgICAgICAgPHJkZjpsaT5zaWduPC9yZGY6bGk+DQogICAgICAgICAgPHJkZjpsaT5zeW1ib2w8L3JkZjpsaT4NCiAgICAgICAgICA8cmRmOmxpPmdyYXBoaWM8L3JkZjpsaT4NCiAgICAgICAgICA8cmRmOmxpPmxpbmU8L3JkZjpsaT4NCiAgICAgICAgICA8cmRmOmxpPmxpbmVhcjwvcmRmOmxpPg0KICAgICAgICAgIDxyZGY6bGk+b3V0bGluZTwvcmRmOmxpPg0KICAgICAgICAgIDxyZGY6bGk+ZmxhdDwvcmRmOmxpPg0KICAgICAgICAgIDxyZGY6bGk+Z2x5cGg8L3JkZjpsaT4NCiAgICAgICAgICA8cmRmOmxpPmdyYWRpZW50PC9yZGY6bGk+DQogICAgICAgICAgPHJkZjpsaT5jaXJjbGU8L3JkZjpsaT4NCiAgICAgICAgICA8cmRmOmxpPnNoYWRvdzwvcmRmOmxpPg0KICAgICAgICAgIDxyZGY6bGk+bG93IHBvbHk8L3JkZjpsaT4NCiAgICAgICAgICA8cmRmOmxpPnBvbHlnb25hbDwvcmRmOmxpPg0KICAgICAgICAgIDxyZGY6bGk+c3F1YXJlPC9yZGY6bGk+DQogICAgICAgIDwvcmRmOkJhZz4NCiAgICAgIDwvZGM6c3ViamVjdD4NCiAgICA8L3JkZjpEZXNjcmlwdGlvbj4NCiAgPC9yZGY6UkRGPg0KPC94OnhtcG1ldGE+DQo8P3hwYWNrZXQgZW5kPSJyIj8+ncdlNwAABG5JREFUWMPtV2tMk1cYfr6vINBRKpVLpVIuGZfOjiARochYO/EyMWHDjOIYYSyQ6MaignEkEgJLyNxMRthmJBkalKmgUacsjMiCBRFWqKsBFJEwtkILLYxBuQi0/c5+sE5mJmvBxR/zJO+fc877vE/ey5NzKEIInuWi8YzXcwIrInCtuirlWnVVykowHGy9qFYqo+bn5pyj4uIarXtBope6H7+nbGp6dZWT0+yGqCjlUyUQEBTUW15SkiOOiLj9/eXLu1sVN6Q6jUYIAD5CoUYilSleT0q6dLO+fmvmwYOfP/UScN3df+cLBIPvbN92fWpijJedtk5XWQT6TM5PkR9Izrw72ZpRkRrr/yvfhz/MXe02aSsuZYsOMAxDH87MPMlfJxjcn7OnitWReg7GjrDH75ktQGkVMDz/csdnFReSWZzgnmVnwGwyOSbLpI1davWGY/n5xaFhYR2HPko/zWrb0vBPwQHAgQXkpgKhvM6wY+/HNXU1X0xOlkkbzSaT4xMZEEKeaDPT02xVy62YrKQ3rxDGQltubmq31NDEFsuUUKTthPjezNQkZ6kYS/aAC5s9U1lWti+36OMCMvxtEsZVG22tbU4qhW8u3hU5G69vX3YTMgxDD/T3B4SIxZ1EVyW3Z75D/IABPcBoq+XLJjA0MOArDAj4GQAwcSfCXpERegO6PnXEsglMTU1xXN3cjAtdaXSz7s/MAl19gHZKqNGOAF0634GZOQcz3GNaF/u7soHpyUd+dhPw8PQ06HVDPgAA57W6v2aXAgrKCBrazKyGzrVDBSfmHSn/vWXU6si2xf6GMWCN9yM/u5VwjZeXYdSg9559+JDt5LWzlvw5fi5OQFoChS+qtAK88GLv/rzs4+zASBVpkd2w+s7OASPjgEfQztoVCdH5k+WZo3q994e5WV8zivXdMI3xFsYX2H2YAC4C7ZXbGl/SvqsWhrodVr+vLgAeXryxt4vviuDkZVi2FMsz3julutWyuV31IJgKr0gHxbJYyyDfRkH+ik6AcWX04uDt9wDVfdoiP1SRvlRwmwjQNM2UVlamfZKXd7T3t4B+SvxltvWMRS8YmDkn616vBvj0NFB66ng2i5/w3b+OylIqtdi0Go0wMUbSOjQ4KGB6CossNTSpPrBgzKhCaqmhibaCJokiigw2FxbZimszAUIIutTq8D3xW36wmE0OFmVC7WICpqs0SQmnSOf5hFpCGMpWTAd7hGV9ePgdiVSmyNu7r8zPx3egU7XQwCOl51J/URJItr5xVZxYcgCgbH9q25MBQgiM4+NcmUjUrair23FJFtt81hnkrDPIZhZIf37eUXvx7H4TcrjcCZ6nx0hsfHx9nEzWsJEGImiAC8B1leP8f/Ym/JvEctwm5a/JFMyQzsc0T4EBwIuK/pGbkVVuN5i9KSOE4C2ZVMFYLPRI4ZHiHjbIfTbILhbISOGRYnuxqOV8zaL9/TR+gYF98w96Qs3DQ3wA0HO4xmalctOq4JAee7Co53/D/z2BPwAlMRlLdQS6SQAAAABJRU5ErkJggg=='
    main()