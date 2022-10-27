import PySimpleGUI as sg

"""
	Demo Program - Realtime output of a shell command in the window
		Shows how you can run a long-running subprocess and have the output
		be displayed in realtime in the window.
    
    Copyright 2022 PySimpleGUI		
"""


def main():
    layout = [
        [sg.Multiline(size=(110, 30), echo_stdout_stderr=True, reroute_stdout=True, autoscroll=True, background_color='black', text_color='white', key='-MLINE-')],
        [sg.T('Promt> '), sg.Input(key='-IN-', focus=True, do_not_clear=False)],
        [sg.Button('Run', bind_return_key=True), sg.Button('Exit')]]

    window = sg.Window('Realtime Shell Command Output', layout)
    while True:  # Event Loop
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        elif event == 'Run':
            cmd_list = values['-IN-'].split(' ')
            sp = sg.execute_command_subprocess(cmd_list[0], *cmd_list[1:], pipe_output=True, wait=False)
            results = sg.execute_get_results(sp, timeout=1)
            print(results[0])

    window.close()


main()
