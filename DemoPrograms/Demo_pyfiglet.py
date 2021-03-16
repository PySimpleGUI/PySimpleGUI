import PySimpleGUI as sg
import sys
import pyfiglet

"""
    Demo pyfiglet integration
    
    Adapted from code originally from this fantastic repository:
    https://github.com/nycynik/ascii-font-processor
    Thank you nycynik for a fantastic headstart
    
    If you are running PySimpleGUI before verion 4.35.0.11, then you'll get an error
    message saying there is a problem with:  bound method Multiline.__del__
    It's because a newer parm is used in this code.  It'll all still work just fine with this error.
    
    This demo has an interesting little trick.  If the window is resized, then it
    will use the new size of the Multiline element to compute the numiber of characters
    wide the Multiline has to work with.  This number is passed to the figlet renderer.
    
    Copyright 2021 PySimpleGUI
"""


def draw_text(font, text, width=80):
    """Simple wrapper for the main draw function"""

    return pyfiglet.Figlet(font=font, width=width).renderText(text)

def main():
    selected_font = 'computer'
    LINE_LENGTH = 100
    MULTILINE_FONT = ('Courier', 12)
    fonts = pyfiglet.FigletFont.getFonts()
    column_left = [[sg.Table(headings=['Font Name'], values=fonts, key='-FONT-LIST-',
                             col_widths=[40], num_rows=30, enable_events=True), sg.VerticalSeparator(pad=((5, 5), 0))]]

    try:
        mline_input = sg.Multiline('PySimpleGUI', size=(40,3), key='-TEXT-TO-SHOW-', no_scrollbar=True, enable_events=True, focus=True)
    except Exception as e:
        mline_input = sg.Multiline('PySimpleGUI', size=(40,3), key='-TEXT-TO-SHOW-', enable_events=True, focus=True)

    column_right = [[sg.Text("Font Name:", size=(10,1)), sg.Input(selected_font, size=(12,1), key='-FONT-NAME-')],
                    [sg.Text("Text:", size=(10,1)), mline_input, sg.T('Font size for display below'), sg.Combo(list(range(4,20)), 12, enable_events=True,  k='-FONT-SIZE-')],
                    [sg.Multiline(size=(LINE_LENGTH, 20), key='-OUTPUT-', font=MULTILINE_FONT)],]

    layout = [[sg.Column(column_left),  sg.Column(column_right, expand_x=True, expand_y=True)],
              [sg.Button('Exit'), sg.T('PySimpleGUI ver ' + sg.version.split(' ')[0] + ' tkinter ver ' + sg.tclversion_detailed + '  Python ver ' + sys.version, font='Default 8', pad=(0,0))],]

    window = sg.Window('Figlet-Me', layout, resizable=True, finalize=True, right_click_menu=['_', ['Edit Me']])

    window['-OUTPUT-'].expand(True, True, expand_row=True)
    window['-OUTPUT-'].update(draw_text(selected_font, 'PySimpleGUI').strip())

    while True:  # Event Loop
        event, values = window.read()
        # print(event,values)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == '-FONT-SIZE-':
            MULTILINE_FONT = (MULTILINE_FONT[0], values['-FONT-SIZE-'])
            window['-OUTPUT-'].update(font=MULTILINE_FONT)
            window.refresh()
        elif event == '-FONT-LIST-':
            # first one is the selected, no multi-select allowed.
            selected_font = fonts[values['-FONT-LIST-'][0]]
            window['-FONT-NAME-'].update(selected_font)
        elif event == 'Edit Me':
            sg.execute_editor(__file__)
        if event in ('Show', '-TEXT-TO-SHOW-', '-FONT-SIZE-', '-FONT-LIST-'):
            text = values['-TEXT-TO-SHOW-']
            if text.strip() == '':
                text = selected_font.strip()
            # fancy way of detecting the size of the multiline so the window can be resized
            # line_length = window["-OUTPUT-"].get_size()[0] // sg.Text.char_width_in_pixels(MULTILINE_FONT)
            line_length = window["-OUTPUT-"].get_size()[0] // sg.tkinter.font.Font(font=MULTILINE_FONT).measure('A')
            window['-OUTPUT-'].update(draw_text(selected_font, text, line_length).rstrip())

    window.close()

if __name__ == "__main__":
    main()