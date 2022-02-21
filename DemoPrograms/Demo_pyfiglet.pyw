import PySimpleGUI as sg
import sys
import pyfiglet

"""
    Demo pyfiglet integration
    
    '##:::::'##:'##::::'##::::'###::::'########::::'####::'######::
     ##:'##: ##: ##:::: ##:::'## ##:::... ##..:::::. ##::'##... ##:
     ##: ##: ##: ##:::: ##::'##:. ##::::: ##:::::::: ##:: ##:::..::
     ##: ##: ##: #########:'##:::. ##:::: ##:::::::: ##::. ######::
     ##: ##: ##: ##.... ##: #########:::: ##:::::::: ##:::..... ##:
     ##: ##: ##: ##:::: ##: ##.... ##:::: ##:::::::: ##::'##::: ##:
    . ###. ###:: ##:::: ##: ##:::: ##:::: ##:::::::'####:. ######::
    :...::...:::..:::::..::..:::::..:::::..::::::::....:::......:::
    :::'###:::::::'########:'####::'######:::'##:::::::'########:'########::'#######::
    ::'## ##:::::: ##.....::. ##::'##... ##:: ##::::::: ##.....::... ##..::'##.... ##:
    :'##:. ##::::: ##:::::::: ##:: ##:::..::: ##::::::: ##:::::::::: ##::::..:::: ##::
    '##:::. ##:::: ######:::: ##:: ##::'####: ##::::::: ######:::::: ##:::::::: ###:::
     #########:::: ##...::::: ##:: ##::: ##:: ##::::::: ##...::::::: ##::::::: ##.::::
     ##.... ##:::: ##:::::::: ##:: ##::: ##:: ##::::::: ##:::::::::: ##:::::::..::::::
     ##:::: ##:::: ##:::::::'####:. ######::: ########: ########:::: ##:::::::'##:::::
    ..:::::..:::::..::::::::....:::......::::........::........:::::..::::::::..::::::

    
    Adapted from code originally from this fantastic repository:
    https://github.com/nycynik/ascii-font-processor
    Thank you nycynik for a fantastic headstart
    
    If you are running PySimpleGUI before verion 4.35.0.11, then you'll get an error
    message saying there is a problem with:  bound method Multiline.__del__
    It's because a newer parm is used in this code.  It'll all still work just fine with this error.
    
    This demo has an interesting little trick.  If the window is resized, then it
    will use the new size of the Multiline element to compute the numiber of characters
    wide the Multiline has to work with.  This number is passed to the figlet renderer.

    
    ____________________________________
      ______                            
        /      /     ,            ,     
    ---/------/__-------__-----------__-
      /      /   ) /   (_ `     /   (_ `
    _/______/___/_/___(__)_____/___(__)_
                                        
                                        
    ___________________________________________________________
                  _____      __     __     _      _____  ______
                  /    '     /    /    )   /      /    '   /   
    ----__-------/__--------/----/--------/------/__------/----
      /   )     /          /    /  --,   /      /        /     
    _(___(_____/________ _/_ __(____/___/____/_/____ ___/______
    


    Copyright 2021 PySimpleGUI
"""


DEFAULT_FONT = 'nancyj-fancy'

def change_theme(location):
    layout = [[sg.Text(f'Current theme {sg.theme()}')],
              [sg.Listbox(values=sg.theme_list(), size=(20, 20), key='-LIST-', enable_events=True)],
              [sg.OK(), sg.Cancel()]]

    window = sg.Window('Look and Feel Browser', layout, location=location, keep_on_top=True)
    while True:  # Event Loop
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit', 'OK', 'Cancel'):
            break
    window.close()

    if event == 'OK' and values['-LIST-']:
        sg.theme(values['-LIST-'][0])
        sg.user_settings_set_entry('-theme-', values['-LIST-'][0])
        return values['-LIST-'][0]
    return  None



def draw_text(font, text, width=80):
    """Simple wrapper for the main draw function"""

    return pyfiglet.Figlet(font=font, width=width).renderText(text)

def make_window():
    selected_font = DEFAULT_FONT
    LINE_LENGTH = 100
    MULTILINE_FONT = ('Courier', 12)
    fonts = pyfiglet.FigletFont.getFonts()
    sg.theme_background_color(sg.theme_input_background_color())
    sg.theme_text_element_background_color(sg.theme_input_background_color())
    column_left = [[sg.Table(headings=['Font Name'], values=fonts, key='-FONT-LIST-',
                             col_widths=[40], num_rows=30, enable_events=True), sg.VerticalSeparator(pad=((5, 5), 0))]]
    try:
        mline_input = sg.Multiline('PySimpleGUI', size=(40,3), key='-TEXT-TO-SHOW-', no_scrollbar=True, enable_events=True, focus=True)
    except Exception as e:
        mline_input = sg.Multiline('PySimpleGUI', size=(40,3), key='-TEXT-TO-SHOW-', enable_events=True, focus=True)

    column_right = [[sg.Text("Font Name:", size=(10,1)), sg.Input(selected_font, size=(12,1), key='-FONT-NAME-')],
                    [sg.Text("Text:", size=(10,1)), mline_input, sg.T('Font size for display below'), sg.Combo(list(range(4,20)), 12, enable_events=True,  k='-FONT-SIZE-')],
                    [sg.Multiline(size=(LINE_LENGTH, 20), key='-OUTPUT-', border_width=0, font=MULTILINE_FONT, expand_x=True, expand_y=True, pad=(40,40), )],
                    [sg.B('Copy to Clipboard'), sg.B('Change Theme')],]

    layout = [[sg.Column(column_left, expand_y=False, expand_x=False),  sg.Column(column_right, expand_x=False, expand_y=False,k='-COL R-')],
              [sg.Button('Exit', right_click_menu=sg.MENU_RIGHT_CLICK_DISABLED), sg.T('PySimpleGUI ver ' + sg.version.split(' ')[0] + ' tkinter ver ' + sg.tclversion_detailed + '  Python ver ' + sys.version, font='Default 8', pad=(0,0))],]
    layout[-1].append(sg.Sizegrip())

    window = sg.Window('psgfiglet', layout, resizable=True, finalize=True, right_click_menu=['_', ['Edit Me', 'Copy', 'Exit']], icon=icon)

    window['-COL R-'].expand(True, True, True)
    # window['-OUTPUT-'].expand(True, True, False)
    # window['-FONT-LIST-'].expand(False, False, False)
    window['-OUTPUT-'].update(draw_text(selected_font, 'PySimpleGUI').strip())
    return window

