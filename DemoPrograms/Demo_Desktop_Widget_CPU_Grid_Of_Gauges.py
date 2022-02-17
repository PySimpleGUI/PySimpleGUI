#!/usr/bin/env python
import PySimpleGUI as sg
import sys
import psutil
import math

"""
    Desktop floating widget - CPU Cores as Gauges
    Uses psutil to display:
        CPU usage of each individual core
    CPU utilization is updated every 2000 ms by default
    Utiliziation is shown as a gauge
    Pointer turns red when usage > 50%
    To achieve a "rainmeter-style" of window, these featurees were used:
      An alpha-channel setting of 0.8 to give a little transparency
      No titlebar
      Grab anywhere, making window easy to move around
    Copyright 2020 PySimpleGUI
"""

# gsize = (120, 75)
# gsize = (85, 40)
gsize = (55, 30)

TRANSPARENCY = .8       # how transparent the window looks. 0 = invisible, 1 = normal window
NUM_COLS = 4
POLL_FREQUENCY = 1500    # how often to update graphs in milliseconds

colors = ('#23a0a0', '#56d856', '#be45be', '#5681d8', '#d34545', '#BE7C29')


class Gauge():
    def mapping(func, sequence, *argc):
        """
        Map function with extra argument, not for tuple.
        : Parameters
          func - function to call.
          sequence - list for iteration.
          argc - more arguments for func.
        : Return
          list of func(element of sequence, *argc)
        """
        if isinstance(sequence, list):
            return list(map(lambda i: func(i, *argc), sequence))
        else:
            return func(sequence, *argc)

    def add(number1, number2):
        """
        Add two number
        : Parameter
          number1 - number to add.
          numeer2 - number to add.
        : Return
          Addition result for number1 and number2.
        """
        return number1 + number2

    def limit(number):
        """
        Limit angle in range 0 ~ 360
        : Parameter
          number: angle degree.
        : Return
          angel degree in 0 ~ 360, return 0 if number < 0, 360 if number > 360.
        """
        return max(min(360, number), 0)
    class Clock():
        """
        Draw background circle or arc
        All angles defined as clockwise from negative x-axis.
        """

        def __init__(self, center_x=0, center_y=0, radius=100, start_angle=0,
                     stop_angle=360, fill_color='white', line_color='black', line_width=2, graph_elem=None):

            instance = Gauge.mapping(isinstance, [center_x, center_y, radius, start_angle,
                                            stop_angle, line_width], (int, float)) + Gauge.mapping(isinstance,
                                                                                             [fill_color, line_color], str)
            if False in instance:
                raise ValueError
            start_angle, stop_angle = Gauge.limit(start_angle), Gauge.limit(stop_angle)
            self.all = [center_x, center_y, radius, start_angle, stop_angle,
                        fill_color, line_color, line_width]
            self.figure = []
            self.graph_elem = graph_elem
            self.new()

        def new(self):
            """
            Draw Arc or circle
            """
            x, y, r, start, stop, fill, line, width = self.all
            start, stop = (180 - start, 180 - stop) if stop < start else (180 - stop, 180 - start)
            if start == stop % 360:
                self.figure.append(self.graph_elem.DrawCircle((x, y), r, fill_color=fill,
                                                              line_color=line, line_width=width))
            else:
                self.figure.append(self.graph_elem.DrawArc((x - r, y + r), (x + r, y - r), stop - start,
                                                           start, style='arc', arc_color=fill))

        def move(self, delta_x, delta_y):
            """
            Move circle or arc in clock by delta x, delta y
            """
            if False in Gauge.mapping(isinstance, [delta_x, delta_y], (int, float)):
                raise ValueError
            self.all[0] += delta_x
            self.all[1] += delta_y
            for figure in self.figure:
                self.graph_elem.MoveFigure(figure, delta_x, delta_y)

    class Pointer():
        """
        Draw pointer of clock
        All angles defined as clockwise from negative x-axis.
        """

        def __init__(self, center_x=0, center_y=0, angle=0, inner_radius=20,
                     outer_radius=80, outer_color='white', pointer_color='blue',
                     origin_color='black', line_width=2, graph_elem=None):

            instance = Gauge.mapping(isinstance, [center_x, center_y, angle, inner_radius,
                                            outer_radius, line_width], (int, float)) + Gauge.mapping(isinstance,
                                                                                               [outer_color, pointer_color, origin_color], str)
            if False in instance:
                raise ValueError

            self.all = [center_x, center_y, angle, inner_radius, outer_radius,
                        outer_color, pointer_color, origin_color, line_width]
            self.figure = []
            self.stop_angle = angle
            self.graph_elem = graph_elem
            self.new(degree=angle, color=pointer_color)

        def new(self, degree=0, color=None):
            """
            Draw new pointer by angle, erase old pointer if exist
            degree defined as clockwise from negative x-axis.
            """
            (center_x, center_y, angle, inner_radius, outer_radius,
             outer_color, pointer_color, origin_color, line_width) = self.all
            pointer_color = color or pointer_color
            if self.figure != []:
                for figure in self.figure:
                    self.graph_elem.DeleteFigure(figure)
                self.figure = []
            d = degree - 90
            self.all[2] = degree
            dx1 = int(2 * inner_radius * math.sin(d / 180 * math.pi))
            dy1 = int(2 * inner_radius * math.cos(d / 180 * math.pi))
            dx2 = int(outer_radius * math.sin(d / 180 * math.pi))
            dy2 = int(outer_radius * math.cos(d / 180 * math.pi))
            self.figure.append(self.graph_elem.DrawLine((center_x - dx1, center_y - dy1),
                                                        (center_x + dx2, center_y + dy2),
                                                        color=pointer_color, width=line_width))
            self.figure.append(self.graph_elem.DrawCircle((center_x, center_y), inner_radius,
                                                          fill_color=origin_color, line_color=outer_color, line_width=line_width))

        def move(self, delta_x, delta_y):
            """
            Move pointer with delta x and delta y
            """
            if False in Gauge.mapping(isinstance, [delta_x, delta_y], (int, float)):
                raise ValueError
            self.all[:2] = [self.all[0] + delta_x, self.all[1] + delta_y]
            for figure in self.figure:
                self.graph_elem.MoveFigure(figure, delta_x, delta_y)

    class Tick():
        """
        Create tick on click for minor tick, also for major tick
        All angles defined as clockwise from negative x-axis.
        """

        def __init__(self, center_x=0, center_y=0, start_radius=90, stop_radius=100,
                     start_angle=0, stop_angle=360, step=6, line_color='black', line_width=2, graph_elem=None):

            instance = Gauge.mapping(isinstance, [center_x, center_y, start_radius,
                                            stop_radius, start_angle, stop_angle, step, line_width],
                               (int, float)) + [Gauge.mapping(isinstance, line_color, (list, str))]
            if False in instance:
                raise ValueError
            start_angle, stop_angle = Gauge.limit(start_angle), Gauge.limit(stop_angle)
            self.all = [center_x, center_y, start_radius, stop_radius,
                        start_angle, stop_angle, step, line_color, line_width]
            self.figure = []
            self.graph_elem = graph_elem

            self.new()

        def new(self):
            """
            Draw ticks on clock
            """
            (x, y, start_radius, stop_radius, start_angle, stop_angle, step,
             line_color, line_width) = self.all
            start_angle, stop_angle = (180 - start_angle, 180 - stop_angle
                                       ) if stop_angle < start_angle else (180 - stop_angle, 180 - start_angle)
            for i in range(start_angle, stop_angle + 1, step):
                start_x = x + start_radius * math.cos(i / 180 * math.pi)
                start_y = y + start_radius * math.sin(i / 180 * math.pi)
                stop_x = x + stop_radius * math.cos(i / 180 * math.pi)
                stop_y = y + stop_radius * math.sin(i / 180 * math.pi)
                self.figure.append(self.graph_elem.DrawLine((start_x, start_y),
                                                            (stop_x, stop_y), color=line_color, width=line_width))

        def move(self, delta_x, delta_y):
            """
            Move ticks by delta x and delta y
            """
            if False in Gauge.mapping(isinstance, [delta_x, delta_y], (int, float)):
                raise ValueError
            self.all[0] += delta_x
            self.all[1] += delta_y
            for figure in self.figure:
                self.graph_elem.MoveFigure(figure, delta_x, delta_y)

    """
    Create Gauge
    All angles defined as count clockwise from negative x-axis.
    Should create instance of clock, pointer, minor tick and major tick first.
    """
    def __init__(self, center=(0, 0), start_angle=0, stop_angle=180, major_tick_width=5, minor_tick_width=2,major_tick_start_radius=90, major_tick_stop_radius=100, minor_tick_step=5, major_tick_step=30, clock_radius=100, pointer_line_width=5, pointer_inner_radius=10, pointer_outer_radius=75, pointer_color='white', pointer_origin_color='black', pointer_outer_color='white', pointer_angle=0, degree=0, clock_color='white', major_tick_color='black', minor_tick_color='black', minor_tick_start_radius=90, minor_tick_stop_radius=100, graph_elem=None):

        self.clock = Gauge.Clock(start_angle=start_angle, stop_angle=stop_angle, fill_color=clock_color, radius=clock_radius, graph_elem=graph_elem)
        self.minor_tick = Gauge.Tick(start_angle=start_angle, stop_angle=stop_angle, line_width=minor_tick_width, line_color=minor_tick_color, start_radius=minor_tick_start_radius, stop_radius=minor_tick_stop_radius, graph_elem=graph_elem, step=minor_tick_step)
        self.major_tick = Gauge.Tick(start_angle=start_angle, stop_angle=stop_angle, line_width=major_tick_width, start_radius=major_tick_start_radius, stop_radius=major_tick_stop_radius, step=major_tick_step, line_color=major_tick_color, graph_elem=graph_elem)
        self.pointer = Gauge.Pointer(angle=pointer_angle, inner_radius=pointer_inner_radius, outer_radius=pointer_outer_radius, pointer_color=pointer_color, outer_color=pointer_outer_color, origin_color=pointer_origin_color, line_width=pointer_line_width, graph_elem=graph_elem)

        self.center_x, self.center_y = self.center = center
        self.degree = degree
        self.dx = self.dy = 1

    def move(self, delta_x, delta_y):
        """
        Move gauge to move all componenets in gauge.
        """
        self.center_x, self.center_y =self.center = (
            self.center_x+delta_x, self.center_y+delta_y)
        if self.clock:
            self.clock.move(delta_x, delta_y)
        if self.minor_tick:
            self.minor_tick.move(delta_x, delta_y)
        if self.major_tick:
            self.major_tick.move(delta_x, delta_y)
        if self.pointer:
            self.pointer.move(delta_x, delta_y)

    def change(self, degree=None, step=1, pointer_color=None):
        """
        Rotation of pointer
        call it with degree and step to set initial options for rotation.
        Without any option to start rotation.
        """
        if self.pointer:
            if degree != None:
                self.pointer.stop_degree = degree
                self.pointer.step = step if self.pointer.all[2] < degree else -step
                return True
            now = self.pointer.all[2]
            step = self.pointer.step
            new_degree = now + step
            if ((step > 0 and new_degree < self.pointer.stop_degree) or
                (step < 0 and new_degree > self.pointer.stop_degree)):
                    self.pointer.new(degree=new_degree, color=pointer_color)
                    return False
            else:
                self.pointer.new(degree=self.pointer.stop_degree, color=pointer_color)
                return True

