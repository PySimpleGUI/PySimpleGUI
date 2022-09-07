import PySimpleGUI as sg
import psutil
import sys
import math

"""
    Another simple Desktop Widget using PySimpleGUI
    This time a RAM Usage indicator using a custom Gauge element
    
    The Gauge class was developed by the brilliant PySimpleGUI user and support-helper @jason990420 
    It has been hacked on a bit, had classes and functions moved around.  It could be cleaned up some
    but it's "good enough" at this point to release as a demo.
    
    This is a good example of how you can use Graph Elements to create your own custom elements.
    This Gauge element is created from a Graph element. 

    Copyright 2020 PySimpleGUI.org
"""

ALPHA = 0.5
THEME = 'Dark Green 5'
UPDATE_FREQUENCY_MILLISECONDS = 2 * 1000






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
                self.figure.append(self.graph_elem.DrawCircle((x, y), r, fill_color=fill, line_color=line, line_width=width))
            else:
                self.figure.append(self.graph_elem.DrawArc((x - r, y + r), (x + r, y - r), stop - start, start, style='arc', arc_color=fill))

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
            self.new(degree=angle)

        def new(self, degree=0):
            """
            Draw new pointer by angle, erase old pointer if exist
            degree defined as clockwise from negative x-axis.
            """
            (center_x, center_y, angle, inner_radius, outer_radius,
             outer_color, pointer_color, origin_color, line_width) = self.all
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
            self.figure.append(self.graph_elem.DrawLine((center_x - dx1, center_y - dy1), (center_x + dx2, center_y + dy2), color=pointer_color, width=line_width))
            self.figure.append(self.graph_elem.DrawCircle((center_x, center_y), inner_radius, fill_color=origin_color, line_color=outer_color, line_width=line_width))

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
                self.figure.append(self.graph_elem.DrawLine((start_x, start_y), (stop_x, stop_y), color=line_color, width=line_width))

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
    def __init__(self, center=(0, 0), start_angle=0, stop_angle=180, major_tick_width=5, minor_tick_width=2,major_tick_start_radius=90, major_tick_stop_radius=100, major_tick_step=30, clock_radius=100, pointer_line_width=5, pointer_inner_radius=10, pointer_outer_radius=75, pointer_color='white', pointer_origin_color='black', pointer_outer_color='white', pointer_angle=0, degree=0, clock_color='white', major_tick_color='black', minor_tick_color='black', minor_tick_start_radius=90, minor_tick_stop_radius=100, graph_elem=None):

        self.clock = Gauge.Clock(start_angle=start_angle, stop_angle=stop_angle, fill_color=clock_color, radius=clock_radius, graph_elem=graph_elem)
        self.minor_tick = Gauge.Tick(start_angle=start_angle, stop_angle=stop_angle, line_width=minor_tick_width, line_color=minor_tick_color, start_radius=minor_tick_start_radius, stop_radius=minor_tick_stop_radius, graph_elem=graph_elem)
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

    def change(self, degree=None, step=1):
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
                    self.pointer.new(degree=new_degree)
                    return False
            else:
                self.pointer.new(degree=self.pointer.stop_degree)
                return True



def human_size(bytes, units=(' bytes', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB')):
    """ Returns a human readable string reprentation of bytes"""
    return str(bytes) + ' ' + units[0] if bytes < 1024 else human_size(bytes >> 10, units[1:])

def main(location):
    sg.theme(THEME)
    gsize = (100, 55)
    layout = [
        [sg.T('RAM', font='Any 20', background_color='black')],
        [sg.Graph(gsize, (-gsize[0] // 2, 0), (gsize[0] // 2, gsize[1]), key='-Graph-')],
        [sg.T(size=(5, 1), font='Any 20', justification='c', background_color='black', k='-gauge VALUE-')],
        [sg.T(size=(8, 1), font='Any 14', justification='c', background_color='black', k='-RAM USED-')],
         ]

    window = sg.Window('CPU Usage Widget Square', layout, location=location, no_titlebar=True, grab_anywhere=True, margins=(0, 0), element_padding=(0, 0), alpha_channel=ALPHA, background_color='black', element_justification='c', finalize=True, right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_VER_EXIT,  enable_close_attempted_event=True)

    gauge = Gauge(pointer_color=sg.theme_text_color(), clock_color=sg.theme_text_color(), major_tick_color=sg.theme_text_color(),
                  minor_tick_color=sg.theme_input_background_color(), pointer_outer_color=sg.theme_text_color(), major_tick_start_radius=45,
                  minor_tick_start_radius=45, minor_tick_stop_radius=50, major_tick_stop_radius=50, major_tick_step=30, clock_radius=50, pointer_line_width=3,
                  pointer_inner_radius=10, pointer_outer_radius=50, graph_elem=window['-Graph-'])

    gauge.change(degree=0)

    while True:  # Event Loop
        ram = psutil.virtual_memory()
        ram_percent = ram.percent

        if gauge.change():
            new_angle = ram_percent*180/100
            window['-gauge VALUE-'].update(f'{ram_percent}%')
            window['-RAM USED-'].update(f'{human_size(ram.used)}')
            gauge.change(degree=new_angle, step=180)
            gauge.change()
        # ----------- update the graphics and text in the window ------------

        # update the window, wait for a while, then check for exit
        event, values = window.read(timeout=UPDATE_FREQUENCY_MILLISECONDS)
        if event in (sg.WIN_CLOSE_ATTEMPTED_EVENT, 'Exit'):
            sg.user_settings_set_entry('-location-', window.current_location())  # The line of code to save the position before exiting
            break
        if event == 'Edit Me':
            sg.execute_editor(__file__)
        elif event == 'Version':
            sg.popup_scrolled(__file__, sg.get_versions(), location=window.current_location(), keep_on_top=True, non_blocking=True)
    window.close()


if __name__ == '__main__':

    if len(sys.argv) > 1:
        location = sys.argv[1].split(',')
        location = (int(location[0]), int(location[1]))
    else:
        location = sg.user_settings_get_entry('-location-', (None, None))
    main(location)
