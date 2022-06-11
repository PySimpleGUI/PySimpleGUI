import PySimpleGUI as sg

"""
    Demo - Element List

    All elements shown in 1 window as simply as possible.

    Copyright 2022 PySimpleGUI
"""


use_custom_titlebar = True if sg.running_trinket() else False

def make_window(theme=None):

    NAME_SIZE = 23


    def name(name):
        dots = NAME_SIZE-len(name)-2
        return sg.Text(name + ' ' + '•'*dots, size=(NAME_SIZE,1), justification='r',pad=(0,0), font='Courier 10')

    sg.theme(theme)

    # NOTE that we're using our own LOCAL Menu element
    if use_custom_titlebar:
        Menu = sg.MenubarCustom
    else:
        Menu = sg.Menu

    treedata = sg.TreeData()

    treedata.Insert("", '_A_', 'Tree Item 1', [1234], )
    treedata.Insert("", '_B_', 'B', [])
    treedata.Insert("_A_", '_A1_', 'Sub Item 1', ['can', 'be', 'anything'], )

    layout_l = [
                [name('Text'), sg.Text('Text')],
                [name('Input'), sg.Input(s=15)],
                [name('Multiline'), sg.Multiline(s=(15,2))],
                [name('Output'), sg.Output(s=(15,2))],
                [name('Combo'), sg.Combo(sg.theme_list(), default_value=sg.theme(), s=(15,22), enable_events=True, readonly=True, k='-COMBO-')],
                [name('OptionMenu'), sg.OptionMenu(['OptionMenu',],s=(15,2))],
                [name('Checkbox'), sg.Checkbox('Checkbox')],
                [name('Radio'), sg.Radio('Radio', 1)],
                [name('Spin'), sg.Spin(['Spin',], s=(15,2))],
                [name('Button'), sg.Button('Button')],
                [name('ButtonMenu'), sg.ButtonMenu('ButtonMenu', sg.MENU_RIGHT_CLICK_EDITME_EXIT)],
                [name('Slider'), sg.Slider((0,10), orientation='h', s=(10,15))],
                [name('Listbox'), sg.Listbox(['Listbox', 'Listbox 2'], no_scrollbar=True,  s=(15,2))],
                [name('Image'), sg.Image(sg.EMOJI_BASE64_HAPPY_THUMBS_UP)],
                [name('Graph'), sg.Graph((125, 50), (0,0), (125,50), k='-GRAPH-')]  ]

    layout_r  = [[name('Canvas'), sg.Canvas(background_color=sg.theme_button_color()[1], size=(125,40))],
                [name('ProgressBar'), sg.ProgressBar(100, orientation='h', s=(10,20), k='-PBAR-')],
                [name('Table'), sg.Table([[1,2,3], [4,5,6]], ['Col 1','Col 2','Col 3'], num_rows=2)],
                [name('Tree'), sg.Tree(treedata, ['Heading',], num_rows=3)],
                [name('Horizontal Separator'), sg.HSep()],
                [name('Vertical Separator'), sg.VSep()],
                [name('Frame'), sg.Frame('Frame', [[sg.T(s=15)]])],
                [name('Column'), sg.Column([[sg.T(s=15)]])],
                [name('Tab, TabGroup'), sg.TabGroup([[sg.Tab('Tab1',[[sg.T(s=(15,2))]]), sg.Tab('Tab2', [[]])]])],
                [name('Pane'), sg.Pane([sg.Col([[sg.T('Pane 1')]]), sg.Col([[sg.T('Pane 2')]])])],
                [name('Push'), sg.Push(), sg.T('Pushed over')],
                [name('VPush'), sg.VPush()],
                [name('Sizer'), sg.Sizer(1,1)],
                [name('StatusBar'), sg.StatusBar('StatusBar')],
                [name('Sizegrip'), sg.Sizegrip()]  ]

    # Note - LOCAL Menu element is used (see about for how that's defined)
    layout = [[Menu([['File', ['Exit']], ['Edit', ['Edit Me', ]]],  k='-CUST MENUBAR-',p=0)],
              [sg.T('PySimpleGUI Elements - Use Combo to Change Themes', font='_ 14', justification='c', expand_x=True)],
              [sg.Checkbox('Use Custom Titlebar & Menubar', use_custom_titlebar, enable_events=True, k='-USE CUSTOM TITLEBAR-', p=0)],
              [sg.Col(layout_l, p=0), sg.Col(layout_r, p=0)]]

    window = sg.Window('The PySimpleGUI Element List', layout, finalize=True, right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_VER_EXIT, keep_on_top=True, use_custom_titlebar=use_custom_titlebar)

    window['-PBAR-'].update(30)                                                     # Show 30% complete on ProgressBar
    window['-GRAPH-'].draw_image(data=sg.EMOJI_BASE64_HAPPY_JOY, location=(0,50))   # Draw something in the Graph Element

    return window


window = make_window()

while True:
    event, values = window.read()
    # sg.Print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    if values['-COMBO-'] != sg.theme():
        sg.theme(values['-COMBO-'])
        window.close()
        window = make_window()
    if event == '-USE CUSTOM TITLEBAR-':
        use_custom_titlebar = values['-USE CUSTOM TITLEBAR-']
        sg.set_options(use_custom_titlebar=use_custom_titlebar)
        window.close()
        window = make_window()
    if event == 'Edit Me':
        sg.execute_editor(__file__)
    elif event == 'Version':
        sg.popup_scrolled(__file__, sg.get_versions(), keep_on_top=True, non_blocking=True)
window.close()