# ------------------------------ BEGINNING OF CPU WIDGET GUI CODE ------------------------------

# DashGraph does the drawing of each graph
class DashGraph(object):
    def __init__(self, gsize, graph_elem, text_elem, starting_count, color):
        self.graph_current_item = 0
        self.graph_elem = graph_elem        # type: sg.Graph
        self.text_elem = text_elem
        self.prev_value = starting_count
        self.max_sent = 1
        self.color = color
        self.line_list = []                 # list of currently visible lines. Used to delete oild figures

        self.gauge = Gauge(pointer_color=color,
                        clock_color=color,
                        major_tick_color=color,
                        minor_tick_color=color,
                        pointer_outer_color=color,
                        major_tick_start_radius=gsize[1] - 10,
                        minor_tick_start_radius=gsize[1] - 10,
                        minor_tick_stop_radius=gsize[1] - 5,
                        major_tick_stop_radius=gsize[1] - 5,
                        clock_radius=gsize[1] - 5,
                        pointer_outer_radius=gsize[1] - 5,
                        major_tick_step=30,
                        minor_tick_step=15,
                        pointer_line_width=3,
                        pointer_inner_radius=10,
                        graph_elem=graph_elem)


        self.gauge.change(degree=0)

    def graph_percentage_abs(self, value):
        if self.gauge.change(pointer_color='red' if value > 50 else None):
            new_angle = value*180/100
            self.gauge.change(degree=new_angle, step=100, pointer_color='red' if value > 50 else None)
            self.gauge.change(pointer_color='red' if value > 50 else None)

    def text_display(self, text):
        self.text_elem.update(text)

