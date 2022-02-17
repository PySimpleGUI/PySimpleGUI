#!/usr/bin/env python
import PySimpleGUI as sg
import psutil
import sys
import math

"""
    Desktop "Rainmeter" style widget - Drive usage
    Requires: psutil
    Uses a "Gauge" to display drive usage
"""

ALPHA = 0.7
THEME = 'black'
UPDATE_FREQUENCY_MILLISECONDS = 20 * 1000

BAR_COLORS = ('#23a0a0', '#56d856', '#be45be', '#5681d8', '#d34545', '#BE7C29')
gsize = (50, 30)

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
        return number1 + number1

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



def human_size(bytes, units=(' bytes', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB')):
    """ Returns a human readable string reprentation of bytes"""
    return str(bytes) + ' ' + units[0] if bytes < 1024 else human_size(bytes >> 10, units[1:])


def update_window(window):
    particians = psutil.disk_partitions()
    for count, part in enumerate(particians):
        mount = part[0]
        try:
            usage = psutil.disk_usage(mount)
            window[('-NAME-', mount)].update(mount)
            # window[('-PROG-', mount)].update_bar(int(usage.percent))
            window[('-%-', mount)].update(f'{usage.percent}%')
            window[('-STATS-', mount)].update(f'{human_size(usage.used)} / {human_size(usage.total)} = {human_size(usage.free)} free')
            gauge = Gauge(pointer_color=window[('-GRAPH-', mount)].metadata,
                          clock_color=window[('-GRAPH-', mount)].metadata,
                          major_tick_color=sg.theme_input_background_color(),
                          minor_tick_color=sg.theme_input_text_color(),
                          pointer_outer_color=sg.theme_input_background_color(),
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
                          graph_elem=window[('-GRAPH-', mount)])
            gauge.change(degree=0)
            gauge.change(degree=180 * usage.percent / 100, step=180)
            gauge.change()
        except KeyError as e:       # A key error means a new drive was added
            print('Got a key error, so a new drive was added. Window will restart')
            return False
        except BaseException as e:
            print(e)



    return True

def create_window(location):
    layout = [[sg.Text('Drive Status', font='Any 16')]]

    # Add a row for every partician that has a bar graph and text stats
    particians = psutil.disk_partitions()
    for count, part in enumerate(particians):
        mount = part[0]
        try:
            bar_color = sg.theme_progress_bar_color()
            this_color = BAR_COLORS[count % len(BAR_COLORS)]
            usage = psutil.disk_usage(mount)
            stats_info = f'{human_size(usage.used)} / {human_size(usage.total)} = {human_size(usage.free)} free'
            layout += [[sg.Text(mount, size=(3, 1), key=('-NAME-', mount)),
                        sg.Graph(gsize, (-gsize[0] // 2, 0), (gsize[0] // 2, gsize[1]), key=('-GRAPH-', mount), metadata=this_color),
                        # sg.ProgressBar(100, 'h', size=(10, 15), key=('-PROG-', mount), bar_color=(this_color, bar_color[1])),
                        sg.Text(f'{usage.percent}%', size=(6, 1), key=('-%-', mount)), sg.T(stats_info, size=(30, 1), key=('-STATS-', mount)),
                        ]]
        except:
            pass
    layout += [[sg.Text('Refresh', font='Any 8', key='-REFRESH-', enable_events=True), sg.Text('❎', enable_events=True, key='Exit Text')]]

    # ----------------  Create Window  ----------------
    window = sg.Window('Drive Status Widget', layout, location=location, keep_on_top=True, grab_anywhere=True, no_titlebar=True, alpha_channel=ALPHA, use_default_focus=False,
                       finalize=True)
    return window

def main(location):
    # Turn off the popups because key errors are normal in this program.
    # Will get a key error is a new drive is added. Want to get the key error as an exception.
    sg.set_options(suppress_error_popups=True, suppress_raise_key_errors=False, suppress_key_guessing=True)
    sg.theme(THEME)

    window = create_window(location)

    update_window(window)  # sets the progress bars

    # ----------------  Event Loop  ----------------
    while True:
        event, values = window.read(timeout=UPDATE_FREQUENCY_MILLISECONDS)
        if event == sg.WIN_CLOSED or event.startswith('Exit'):
            break
        if not update_window(window):
            window.close()
            window = create_window(location)
            update_window(window)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        location = sys.argv[1].split(',')
        location = (int(location[0]), int(location[1]))
    else:
        location = (None, None)
    main(location)

