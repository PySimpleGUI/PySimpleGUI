import PySimpleGUI as sg
import inspect
import sys

"""
    Displays a window showing the parms for the PySimpleGUI functions
    
    The default view is to only show function names that are all lower case.
    You can change this by right clicking and choosing "Upper Case Too" 
    
    Copyright 2022 PySimpleGUI Project
"""


def main():
    """
    Display a window that will display the docstrings for each PySimpleGUI Element and the Window object

    """

    sg.set_options(font='courier 12')

    functions = [m for m in inspect.getmembers(sys.modules['PySimpleGUI'], inspect.isfunction)]
    functions_names_lower = [f for f in functions if f[0][0].islower()]
    functions_names_upper = [f for f in functions if f[0][0].isupper()]
    # functions_names = sorted(functions_names_lower) + sorted(functions_names_upper)
    # func_names_str = [f[0] for f in functions if f[0][0].islower()]
    func_names_str = [f[0] for f in functions]

    func_parm_dict = {}

    # for func_str, func in functions_names_lower:
    for func_str, func in functions:
        # Build info about init method
        args = inspect.signature(func)
        params = args.parameters
        func_parm_list = []
        for a in params.values():
            func_def = str(a).split('=')
            if len(func_def) == 1:
                name, default = func_def[0], '*Required*'
                if name[0] == '*':
                    default = '*Optional*'
            elif len(func_def) == 2:
                name, default = func_def[0], func_def[1]
            elif len(func_def) == 0:
                name, default = '', ''
            else:
                name, default = func_def[0], '*Object*'
            func_parm_list.append((name, default))
        func_parm_dict[func_str] = func_parm_list

    sg.theme('black')
    sg.theme_background_color('#131314')
    sg.theme_text_element_background_color('#131314')
    sg.theme_input_background_color('#131314')
    ml = sg.Multiline(size=(35, 20), key='-ML-', write_only=True, reroute_stdout=False, expand_y=True, expand_x=True)

    layout = [
                [sg.Titlebar('Func Parm Viewer', background_color='#131314', text_color='white')],
                # [sg.Combo([e for e in sorted(func_names_str)],background_color='#131314', size=(25,30), enable_events=True, key='-COMBO-'), sg.T(' '*6, grab=True)],
                [sg.Combo([e for e in sorted([f[0] for f in functions if f[0][0].islower()])],background_color='#131314', size=(25,30), enable_events=True, readonly=True, expand_x=True,  key='-COMBO-', tooltip='Right click for more options')],
              sg.vtop([ml], expand_x=True, expand_y=True)] + [[sg.Sizegrip()]]

    window = sg.Window('Func Parms', layout, use_default_focus=False, keep_on_top=True, no_titlebar=True, margins=(0,0), right_click_menu=[[],['Edit Me', 'Upper Case Too', 'Lower Case Only', 'Exit']], resizable=True)
    while True:  # Event Loop
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        if event == 'Edit Me':
            sg.execute_editor(__file__)
            continue
        elif event.startswith('Upper'):
            window['-COMBO-'].update(values=[f[0] for f in functions if not f[0][0].startswith('_')])
        elif event.startswith('Lower'):
            window['-COMBO-'].update(values=[f[0] for f in functions if f[0][0].islower()])
        else:
            # ml.print(event, values)
            if event == '-COMBO-':
                func_chosen = values[event]
            else:
                func_chosen = None
            window['-ML-'].update('')

            ml.print(f'= {func_chosen} =', background_color='#FFFF00', text_color='black')
            func_parms = func_parm_dict[func_chosen]
            # print(func_parms)
            for parm, default in func_parms:
                ml.print(f'{parm:18}', text_color='green yellow', end=' = ')
                if default != inspect._empty:
                    if isinstance(default, str):
                        if default in ('None', '(None, None)', '(None,None)'):
                            color = 'pink'
                        elif default in ('False', 'True'):
                            color = '#00FF7F'
                        else:
                            color = None
                        ml.print(f'{default}', end='\n', text_color=color)
                    else:
                        ml.print(default, end='\n')
                else:
                    ml.print(f'{default}', end='\n')
            ml.set_vscroll_position(0)

    window.close()



if __name__ == '__main__':
    main()