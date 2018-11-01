#!/usr/bin/env python
import sys
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg
import psutil

"""
    Desktop floating widget - System status dashboard
    Uses psutil to display:
        Network I/O
        Disk I/O
        CPU Used
        Mem Used
    Information is updated once a second and is shown as an area graph that scrolls
"""

GRAPH_WIDTH = 120       # each individual graph size in pixels
GRAPH_HEIGHT = 40
ALPHA = .7

class DashGraph(object):
    def __init__(self, graph_elem, starting_count, color):
        self.graph_current_item = 0
        self.graph_elem = graph_elem
        self.prev_value = starting_count
        self.max_sent = 1
        self.color = color

    def graph_value(self, current_value):
        delta = current_value - self.prev_value
        self.prev_value = current_value
        self.max_sent = max(self.max_sent, delta)
        percent_sent = 100 * delta / self.max_sent
        self.graph_elem.DrawLine((self.graph_current_item, 0), (self.graph_current_item, percent_sent), color=self.color)
        if self.graph_current_item >= GRAPH_WIDTH:
            self.graph_elem.Move(-1,0)
        else:
            self.graph_current_item += 1
        return delta

    def graph_percentage_abs(self, value):
        self.graph_elem.DrawLine((self.graph_current_item, 0), (self.graph_current_item, value), color=self.color)
        if self.graph_current_item >= GRAPH_WIDTH:
            self.graph_elem.Move(-1,0)
        else:
            self.graph_current_item += 1


def human_size(bytes, units=[' bytes','KB','MB','GB','TB', 'PB', 'EB']):
    """ Returns a human readable string reprentation of bytes"""
    return str(bytes) + units[0] if bytes < 1024 else human_size(bytes>>10, units[1:])

def main():
    # Make the layout less cluttered and allow bulk-changes to text formatting
    def Txt(text, **kwargs):
        return(sg.Text(text, font=('Helvetica 8'), **kwargs))
    # Update a Text Element
    def Txt_Update(window, key, value):
        window.FindElement(key).Update(value)

    # ----------------  Create Window  ----------------
    sg.ChangeLookAndFeel('Black')
    sg.SetOptions(element_padding=(0,0), margins=(1,1), border_width=0)

    def GraphColumn(name, key):
        col = sg.Column([[Txt(name, key=key+'TXT_'), ],
                    [sg.Graph((GRAPH_WIDTH, GRAPH_HEIGHT), (0, 0), (GRAPH_WIDTH, 100), background_color='black',
                              key=key+'GRAPH_')]], pad=(2, 2))
        return col

    layout = [[sg.Text('System Status Dashboard'+' '*18), sg.Button('', image_data=red_x, button_color=('black', 'black'), key='Exit', tooltip='Closes window')],
              [GraphColumn('Net Out', '_NET_OUT_'),
              GraphColumn('Net In', '_NET_IN_')],
              [GraphColumn('Disk Read', '_DISK_READ_'),
              GraphColumn('Disk Write', '_DISK_WRITE_')],
              [GraphColumn('CPU Usage', '_CPU_'),
              GraphColumn('Memory Usage', '_MEM_')],]

    window = sg.Window('PSG System Dashboard',
                       keep_on_top=True,
                       auto_size_buttons=False,
                       grab_anywhere=True,
                       no_titlebar=True,
                       default_button_element_size=(12, 1),
                       return_keyboard_events=True,
                       alpha_channel=ALPHA,
                       use_default_focus=False,
                       ).Layout(layout).Finalize()

    # setup graphs & initial values
    netio = psutil.net_io_counters()
    net_graph_in = DashGraph(window.FindElement('_NET_IN_GRAPH_'), netio.bytes_recv, '#23a0a0')
    net_graph_out = DashGraph(window.FindElement('_NET_OUT_GRAPH_'), netio.bytes_sent, '#56d856')


    diskio = psutil.disk_io_counters()
    disk_graph_write = DashGraph(window.FindElement('_DISK_WRITE_GRAPH_'), diskio.write_bytes, '#be45be')
    disk_graph_read = DashGraph(window.FindElement('_DISK_READ_GRAPH_'), diskio.read_bytes, '#5681d8')

    cpu_usage_graph = DashGraph(window.FindElement('_CPU_GRAPH_'), 0, '#d34545')
    mem_usage_graph = DashGraph(window.FindElement('_MEM_GRAPH_'), 0, '#BE7C29')

    print(psutil.cpu_percent(percpu=True))
    # ----------------  main loop  ----------------
    while (True):
        # --------- Read and update window once a second--------
        event, values = window.Read(timeout=1000)
        if event in (None, 'Exit'):         # Be nice and give an exit, expecially since there is no titlebar
            break
        # ----- Network Graphs -----
        netio = psutil.net_io_counters()
        write_bytes = net_graph_out.graph_value(netio.bytes_sent)
        read_bytes = net_graph_in.graph_value(netio.bytes_recv)
        Txt_Update(window, '_NET_OUT_TXT_', 'Net out {}'.format(human_size(write_bytes)))
        Txt_Update(window, '_NET_IN_TXT_', 'Net In {}'.format(human_size(read_bytes)))
        # ----- Disk Graphs -----
        diskio = psutil.disk_io_counters()
        write_bytes = disk_graph_write.graph_value(diskio.write_bytes)
        read_bytes = disk_graph_read.graph_value(diskio.read_bytes)
        Txt_Update(window, '_DISK_WRITE_TXT_', 'Disk Write {}'.format(human_size(write_bytes)))
        Txt_Update(window, '_DISK_READ_TXT_', 'Disk Read {}'.format(human_size(read_bytes)))
        # ----- CPU Graph -----
        cpu = psutil.cpu_percent(0)
        cpu_usage_graph.graph_percentage_abs(cpu)
        Txt_Update(window, '_CPU_TXT_', '{0:2.0f}% CPU Used'.format(cpu))
        # ----- Memory Graph -----
        mem_used = psutil.virtual_memory().percent
        mem_usage_graph.graph_percentage_abs(mem_used)
        Txt_Update(window, '_MEM_TXT_', '{}% Memory Used'.format(mem_used))

