import PySimpleGUI as sg
import subprocess
import shutil
import os
import sys
'''
    Make a "Windows os" executable with PyInstaller
'''

def main():
    sg.theme('LightGreen')

    layout = [[sg.Text('PyInstaller EXE Creator', font='Any 15')],
              [sg.Text('Source Python File'), sg.Input(key='-sourcefile-', size=(45, 1)),
               sg.FileBrowse(file_types=(("Python Files", "*.py"),))],
              [sg.Text('Icon File'), sg.Input(key='-iconfile-', size=(45, 1)),
               sg.FileBrowse(file_types=(("Icon Files", "*.ico"),))],
              [sg.Frame('Output', font='Any 15', layout=[
                        [sg.Output(size=(65, 15), font='Courier 10')]])],
              [sg.Button('Make EXE', bind_return_key=True),
               sg.Button('Quit', button_color=('white', 'firebrick3')) ],
              [sg.Text('Made with PySimpleGUI (www.PySimpleGUI.org)', auto_size_text=True, font='Courier 8')]]

    window = sg.Window('PySimpleGUI EXE Maker', layout, auto_size_text=False, auto_size_buttons=False, default_element_size=(20,1), text_justification='right')
    # ---===--- Loop taking in user input --- #
    while True:

        event, values = window.read()
        if event in ('Exit', 'Quit', None):
            break

        source_file = values['-sourcefile-']
        icon_file = values['-iconfile-']

        icon_option = '-i "{}"'.format(icon_file) if icon_file else ''
        source_path, source_filename = os.path.split(source_file)
        workpath_option = '--workpath "{}"'.format(source_path)
        dispath_option = '--distpath "{}"'.format(source_path)
        specpath_option = '--specpath "{}"'.format(source_path)
        folder_to_remove = os.path.join(source_path, source_filename[:-3])
        file_to_remove = os.path.join(source_path, source_filename[:-3]+'.spec')
        command_line = 'pyinstaller -wF --clean "{}" {} {} {} {}'.format(source_file, icon_option, workpath_option, dispath_option, specpath_option)

        if event == 'Make EXE':
            try:
                print(command_line)
                print('Making EXE...the program has NOT locked up...')
                window.refresh()
                # print('Running command {}'.format(command_line))
                out, err = runCommand(command_line, window=window)
                shutil.rmtree(folder_to_remove)
                os.remove(file_to_remove)
                print('**** DONE ****')
            except:
                sg.PopupError('Something went wrong', 'close this window and copy command line from text printed out in main window','Here is the output from the run', out)
                print('Copy and paste this line into the command prompt to manually run PyInstaller:\n\n', command_line)


def runCommand(cmd, timeout=None, window=None):
    """ run shell command

	@param cmd: command to execute
	@param timeout: timeout for command execution

	@return: (return code from command, command output)
	"""

    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = ''
    for line in p.stdout:
        line = line.decode(errors='replace' if (sys.version_info) < (3, 5)
                           else 'backslashreplace').rstrip()
        output += line
        print(line)
        if window:
            window.Refresh()

    retval = p.wait(timeout)

    return (retval, output)


if __name__ == '__main__':
    main()
