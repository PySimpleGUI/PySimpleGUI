import inspect
import PySimpleGUIlib

""" 
    Create All Possible Tags
    Will output to STDOUT all of the different tags for classes, members and functions for a given PySimpleGUIlib.py
    file.  Functions that begin with _ are filtered out from the list.
    Displays the results in a PySimpleGUI window which can be used to copy and paste into other places.

"""
PySimpleGUIlib.theme('Dark Green 2')

layout = [[PySimpleGUIlib.Output(size=(80,50))]]
window = PySimpleGUIlib.Window('Dump of tags', layout, resizable=True).Finalize()

psg_members = inspect.getmembers(PySimpleGUIlib)

psg_funcs    = [o for o in psg_members if inspect.isfunction(o[1])]
psg_classes  = [o for o in psg_members if inspect.isclass(o[1])]
# I don't know how this magic filtering works, I just know it works. "Private" stuff (begins with _) are somehow
# excluded from the list with the following 2 lines of code.  Very nicely done Kol-ee-ya!
psg_classes_ = list(set([i[1] for i in psg_classes])) # filtering of anything that starts with _ (methods, classes, etc)
psg_classes  = list(zip([i.__name__ for i in psg_classes_], psg_classes_))

for i in sorted(psg_classes):
    if 'Tk' in i[0] or 'TK' in i[0] or 'Element' == i[0]: # or 'Window' == i[0]:
        continue
    print(f'## {i[0]} Element')
    print('')
    print(f'<!-- <+{i[0]}.doc+> -->')
    print(f'<!-- <+{i[0]}.__init__+> -->')
    print('')
    print('\n'.join([f"### {j[0]}\n\n<!-- <+{i[0]}.{j[0]}+> -->\n" for j in inspect.getmembers(i[1]) if not j[0].startswith('_')  ]))

print('\n------------------------- Functions start here -------------------------\n')

for f in psg_funcs:
    if '_' != f[0][0]:          # if doesn't START with _
        print(f"<!-- <+func.{f[0]}+> -->")

window.Read()