if __name__ == "__main__":
    # the clever Red X graphic
    red_x = "R0lGODlhEAAQAPeQAIsAAI0AAI4AAI8AAJIAAJUAAJQCApkAAJoAAJ4AAJkJCaAAAKYAAKcAAKcCAKcDA6cGAKgAAKsAAKsCAKwAAK0AAK8AAK4CAK8DAqUJAKULAKwLALAAALEAALIAALMAALMDALQAALUAALYAALcEALoAALsAALsCALwAAL8AALkJAL4NAL8NAKoTAKwbAbEQALMVAL0QAL0RAKsREaodHbkQELMsALg2ALk3ALs+ALE2FbgpKbA1Nbc1Nb44N8AAAMIWAMsvAMUgDMcxAKVABb9NBbVJErFYEq1iMrtoMr5kP8BKAMFLAMxKANBBANFCANJFANFEB9JKAMFcANFZANZcANpfAMJUEMZVEc5hAM5pAMluBdRsANR8AM9YOrdERMpIQs1UVMR5WNt8X8VgYMdlZcxtYtx4YNF/btp9eraNf9qXXNCCZsyLeNSLd8SSecySf82kd9qqc9uBgdyBgd+EhN6JgtSIiNuJieGHhOGLg+GKhOKamty1ste4sNO+ueenp+inp+HHrebGrefKuOPTzejWzera1O7b1vLb2/bl4vTu7fbw7ffx7vnz8f///wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAJAALAAAAAAQABAAAAjUACEJHEiwYEEABniQKfNFgQCDkATQwAMokEU+PQgUFDAjjR09e/LUmUNnh8aBCcCgUeRmzBkzie6EeQBAoAAMXuA8ciRGCaJHfXzUMCAQgYooWN48anTokR8dQk4sELggBhQrU9Q8evSHiJQgLCIIfMDCSZUjhbYuQkLFCRAMAiOQGGLE0CNBcZYmaRIDLqQFGF60eTRoSxc5jwjhACFWIAgMLtgUocJFy5orL0IQRHAiQgsbRZYswbEhBIiCCH6EiJAhAwQMKU5DjHCi9gnZEHMTDAgAOw=="

    main()
    sys.exit(69)