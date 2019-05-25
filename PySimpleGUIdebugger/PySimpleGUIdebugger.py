import subprocess
import sys
import PySimpleGUI as sg


"""
    The Offiicial Unofficiall official PySimpleGUI debug tool
    Not calling it a debugger, but it is also quite a step up from "print statemements"
"""
PSGDebugLogo = b'R0lGODlhMgAtAPcAAAAAADD/2akK/4yz0pSxyZWyy5u3zZ24zpW30pG52J250J+60aC60KS90aDC3a3E163F2K3F2bPI2bvO3rzP3qvJ4LHN4rnR5P/zuf/zuv/0vP/0vsDS38XZ6cnb6f/xw//zwv/yxf/1w//zyP/1yf/2zP/3z//30wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAP8ALAAAAAAyAC0AAAj/AP8JHEiwoMGDCBMqXMiwoUOFAiJGXBigYoAPDxlK3CigwUGLIAOEyIiQI8cCBUOqJFnQpEkGA1XKZPlPgkuXBATK3JmRws2bB3TuXNmQw8+jQoeCbHj0qIGkSgNobNoUqlKIVJs++BfV4oiEWalaHVpyosCwJidw7Sr1YMQFBDn+y4qSbUW3AiDElXiWqoK1bPEKGLixr1jAXQ9GuGn4sN22Bl02roo4Kla+c8OOJbsQM9rNPJlORlr5asbPpTk/RP2YJGu7rjWnDm2RIQLZrSt3zgp6ZmqwmkHAng3ccWDEMe8Kpnw8JEHlkXnPdh6SxHPILaU/dp60LFUP07dfRq5aYntohAO0m+c+nvT6pVMPZ3jv8AJu8xktyNbw+ATJDtKFBx9NlA20gWU0DVQBYwZhsJMICRrkwEYJJGRCSBtEqGGCAQEAOw=='

COLOR_SCHEME = 'LightGreen'

WIDTH_VARIABLES = 12
WIDTH_RESULTS = 36

# done purely for testing / show
def func(x=''):
    return 'return value from func()={}'.format(x)


def non_user_init():
    global watcher_window
    sg.ChangeLookAndFeel(COLOR_SCHEME)
    def InVar(key1, key2):
        row1 = [sg.T('    '),
                sg.I(key=key1, size=(WIDTH_VARIABLES,1)),
                sg.T('',key=key1+'CHANGED_', size=(WIDTH_RESULTS,1)),sg.B('Detail', key=key1+'DETAIL_'), sg.T(' '),
                sg.T(' '), sg.I(key=key2, size=(WIDTH_VARIABLES, 1)), sg.T('',key=key2 + 'CHANGED_', size=(WIDTH_RESULTS, 1)), sg.B('Detail', key=key2+'DETAIL_'),]
        return row1

    variables_frame = [ InVar('_VAR1_', '_VAR2_'),
                        InVar('_VAR3_', '_VAR4_'),
                        InVar('_VAR5_', '_VAR6_'),]

    interactive_frame = [[sg.T('>>> '), sg.In(size=(83,1), key='_INTERACTIVE_'), sg.B('Go', bind_return_key=True, visible=False)],
                         [sg.Multiline(size=(88,12),key='_OUTPUT_',autoscroll=True, do_not_clear=True)],]

    layout = [  [sg.Frame('Variables or Expressions to Watch', variables_frame, )],
                [sg.Frame('REPL-Light', interactive_frame,)],
                [sg.Button('Exit')]]

    window = sg.Window('PySimpleGUI Debugger', layout, icon=PSGDebugLogo).Finalize()
    window.Element('_INTERACTIVE_').SetFocus()
    watcher_window = window
    sg.ChangeLookAndFeel('SystemDefault')
    return window

def _event_once(mylocals, myglobals):
    global myrc, watcher_window
    if not watcher_window:
        return False
    _window = watcher_window
    _event, _values = _window.Read(timeout=1)
    if _event in (None, 'Exit'):
        _window.Close()
        watcher_window = None
        return False
    cmd = _values['_INTERACTIVE_']
    if _event == 'Run':
        _runCommand(cmd=cmd, window=_window)
    elif _event == 'Go':
        _window.Element('_INTERACTIVE_').Update('')
        _window.Element('_OUTPUT_').Update(">>> {}\n".format(cmd), append=True, autoscroll=True)
        expression = """
global myrc
PySimpleGUIdebugger.PySimpleGUIdebugger.myrc = {} """.format(cmd)
        try:
            exec(expression, myglobals, mylocals)
            _window.Element('_OUTPUT_').Update('{}\n'.format(myrc),append=True, autoscroll=True)

        except Exception as e:
            _window.Element('_OUTPUT_').Update('Exception {}\n'.format(e),append=True, autoscroll=True)

    elif _event.endswith('_DETAIL_'):
        expression = """
global myrc
PySimpleGUIdebugger.PySimpleGUIdebugger.myrc = {} """.format(_values['_VAR{}_'.format(_event[4])])
        try:
            exec(expression, myglobals, mylocals)
            sg.PopupScrolled(str(_values['_VAR{}_'.format(_event[4])]) + '\n' + str(myrc))
        except:
            print('Detail failed')

    # -------------------- Process the "watch list" ------------------
    for i in range(1, 7):
        key = '_VAR{}_'.format(i)
        out_key = '_VAR{}_CHANGED_'.format(i)
        myrc =''
        if _window.Element(key):
            if _values[key]:
                expression = """
global myrc
PySimpleGUIdebugger.PySimpleGUIdebugger.myrc = {} """.format(_values[key])
                try:
                    exec(expression, myglobals, mylocals)
                except Exception as e:
                    pass
                _window.Element(out_key).Update(myrc)
            else:
                _window.Element(out_key).Update('')
    return True


def _runCommand(cmd, timeout=None, window=None):
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
        window.Refresh() if window else None        # yes, a 1-line if, so shoot me

    retval = p.wait(timeout)
    return (retval, output)

def refresh(locals, globals):
    return _event_once(locals, globals)

def initialize():
    global watcher_window
    watcher_window = non_user_init()

myrc = ''
watcher_window = None
