import subprocess
import sys
import ast
import copy
import PySimpleGUI as sg

"""
    Python repl with a "watch list"
    This Demo Program was created as an answer to a Reddit question.
    The idea is to build a Python interpreter >>> prompt, accept command and execute them... and
    to also inslude a watcher feature.  The "Watched" variables or expressions are constantly updated
    as the proram runs.
    At the moment, the event loop runs once a second.  It could easily be shortened if that's too slow
"""


def convertExpr2Expression(Expr):
        Expr.lineno = 0
        Expr.col_offset = 0
        result = ast.Expression(Expr.value, lineno=0, col_offset = 0)

        return result

def exec_with_return(code):
    code_ast = ast.parse(code)

    init_ast = copy.deepcopy(code_ast)
    init_ast.body = code_ast.body[:-1]

    last_ast = copy.deepcopy(code_ast)
    last_ast.body = code_ast.body[-1:]

    exec(compile(init_ast, "<ast>", "exec"), globals())
    if type(last_ast.body[0]) == ast.Expr:
        return eval(compile(convertExpr2Expression(last_ast.body[0]), "<ast>", "eval"),globals())
    else:
        exec(compile(last_ast, "<ast>", "exec"),globals())


def func(x=''):
    return f'return value from func()={x}'


def main():
    def InVar(key1, key2):
        row1 = [sg.T(''), sg.I(key=key1, size=(18,1)), sg.I(key=key1+'CHANGED_', size=(18,1)),                sg.T('  '),
                sg.T(''), sg.I(key=key2, size=(18, 1)), sg.I(key=key2 + 'CHANGED_', size=(18, 1))]
        return row1

    variables_frame = [ InVar('_VAR1_', '_VAR2_'),
                        InVar('_VAR3_', '_VAR4_'),
                        InVar('_VAR5_', '_VAR6_'),]

    interactive_frame = [[sg.T('>>> '), sg.In(size=(70,1), key='_INTERACTIVE_'), sg.B('Go', bind_return_key=True, visible=False)],
                [sg.Output(size=(70,8))],]

    layout = [
                [sg.Frame('Variables or Expressions to Watch', variables_frame)],
                [sg.Frame('Interactive REPL', interactive_frame)],
                [sg.Button('Exit')]]

    window = sg.Window('Realtime REPL Command Output + Watches', layout).Finalize()
    window.Element('_INTERACTIVE_').SetFocus()
    event_loop(window)


def event_loop(window):
    var = 0
    while True:             # Event Loop
        event, values = window.Read(timeout=1000)
        if event in (None, 'Exit'):
            break
        cmd = values['_INTERACTIVE_']
        if event == 'Run':
            runCommand(cmd=cmd, window=window)
        elif event == 'Go':
            window.Element('_INTERACTIVE_').Update('')
            out=''
            print(">>> ", cmd)
            try:
                print(exec_with_return(cmd))
            except Exception as e:
                print(f'Exception on output {e}')
        # -------------------- Process the "watch list" ------------------
        for i in range(1, 6):
            key = f'_VAR{i}_'
            out_key = f'_VAR{i}_CHANGED_'
            if window.Element(key):
                if values[key]:
                    try:
                        window.Element(out_key).Update(eval(values[key]))
                    except:
                        window.Element(out_key).Update('')
        var += 1
    window.Close()


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
        window.Refresh() if window else None        # yes, a 1-line if, so shoot me

    retval = p.wait(timeout)
    return (retval, output)

main()
print('Exited program....')