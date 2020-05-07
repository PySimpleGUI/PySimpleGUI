#!/usr/bin/env python
import PySimpleGUI as sg
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
    Copyright 2020 PySimpleGUI
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

def main():
    # A couple of "User defined elements" that combine several elements and enable bulk edits
    def Txt(text, **kwargs):
        return(sg.Text(text, font=('Helvetica 8'), **kwargs))

    def GraphColumn(name, key):
        return sg.Column([[Txt(name, size=(10,1), key=key+'_TXT_'), ],
                    [sg.Graph((GRAPH_WIDTH, GRAPH_HEIGHT), (0, 0), (GRAPH_WIDTH, 100), background_color='black', key=key+'_GRAPH_')]], pad=(2, 2))

    num_cores = len(psutil.cpu_percent(percpu=True))        # get the number of cores in the CPU

    sg.theme('Black')
    sg.set_options(element_padding=(0,0), margins=(1,1), border_width=0)

    # the clever Red X graphic
    red_x = "R0lGODlhEAAQAPeQAIsAAI0AAI4AAI8AAJIAAJUAAJQCApkAAJoAAJ4AAJkJCaAAAKYAAKcAAKcCAKcDA6cGAKgAAKsAAKsCAKwAAK0AAK8AAK4CAK8DAqUJAKULAKwLALAAALEAALIAALMAALMDALQAALUAALYAALcEALoAALsAALsCALwAAL8AALkJAL4NAL8NAKoTAKwbAbEQALMVAL0QAL0RAKsREaodHbkQELMsALg2ALk3ALs+ALE2FbgpKbA1Nbc1Nb44N8AAAMIWAMsvAMUgDMcxAKVABb9NBbVJErFYEq1iMrtoMr5kP8BKAMFLAMxKANBBANFCANJFANFEB9JKAMFcANFZANZcANpfAMJUEMZVEc5hAM5pAMluBdRsANR8AM9YOrdERMpIQs1UVMR5WNt8X8VgYMdlZcxtYtx4YNF/btp9eraNf9qXXNCCZsyLeNSLd8SSecySf82kd9qqc9uBgdyBgd+EhN6JgtSIiNuJieGHhOGLg+GKhOKamty1ste4sNO+ueenp+inp+HHrebGrefKuOPTzejWzera1O7b1vLb2/bl4vTu7fbw7ffx7vnz8f///wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAJAALAAAAAAQABAAAAjUACEJHEiwYEEABniQKfNFgQCDkATQwAMokEU+PQgUFDAjjR09e/LUmUNnh8aBCcCgUeRmzBkzie6EeQBAoAAMXuA8ciRGCaJHfXzUMCAQgYooWN48anTokR8dQk4sELggBhQrU9Q8evSHiJQgLCIIfMDCSZUjhbYuQkLFCRAMAiOQGGLE0CNBcZYmaRIDLqQFGF60eTRoSxc5jwjhACFWIAgMLtgUocJFy5orL0IQRHAiQgsbRZYswbEhBIiCCH6EiJAhAwQMKU5DjHCi9gnZEHMTDAgAOw=="
    layout = [[ sg.Button(image_data=red_x, button_color=('black', 'black'), key='Exit', tooltip='Closes window'),
                sg.Text('     CPU Core Usage')] ]

    # add on the graphs
    for rows in range(num_cores//NUM_COLS+1):
        # for cols in range(min(num_cores-rows*NUM_COLS, NUM_COLS)):
        layout += [[GraphColumn('CPU '+str(rows*NUM_COLS+cols), '_CPU_'+str(rows*NUM_COLS+cols)) for cols in range(min(num_cores-rows*NUM_COLS, NUM_COLS))]]

    # ----------------  Create Window  ----------------
    window = sg.Window('PSG System Dashboard', layout,
                       keep_on_top=True,
                       auto_size_buttons=False,
                       grab_anywhere=True,
                       no_titlebar=True,
                       default_button_element_size=(12, 1),
                       return_keyboard_events=True,
                       alpha_channel=TRANSPARENCY,
                       use_default_focus=False,
                       finalize=True)

    # setup graphs & initial values
    graphs = [DashGraph(window['_CPU_'+str(i)+'_GRAPH_'],
                                window['_CPU_'+str(i) + '_TXT_'],
                                0, colors[i%6]) for i in range(num_cores) ]

    # ----------------  main loop  ----------------
    while True :
        # --------- Read and update window once every Polling Frequency --------
        event, values = window.read(timeout=POLL_FREQUENCY)
        if event in (sg.WIN_CLOSED, 'Exit'):         # Be nice and give an exit
            break
        # read CPU for each core
        stats = psutil.cpu_percent(percpu=True)

        # update each graph
        for i, util in enumerate(stats):
            graphs[i].graph_percentage_abs(util)
            graphs[i].text_display('{} CPU {:2.0f}'.format(i, util))

    window.close()

if __name__ == "__main__":
    main()
