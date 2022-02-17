import PySimpleGUI as sg
import math
"""
    Another simple Desktop Widget using PySimpleGUI

    A Counter Widget... X out of Y

    Maybe you're counting the number of classes left in a course you're
    working your way through, or the number of pokemons left to capture.

    Whatever it is, sometimes knowing your progress helps.  This widget shows
    you the current count and the total along with your % complete via a gauge.
    (Again, thank you to Jason for the gauge!)

    Copyright 2021 PySimpleGUI
"""

ALPHA = 0.9                 # Initial alpha until user changes
THEME = 'Dark green 3'      # Initial theme until user changes
refresh_font = sg.user_settings_get_entry('-refresh font-', 'Courier 8')
title_font = sg.user_settings_get_entry('-title font-', 'Courier 8')
main_number_font = sg.user_settings_get_entry('-main number font-', 'Courier 70')
main_info_size = (3,1)




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

GSIZE = (160, 160)

def choose_theme(location):
    layout = [[sg.Text(f'Current theme {sg.theme()}')],
              [sg.Listbox(values=sg.theme_list(), size=(20, 20), key='-LIST-', enable_events=True)],
              [sg.OK(), sg.Cancel()]]

    window = sg.Window('Look and Feel Browser', layout, location=location, keep_on_top=True)
    old_theme = sg.theme()
    while True:  # Event Loop
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit', 'OK', 'Cancel'):
            break
        sg.theme(values['-LIST-'][0])
        test_window=make_window(location=(location[0]-200, location[1]), test_window=True)
        test_window.read(close=True)
    window.close()

    if event == 'OK' and values['-LIST-']:
        sg.theme(values['-LIST-'][0])
        sg.user_settings_set_entry('-theme-', values['-LIST-'][0])
        return values['-LIST-'][0]
    else:
        sg.theme(old_theme)
    return  None

