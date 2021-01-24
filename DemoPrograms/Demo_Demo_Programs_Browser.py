import os.path
import subprocess
import sys

import PySimpleGUI as sg

"""
    Demo Browser
    
    Makes using the Demo Programs each even more powerful.
    Now you can quickly filter and search to find the demo you need.
    You can launch editing the demo using your favorite editor.
    
    On first run, click settings button to enter location of your demo programs.
    
    Filter the list of demos using:
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

    demo_path = sg.user_settings_get_entry('-demos folder-', '.')

    try:
        demo_files = os.listdir(demo_path)
    except:
        demo_files = []

    return demo_files


def find_in_file(string):
    """
    Search through the demo files for a string.
    The case of the string and the file contents are ignored

    :param string: String to search for
    :return: List of files containing the string
    :rtype: List[str]
    """

    demo_path = sg.user_settings_get_entry('-demos folder-')
    demo_files = get_demo_git_files()
    string = string.lower()
    file_list = []
    for file in demo_files:
        filename = os.path.join(demo_path, file)
        try:
            with open(filename, 'r') as f:
                for line in f.readlines():
                    if string in line.lower():
                        file_list.append(file)
                        # print(f'{os.path.basename(file)} -- {line}')
        except Exception as e:
            pass
            # print(e)
    return list(set(file_list))


def settings_window():
    """
    Show the settings window.
    This is where the folder paths and program paths are set.
    Returns True if settings were changed

    :return: True if settings were changed
    :rtype: (bool)
    """

    layout = [[sg.T('Program Settings', font='DEFAIULT 18')],
              [sg.T('Path to Demos', size=(20,1)), sg.In(sg.user_settings_get_entry('-demos folder-', '.'), k='-DEMOS-'), sg.FolderBrowse()],
              [sg.T('Editor Program', size=(20,1)), sg.In(sg.user_settings_get_entry('-Editor Program-', ''),k='-EDITOR PROGRAM-'), sg.FileBrowse()],
              [sg.T(r"For PyCharm, Add this to your PyCharm main program's folder \bin\pycharm.bat")],
              [sg.Combo(sg.theme_list(), sg.user_settings_get_entry('-theme-', None), k='-THEME-')],
              [sg.B('Ok', bind_return_key=True), sg.B('Cancel')],
              ]

    window = sg.Window('Settings', layout)
    event, values = window.read(close=True)
    if event == 'Ok':
        sg.user_settings_set_entry('-demos folder-', values['-DEMOS-'])
        sg.user_settings_set_entry('-Editor Program-', values['-EDITOR PROGRAM-'])
        sg.user_settings_set_entry('-theme-', values['-THEME-'])
        return True

    return False

# --------------------------------- Create the window ---------------------------------
def make_window():
    """
    Creates the main window
    :return: The main window object
    :rtype: (Window)
    """

    theme = sg.user_settings_get_entry('-theme-')
    demo_files = get_demo_git_files()
    if not theme:
        theme = sg.OFFICIAL_PYSIMPLEGUI_THEME
    sg.theme(theme)
    # First the window layout...2 columns

    find_tooltip = "Find in file\nEnter a string in box to search for string inside of the files.\nFile list will update with list of files string found inside."
    filter_tooltip = "Filter files\nEnter a string in box to narrow down the list of files.\nFile list will update with list of files with string in filename."

    ML_KEY = '-ML-'         # Multline's key

    left_col = [
        [sg.Listbox(values=demo_files, select_mode=sg.SELECT_MODE_EXTENDED, size=(40, 20), key='-DEMO LIST-')],
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

    layout = [[sg.Text('Demo Programs Browser', font='Any 20')],
              [sg.T('Click settings to specify location of demo files')],
                sg.vtop([sg.Column(left_col, element_justification='c'),sg.Col(right_col, element_justification='c') ])]

    # --------------------------------- Create Window ---------------------------------
    window = sg.Window('PySimpleGUI Demo Program Browser', layout, icon=icon)

    sg.cprint_set_output_destination(window, ML_KEY)
    return window
# --------------------------------- Main Program Layout ---------------------------------

def main():
    """
    The main program that contains the event loop.
    It will call the make_window function to create the window.
    """

    demo_path = sg.user_settings_get_entry('-demos folder-', '.')
    editor_program = sg.user_settings_get_entry('-Editor Program-', '')
    demo_files = get_demo_git_files()

    window = make_window()

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Exit':
            break
        if event == 'Edit':
            for file in values['-DEMO LIST-']:
                sg.cprint(f'opening (in editor)', text_color='white', background_color='red', end='')
                sg.cprint('')
                sg.cprint(f'{os.path.join(demo_path, file)}', text_color='white', background_color='purple')
                execute_command_subprocess(f'{editor_program}', os.path.join(demo_path, file))
        elif event == 'Run':
            sg.cprint('Running Demo Programs....', c='white on green', end='')
            sg.cprint('')
            for file in values['-DEMO LIST-']:
                sg.cprint(os.path.join(demo_path, file),text_color='white', background_color='purple')
                run_py(os.path.join(demo_path, file))
        elif event.startswith('Edit Me'):
            sg.cprint(f'opening using {editor_program}\nThis file - {__file__}', text_color='white', background_color='green', end='')
            execute_command_subprocess(f'{editor_program}', __file__)
        elif event == '-FILTER-':
            new_list = [i for i in demo_files if values['-FILTER-'].lower() in i.lower()]
            window['-DEMO LIST-'].update(new_list)
            window['-FILTER NUMBER-'].update(f'{len(new_list)} files')
            window['-FIND NUMBER-'].update('')
        elif event == '-FIND-':
            file_list = find_in_file(values['-FIND-'])
            window['-DEMO LIST-'].update(sorted(file_list))
            window['-FIND NUMBER-'].update(f'{len(file_list)} files')
            window['-FILTER NUMBER-'].update('')
        elif event == 'Settings':
            if settings_window() is True:
                window.close()
                window = make_window()
                demo_path = sg.user_settings_get_entry('-demos folder-')
                editor_program = sg.user_settings_get_entry('-Editor Program-')
                demo_files = get_demo_git_files()
        elif event == 'Clear':
            window['-FILTER-'].update('')
            window['-FIND-'].update('')
            window['-DEMO LIST-'].update(demo_files)
            window['-FILTER NUMBER-'].update('')
            window['-FIND NUMBER-'].update('')

    window.close()


def run(app_name, parm=''):
    execute_command_subprocess(app_name, parm)


def run_py(pyfile, parms=None):
    if parms is not None:
        execute_command_subprocess('python', pyfile, parms)
    else:
        execute_command_subprocess('python', pyfile)


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

    icon = b'iVBORw0KGgoAAAANSUhEUgAAAgAAAAIACAYAAAD0eNT6AAAACXBIWXMAAAsSAAALEgHS3X78AAAbWElEQVR4nO3d/XEUx7rA4elb/h9uBOAIkCMARwAnAkQExhEYR2AcAXIEhggQERwRwYEIDkTQpwa37EWspP2Yj7e7n6dKZR9X3ctqdtn+TU9PT8o5D0tLKT0ahuHt4n8wwLSe5ZzPHFNq9H/eNYCDvUopnTp81EgAABxHBFAlAQBwPBFAdQQAwDREAFURAADTEQFUQwAATEsEUAUBADA9EUB4AgBgHiKA0AQAwHxEAGEJAIB5iQBCEgAA8xMBhCMAAJYhAghFAAAsRwQQhgAAWJYIIAQBALA8EcDqBADAOkQAqxIAAOsRAaxGAACsSwSwCgEAsD4RwOIEAEAMIoBFCQCAOEQAixEAALGIABYhAADiEQHMTgAAxCQCmJUAAIhLBDAbAQAQmwhgFgIAID4RwOQEAEAdRACTEgAA9RABTEYAANRFBDAJAQBQHxHA0QQAQJ1EAEcRAAD1EgEc7DuHbvgxwGsA1nMyDMNvFR//MQKGnPNZgNdCRboPgJzzeYCXAaznPKX0aRxIK34PRAB7cwkA6F4ZOJ9VfhxcDmAvAgBABNAhAQBQiAB6IgAANogAeiEAAK4QAfRAAABsIQJonQAAuIYIoGUCAOAGIoBWCQCAW4gAWiQAAHYgAmiNAADYkQigJQIAYA8igFYIAIA9iQBaIAAADiACqJ0AADiQCKBmAgDgCCKAWgkAgCOJAGokAAAmIAKojQAAmIgIoCYCAGBCIoBaCACAiYkAaiAAAGYgAohOAADMRAQQmQAAmJEIICoBADAzEUBEAgBgASKAaAQAwEJEAJEIAIAFiQCiEAAACxMBRCAAAFYgAlibAABYiQhgTQIAYEUigLUIAICViQDWIAAAAhABLE0AAAQhAliSAAAIRASwFAEAEIwIYAkCACAgEcDcBABAUCKAOQkAgMBEAHMRAADBiQDmIAAAKiACmJoAAKiECGBKAgCgIiKAqQgAgMqIAKYgAAAqJAI4lgAAqJQI4BgCAKBiIoBDCQCAyokADiEAABogAtiXAABohAhgHwIAoCEigF0JAIDGiAB2IQAAGiQCuI0AAGiUCOAmAgCgYSKA6wgAgMaJALYRAAAdEAFcJQAAOiEC2CQAADoiArgkAAA6IwIYBABAn0QAAgCgUyKgbwIAoGMioF8CAKBzIqBPAgAAEdAhAQDAFyKgLwIAgL+JgH4IAAC+IgL6IAAA+IYIaJ8AAGArEdA2AQDAtURAuwQAADcSAW0SAADcSgS0RwAAsBMR0BYBAMDOREA7BAAAexEBbRAAAOxNBNRPAABwEBFQNwEAwMFEQL0EAABHEQF1EgAAHE0E1EcAADAJEVAXAQDAZERAPQQAAJMSAXUQAABMTgTEJwAAmIUIiE0AADAbERCXAABgViIgJgEAwOxEQDwCAIBFiIBYBAAAixEBcQgAABYlAmIQAAAsTgSsTwAAsAoRsC4BAMBqRMB6BAAAqxIB6xAAAKxOBCxPAAAQgghYlgAAIAwRsBwBAEAoImAZAgCAcETA/AQAACGJgHkJAADCEgHzEQAAhCYC5iEAAAhPBExPAABQBREwLQEAQDVEwHQEAABVEQHT+G7NPxx6k1K6PwzD5s/dYRhONg7D+O939jws74dh+FT+/UP5Gf/3xfjPnPOFDxqtGSMgpTT+Vq8q/tXGCLgMmsWlnPPyf2hKj4ZheLvGL3xVzjlFeB20pQz0Jxs/4/9+sOIv+bGEwXn554UwoAXlLLrmCBj9sMbfRzMAMIEStZc/h5zFz+1e+Xl4+eeUs6d3JQrGL5/znPOntV4gHKKRmYC7a/yhAgAOkFIaB/knZcB/WPExfHglCt6XIHidcz5f96XBbhqJgMUJANhBSuluGeyflJ9oZ/hTeVB+fkopfb6MgRIEZgcISwTsz10AcIOU0pOU0jgA/ncYhj+HYXja8OB/1fh7Pi5fqP8dj8N4vbXEEITTyN0BixEAcMU4vZ9SGs8mPpVB/7Fj9MVmDJyVdQ8QigjYnQCAMsWfUnqeUhpXyP+7szP9Q4zH5+14vMpxMytAGCJgNwKAro23641ns+XWuN/KSnl2d68ct8tZgRPHjghEwO0EAF0ap6/LwP8fZ/uTGY/jv1NK5y4PEIEIuJkAoCtl4D8vG1E99e7P4mG5PCAEWJ0IuJ4AoAtXBv6a79uviRAgBBGwnQCgaRvX+A3869kMgfu9HgTWJQK+JQBoUlnV/2LjGj/rG0PgP2WxoLsGWJwI+JoAoDnl4SDjqv5fvLshjUH25fbB3g8EyxMB/xAANKNM95+XzWqs6o9tfH9+SylduHWQpYmAvwgAmrAx3e86f10elFsHX/R+IFjWWs/gj0QAULWybe+F6f7q/WI2AJYlAKhWuYb873IWSf3MBsCCBADVKSv8z8sWtLTncjbALYMwIwFAVcqGMh9c62/eOBswRsCT3g8EzEUAUI0yNfzWCv9ujO/znymll70fCJiDACC8MuX/2kK/bv1UdhG0eRBMSAAQWrkOPF7vf+yd6trDcknAXQIwEQFAWOXL/sIqf4p7Ywx6sBBMQwAQUtnO99z1fq64Ux4sdOrAwHEEAOGUL3fb+XKTV54lAMcRAIRSvtRfeVfYwW/lUc/AAb5z0IiifJl7dC/7eJpSGvd1d0kA9mQGgBAM/hzhqZkA2J8AYHUGfyYgAmBPAoBVGfyZkAiAPQgAVlMW/Bn8mZIIgB0JAFZRbvXzND/m8NQ+AXA7dwGwuI37/PnHu/Jv486Hnzb++/mWY7S5E964P/7l9riekPiPV+XuALMBcA0BwKLK9r49P93tfRnUP5TB/iLn/GmH/7tN26Lgb2Wr3PslDE46DoMxAsbjexHgtUA4AoDFlKe59ba977vyO5/nnG8cuKey7c8pUXD501MQfHl2gAiAbwkAFtHZ4P9mGIbx8cWvDzi7n0WJgi9hUN6LMQSelJ+W35PxdzsrERDivYAoBABLedn4U/3CDfrXKa/vdfm5XJPxpOFHLo+fu7PyOwKFuwCYXcO3+30ehuHXYRi+zzk/GRec1XiWWV73ODh+X36fjwFe1tQep5RetPUrwXEEALMqi/5au91vHCCf5Zzv5pxf5Jw/BHhNRxt/j/L7jAsInzUYAr+UtRDQvUEAMKdyrfl1Qwf5cuC/3/rtZWVWYAyBf5U7F1rxunwuoXsCgDmNg+S9Bo5wNwP/VTnncU3DSUMzAncai1I4mABgFuW6f+2Lyi6v8Z/0vqHMxozAr+W41Oxh+XxC1wQAk0spjQNF7Quu3pSB/4Xbx/4xHo+yydCbKK/pQL+V9SnQLQHAHM4qvrd8PLv9V1nV38TivqmNQVTuGvix8ssCtgmmawKASZWp1Vp3mhvPasfr/K4R76BsLnRS8WzAA7cG0jMBwGQqnvofz/p/Lmf9pvv3sDEb8KzStQG/lM8tdEcAMKWXFU79j1PY4zaxPT+g6GhlkeSjSm8ZdCmALgkAJpFSqnEr2XdloZ8HxUygHMcxAv6o7KU/LJ9f6IoAYCq1nUH/kXP2gJiJlUsCp+V2wZq8tEEQvREAHK0spKppw59nZZBiJuV2wWcVHd/x82tvALoiADhKOWuq6YvzWe+b+iylHOeaFgdaEEhXBADHqmnhn8F/YRuLA2uJALcF0g0BwMHK2VItj/k1+K9kY3FgDRHw1CwAvRAAHKOWsyWD/8oqiwCfFbogADhIRWf/Bv8gSgTUsF5kvC3wUYDXAbMSAByqhrP/nw3+sWwsDIzOHQE0TwCwt0rO/v+wu19MJQJ+D/4yH1sLQOsEAIeIfvb/zn3+seWcn1fwECF3BNA0AcBeyn3/kc/+x739betah9Pgzw5wRwBNEwDsK/q1UU/0q0R5n06D3xlgJolmCQD2FfkL8WcP9qlLeb8iT7VbDEizBAA7SymdBt7z/51Ff3Uq71vU9QB3yucemiMA2EfUL8LPpmqrF/lSgM8WTRIA7KQshnoY9Gi9yDl/CPA6ONDGeoCIHloMSIsEALuK+uVs6r8ROefX4/sZ9LexFoDmCAB2FTUAfDG3JernzK2lNEcAcKuU0knQxX+/W/XflnIp59eAv9S9lJIIoCkCgF1EPCv7bKe2Zr0MuiBQANAUAcAuIn7xvbThT5vK+xrx0o4AoCkCgBsFnf7/XM4SaVR5YNDHYL/dHY8JpiUCgNtEnP539t+HiJd4zALQDAHAbaKd8Tj770TQWQABQDMEANcqm588CHaEnP33JVrs3bMpEK0QANwk4vVOZ/99OQt4R4BZAJogALhJtAD4w9l/X8r7/TrYL20hIE0QANwk2hfdWYDXwPKizfoIAJogANiqXOeMdPvfx5zzeYDXwcLKbo/vAx33O+X2WKiaAOA60c5yXPvvW7TZH7MAVE8AcJ1oX3DRrgOzrGgBYAaA6gkArhPpC+695/33rSwGjPSoYAFA9QQA14l0/7+zf4Zgn4No+2PA3gQA3wi437kAYIj2OfBcAGonANgm0k5nnz3zn+GvywAfgm0N7DIAVRMAbBMpAJz9synSraC2BKZqAoBtIk1tuvefTZE+D2YAqJoAYJu7gY6K6X82mQGAiQgAtgmzwtn1fzYFWwcQaadM2JsA4CvBHnUa6b5v4gizJ4QtgamZAOCqSAHg7J9tIl0GiHS5DPYiALgq0hea3f/YJlIYWgdAtQQAV0Wa0jQDwDafAh0VAUC1BACRCQC+4bHQMA0BwFVhzmjKA2AgMjMAVEsAcFWUL7RIW74ST5Q7RAQA1RIARGUBIMCMBABQI5eH4EgCgKh8wXMTC0ThSAKAq6LsA+ALnhrYCZBqCQCuCvMcAKjAHW8StRIAANAhAQAAHRIAANAhAQAAHRIAXOUZ/LC7944VtRIARPXIO8MNotyuar8KqiUAgBq5/x6OJAAAoEMCgKgeeme4QZRLAFAtAcBV544IFYiyY6W/L1RLABBWSsl1Xr6RUnL2DxMQAETmi55thCFMQABwVaQpTbcCsk2kAHAJgGoJACK7791hC58LmIAA4Cs550hnNKZ62SbS5+IiwGuAgwgAIouy0ptYwtwimnO2EyDVEgBsE+Z5ACkl6wD4W7A7Qzw3g6oJALaJdFYjANgU6fPg7J+qCQC2iXRdUwCwKdLnwfV/qiYA2CbSF9tDG7+wQQDARAQA20T7YjMLwOV6kDuBjoQAoGoCgG/knD8Mw/A50JF5EuA1sL5In4PP5e8JVEsAcJ1IZzcCgCHY58DZP9UTAFwn0oZAd1JKIqBj5fa/e4GOgC2AqZ4A4DrRznAEQN9Og/32AoDqCQCuE+0L7om7AboWLQBcAqB6AoCtyhan7wMdnTtmAfpULv9EWv3/3hbAtEAAcJNoswDPA7wGlhftfTf9TxMEADeJ9kX3wLMB+pJSuh/p4T+FAKAJAoBr5ZxfBzw6ZgH68iLabxv07wXsTQBwmzfBjtDjclZI48r7/DTYbxnt7wMcTABwm4hnO+HOCplFtJX/Q9C/D3AQAcBtIl7vfGoWoG3l/Y14ucf1f5ohALhR2e880u2Al17GeBnM5EWwW/+Gcvuf/f9phgBgF2cBj9JjdwS0Kei1/yHo3wM4mABgF1Gve5oFaFPUgdb1f5oiALhVmfaMuPp53BfAbYENKbv+Rbvvf/TG9D+tEQDsKurZzwvPCGhDeR+jzuo4+6c5AoCd5JzHadnPAY/WHddmm/Ei2CN/L30un39oigBgH1HPgh6XqWMqVRZ0/hT01Tv7p0kCgH1E3oDnzKWAOpX3LfIZto2naJIAYGdlEdS7oEfsjjO1ap0FnfofvbP4j1YJAPYV+da7hyklZ2sVSSmN2/0+DvyK3WpKswQAeylPQvsY+Kj9Yj1AHVJKJ8MwvAr8Yj968h8tEwAcIvpZ9lkZXAiqXPePvq++2SSaJgDYW+BbAi/dsSgwro3BP9pe/5vc+kfzBACHin5t9ME4yIiAkM7K+xOZa/80TwBwqJfBZwGGMsj4Ig8kpXQWfNHfUD7XPjc0TwBwkJzzp0q+JJ+WQYeVlfch4lP+rnpZPt/QNAHAwXLOL4LfEXBJBKysosH/Y/lcQ/MEAMeq5ctSBKykosF/sPKfnggAjlJWSr+v5CiOEfDawsDlVDb4v7fyn54IAKZQ0zP5H7s7YH7j8R1jq6LBf6jscwxHEwAcLec83tP9pqIjOd4dcGGzoHmklO6X+/yjr/bf9KZ8jqEbAoCpPK/gtsBN98pMgG2DJ1Qe63tRwX3+mz47+6dHAoBJlCem1baAatyJ7s+Uknu+J5BSGgfRt8F3+NvmhSf+0SMBwGRyzi8rWhC46aeU0kWZumZPG9f7f6vw2L0vn1vojgBgaqeVHtHLdQGmgvdQLqF8qOx6/6ZaP69wNAHApHLO4/XfXys9quPU9W8ppXOzATfbOOv/s8Ip/0u/ls8rdEkAMLmyk1qNlwIuPSyzATaF2SKldFr5Wf9Qpv69v3RNADCX08ruCrhqPKv9JaX0oaxs7954HMa1EsMwvKr4rH8on0t3f9A9AcAsytRqC2dY4+2Cb8tlgS5DYLwcUqb731Z2e991nlv1DwKAGZXV1TVtEHSTh72FQBn4x61x/1P5dP+m8ez/dZyXA+sRAMzttPL1AFdthkCTK8jLVP95Gfhr2sp3F3dsBQ1/EQDMqjxXvfb1ANuMIfCqrBF4UftdA2VV//Px9ylT/Q8DvKy5PBABIABYQFkP0Or99eMagV/Gs+XypMHTmgaW8nrHKfH/lo187gV4WUsQAXQv5ZwXPwblGurbCAc/55wCvIwulC13f+rk131THojzOtKCszJT8aisgm/luv4xxstTj8pMFZ1JKS0/AG734xoPoxIAAmBRlT0ffiofSwyMPxdLbj6zMeCflH+2sIp/aiKgUwJAAAiABZUp13MD0fCuPDXvUzken44Jg/Jo47tloL9f/nlS+f36SxIBHRIAAkAALEwE3Opj2WnvNncdw0mJgM70HgDfLf0HwvgFW26hO3eGutW9jhbjRXK5MFAE0AV3AbCKMt39qMHbA6mbuwPohgBgNSKAoEQAXRAArEoEEJQIoHkCgNWJAIISATRNABCCCCAoEUCzBABhiACCEgE0SQAQSomAk8aeIEj9RADNEQCEU/bOfyQCCEYE0BQBQEjjRiw553Em4A/vEIGIAJohAAgt5zzuGPird4lARABNEACEl3N+MQzDvywOJBARQPUEAFXIOb+2OJBgRABVEwBUY2NxoHUBRCECqJYAoCplceCpSwIEIgKokgCgShuXBN55BwlABFAdAUC1xksCOefxksDPZgOq97nc7VHz+ygCqIoAoHo555dmA6r2ZhiG++Vuj9q3ghYBVEMA0ISN2YBnZgOq8XFcy5FzfjKu7RjaeR6ECKAKAoCm5JzPxrPJYRh+986GNk73n5S1HF8RAbAMAUBzyp0Cz4dh+N5lgXDG6f7vx+n+y7P+bUQAzE8A0KyNywI/CoHVjcf/xzLd/2GXFyMCYF4CgOblnM831gd89I4v6nLgfzS+D/v+wSIA5iMA6Ma4PiDnfF8ILOKogX+TCIB5CAC6sxECLg1Mb7KBf5MIgOkJALq1cWngB88XOMrncvy+n3rg3yQCYFoCgO6NA0t5vsD/l10FXR7YzftyOWXcxOd018V9xxABMB0BAEW5ffBluTzwQ9lLwKZCX/tYjssPOeeTcjnl2tv55iACYBoCALYoswLPc853y5MH/+g4Bi6n+Mdd++6X43Kx5gsSAXC8lHNe/DCmlMa/uG8jvH855xTgZVCJ8tl9UgafBw2/b+P0/ngt/2ztwf4mKaWT8jrvRH2NOxiP9aOlZ1L48vlZfgDc7se51s7c5Lul/0CoWflL+uUvakrpfgmBy597Ff9qH8vv9eVniev5UxjjpERZzRFwORMgAliUGQAzAEykBMFJ+XlU/hlxUBqnzS/KoHlRBvyqBx4zARyi9xkAASAAmFGJgsuZgrslCu4vNFswntV/KIP8pzJAfqjl7H5fIoB99R4ALgHAjMpg++HyssGmsvjrpPyny1DYdFKi4arL/5+bNv/bRY8DiMsBsB8BACspX/CLV3/LRADszm2AQFPcIgi7EQBAc0QA3E4AAE0SAXAzAQA0SwTA9QQA0DQRANsJAKB5IgC+JQCALogA+JoAALohAuAfAgDoigiAvwgAoDsiAAQA0CkRQO8EANAtEUDPBADQNRFArwQA0D0RQI8EAIAIoEMCAKAQAfREAABsEAH0QgAAXCEC6IEAANhCBNA6AQBwDRFAywQAwA1EAK0SAAC3EAG0SAAA7EAE0BoBALAjEUBLBADAHkQArRAAAHsSAbRAAAAcQARQOwEAcCARQM0EAMARRAC1EgAAR2ooAk4DvA4WIgAAJtBABPyRc34Z4HWwEAEAMJGKI2Ac/J39d0YAAEyowggw+HdKAABMrKIIMPh3TAAAzKCCCDD4d04AAMwkcAQY/BEAAHMKGAEGf74QAAAzCxQBBn/+JgAAFhAgAgz+fEUAACxkxQgw+PMNAQCwoBUiwODPVgIAYGELRoDBn2sJAIAVLBABBn9uJAAAVjJjBBj8uZUAAFjRDBFg8GcnAgBgZRNGgMGfnQkAgAAmiACDP3sRAABBHBEBBn/2JgAAAjkgAgz+HEQAAASzRwQY/DmYAAAIaIcIMPhzFAEAENQNEWDw52gCACCwLRFg8GcSAgAguI0I+N3gz1S+cyQB4isR8NxbxVTMAABAhwQAAHRIAABAhwQAAHRIAABAhwQAAHRIAABAhwQAAHRIAABAhwQAAHRIAABAhwQAAHRIAABAhwQAAHRIAABAhwQAAHRIAABAhwQAAHRIAABAhwQAAHRIAABAhwQAAHRIAABAhwQAAHRIAABAhwQAAHRIAABAhwQAAHRIAABAhwQAAHRIAABAhwQAAHRIAABAhwQAAHRIAABAhwQAAHRIAABAhwQAAHRIAABAhwQAAHRIAABAhwQAAHRIAABAhwQAAHRIAABAhwQAAHRIAABAhwQAAHRIAABAhwQAAHRIAABAhwQAAHRIAABAhwQAAHRIAABAhwQAAHRIAABAhwQAAHRIAABAhwQAAHRIAABAhwQAAHRIAABAhwQAAHRIAABAhwQAAHRIAABAhwQAAHRIAABAhwQAAHRIAABAh77r/U1PKT0K8DIAYFHdB8AwDG8DvAYAWJRLAADQIQEAAB0SAADQIQEAAB0SAADQIQEAAB0SAADQIQEAAB0SAADQIQEAAB0SAADQIQEAAB0SAADQIQEAAB0SAADQIQEAAB0SAADQIQEAAB0SAADQIQEAAB0SAADQIQEAAB0SAADQIQEAAB0SAADQIQEAAB0SAADQIQEAAB0SAADQIQEAAB0SAADQIQEAAB0SAADQm2EY/gdBYKD47cwKVAAAAABJRU5ErkJggg=='

    main()
