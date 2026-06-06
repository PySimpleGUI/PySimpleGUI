import PySimpleGUI as sg
from tkinterdnd2 import TkinterDnD, DND_FILES, DND_TEXT, DND_ALL,  CF_UNICODETEXT, CF_HDROP
import re

# tkinterdnd2 drop type constants
DROP_EVENT_TEXT = CF_UNICODETEXT
DROP_EVENT_FILES = CF_HDROP

# PySimpleGUI drop type constants
DROP_TYPE_TEXT = '+TEXT+'
DROP_TYPE_FILES = '+FILES+'
DROP_TYPE_UNKNOWN = '+UNKNOWN+'

"""
    Demo - Drag and Drop using tkinterdnd2
    
    Experimental / Prototype
    
    Drag and drop demo using tkinterdnd2 (you'll need to pip install it)
        python -m pip install tkinterdnd2
    Routes drop event through the window.read.
    
    Usage:
        * Call Init
            dnb_init()
        * Register elements for drop events
            register_element_dnd(element, window)
    
        * In event loop - drop events are tuples
            event = ('+DROP+', drop type, key of element dropped on, ).  
            values[event] = filename(s) or text that was dropped as a string            
    
    Copyright 2018-2026 PySimpleGUI. All rights reserved.
"""



#     _______ _     _ _____ __   _ _______ _______  ______ ______  __   _ ______
#        |    |____/    |   | \  |    |    |______ |_____/ |     \ | \  | |     \
#        |    |    \_ __|__ |  \_|    |    |______ |    \_ |_____/ |  \_| |_____/  2



#     _____ __   _ _____ _______
#       |   | \  |   |      |
#     __|__ |  \_| __|__    |
#               AND
#     _______ _     _ _____ _______
#     |______  \___/    |      |
#     |______ _/   \_ __|__    |




def dnd_init():
    # Call once at the top of your program
    # Make a TkinterDnD drag and drop window and hide it
    root = TkinterDnD.Tk()
    root.attributes('-alpha', 0)
    root.withdraw()
    dnd_init.root = root


def dnd_exit():
    # destroy the hidden drag and drop window
    dnd_init.root.destroy()





#     ______   ______  _____   _____
#     |     \ |_____/ |     | |_____]
#     |_____/ |    \_ |_____| |
#
#          HELPER FUNCTIONS

def register_element_dnd(element:sg.Element, window:sg.Window):
    element.widget.drop_target_register(DND_FILES, DND_TEXT)
    # When get drop event, send an event through the window.read call in the event loop
    # Format of event is a tuple.  event = ('+DROP+', key of element dropped on).  In values dict key = filename that was dropped as a string
    # element.widget.dnd_bind("<<Drop>>", lambda event, element=element, window=window : window.write_event_value(('+DROP+', element.key), reformat_filenames(event.data)))
    element.widget.dnd_bind("<<Drop>>", lambda event, element=element, window=window : on_drop(event, element, window))


def on_drop(event, element:sg.Element, window:sg.Window):
    # When drop event happens, send event to event loop.  Event is a tuple with:
    #       ( '+DROP+', DropType, key )
    #       ( hardcoded string to indicate it's a drop event, String indicating drop type, key of element dropped onto )
    if event.type == DROP_EVENT_TEXT:
        drop_type = DROP_TYPE_TEXT
        value_data = event.data
    elif event.type == DROP_EVENT_FILES:
        drop_type = DROP_TYPE_FILES
        value_data = reformat_filenames(event.data)
    else:
        drop_type = DROP_TYPE_UNKNOWN
        value_data = ''
    window.write_event_value(('+DROP+', drop_type, element.key), value_data)


def reformat_filenames(filenames:str) -> str:
    # reformat the string of filenames so that each filename is separated with a ","
    # input string has filenames separated with a space AND if a filename contains spaces it is surrounded by { }
    # I'm not good at Regex and asked for help from a CheatBot
    files = re.findall(r'\{([^}]*)\}|(\S+)', filenames)
    return ','.join(a or b for a, b in files)



#     _______ _______ _____ __   _
#     |  |  | |_____|   |   | \  |
#     |  |  | |     | __|__ |  \_|


def main():
    dnd_init()

    layout = [[sg.Text("Drag & Drop on any element including the entire window", key="-TEXT-")],
              [sg.Input("", key="-INPUT-", expand_x=True)],
              [sg.Listbox(['a', 'b'], k='-LB-', size=(50, 10), expand_y=True)],
              [sg.MLine(s=(80,20), k='-ML-', write_only=True, expand_x=True, expand_y=True)],
              [sg.Button("OK"), sg.Button("Cancel"), sg.Sizegrip()]]

    layout = [[sg.Column(layout, p=0, k='-COL-', expand_y=True, expand_x=True)]]        # if want to make the entire window the target

    window = sg.Window("File Drop", layout, finalize=True, auto_save_location=True, resizable=True)

    # register all elements to receive drop events
    for key, element in window.key_dict.items():
        register_element_dnd(element, window)

    while True:
        event, values = window.read()
        print(event)
        print(values)
        if event in (sg.WIN_CLOSED, "Cancel"):
            break
        if event[0] == '+DROP+':                        # If a Drop event
            drop_type = event[1]
            key = event[2]
            if key in ('-TEXT-', '-INPUT-'):            # if the element can be safely updated with dropped string
                window[event[2]].update(values[event])
            elif key == '-LB-'and drop_type == DROP_TYPE_FILES:      # Listbox - only accept files drop type
                window[key].update(window[key].get_list_values() + values[event].split(','))
            elif key == '-ML-':                         # Mulitiline
                window[key].update(values[event].replace(',','\n') + '\n', append=True)
            elif key == '-COL-':                       # Dropped on the window. Display in multiline
                window['-ML-'].update(f"Window drop\n" + values[event].replace(',', '\n') + "\n", append=True)
                # window['-ML-'].update(f"Window drop\n" + values[event] + '\n', append=True)

    window.close()

    dnd_exit()          # being a good citizen and cleaning up the dummy window. May be able to get away with not destroying it

if __name__ == '__main__':
    main()


