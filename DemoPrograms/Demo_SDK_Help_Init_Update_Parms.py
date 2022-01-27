import PySimpleGUI as sg
import inspect

"""
    Displays a window showing the Init and Update parms for the PySimpleGUI Elements
    
    The Function based elements (e.g. Push) can be found using the Demo Program Demo_SDK_Help_Func_Parms.py
    
    If you've seen the Udemy course, then you saw this tool used in the element lessons
    
    The Pink parameter signify the "Common" paramters that are shared among many of the elements
    
    Copyright 2022 PySimpleGUI Project
"""

def main():
    """
    Display a window that displays the parms for the init and update methods for each element

    """

    common_parms = ['key','k','font','pad','p', 'visible','size','s', 'change_submits', 'enable_events','right_click_menu','tooltip','metadata', 'expand_x', 'expand_y']
    element_classes = sg.Element.__subclasses__()
    element_names = {element.__name__: element for element in element_classes}
    element_names['Window'] = sg.Window
    element_names['SystemTray'] = sg.SystemTray
    # vars3 = [m for m in inspect.getmembers(sys.modules[__name__])]
    element_arg_default_dict = {}
    element_arg_default_dict_update = {}
    for element in element_classes:
        # Build info about init method
        args = inspect.getfullargspec(element.__init__).args[1:]
        defaults = inspect.getfullargspec(element.__init__).defaults
        if len(args) != len(defaults):
            diff = len(args) - len(defaults)
            defaults = ('NO DEFAULT',)*diff + defaults
        args_defaults = []
        for i, a in enumerate(args):
            args_defaults.append((a, defaults[i]))
        element_arg_default_dict[element.__name__] = args_defaults

        # Build info about update method
        args = inspect.getfullargspec(element.update).args[1:]
        defaults = inspect.getfullargspec(element.update).defaults
        if args is None or defaults is None:
            element_arg_default_dict_update[element.__name__] = (('',''),)
            continue
        if len(args) != len(defaults):
            diff = len(args) - len(defaults)
            defaults = ('NO DEFAULT',)*diff + defaults
        args_defaults = []
        for i, a in enumerate(args):
            args_defaults.append((a, defaults[i]))
        element_arg_default_dict_update[element.__name__] = args_defaults if len(args_defaults) else (('',''),)

    sg.theme('black')
    sg.theme_background_color('#131314')
    sg.theme_text_element_background_color('#131314')
    sg.theme_input_background_color('#131314')
    ml = sg.Multiline(size=(40, 30), key='-ML-', write_only=True, reroute_stdout=True, expand_y=True, expand_x=True)
    layout = [  [sg.Titlebar('Element Init & Update Parm Viewer', background_color='#131314', text_color='white')],
                [sg.Combo([e for e in sorted(element_names.keys())],background_color='#131314', size=(25,30), enable_events=True, readonly=True, expand_x=True, key='-COMBO-')],
              sg.vtop([ml], expand_y=True, expand_x=True) ] + [[sg.Sizegrip()]]
    # layout += [[Button('Exit', size=(15, 1))]]

    window = sg.Window('Init & Update Parms', layout, use_default_focus=False, keep_on_top=True, no_titlebar=True, margins=(0,0),font='Courier 12', right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_EXIT, resizable=True)
    # ml = window['-ML-']     # type: sg.MLine
    while True:  # Event Loop
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        # ml.print(event, values)
        if event == '-COMBO-':
            element_chosen = values[event]
        else:
            element_chosen = None
        if element_chosen in element_arg_default_dict:
            window['-ML-'].update('')
            ml.print('========== Init Parms ==========', background_color='#FFFF00', text_color='black')
            for parm, default in element_arg_default_dict[element_chosen]:
                ml.print(f'{parm:18}', text_color='hot pink' if parm in common_parms else 'green yellow', end=' = ')
                ml.print(default, text_color='hot pink' if parm in common_parms else 'white', end = ',\n')
            ml.print('========== Update Parms ==========', background_color='#FFFF00', text_color='black')
            # print(element_arg_default_dict_update[element_chosen])
            for parm, default in element_arg_default_dict_update[element_chosen]:
                ml.print(f'{parm:18}', text_color='hot pink' if parm in common_parms else 'green yellow', end=' = ')
                ml.print(default, text_color='hot pink' if parm in common_parms else 'white', end = ',\n')
        elif event == 'Edit Me':
            sg.execute_editor(__file__)

    window.close()



if __name__ == '__main__':
    main()