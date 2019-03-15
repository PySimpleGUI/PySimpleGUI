import PySimpleGUIWeb as sg
import random
import string

"""
ooooooooooooo            .o8       oooo                                      
8'   888   `8           "888       `888                                      
     888       .oooo.    888oooo.   888   .ooooo.                            
     888      `P  )88b   d88' `88b  888  d88' `88b                           
     888       .oP"888   888   888  888  888ooo888                           
     888      d8(  888   888   888  888  888    .o                           
    o888o     `Y888""8o  `Y8bod8P' o888o `Y8bod8P'                           
                                                                             
                                                                             
                                                                             
oooooooooooo oooo                                                        .   
`888'     `8 `888                                                      .o8   
 888          888   .ooooo.  ooo. .oo.  .oo.    .ooooo.  ooo. .oo.   .o888oo 
 888oooo8     888  d88' `88b `888P"Y88bP"Y88b  d88' `88b `888P"Y88b    888   
 888    "     888  888ooo888  888   888   888  888ooo888  888   888    888   
 888       o  888  888    .o  888   888   888  888    .o  888   888    888 . 
o888ooooood8 o888o `Y8bod8P' o888o o888o o888o `Y8bod8P' o888o o888o   "888"                                                                          
"""


# ------------------ Create a fake table ------------------
class Fake():
    @classmethod
    def word(self):
        return ''.join(random.choice(string.ascii_lowercase) for i in range(10))

    @classmethod
    def number(self, max=1000):
        return random.randint(0,max)


def make_table(num_rows, num_cols):
    data = [[j for j in range(num_cols)] for i in range(num_rows)]
    data[0] = [Fake.word() for _ in range(num_cols)]
    for i in range(1, num_rows):
        data[i] = [Fake.word(), *[Fake.number() for i in range(num_cols - 1)]]
    return data

table_data = make_table(num_rows=15, num_cols=6)

# ------------------ Create a window layout ------------------
layout = [[sg.Table(values=table_data,
                    enable_events=True,
                    display_row_numbers=True,
                    font='Courier 14',
                    row_header_text='Row #',
                    key='_table_',
                    text_color='red')],
          [sg.Button('Exit')],
          [sg.T('Selected rows = '), sg.T('', size=(30,1), key='_selected_rows_')],
          [sg.T('Selected value = '), sg.T('', size=(30,1), key='_selected_value_')]]

# ------------------ Create the window ------------------
window = sg.Window('Table Element Example').Layout(layout)

# ------------------ The Event Loop ------------------
while True:
    event, values = window.Read()
    print(event, values)
    if event in (None, 'Exit'):
        break
    window.Element('_selected_rows_').Update(values['_table_'])
    window.Element('_selected_value_').Update(window.Element('_table_').SelectedItem)
# ------------------ User closed window so exit ------------------
window.Close()
