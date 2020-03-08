import inspect
import PySimpleGUIlib

""" 
    Create All Possible Tags
    Will output to STDOUT all of the different tags for classes, members and functions for a given PySimpleGUIlib.py
    file.  Functions that begin with _ are filtered out from the list.
    Displays the results in a PySimpleGUI window which can be used to copy and paste into other places.
"""

layout = [[PySimpleGUIlib.Output(size=(80,40))]]
window = PySimpleGUIlib.Window('Dump of tags', layout, resizable=True).Finalize()



SHOW_UNDERSCORE_METHODS = not False

def valid_field(pair):
    bad_fields = 'LOOK_AND_FEEL_TABLE copyright __builtins__'.split(' ')
    bad_prefix = 'TITLE_ TEXT_ ELEM_TYPE_ DEFAULT_ BUTTON_TYPE_ LISTBOX_SELECT METER_ POPUP_ THEME_'.split(' ')

    field_name, python_object = pair
    if type(python_object) is bytes:
        return False
    if field_name in bad_fields:
        return False
    if any([i for i in bad_prefix if field_name.startswith(i)]):
        return False

    return True

psg_members  = [i for i in inspect.getmembers(PySimpleGUIlib) if valid_field(i)]
psg_funcs    = [o[0] for o in psg_members if inspect.isfunction(o[1])]
psg_classes  = [o for o in psg_members if inspect.isclass(o[1])]
# psg_props    = [o for o in psg_members if type(o[1]).__name__ == 'property']

# I don't know how this magic filtering works, I just know it works. "Private" stuff (begins with _) are somehow
# excluded from the list with the following 2 lines of code.  Very nicely done Kol-ee-ya!
psg_classes = sorted(list(set([i[1] for i in psg_classes])), key=lambda x : x.__name__) # filtering of anything that starts with _ (methods, classes, etc)

for aclass in psg_classes:
    class_name = aclass.__name__
    if 'Tk' in class_name or 'TK' in class_name or 'Element' == class_name: # or 'Window' == class_name:
        continue
    print(f'### {class_name} Element ')
    print(f'<!-- <+{class_name}.doc+> -->')
    print(f'<!-- <+{class_name}.__init__+> -->\n')
    print('\n'.join([f"#### {name}\n<!-- <+{class_name}.{name}+> -->\n" for name, obj in inspect.getmembers(aclass) if not name.startswith('_')  ]))

print('\n------------------------- Functions start here -------------------------\n')

if SHOW_UNDERSCORE_METHODS:
    for i in psg_funcs:
        if '_' in i:
            print( f"<!-- <+func.{i}+> -->" )
else:
    for i in psg_funcs:
        print( f"<!-- <+func.{i}+> -->" )




window.Read()