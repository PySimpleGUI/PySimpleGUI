import PySimpleGUI as sg
import textwrap


"""
    The Offiicial Unofficiall official PySimpleGUI debug tool
    Not calling it a debugger, but it is also quite a step up from "print statemements"
"""
PSGDebugLogo = b'R0lGODlhMgAtAPcAAAAAADD/2akK/4yz0pSxyZWyy5u3zZ24zpW30pG52J250J+60aC60KS90aDC3a3E163F2K3F2bPI2bvO3rzP3qvJ4LHN4rnR5P/zuf/zuv/0vP/0vsDS38XZ6cnb6f/xw//zwv/yxf/1w//zyP/1yf/2zP/3z//30wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAP8ALAAAAAAyAC0AAAj/AP8JHEiwoMGDCBMqXMiwoUOFAiJGXBigYoAPDxlK3CigwUGLIAOEyIiQI8cCBUOqJFnQpEkGA1XKZPlPgkuXBATK3JmRws2bB3TuXNmQw8+jQoeCbHj0qIGkSgNobNoUqlKIVJs++BfV4oiEWalaHVpyosCwJidw7Sr1YMQFBDn+y4qSbUW3AiDElXiWqoK1bPEKGLixr1jAXQ9GuGn4sN22Bl02roo4Kla+c8OOJbsQM9rNPJlORlr5asbPpTk/RP2YJGu7rjWnDm2RIQLZrSt3zgp6ZmqwmkHAng3ccWDEMe8Kpnw8JEHlkXnPdh6SxHPILaU/dp60LFUP07dfRq5aYntohAO0m+c+nvT6pVMPZ3jv8AJu8xktyNbw+ATJDtKFBx9NlA20gWU0DVQBYwZhsJMICRrkwEYJJGRCSBtEqGGCAQEAOw=='

COLOR_SCHEME = 'LightGreen'

WIDTH_VARIABLES = 12
WIDTH_RESULTS = 36

WIDTH_LOCALS = 80

# done purely for testing / show
def func(x=''):
    return 'return value from func()={}'.format(x)


def _non_user_init():
    global watcher_window
    sg.ChangeLookAndFeel(COLOR_SCHEME)
    def InVar(key1, key2):
        row1 = [sg.T('    '),
                sg.I(key=key1, size=(WIDTH_VARIABLES,1)),
                sg.T('',key=key1+'CHANGED_', size=(WIDTH_RESULTS,1)),sg.B('Detail', key=key1+'DETAIL_'),sg.B('Obj', key=key1+'OBJ_'), sg.T(' '),
                sg.T(' '), sg.I(key=key2, size=(WIDTH_VARIABLES, 1)), sg.T('',key=key2 + 'CHANGED_', size=(WIDTH_RESULTS, 1)), sg.B('Detail', key=key2+'DETAIL_'),sg.B('Obj', key=key2+'OBJ_')]
        return row1

    variables_frame = [ InVar('_VAR1_', '_VAR2_'),
                        InVar('_VAR3_', '_VAR4_'),
                        InVar('_VAR5_', '_VAR6_'),]

    interactive_frame = [[sg.T('>>> '), sg.In(size=(83,1), key='_INTERACTIVE_'), sg.B('Go', bind_return_key=True, visible=False)],
                         [sg.Multiline(size=(88,12),key='_OUTPUT_',autoscroll=True, do_not_clear=True)],]

    layout = [  [sg.Frame('Variables or Expressions to Watch', variables_frame, )],
                [sg.Frame('REPL-Light', interactive_frame,)],
                [sg.Button('All Local Variables',key='_LOCALS_'), sg.Button('Exit')]]

    window = sg.Window('PySimpleGUI Debugger', layout, icon=PSGDebugLogo).Finalize()
    window.Element('_VAR1_').SetFocus()
    watcher_window = window
    sg.ChangeLookAndFeel('SystemDefault')
    return window