def main(location):
    # A couple of "User defined elements" that combine several elements and enable bulk edits
    def Txt(text, **kwargs):
        return(sg.Text(text, font=('Helvetica 8'), **kwargs))

    def GraphColumn(name, key):
        layout = [
            [sg.Graph(gsize, (-gsize[0] // 2, 0), (gsize[0] // 2, gsize[1]), key=key+'-GRAPH-')],
            [sg.T(size=(5, 1), justification='c', font='Courier 10', k=key+'-GAUGE VALUE-')]]
        return sg.Column(layout, pad=(2, 2), element_justification='c')

    num_cores = len(psutil.cpu_percent(percpu=True))        # get the number of cores in the CPU

    sg.theme('black')
    sg.set_options(element_padding=(0,0), margins=(1,1), border_width=0)

    layout = [[ sg.Button(image_data=sg.red_x, button_color=('black', 'black'), key='Exit', tooltip='Closes window'),
                sg.Text('     CPU Core Usage')] ]

    # add on the graphs
    for rows in range(num_cores//NUM_COLS+1):
        # for cols in range(min(num_cores-rows*NUM_COLS, NUM_COLS)):
        layout += [[GraphColumn('CPU '+str(rows*NUM_COLS+cols), '-CPU-'+str(rows*NUM_COLS+cols)) for cols in range(min(num_cores-rows*NUM_COLS, NUM_COLS))]]

    # ----------------  Create Window  ----------------
    window = sg.Window('CPU Cores Usage Widget', layout,
                       keep_on_top=True,
                       auto_size_buttons=False,
                       grab_anywhere=True,
                       no_titlebar=True,
                       default_button_element_size=(12, 1),
                       return_keyboard_events=True,
                       alpha_channel=TRANSPARENCY,
                       use_default_focus=False,
                       finalize=True,
                       location=location,
                       right_click_menu=[[''], 'Exit'],
                       # transparent_color='black',
                       )

    # setup graphs & initial values
    graphs = [DashGraph(gsize, window['-CPU-'+str(i)+'-GRAPH-'],
                                window['-CPU-'+str(i) + '-GAUGE VALUE-'],
                                0, colors[i%6]) for i in range(num_cores) ]

    # ----------------  main loop  ----------------
    while True :
        # --------- Read and update window once every Polling Frequency --------
        event, values = window.read(timeout=POLL_FREQUENCY/2)
        if event in (sg.WIN_CLOSED, 'Exit'):         # Be nice and give an exit
            break
        # read CPU for each core
        stats = psutil.cpu_percent(interval=POLL_FREQUENCY/2/1000, percpu=True)

        # update each graph
        for i, util in enumerate(stats):
            graphs[i].graph_percentage_abs(util)
            graphs[i].text_display('{:2.0f}'.format(util))

    window.close()

if __name__ == "__main__":
    # when invoking this program, if a location is set on the command line, then the window will be created there. Use x,y with no ( )
    if len(sys.argv) > 1:
        location = sys.argv[1].split(',')
        location = (int(location[0]), int(location[1]))
    else:
        location = (None, None)
    main(location)
