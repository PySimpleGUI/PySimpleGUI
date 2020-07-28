#!/usr/bin/env python
import PySimpleGUI as sg
import psutil
import sys

"""
    Desktop floating widget - System status dashboard
    Uses psutil to display:
        Network I/O
        Disk I/O
        CPU Used
        Mem Used
    Information is updated once a second and is shown as an area graph that scrolls
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


def main(location):
    # ----------------  Create Window  ----------------
    sg.theme('Black')
    sg.set_options(element_padding=(0, 0), margins=(1, 1), border_width=0)

    def GraphColumn(name, key):
        layout = [
            [sg.Text(name, size=(18,1), font=('Helvetica 8'), key=key+'TXT_')],
            [sg.Graph((GRAPH_WIDTH, GRAPH_HEIGHT),
                      (0, 0),
                      (GRAPH_WIDTH, 100),
                      background_color='black',
                      key=key+'GRAPH_')]]
        return sg.Col(layout, pad=(2, 2))

    red_x = b"R0lGODlhEAAQAPeQAIsAAI0AAI4AAI8AAJIAAJUAAJQCApkAAJoAAJ4AAJkJCaAAAKYAAKcAAKcCAKcDA6cGAKgAAKsAAKsCAKwAAK0AAK8AAK4CAK8DAqUJAKULAKwLALAAALEAALIAALMAALMDALQAALUAALYAALcEALoAALsAALsCALwAAL8AALkJAL4NAL8NAKoTAKwbAbEQALMVAL0QAL0RAKsREaodHbkQELMsALg2ALk3ALs+ALE2FbgpKbA1Nbc1Nb44N8AAAMIWAMsvAMUgDMcxAKVABb9NBbVJErFYEq1iMrtoMr5kP8BKAMFLAMxKANBBANFCANJFANFEB9JKAMFcANFZANZcANpfAMJUEMZVEc5hAM5pAMluBdRsANR8AM9YOrdERMpIQs1UVMR5WNt8X8VgYMdlZcxtYtx4YNF/btp9eraNf9qXXNCCZsyLeNSLd8SSecySf82kd9qqc9uBgdyBgd+EhN6JgtSIiNuJieGHhOGLg+GKhOKamty1ste4sNO+ueenp+inp+HHrebGrefKuOPTzejWzera1O7b1vLb2/bl4vTu7fbw7ffx7vnz8f///wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAJAALAAAAAAQABAAAAjUACEJHEiwYEEABniQKfNFgQCDkATQwAMokEU+PQgUFDAjjR09e/LUmUNnh8aBCcCgUeRmzBkzie6EeQBAoAAMXuA8ciRGCaJHfXzUMCAQgYooWN48anTokR8dQk4sELggBhQrU9Q8evSHiJQgLCIIfMDCSZUjhbYuQkLFCRAMAiOQGGLE0CNBcZYmaRIDLqQFGF60eTRoSxc5jwjhACFWIAgMLtgUocJFy5orL0IQRHAiQgsbRZYswbEhBIiCCH6EiJAhAwQMKU5DjHCi9gnZEHMTDAgAOw=="
    layout = [
        [sg.Text('System Status Dashboard'+' '*18),
         sg.Button('', image_data=red_x, button_color=('black', 'black'), key='Exit', tooltip='Closes window')],
        [GraphColumn('Net Out', '_NET_OUT_'),
         GraphColumn('Net In', '_NET_IN_')],
        [GraphColumn('Disk Read', '_DISK_READ_'),
         GraphColumn('Disk Write', '_DISK_WRITE_')],
        [GraphColumn('CPU Usage', '_CPU_'),
         GraphColumn('Memory Usage', '_MEM_')], ]

    window = sg.Window('PSG System Dashboard', layout,
             keep_on_top=True,
             grab_anywhere=True, no_titlebar=True,
             return_keyboard_events=True, alpha_channel=ALPHA,
             use_default_focus=False, finalize=True, location=location)

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
        # Be nice and give an exit, expecially since there is no titlebar
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
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
    if len(sys.argv) > 1:
        location = sys.argv[1].split(',')
        location = (int(location[0]), int(location[1]))
    else:
        location = (None, None)
    main(location)