def _event_once(mylocals, myglobals):
    global myrc, watcher_window, locals_window
    if not watcher_window:
        return False
    if locals_window:
        _locals_window_event_loop(mylocals)
    # _window = watcher_window
    event, values = watcher_window.Read(timeout=1)
    if event in (None, 'Exit'):
        watcher_window.Close()
        watcher_window = None
        return False
    cmd = values['_INTERACTIVE_']

    if event == 'Go':
        watcher_window.Element('_INTERACTIVE_').Update('')
        watcher_window.Element('_OUTPUT_').Update(">>> {}\n".format(cmd), append=True, autoscroll=True)
        expression = """
global myrc
imwatchingyou.imwatchingyou.myrc = {} """.format(cmd)
        try:
            exec(expression, myglobals, mylocals)
            watcher_window.Element('_OUTPUT_').Update('{}\n'.format(myrc),append=True, autoscroll=True)

        except Exception as e:
            watcher_window.Element('_OUTPUT_').Update('Exception {}\n'.format(e),append=True, autoscroll=True)

    elif event.endswith('_DETAIL_'):
        expression = """
global myrc
imwatchingyou.imwatchingyou.myrc = {} """.format(values['_VAR{}_'.format(event[4])])
        try:
            exec(expression, myglobals, mylocals)
            sg.PopupScrolled(str(values['_VAR{}_'.format(event[4])]) + '\n' + str(myrc))
        except:
            print('Detail failed')
    elif event.endswith('_OBJ_'):
        var = values['_VAR{}_'.format(event[4])]
        expression = """
global myrc
imwatchingyou.imwatchingyou.myrc = {} """.format(var)
        try:
            exec(expression, myglobals, mylocals)
            sg.PopupScrolled(sg.ObjToStringSingleObj(myrc))
        except:
            print('Detail failed')
    elif event == '_LOCALS_' and locals_window is None:
        locals_window = _locals_window_initialize(mylocals)

    # -------------------- Process the "watch list" ------------------
    for i in range(1, 7):
        key = '_VAR{}_'.format(i)
        out_key = '_VAR{}_CHANGED_'.format(i)
        myrc =''
        if watcher_window.Element(key):
            if values[key]:
                expression = """
global myrc
imwatchingyou.imwatchingyou.myrc = {} """.format(values[key])
                try:
                    exec(expression, myglobals, mylocals)
                except Exception as e:
                    pass
                watcher_window.Element(out_key).Update(myrc)
            else:
                watcher_window.Element(out_key).Update('')
    return True


def _locals_window_event_loop(my_locals):
    global locals_window

    output_text = ''
    for key in my_locals:
        value = "{} : {}".format(key, str(my_locals[key]))
        wrapped = '\n'.join(textwrap.wrap(value,WIDTH_LOCALS))
        output_text += '\n' + wrapped

    locals_window.Element('_MULTI_').Update(output_text)

    event, values = locals_window.Read(timeout=1)

    if event in (None, 'Exit'):
        locals_window.Close()
        locals_window = None


def _locals_window_initialize(my_locals):
    sg.ChangeLookAndFeel(COLOR_SCHEME)

    output_text = ''
    num_lines = 1
    for key in my_locals:
        value = "{} : {}".format(key, str(my_locals[key]))
        num_lines += len(textwrap.wrap(value, WIDTH_LOCALS))
        wrapped = '\n'.join(textwrap.wrap(value,WIDTH_LOCALS))
        output_text += wrapped

    layout = [[sg.Multiline(output_text, key='_MULTI_', size=(WIDTH_LOCALS, num_lines))],
              [sg.Exit()]]

    window = sg.Window('All Locals', layout, icon=PSGDebugLogo).Finalize()
    sg.ChangeLookAndFeel('SystemDefault')

    return window

def refresh(locals, globals):
    return _event_once(locals, globals)

def initialize():
    global watcher_window
    watcher_window = _non_user_init()

myrc = ''
locals_window = watcher_window = None



if __name__ == '__main__':
    initialize()
    while True:
        refresh(locals(), globals())