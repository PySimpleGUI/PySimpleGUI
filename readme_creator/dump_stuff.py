import inspect
import PySimpleGUI as sg

psg_members = inspect.getmembers(PySimpleGUI)

psg_funcs    = [o for o in psg_members if inspect.isfunction(o[1])]
psg_classes  = [o for o in psg_members if inspect.isclass(o[1])]
psg_classes_ = list(set([i[1] for i in psg_classes])) # filtering
psg_classes  = list(zip([i.__name__ for i in psg_classes_], psg_classes_))

for i in psg_funcs:
    if 'Tk' in i[0] or 'TK' in i[0] or 'Element' == i[0]: # or 'Window' == i[0]:
        continue
    print('')
    print(f'<!-- <+func.{i[0]}+> -->')
    print('\n'.join(['\t' +  j[0] for j in inspect.getmembers(i[1]) if not j[0].startswith('_')]))

sg.Popup()
sg.Button()