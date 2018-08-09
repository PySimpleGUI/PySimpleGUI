import PySimpleGUI as gg
import time

def main():
    # -------  Make a new FlexForm  ------- #
    form = gg.FlexForm('GoodColors', auto_size_text=True, default_element_size=(30,2))
    form.AddRow(gg.Text('Having trouble picking good colors? Try one of the colors defined by PySimpleGUI'))
    form.AddRow(gg.Text('Here come the good colors as defined by PySimpleGUI'))

    #===== Show some nice BLUE colors with yellow text ===== ===== ===== ===== ===== =====  =====#
    text_color = gg.YELLOWS[0]
    buttons = (gg.SimpleButton('BLUES[{}]\n{}'.format(j, c), button_color=(text_color, c), size=(10,2)) for j, c in enumerate(gg.BLUES))
    form.AddRow(gg.T('Button Colors Using PySimpleGUI.BLUES'))
    form.AddRow(*buttons)
    form.AddRow(gg.Text('_' * 100, size=(65, 1)))

    #===== Show some nice PURPLE colors with yellow text ===== ===== ===== ===== ===== =====  =====#
    buttons = (gg.SimpleButton('PURPLES[{}]\n{}'.format(j, c), button_color=(text_color, c), size=(10,2)) for j, c in enumerate(gg.PURPLES))
    form.AddRow(gg.T('Button Colors Using PySimpleGUI.PURPLES'))
    form.AddRow(*buttons)
    form.AddRow(gg.Text('_' * 100, size=(65, 1)))

    #===== Show some nice GREEN colors with yellow text ===== ===== ===== ===== ===== =====  =====#
    buttons = (gg.SimpleButton('GREENS[{}]\n{}'.format(j, c), button_color=(text_color, c),  size=(10,2)) for j, c in enumerate(gg.GREENS))
    form.AddRow(gg.T('Button Colors Using PySimpleGUI.GREENS'))
    form.AddRow(*buttons)
    form.AddRow(gg.Text('_' * 100, size=(65, 1)))

    #===== Show some nice TAN colors with yellow text ===== ===== ===== ===== ===== =====  =====#
    text_color = gg.GREENS[0]        # let's use GREEN text on the tan
    buttons = (gg.SimpleButton('TANS[{}]\n{}'.format(j, c), button_color=(text_color, c),  size=(10,2)) for j, c in enumerate(gg.TANS))
    form.AddRow(gg.T('Button Colors Using PySimpleGUI.TANS'))
    form.AddRow(*buttons)
    form.AddRow(gg.Text('_' * 100, size=(65, 1)))

    #===== Show some nice YELLOWS colors with black text ===== ===== ===== ===== ===== =====  =====#
    text_color = 'black'       # let's use black text on the tan
    buttons = (gg.SimpleButton('YELLOWS[{}]\n{}'.format(j, c), button_color=(text_color, c),  size=(10,2)) for j, c in enumerate(gg.YELLOWS))
    form.AddRow(gg.T('Button Colors Using PySimpleGUI.YELLOWS'))
    form.AddRow(*buttons)
    form.AddRow(gg.Text('_' * 100, size=(65, 1)))


    #===== Add a click me button for fun and SHOW the form ===== ===== ===== ===== ===== =====  =====#
    form.AddRow(gg.SimpleButton('Click ME!'))
    (button, value) = form.Show()               # show it!


if __name__ == '__main__':
    main()
