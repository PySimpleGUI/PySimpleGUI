import PySimpleGUI as sg
# import PySimpleGUIWeb as sg
# import PySimpleGUIQt as sg

"""
    If you're using the PySimpleGUI color themes, then your code will a line that looks something like this:
        sg.theme('Light Green 1') or sg.theme('LightGreen1')
    This demo shows how to access the list of all themes to build your own previewer
"""

# Use the built-in Theme Viewer to show all of the themes and their names
# sg.theme_previewer()

# The remainder of the program duplicates the built-in Theme Viewer, allowing you to create your
# own custom theme viewer window.  You can configure the number of frames per row for example. Or maybe you only
# want to see the dark themes

window_background = 'black'

def sample_layout():
    return [[sg.Text('Text element'), sg.InputText('Input data here', size=(15, 1))],
            [sg.Button('Ok'), sg.Button('Cancel'), sg.Slider((1, 10), orientation='h', size=(10, 15))]]


layout = [[sg.Text('List of Dark Themes Provided by PySimpleGUI', font='Default 18', background_color=window_background)]]

FRAMES_PER_ROW = 9
names = sg.theme_list()
names = [name for name in names  if 'dark' in name.lower()]
row = []
for count, theme in enumerate(names):
    sg.theme(theme)
    if not count % FRAMES_PER_ROW:
        layout += [row]
        row = []
    row += [sg.Frame(theme, sample_layout())]
if row:
    layout += [row]

window = sg.Window('Custom Preview of Themes', layout, background_color=window_background)
window.read()
window.close()
