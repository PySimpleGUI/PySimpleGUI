#!/usr/bin/env python
import PySimpleGUI as sg
import sys
import psutil

"""
    Desktop floating widget - CPU Cores 
    Uses psutil to display:
        CPU usage of each individual core
    CPU utilization is updated every 500 ms by default
    Utiliziation is shown as a scrolling area graph
    To achieve a "rainmeter-style" of window, these featurees were used:
      An alpha-channel setting of 0.8 to give a little transparency
      No titlebar
      Grab anywhere, making window easy to move around
    Note that the keys are tuples, with a tuple as the second item
        ('-KEY-', (row, col))      
    Copyright 2020, 2022 PySimpleGUI
"""

GRAPH_WIDTH = 120       # each individual graph size in pixels
GRAPH_HEIGHT = 40
TRANSPARENCY = .8       # how transparent the window looks. 0 = invisible, 1 = normal window
NUM_COLS = 4
POLL_FREQUENCY = 1500    # how often to update graphs in milliseconds

colors = ('#23a0a0', '#56d856', '#be45be', '#5681d8', '#d34545', '#BE7C29')

# DashGraph does the drawing of each graph
class DashGraph(object):
    def __init__(self, graph_elem, text_elem, starting_count, color):
        self.graph_current_item = 0
        self.graph_elem = graph_elem        # type: sg.Graph
        self.text_elem = text_elem
        self.prev_value = starting_count
        self.max_sent = 1
        self.color = color
        self.line_list = []                 # list of currently visible lines. Used to delete oild figures

    def graph_percentage_abs(self, value):
        self.line_list.append(self.graph_elem.draw_line(            # draw a line and add to list of lines
            (self.graph_current_item, 0),
            (self.graph_current_item, value),
            color=self.color))
        if self.graph_current_item >= GRAPH_WIDTH:
            self.graph_elem.move(-1,0)
            self.graph_elem.delete_figure(self.line_list[0])        # delete the oldest line
            self.line_list = self.line_list[1:]                     # remove line id from list of lines
        else:
            self.graph_current_item += 1

    def text_display(self, text):
        self.text_elem.update(text)

def main(location):
    # A couple of "User defined elements" that combine several elements and enable bulk edits
    def Txt(text, **kwargs):
        return(sg.Text(text, font=('Helvetica 8'), **kwargs))

    def GraphColumn(name, key):
        return sg.Column([[Txt(name, size=(10,1), key=('-TXT-', key))],
                          [sg.Graph((GRAPH_WIDTH, GRAPH_HEIGHT), (0, 0), (GRAPH_WIDTH, 100), background_color='black', key=('-GRAPH-', key))]], pad=(2, 2))

    num_cores = len(psutil.cpu_percent(percpu=True))        # get the number of cores in the CPU

    sg.theme('Black')

    layout = [[sg.Text('CPU Core Usage', justification='c', expand_x=True)] ]

    # add on the graphs
    for rows in range(num_cores//NUM_COLS+1):
        # for cols in range(min(num_cores-rows*NUM_COLS, NUM_COLS)):
        layout += [[GraphColumn('CPU '+str(rows*NUM_COLS+cols), (rows, cols)) for cols in range(min(num_cores-rows*NUM_COLS, NUM_COLS))]]

    # ----------------  Create Window  ----------------
    window = sg.Window('CPU Cores Usage Widget', layout,
                       keep_on_top=True,
                       grab_anywhere=True,
                       no_titlebar=True,
                       return_keyboard_events=True,
                       alpha_channel=TRANSPARENCY,
                       use_default_focus=False,
                       finalize=True,
                       margins=(1,1),
                       element_padding=(0,0),
                       border_depth=0,
                       location=location,
                       enable_close_attempted_event=True,
                       right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_VER_EXIT)


    graphs = []
    for rows in range(num_cores//NUM_COLS+1):
        for cols in range(min(num_cores-rows*NUM_COLS, NUM_COLS)):
            graphs += [DashGraph(window[('-GRAPH-', (rows, cols))],
                                 window[('-TXT-',  (rows, cols))],
                                 0, colors[(rows*NUM_COLS+cols)%len(colors)])]


    # ----------------  main loop  ----------------
    while True :
        # --------- Read and update window once every Polling Frequency --------
        event, values = window.read(timeout=POLL_FREQUENCY)
        if event in (sg.WIN_CLOSE_ATTEMPTED_EVENT, 'Exit'):         # Be nice and give an exit
            sg.user_settings_set_entry('-location-', window.current_location())     # save window location before exiting
            break
        elif event == sg.WIN_CLOSED:
            break
        elif event == 'Edit Me':
            sg.execute_editor(__file__)
        elif event == 'Version':
            sg.popup_scrolled(__file__, sg.get_versions(), keep_on_top=True, location=window.current_location())
        # read CPU for each core
        stats = psutil.cpu_percent(percpu=True)

        # update each graph
        for i, util in enumerate(stats):
            graphs[i].graph_percentage_abs(util)
            graphs[i].text_display('{} CPU {:2.0f}'.format(i, util))

    window.close()

if __name__ == "__main__":
    # when invoking this program, if a location is set on the command line, then the window will be created there. Use x,y with no ( )
    if len(sys.argv) > 1:
        location = sys.argv[1].split(',')
        location = (int(location[0]), int(location[1]))
    else:
        location = sg.user_settings_get_entry('-location-', (None, None))

    main(location)