def make_window(location, test_window=False):
    title_font = sg.user_settings_get_entry('-title font-', 'Courier 8')
    title = sg.user_settings_get_entry('-title-', '')
    main_number_font = sg.user_settings_get_entry('-main number font-', 'Courier 70')

    if not test_window:
        theme = sg.user_settings_get_entry('-theme-', THEME)
        sg.theme(theme)

    alpha = sg.user_settings_get_entry('-alpha-', ALPHA)

    # ------------------- Window Layout -------------------
    # If this is a test window (for choosing theme), then uses some extra Text Elements to display theme info
    # and also enables events for the elements to make the window easy to close
    if test_window:
        top_elements = [[sg.Text(title, size=(20, 1), font=title_font, justification='c', k='-TITLE-', enable_events=True)],
                        [sg.Text('Click to close', font=title_font, enable_events=True)],
                        [sg.Text('This is theme', font=title_font, enable_events=True)],
                        [sg.Text(sg.theme(), font=title_font, enable_events=True)]]
        right_click_menu = [[''], ['Exit',]]
    else:
        top_elements = [[sg.Text(title, size=(20, 1), font=title_font, justification='c', k='-TITLE-')]]
        right_click_menu = [[''], ['Set Count','Set Goal','Choose Title', 'Edit Me', 'Change Theme', 'Save Location', 'Refresh', 'Set Title Font', 'Set Main Font','Alpha', [str(x) for x in range(1, 11)], 'Exit', ]]

    gsize = (100, 55)


    layout = top_elements + \
              [[sg.Text('0', size=main_info_size, font=main_number_font, k='-MAIN INFO-', justification='c', enable_events=test_window)],
               sg.vbottom([sg.Text(0, size=(3, 1), justification='r', font='courier 20'),
                           sg.Graph(gsize, (-gsize[0] // 2, 0), (gsize[0] // 2, gsize[1]), key='-Graph-'),
                           sg.Text(0, size=(3, 1), font='courier 20', k='-GOAL-')]),
               ]



    try:
        window = sg.Window('Counter Widget', layout, location=location, no_titlebar=True, grab_anywhere=True, margins=(0, 0), element_justification='c', element_padding=(0, 0), alpha_channel=alpha, finalize=True, right_click_menu=right_click_menu, right_click_menu_tearoff=False, keep_on_top=True)
    except Exception as e:
        if sg.popup_yes_no('Error creating your window', e, 'These are your current settings:', sg.user_settings(), 'Do you want to delete your settings file?') == 'Yes':
            sg.user_settings_delete_filename()
            sg.popup('Settings deleted.','Please restart your program')
            exit()
        window = None

    window.gauge = Gauge(pointer_color=sg.theme_text_color(), clock_color=sg.theme_text_color(), major_tick_color=sg.theme_text_color(),
                  minor_tick_color=sg.theme_input_background_color(), pointer_outer_color=sg.theme_text_color(), major_tick_start_radius=45,
                  minor_tick_start_radius=45, minor_tick_stop_radius=50, major_tick_stop_radius=50, major_tick_step=30, clock_radius=50, pointer_line_width=3, pointer_inner_radius=10, pointer_outer_radius=50, graph_elem=window['-Graph-'])

    window.gauge.change(degree=0)

    return window

def main():
    loc =  sg.user_settings_get_entry('-location-', (None, None))
    window = make_window(loc)
    try:
        current_count = int(sg.user_settings_get_entry('-current count-', 0))
        current_goal = int(sg.user_settings_get_entry('-goal-', 100))
        current_goal = current_goal if current_goal != 0 else 100
    except:
        if sg.popup_yes_no('Your count or goal number is not good.  Do you want to delete your settings file?', location=window.current_location()) == 'Yes':
            sg.user_settings_delete_filename()
            sg.popup('Settings deleted.','Please restart your program', location=window.current_location())
            exit()

    window['-MAIN INFO-'].update(current_count)
    window['-GOAL-'].update(current_goal)

    while True:             # Event Loop
        window.gauge.change()
        new_angle = current_count / current_goal * 180
        window.gauge.change(degree=new_angle, step=180)
        window.gauge.change()
        window['-GOAL-'].update(current_goal)
        window['-MAIN INFO-'].update(current_count)

        # -------------- Start of normal event loop --------------
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == 'Edit Me':
            sg.execute_editor(__file__)
        elif event == 'Set Count':
            new_count = sg.popup_get_text('Enter current count', default_text=current_count, location=window.current_location(), keep_on_top=True)
            if new_count is not None:
                try:
                    current_count = int(new_count)
                except:
                    sg.popup_error('Your count is not good.  Ignoring input.', location=window.current_location())
                    continue
                sg.user_settings_set_entry('-current count-', current_count)
        elif event == 'Set Goal':
            new_goal = sg.popup_get_text('Enter Goal', default_text=current_goal, location=window.current_location(), keep_on_top=True)
            if new_goal is not None:
                try:
                    current_goal = int(new_goal)
                except:
                    sg.popup_error('Your goal number is not good.  Ignoring input.', location=window.current_location())
                    continue
                current_goal = current_goal if current_goal != 0 else 100
                sg.user_settings_set_entry('-goal-', current_goal)
        elif event == 'Choose Title':
            new_title = sg.popup_get_text('Choose a title for your date', default_text=sg.user_settings_get_entry('-title-', '') , location=window.current_location(), keep_on_top=True)
            if new_title is not None:
                window['-TITLE-'].update(new_title)
                sg.user_settings_set_entry('-title-', new_title)
        elif event == 'Save Location':
            sg.user_settings_set_entry('-location-', window.current_location())
        elif event in [str(x) for x in range(1,11)]:
            window.set_alpha(int(event)/10)
            sg.user_settings_set_entry('-alpha-', int(event)/10)
        elif event == 'Change Theme':
            loc = window.current_location()
            if choose_theme(loc) is not None:
                # this is result of hacking code down to 99 lines in total. Not tried it before. Interesting test.
                _, window = window.close(), make_window(loc)
        elif event == 'Set Main Font':
            font = sg.popup_get_text('Main Information Font and Size (e.g. courier 70)', default_text=sg.user_settings_get_entry('-main number font-', main_number_font),location=window.current_location(), keep_on_top=True)
            if font:
                loc = window.current_location()
                sg.user_settings_set_entry('-main number font-', font)
                _, window = window.close(), make_window(loc)
        elif event == 'Set Title Font':
            font = sg.popup_get_text('Title Font and Size (e.g. courier 8)', default_text=sg.user_settings_get_entry('-title font-', title_font), location=window.current_location(), keep_on_top=True)
            if font:
                loc = window.current_location()
                sg.user_settings_set_entry('-title font-', font)
                _, window = window.close(), make_window(loc)



    window.close()


if __name__ == '__main__':
    main()