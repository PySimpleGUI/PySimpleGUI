import PySimpleGUI as sg; web=False
# import PySimpleGUIWeb as sg; web=True
# import PySimpleGUIQT as sg; web=False

WINDOW_BACKGROUND = 'lightblue'

def sample_layout():
    return [[sg.Text('Text element'), sg.InputText('Input data here', size=(15,1))],
                [sg.Button('Ok'), sg.Button('Cancel'), sg.Slider((1,10), orientation='h', size=(10,15)) ]]

layout =   [[sg.Text('Here is a complete list of themes', font='Default 18', background_color=WINDOW_BACKGROUND)]]

row = []
for count, theme in enumerate(sg.ListOfLookAndFeelValues()):
    sg.change_look_and_feel(theme)
    if not count % 3:
        layout += [row]
        row = []
    row += [sg.Frame(theme, sample_layout()  if not web else [[sg.T(theme)]]+sample_layout())]
if row:
    layout += [row]

sg.Window('Preview of all Look and Feel choices', layout, background_color=WINDOW_BACKGROUND).read()
