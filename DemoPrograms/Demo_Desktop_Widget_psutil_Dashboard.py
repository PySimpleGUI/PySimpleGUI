#!/usr/bin/env python
import PySimpleGUI as sg
import psutil

"""
    Desktop floating widget - System status dashboard
    Uses psutil to display:
        Network I/O
        Disk I/O
        CPU Used
        Mem Used
    Information is updated once a second and is shown as an area graph that scrolls
    Copyright 2022 PySimpleGUI
"""

GRAPH_WIDTH, GRAPH_HEIGHT = 120, 40       # each individual graph size in pixels
ALPHA = .7


class DashGraph(object):
    def __init__(self, graph_elem, starting_count, color):
        self.graph_current_item = 0
        self.graph_elem = graph_elem            # type:sg.Graph
        self.prev_value = starting_count
        self.max_sent = 1
        self.color = color
        self.graph_lines = []

    def graph_value(self, current_value):
        delta = current_value - self.prev_value
        self.prev_value = current_value
        self.max_sent = max(self.max_sent, delta)
        percent_sent = 100 * delta / self.max_sent
        line_id = self.graph_elem.draw_line((self.graph_current_item, 0), (self.graph_current_item, percent_sent), color=self.color)
        self.graph_lines.append(line_id)
        if self.graph_current_item >= GRAPH_WIDTH:
            self.graph_elem.delete_figure(self.graph_lines.pop(0))
            self.graph_elem.move(-1, 0)
        else:
            self.graph_current_item += 1
        return delta

    def graph_percentage_abs(self, value):
        self.graph_elem.draw_line((self.graph_current_item, 0), (self.graph_current_item, value), color=self.color)
        if self.graph_current_item >= GRAPH_WIDTH:
            self.graph_elem.move(-1, 0)
        else:
            self.graph_current_item += 1


def human_size(bytes, units=(' bytes', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB')):
    """ Returns a human readable string reprentation of bytes"""
    return str(bytes) + units[0] if bytes < 1024 else human_size(bytes >> 10, units[1:])


def main():
    # ----------------  Create Window  ----------------
    sg.theme('Black')
    sg.set_options(element_padding=(0, 0), margins=(1, 1), border_width=0)
    location =  sg.user_settings_get_entry('-location-', (None, None))

    def GraphColumn(name, key):
        layout = [
            [sg.Text(name, size=(18,1), font=('Helvetica 8'), key=key+'TXT_')],
            [sg.Graph((GRAPH_WIDTH, GRAPH_HEIGHT),
                      (0, 0),
                      (GRAPH_WIDTH, 100),
                      background_color='black',
                      key=key+'GRAPH_')]]
        return sg.Col(layout, pad=(2, 2))

    layout = [
        [sg.Text('System Status Dashboard'+' '*18)],
        [GraphColumn('Net Out', '_NET_OUT_'),
         GraphColumn('Net In', '_NET_IN_')],
        [GraphColumn('Disk Read', '_DISK_READ_'),
         GraphColumn('Disk Write', '_DISK_WRITE_')],
        [GraphColumn('CPU Usage', '_CPU_'),
         GraphColumn('Memory Usage', '_MEM_')], ]

    window = sg.Window('PSG System Dashboard', layout,
             keep_on_top=True,
             grab_anywhere=True, no_titlebar=True,
             return_keyboard_events=True, alpha_channel=ALPHA, enable_close_attempted_event=True,
             use_default_focus=False, finalize=True, location=location,right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_VER_EXIT,)

    # setup graphs & initial values
    netio = psutil.net_io_counters()
    net_in = window['_NET_IN_GRAPH_']
    net_graph_in = DashGraph(net_in, netio.bytes_recv, '#23a0a0')
    net_out = window['_NET_OUT_GRAPH_']
    net_graph_out = DashGraph(net_out, netio.bytes_sent, '#56d856')

    diskio = psutil.disk_io_counters()
    disk_graph_write = DashGraph(window['_DISK_WRITE_GRAPH_'], diskio.write_bytes, '#be45be')
    disk_graph_read = DashGraph(window['_DISK_READ_GRAPH_'], diskio.read_bytes, '#5681d8')

    cpu_usage_graph = DashGraph(window['_CPU_GRAPH_'], 0, '#d34545')
    mem_usage_graph = DashGraph(window['_MEM_GRAPH_'], 0, '#BE7C29')

    # print(psutil.cpu_percent(percpu=True))
    # ----------------  main loop  ----------------
    while True :
        # --------- Read and update window once a second--------
        event, values = window.read(timeout=1000)
        if event in (sg.WIN_CLOSE_ATTEMPTED_EVENT, 'Exit'):
            sg.user_settings_set_entry('-location-', window.current_location())     # save window location before exiting
            break
        elif event == 'Edit Me':
            sp = sg.execute_editor(__file__)
        elif event == 'Version':
            sg.popup_scrolled(__file__, sg.get_versions(), keep_on_top=True, location=window.current_location())

        # ----- Network Graphs -----
        netio = psutil.net_io_counters()
        write_bytes = net_graph_out.graph_value(netio.bytes_sent)
        read_bytes = net_graph_in.graph_value(netio.bytes_recv)
        window['_NET_OUT_TXT_'].update('Net out {}'.format(human_size(write_bytes)))
        window['_NET_IN_TXT_'].update('Net In {}'.format(human_size(read_bytes)))
        # ----- Disk Graphs -----
        diskio = psutil.disk_io_counters()
        write_bytes = disk_graph_write.graph_value(diskio.write_bytes)
        read_bytes = disk_graph_read.graph_value(diskio.read_bytes)
        window['_DISK_WRITE_TXT_'].update('Disk Write {}'.format(human_size(write_bytes)))
        window['_DISK_READ_TXT_'].update('Disk Read {}'.format(human_size(read_bytes)))
        # ----- CPU Graph -----
        cpu = psutil.cpu_percent(0)
        cpu_usage_graph.graph_percentage_abs(cpu)
        window['_CPU_TXT_'].update('{0:2.0f}% CPU Used'.format(cpu))
        # ----- Memory Graph -----
        mem_used = psutil.virtual_memory().percent
        mem_usage_graph.graph_percentage_abs(mem_used)
        window['_MEM_TXT_'].update('{}% Memory Used'.format(mem_used))

if __name__ == '__main__':
    main()

