import PySimpleGUI as sg
from win32com.client import Dispatch
import os

"""
    Demo Program = Make Windows Shortcut

    Creates a shortcut to your python file.

    Input just the .PY or .PYW file
    or...
    Optionally Add:
        - The interpreter to use
        - An icon for your shortcut
        - A new name for the shortcut that's different than your Python filename

    Copyright 2021 PySimpleGUI
"""




def create_shortcut(path, target='', icon=''):
    """
    Create a shortcut for a given target filename
    :param path str: full path and filename to make link to
    :param target str: what to launch (e.g. python)
    :param icon str: .ICO file
    :return: filename of the created shortcut file
    :rtype: str
    """
    filename, ext = os.path.splitext(path)
    working_dir = os.path.dirname(filename)
    shell = Dispatch('WScript.Shell')
    shortcut_filename = filename + ".lnk"
    shortcut = shell.CreateShortCut(f'{shortcut_filename}')
    target_path = f'{target}'
    shortcut.Targetpath = target_path
    shortcut.Arguments = f'"{path}"'
    shortcut.WorkingDirectory = working_dir
    if icon == '':
        pass
    else:
        shortcut.IconLocation = icon
    shortcut.save()
    return shortcut_filename


def main():
    python_command = sg.execute_py_get_interpreter()
    sg.theme('dark grey 13')
    txt_size = 22

    layout = [[sg.Text('Create a link to your Python file (Click Go or return key to start)', font='_ 15')],
              [sg.T('Python file', s=txt_size), sg.Input(key='-IN FILE-'), sg.FileBrowse(file_types=(("Python Files", "*.py *.pyw *.PY *.PYW"),), )],
              [sg.T('Icon file (optional)', s=txt_size), sg.Input(key='-ICON-'), sg.FileBrowse(file_types=(("Icon Files", "*.ico *.ICO",),), )],
              [sg.T('Shortcut Name (optional)', s=txt_size), sg.Input(key='-SHORTCUT NAME-')],
              [sg.T('Python Command (optional)', s=txt_size), sg.Input(key='-PYTHON COMMAND-')],
              [sg.Button('Go', bind_return_key=True), sg.Button('Exit')]]

    window = sg.Window('Create Shortcut To Python File', layout, icon=main_icon)

    while True:
        event, values = window.read()
        # print(event, values)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == 'Go':
            try:
                if values['-PYTHON COMMAND-']:
                    py_cmd = values['-PYTHON COMMAND-']
                else:
                    py_cmd = python_command
                    if '.pyw' in values['-IN FILE-'].lower():       # if a .pyw file specified, use pythonw to launch it
                        if 'pythonw' not in py_cmd:
                            py_cmd = py_cmd.replace('python.exe', 'pythonw.exe')
                shortcut_name = create_shortcut(values['-IN FILE-'], target=fr'{py_cmd}', icon=values['-ICON-'])
                if values['-SHORTCUT NAME-']:
                    new_shortcut_name = os.path.join(os.path.dirname(shortcut_name), values['-SHORTCUT NAME-'] + '.lnk')
                    os.rename(shortcut_name, new_shortcut_name)
                    shortcut_name = new_shortcut_name
                window.close()
                choice = sg.popup('Done!', 'Created shortcut:', shortcut_name, custom_text=('Take me there', 'Close'))
                if choice == 'Take me there':
                    sg.execute_command_subprocess(r'explorer.exe', os.path.dirname(shortcut_name))
                break
            except Exception as e:
                sg.popup_error('Error encountered', e)

    window.close()


if __name__ == '__main__':
    main_icon = b'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAACWElEQVRYR7WXO2tVQRSFv7QWRmMIIggKAUW0SKNFGvMjFLsUooWPNIqVoqI2ShpFQbCwFNME/QMWggqCj0pQJIiSIkSSQgVRkHWZCTs7Z85rxg2Xe8+ZuXuts2ftNXOG+D+xE9gL7AH+AB+Aj8A3DzdUGH8CuAAcS+R9CpwLZAZTShK4HMA3tXioK8DVkgQErqQ2VoEvwF9gF7DFjYvorxIVqAJfe0ID+hg4Yq5vABdzCbQFj7h+/lgOga7gkcQKMBwupvoS6Asu3PfAgUDgdB8COeDZBMaBV8CIEVOV4Oo6MWsJbgNnM8CzRDgKLBnwOeBoC9OJU24B5838O8BMFw1MAs9DApVxq0n2ANgGvI0O54gJ7Iy59x04BHzqQuAkcD8kEZB8X3EKuGuS7wAWzfU1GY4j1MuKUwT0JC8NwKwptcS6nALX/VQFZJn7gHfAfEhQtwRenGNBL/L7H3WirSJglboA7A4JvAgHIjLJ17UX8CyMxYd5AzzxovUEfJt8BXS4iCENaCliTBmgdQ4H3GvTIZZAlcNdAq6bRCKjLTbGCUAdoMgiUOVwKq/K7ENEDwKfnSmllqC2ELECXkQyDKm5bWxwOGdayTwikOtwHtyLs7ECde3VVAEPvuZwTX+M46pAymCacuRuy4P8fQkUAY8Eui5BMfBIoIsIi4JHAvp+CEybRW9zrNb0rqehDbqKPrAZ0IuEDdnwi7CZHA4vF3Y8G9xWQL+rylvVCT+Bm4mDR1PnJCsQB7YH7z+eyPQogGtnKxKp88B+QN2hz++w470Or9lFgGOSf3MNjp/Wcz63AAAAAElFTkSuQmCC'
    main()