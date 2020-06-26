import PySimpleGUI as sg
import subprocess

"""
    Demo mini-PyCharm "favorites" launcher
    Open a python file for editing using a small window that sits in the corner of your desktop

    Copyright 2020 PySimpleGUI.org
"""

# ----------------------------  Items for you to edit specific to your setup --------------------
LOCATION = (2340, 1240)     # where the window should be located
TRANSPARENCY = .7

# A list of the files to edit
PSG = r'C:\Python\PycharmProjects\PySimpleGUI\PySimpleGUI.py'
PSGQT = r'C:\Python\PycharmProjects\PySimpleGUI\PySimpleGUIQt.py'
PSGWX = r'C:\Python\PycharmProjects\PySimpleGUI\PySimpleGUIWx.py'
PSGWEB = r'C:\Python\PycharmProjects\PySimpleGUI\PySimpleGUIWeb.py'

# The command that will be executed that causes a file to be opened in PyCharm
PYCHARM = r"C:\Program Files\JetBrains\PyCharm Community Edition 2019.1.1\bin\pycharm.bat"

# Dictionary of buttons to display and their corresponding file to open in PyCharm
button_dict = {'PySimpleGUI': PSG,
               'PySimpleGUIQt': PSGQT,
               'PySimpleGUIWx': PSGWX,
               'PySimpleGUIWeb': PSGWEB,
               'This Progam': __file__, }

# ----------------------------- The main program -----------------------------
def mini_launcher():
    """
    The main program.  Creates the Window and runs the event loop
    """

    sg.theme('dark')
    sg.set_options(border_width=0)

    # layout is built rather than a static definion
    # starting with a blank line. This will give you a place to "grab" the window to move it around on the screen
    layout = [[sg.Text(' ' * 10, background_color='black')]]

    # add the buttons to the layout
    for button_text in button_dict:
        layout += [[sg.Button(button_text)]]

    # complete the layout with a text "X" that will generate an event when clicked
    layout += [[sg.T('❎', background_color='black', enable_events=True, key='Exit')]]

    # Create the Window
    window = sg.Window('Script launcher', layout, no_titlebar=True, grab_anywhere=True, keep_on_top=True, element_padding=(0, 0), default_button_element_size=(20, 1), location=LOCATION, auto_size_buttons=False, use_default_focus=False, alpha_channel=TRANSPARENCY, background_color='black', )

    while True:  # The Event Loop
        event, values = window.read()
        if event == 'Exit' or event == sg.WINDOW_CLOSED:
            break

        file_to_edit = button_dict.get(event)  # Use button to find associated filename
        try:
            execute_command_blocking(PYCHARM, file_to_edit)     # launch PyCharm
        except Exception as e:
            sg.Print(f'Got an exception {e} trying to open in PyCharm this file:', file_to_edit)


def execute_command_blocking(command, *args):
    """
    Creates a subprocess using supplied command and arguments.
    Will not return until the process completes running
    :param command: The command (full path) to execute
    :param args: a tuple of arguments
    :return: string with the output from the command

    """
    print(f'Executing {command} with {args}')
    expanded_args = [a for a in args]
    try:
        sp = subprocess.Popen([command, expanded_args], shell=True,
                              stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = sp.communicate()
        if out:
            print(out.decode("utf-8"))
        if err:
            print(err.decode("utf-8"))
    except Exception as e:
        sg.Print(f'execute got exception {e}')
        out = ''
    return out


# ----------------------------- When program is first started -----------------------------
if __name__ == '__main__':
    mini_launcher()