def main():
    window = make_window()
    selected_font = DEFAULT_FONT
    LINE_LENGTH = 100
    MULTILINE_FONT = ('Courier', 12)
    fonts = pyfiglet.FigletFont.getFonts()

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
        if event.startswith('Copy'):
            sg.clipboard_set(window['-OUTPUT-'].get())
        elif event == 'Change Theme':
            if change_theme(window.current_location()):
                window.close()
                window = make_window()
    window.close()

if __name__ == "__main__":
    # sg.theme('Dark red')
    sg.theme(sg.user_settings_get_entry('-theme-', sg.theme()))
    # sg.theme('Dark Gray 13')
    # sg.theme_input_background_color('#36393F')
    # sg.theme_background_color('#36393F')
    # sg.theme_input_text_color('white')
    icon = b'iVBORw0KGgoAAAANSUhEUgAAAFAAAABQCAMAAAC5zwKfAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAH+UExURf/YAL2gAJB5AMysAP7XAG5dAAAAAAcFAEM4AHxpAPHMALKWACUfABQQAJiAAH9rAEA2AMurAO7JAFJFAMqrACQeACMdALWZAAsJAPbQAKGIAMipAKKJAJqCALebAGtaAAoIAD0zAG9eABgUAEs/AFVIAJV+AHhlAFFEABwXACchAMeoAOC9AKaMAGFSAOzHAAQDAPvUALGVAFlLANCwAN68ADAoAOfDAIl0ACojALOXALqdAGlYALibADcuAJZ/AJ6FAHZjANOyAFNGAA8MADEpAEQ5AAkHAHpnANi2AKyRAAYFAPzVAIBsAEo+AFBDAI95ABANANa1ACAbAPTOAPLMAOTBAE1BACwlABsWACskAEI3AFpMAHFfAIhzAMGjAGVVAAEAAEE3AGNTAKuQAPjSAH1pAB4ZAPPNAK2SAMCiAMWmAN27AIt1APXPACghACEbAL+hAA4LAFRHAHdkAJuDAMmqACYgAEk9AFxNAIFtAI54AI13AAwKAKqQAE9CANKxAKeNAObCAK6TAGxbANy6AHtoAMSmAD81AF1OANW0APnSAOPAAGZWAKmPAO3IAOXBAFhKADoxAOK/AO/KAGBRAIx2ABYSABEOAAUEAJJ7AGRUAHBeAHJgAJyEALmcAFdJAIZxANGxAKOKAAMCADsxACIcALaaAL6gAOG+AFD17/gAAAAJcEhZcwAADsMAAA7DAcdvqGQAAALDSURBVFhH7df5W0xhFAfwS3VHUkpMqQYZ00Ixxq5FIYxMaLFEUhTJMhGFyDItpkRMdtm3/9Lcc78z7oy7vvc+jx/M55fe855zvs/TU93ucAkJ/8acuUk4WSI5hed527zU+ajNSlsQzhOkZ+DGnIWIE2Rm4ZLdomxkibJxzWzxEiSBHfescnIRFLUUHTZ5SJHIR4tJAUKkHOixWIaMGMvRZJC0AhkxCtFlsBIRsZzoMlglJriKiktKxSNBl8FqMWCNcC4rX+sUS34dNVm4xYD1KDnPBqo3ojRsE63zm1EKtmzdxvPbURhWIQZWooSq6h04GZYhBtagNK9WDNyJ0rxdlLcblQXqKHAPKgvspcB9qMzzUh5fhdK8/ZRXfwCleT4KbEBlgYMUeAiVBQ5ToHW/hY2U14TKpOaWliOpFBj3h8zg6LHjcf843aWtJ062nSpoL0vGjBGnkSKro6nzzNkuTOrTjVVl585jVJcibCmrxaQ+PdhSdgGT+vRiS1FJMyb1uYg1RZcwqNNlrMlIv+K08f4+DEY04quSq9iWqLvWf73CK36ffz10bvBtOMkT36IHqgdvpty67RgSila05IXfk+/cxVkbvTOoj/uFkeF7qDTQ/7tMFPLuCyNh/Q9woeYhjao/+ztpRhDw4krRCD0JR1HJG6MscKXhVl5voTA0jkrBI0qKsvuCaMSZ8FTaacKt/qSepKEY9sdTT9CNeDo1bUOXz8OdglGMxXnWXZOT9XyC40Ij+Y6ZAdwKXmBRyUvMyXv1GocozYdUHwZ1msGaijcY1eUtllS9w7AO77GioRjjmnxY0CT9FK3CwKvHbD12VPg/YFiX4DjWFH0MYVSvTzKPZYkhjBkQUvnZTH/GkDGTPunnwD8G2zHA4EvDV6RE5Lo86DHq8gS+Rd6xOr4HfuDapODPntnysV+oEhIS/jsc9xvWwm7SqLETuAAAAABJRU5ErkJggg=='
    main()