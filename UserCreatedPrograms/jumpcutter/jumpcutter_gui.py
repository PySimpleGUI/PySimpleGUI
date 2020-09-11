import PySimpleGUI as sg
import subprocess
import sys

"""
    Jumpcutter GUI
    
    This is a front-end GUI for a command line tool named jumpcutter.
    
    jumpcutter is a command line based tool written by Carykh.  You'll find the repo here:
    https://github.com/carykh/jumpcutter
    
    The design of this GUI was made in a way that should not have required any changes to the
    jumpcutter.py file.  However, there appears to be a bug in the original code. The sample rate
    argument was specified as a float, but this later causes a crash in the program, so a single
    change was made to line 68, changing the parameter from a float to an int.  You can get around
    this change by not specifying a default value in this GUI.  Rather than specifying 44100, leave it blank
    which will cause the parameter to be skipped.
    
    This kind of GUI can be applied to a large number of other commandline programs.
    
    NOTE - it has not yet been tested on Linux.  It's only been tested on Windows.  Hoping to get it
    tested out on Linux shortly.
    
    Copyright 2020 PySimpleGUI.org
"""

def build_parameter_string(values):
    values_to_parm = {'-FILE-' : '--input_file',
                      '-URL-' : '--url',
                      '-OUT FILE-' : '--output_file',
                      '-SILENT THRESHOLD-' : '--silent_threshold',
                      '-SOUNDED SPEED-' : '--sounded_speed',
                      '-SILENT SPEED-' : '--silent_speed',
                      '-FRAME MARGIN-' : '--frame_margin',
                      '-SAMPLE RATE-' : '--sample_rate',
                      '-FRAME RATE-' : '--frame_rate',
                      '-FRAME QUALITY-' : '--frame_quality',
                      }
    parms = ''
    for key in values:
        if key not in values_to_parm:
            continue
        if values[key] != '':
            parms += f"{values_to_parm[key]} {values[key]} "
    return(parms)


def main():
    def FText(text, in_key=None, default=None, tooltip=None, input_size=(20,1)):
        """
        A "Fixed-sized Text Input".  Returns a row with a Text and an Input element.
        """
        return [sg.Text(text, size=(20, 1), justification='r', tooltip=tooltip), sg.Input(default_text=default, key=in_key, size=input_size)]

    layout = [
        [sg.Text('Jump Cutter', font='Any 20')],
        FText('Input File', '-FILE-', '', 'the video file you want modified', input_size=(40,1)) + [sg.FileBrowse()],
        FText('URL', '-URL-', '', 'A youtube url to download and process', input_size=(40,1)),
        FText('Output File', '-OUT FILE-', '', "the output file. (optional. if not included, it'll just modify the input file name)", input_size=(40,1)) + [sg.FileSaveAs()],
        FText('Silent Threshold', '-SILENT THRESHOLD-', 0.03,
              "the volume amount that frames' audio needs to surpass to be consider \"sounded\". It ranges from 0 (silence) to 1 (max volume)"),
        FText('Sounded Speed', '-SOUNDED SPEED-', 1.00, "the speed that sounded (spoken) frames should be played at. Typically 1."),
        FText('Silent Speed', '-SILENT SPEED-', 5.00, "the speed that silent frames should be played at. 999999 for jumpcutting."),
        FText('Frame Margin', '-FRAME MARGIN-', 1,
              "some silent frames adjacent to sounded frames are included to provide context. How many frames on either the side of speech should be included? That's this variable."),
        FText('Sample Rate', '-SAMPLE RATE-', '44100', "sample rate of the input and output videos"),
        FText('Frame Rate', '-FRAME RATE-', 30,
              "frame rate of the input and output videos. optional... I try to find it out myself, but it doesn't always work."),
        FText('Frame Quality', '-FRAME QUALITY-', 3, "quality of frames to be extracted from input video. 1 is highest, 31 is lowest, 3 is the default."),
        [sg.MLine(size=(90,10), reroute_stdout=True, reroute_stderr=True, reroute_cprint=True, write_only=True, font='Courier 10', autoscroll=True, key='-ML-')],
        [sg.Button('Start'), sg.Button('Exit')],
    ]

    window = sg.Window('Jump Cutter', layout)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        if event == 'Start':
            parms = build_parameter_string(values)
            print('Your parameters = ', parms)
            runCommand(cmd=r'python .\jumpcutter.py ' + parms, window=window)
            sg.cprint('*'*20+'DONE'+'*'*20, background_color='red', text_color='white')
    window.close()


def runCommand(cmd, timeout=None, window=None):
    """ run shell command
    @param cmd: command to execute
    @param timeout: timeout for command execution
    @param window: the PySimpleGUI window that the output is going to (needed to do refresh on)
    @return: (return code from command, command output)
    """
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = ''
    for line in p.stdout:
        line = line.decode(errors='replace' if (sys.version_info) < (3, 5) else 'backslashreplace').rstrip()
        output += line
        print(line)
        window.refresh() if window else None  # yes, a 1-line if, so shoot me

    retval = p.wait(timeout)
    return (retval, output)

if __name__ == '__main__':
    # sg.theme('Dark Grey 11')
    main()
