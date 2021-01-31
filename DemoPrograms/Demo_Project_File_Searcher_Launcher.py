import os.path
import subprocess
import sys

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
                
    Copyright 2021 PySimpleGUI.org
"""



def get_demo_git_files():
    """
    Get the files in the demo and the GitHub folders
    Returns files as 2 lists

    :return: two lists of files
    :rtype: Tuple[List[str], List[str]]
    """

    demo_path = get_demo_path()
    demo_files_dict = {}
    for dirname, dirnames, filenames in os.walk(demo_path):
        for filename in filenames:
            if filename.endswith('.py'):
                fname_full = os.path.join(dirname, filename)
                if filename not in demo_files_dict.keys():
                    demo_files_dict[filename] = fname_full
                else:
                    # print(f'duplicate filename found {filename} path {dirname}')
                    demo_files_dict[f'{filename}_1'] = fname_full

    return demo_files_dict


def get_demo_path():
    demo_path = sg.user_settings_get_entry('-demos folder-', os.path.dirname(__file__))

    return demo_path


def get_editor():
    try:    # in case running with old version of PySimpleGUI that doesn't have a global PSG settings path
        global_editor = sg.pysimplegui_user_settings.get('-editor program-')
    except:
        global_editor = ''

    return sg.user_settings_get_entry('-editor program-', global_editor)


def get_theme():
    try:
        global_theme = sg.theme_global()
    except:
        global_theme = sg.theme()

    return sg.user_settings_get_entry('-theme-', global_theme)

def find_in_file(string):
    """
    Search through the demo files for a string.
    The case of the string and the file contents are ignored

    :param string: String to search for
    :return: List of files containing the string
    :rtype: List[str]
    """

    demo_files_dict = get_demo_git_files()
    string = string.lower()
    file_list = []
    for file in demo_files_dict:
        full_filename = demo_files_dict[file]
        try:
            with open(full_filename, 'r', encoding="utf8") as f:
                for line in f.readlines():
                    if string in line.lower():
                        file_list.append(file)
                        # print(f'{os.path.basename(file)} -- {line}')
        except Exception as e:
            pass
            print(f'{file}',e)
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
              [sg.T('Path to Demos', size=(20,1)), sg.In(sg.user_settings_get_entry('-demos folder-', '.'), k='-DEMOS-'), sg.FolderBrowse()],
              [sg.T('Editor Program', size=(20,1)), sg.In(sg.user_settings_get_entry('-editor program-', editor_program),k='-EDITOR PROGRAM-'), sg.FileBrowse()],
              [sg.T(r"For PyCharm, Add this to your PyCharm main program's folder \bin\pycharm.bat")],
              [sg.Combo(['']+sg.theme_list(), sg.user_settings_get_entry('-theme-', None), k='-THEME-')],
              [sg.B('Ok', bind_return_key=True), sg.B('Cancel')],
              ]

    window = sg.Window('Settings', layout)
    event, values = window.read(close=True)
    if event == 'Ok':
        sg.user_settings_set_entry('-demos folder-', values['-DEMOS-'])
        new_editor = editor_program if not values['-EDITOR PROGRAM-'] else values['-EDITOR PROGRAM-']
        sg.user_settings_set_entry('-editor program-', new_editor)
        new_theme = get_theme() if values['-THEME-'] == '' else values['-THEME-']
        sg.user_settings_set_entry('-theme-', new_theme)
        return True

    return False

# --------------------------------- Create the window ---------------------------------
def make_window():
    """
    Creates the main window
    :return: The main window object
    :rtype: (Window)
    """

    theme = get_theme()
    editor = get_editor()
    demo_files_dict = get_demo_git_files()
    if not theme:
        theme = sg.OFFICIAL_PYSIMPLEGUI_THEME
    sg.theme(theme)
    # First the window layout...2 columns

    find_tooltip = "Find in file\nEnter a string in box to search for string inside of the files.\nFile list will update with list of files string found inside."
    filter_tooltip = "Filter files\nEnter a string in box to narrow down the list of files.\nFile list will update with list of files with string in filename."

    ML_KEY = '-ML-'         # Multline's key

    left_col = [
        [sg.Listbox(values=list(demo_files_dict.keys()), select_mode=sg.SELECT_MODE_EXTENDED, size=(40, 20), key='-DEMO LIST-')],
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
              [sg.T('Click settings to set top of your tree')],
              sg.vtop([sg.Column(left_col, element_justification='c'), sg.Col(right_col, element_justification='c') ])]

    # --------------------------------- Create Window ---------------------------------
    window = sg.Window('PSG Finder Launcher', layout)

    sg.cprint_set_output_destination(window, ML_KEY)
    return window
# --------------------------------- Main Program Layout ---------------------------------

def main():
    """
    The main program that contains the event loop.
    It will call the make_window function to create the window.
    """

    editor_program = get_editor()
    demo_files_dict = get_demo_git_files()
    demo_files = demo_files_dict.keys()
    window = make_window()

    while True:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, 'Exit'):
            break
        if event == 'Edit':
            for file in values['-DEMO LIST-']:
                sg.cprint(f'Editing using {editor_program}', text_color='white', background_color='red', end='')
                sg.cprint('')
                sg.cprint(f'{demo_files_dict[file]}', text_color='white', background_color='purple')
                execute_command_subprocess(f'{editor_program}', f'"{demo_files_dict[file]}"')
        elif event == 'Run':
            sg.cprint('Running....', c='white on green', end='')
            sg.cprint('')
            sg.cprint(f"Chose {values['-DEMO LIST-']}")
            for file in values['-DEMO LIST-']:
                file_to_run = str(demo_files_dict[file])
                sg.cprint(file_to_run,text_color='white', background_color='purple')
                execute_command_subprocess('python', f'{file_to_run}')
                # run_py(file_to_run)
        elif event.startswith('Edit Me'):
            sg.cprint(f'opening using {editor_program}\nThis file - {__file__}', text_color='white', background_color='green', end='')
            execute_command_subprocess(f'{editor_program}', f'"{__file__}"')
        elif event == '-FILTER-':
            new_list = [i for i in demo_files if values['-FILTER-'].lower() in i.lower()]
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
                demo_files_dict = get_demo_git_files()
                demo_files = demo_files_dict.keys()
        elif event == 'Clear':
            window['-FILTER-'].update('')
            window['-FIND-'].update('')
            window['-DEMO LIST-'].update(demo_files)
            window['-FILTER NUMBER-'].update('')
            window['-FIND NUMBER-'].update('')

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


    main()
