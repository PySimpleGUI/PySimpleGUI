import PySimpleGUI as gg
import time

def main():
    # -------  Make a new Window  ------- #
    window = gg.Window('GoodColors', auto_size_text=True, default_element_size=(30,2))
    window.AddRow(gg.Text('Having trouble picking good colors? Try one of the colors defined by PySimpleGUI'))
    window.AddRow(gg.Text('Here come the good colors as defined by PySimpleGUI'))

    #===== Show some nice BLUE colors with yellow text ===== ===== ===== ===== ===== =====  =====#
    text_color = gg.YELLOWS[0]
    buttons = (gg.Button('BLUES[{}]\n{}'.format(j, c), button_color=(text_color, c), size=(10,2)) for j, c in enumerate(gg.BLUES))
    window.AddRow(gg.T('Button Colors Using PySimpleGUI.BLUES'))
    window.AddRow(*buttons)
    window.AddRow(gg.Text('_' * 100, size=(65, 1)))

    #===== Show some nice PURPLE colors with yellow text ===== ===== ===== ===== ===== =====  =====#
    buttons = (gg.Button('PURPLES[{}]\n{}'.format(j, c), button_color=(text_color, c), size=(10,2)) for j, c in enumerate(gg.PURPLES))
    window.AddRow(gg.T('Button Colors Using PySimpleGUI.PURPLES'))
    window.AddRow(*buttons)
    window.AddRow(gg.Text('_' * 100, size=(65, 1)))

    #===== Show some nice GREEN colors with yellow text ===== ===== ===== ===== ===== =====  =====#
    buttons = (gg.Button('GREENS[{}]\n{}'.format(j, c), button_color=(text_color, c),  size=(10,2)) for j, c in enumerate(gg.GREENS))
    window.AddRow(gg.T('Button Colors Using PySimpleGUI.GREENS'))
    window.AddRow(*buttons)
    window.AddRow(gg.Text('_' * 100, size=(65, 1)))

    #===== Show some nice TAN colors with yellow text ===== ===== ===== ===== ===== =====  =====#
    text_color = gg.GREENS[0]        # let's use GREEN text on the tan
    buttons = (gg.Button('TANS[{}]\n{}'.format(j, c), button_color=(text_color, c),  size=(10,2)) for j, c in enumerate(gg.TANS))
    window.AddRow(gg.T('Button Colors Using PySimpleGUI.TANS'))
    window.AddRow(*buttons)
    window.AddRow(gg.Text('_' * 100, size=(65, 1)))

    #===== Show some nice YELLOWS colors with black text ===== ===== ===== ===== ===== =====  =====#
    text_color = 'black'       # let's use black text on the tan
    buttons = (gg.Button('YELLOWS[{}]\n{}'.format(j, c), button_color=(text_color, c),  size=(10,2)) for j, c in enumerate(gg.YELLOWS))
    window.AddRow(gg.T('Button Colors Using PySimpleGUI.YELLOWS'))
    window.AddRow(*buttons)
    window.AddRow(gg.Text('_' * 100, size=(65, 1)))


    #===== Add a click me button for fun and SHOW the window ===== ===== ===== ===== ===== =====  =====#
    window.AddRow(gg.Button('Click ME!'))
    (button, value) = window.Show()               # show it!


if __name__ == '__main__':
    main()
