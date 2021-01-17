import inspect
import PySimpleGUI

""" 
    Create All Possible Tags
    Will output to STDOUT all of the different tags for classes, members and functions for a given PySimpleGUI.py
    file.  Functions that begin with _ are filtered out from the list.
    Displays the results in a PySimpleGUI window which can be used to copy and paste into other places.

"""


def new_name(name):
    name = name.replace("OK", "*1")
    name = name.replace("TK", "*2")
    name = name.replace("RGB", "*3")
    new = name[0].lower()
    for c in name[1:]:
        new += '_' + c.lower() if (c.isupper() or c == "*") else c
    new=new.replace("*1", "ok")
    new = new.replace("*2", "tk")
    new = new.replace("*3", "rgb")
    return new

layout = [[PySimpleGUI.Output(size=(600,300))]]
window = PySimpleGUI.Window('Dump of tags', layout, resizable=True).Finalize()

psg_members = inspect.getmembers(PySimpleGUI)

psg_funcs    = [o for o in psg_members if inspect.isfunction(o[1])]
psg_classes  = [o for o in psg_members if inspect.isclass(o[1])]
# I don't know how this magic filtering works, I just know it works. "Private" stuff (begins with _) are somehow
# excluded from the list with the following 2 lines of code.  Very nicely done Kol-ee-ya!
psg_classes_ = list(set([i[1] for i in psg_classes])) # filtering of anything that starts with _ (methods, classes, etc)
psg_classes  = list(zip([i.__name__ for i in psg_classes_], psg_classes_))

for pclass in sorted(psg_classes):
    if 'Tk' in pclass[0] or 'TK' in pclass[0] or 'Element' == pclass[0]: # or 'Window' == i[0]:
        continue
    # print(f'### {pclass[0]} Element')
    # print('')
    # print(f'<!-- <+{pclass[0]}.doc+> -->')
    # print(f'<!-- <+{pclass[0]}.__init__+> -->')
    print('')
    print(f'{pclass[0]} methods in PEP8 format --------------------------------------')
    for funcs in inspect.getmembers(pclass[1]):
        if '_' not in funcs[0]:
            # print(f'{pclass[0]}.{new_name(funcs[0])} = {pclass[0]}.{funcs[0]}')   # version that has class on front
            print(f'{new_name(funcs[0])} = {funcs[0]}')                           # version without class on front (use for most)
    # print('\n'.join([f"#### {j[0]}\n\n<!-- <+{pclass[0]}.{j[0]}+> -->\n" for j in inspect.getmembers(pclass[1]) if '_' not in j[0]]))

# print('\n------------------------- Functions start here -------------------------\n')
#
for f in psg_funcs:
    if f[0][0] == '_':
        continue
    print(f'{new_name(f[0])} = {f[0]}')
    # print(f"<!-- <+func.{f[0]}+> -->")

window.Read()
