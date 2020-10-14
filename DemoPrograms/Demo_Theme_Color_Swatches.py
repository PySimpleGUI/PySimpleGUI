import PySimpleGUI as sg

"""
    Demo Theme Color Swatches
    
    Sometimes when working with themes, it's nice ot know all of the hex values
    for the theme.  Or, maybe you want to scroll through the list of themes and
    look at the colors in the theme as groups of color swatches.  Whatever thr
    reason, this ia good candidate for you.
    
    Thie program is interactive.  In addition to showing you the swatches, you can
    interact with them.  
    * If you hover with your mouse, you'll get a tooltip popup  that tells you the hex value.  
    * If you left click, then the value it posted to the clipboard.
    * If you right click a swatch, then the right clip menu will show you the hex value.
      If you then select that menu item, it's copied to the clipbard.
    
    The code has several examples you may want to try out in your prgorams.  Everything from
    using "Symbols" to make the swatches, so generating layouts, integrating (optionally) other
    packages like pyperclip, moving a window based on the size of the window
    
    This code's pattern is becoming more widespread lately:
    * Have a "create_window' function where the layout and Window is defined
    * Use a "main" program function where the event loop also lives
    
    Copyright 2020  PySimpleGUI.org
"""

# Try and import pyperclip. Save if can be used or not.
try:
    import pyperclip
    pyperclip_available=True
except:
    pyperclip_available=False


def create_window():
    # Begin the layout with a header
    layout = [[sg.Text('Themes as color swatches', text_color='white', background_color='black', font='Default 25')],
              [sg.Text('Tooltip and right click a color to get the value', text_color='white', background_color='black', font='Default 15')],
              [sg.Text('Left click a color to copy to clipboard (requires pyperclip)', text_color='white', background_color='black', font='Default 15')]]
    layout =[[sg.Column(layout, element_justification='c', background_color='black')]]
    # Create the pain part, the rows of Text with color swatches
    for i, theme in enumerate(sg.theme_list()):
        sg.theme(theme)
        colors = [sg.theme_background_color(), sg.theme_text_color(), sg.theme_input_background_color(),
                  sg.theme_input_text_color()]
        if sg.theme_button_color() != sg.COLOR_SYSTEM_DEFAULT:
            colors.append(sg.theme_button_color()[0])
            colors.append(sg.theme_button_color()[1])
        colors = list(set(colors))      # de-duplicate items
        row = [sg.T(sg.theme(), background_color='black', text_color='white',  size=(20,1), justification='r')]
        for color in colors:
            if color != sg.COLOR_SYSTEM_DEFAULT:
                row.append(sg.T(sg.SYMBOL_SQUARE, text_color=color, background_color='black', pad=(0,0), font='DEFAUlT 20', right_click_menu=['Nothing',[color]], tooltip=color, enable_events=True, key=(i,color)))
        layout += [row]
    # finish the layout by adding an exit button
    layout += [[sg.B('Exit')]]
    # place layout inside of a Column so that it's scrollable
    layout = [[sg.Column(layout, scrollable=True,vertical_scroll_only=True,  background_color='black')]]
    # create and return Window that uses the layout
    return sg.Window('Theme Color Swatches', layout, background_color='black', finalize=True)



def main():
    sg.popup_quick_message('This is going to take a minute...', text_color='white', background_color='red', font='Default 20')
    window = create_window()
    sg.theme(sg.OFFICIAL_PYSIMPLEGUI_THEME)
    if window.size[1] > 100:
        window.size = (window.size[0], 1000)
    window.move(window.get_screen_size()[0]//2-window.size[0]//2, window.get_screen_size()[1]//2-500)

    while True:             # Event Loop
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if isinstance(event, tuple):       # someone clicked a swatch
            chosen_color = event[1]
        else:
            if event[0] == '#':  # someone right clicked
                chosen_color = event
            else:
                chosen_color = ''

        if pyperclip_available:
            pyperclip.copy(chosen_color)
            sg.popup_auto_close(f'{chosen_color}\nColor copied to clipboard', auto_close_duration=1)
        else:
            sg.popup_auto_close(f'pyperclip not installed\nPlease install pyperclip', auto_close_duration=3)

    window.close()

if __name__ == '__main__':
    main()