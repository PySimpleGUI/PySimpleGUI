import PySimpleGUI as sg
# import PySimpleGUIWeb as sg
import pymunk
import random
import socket

# Yet another usage of Graph element and physics from pymunk.


"""
    To get a good version of pymunk that works with this code:
    python -m pip install pymunk==5.7.0
    Demo that shows integrating PySimpleGUI with the pymunk library.  This combination
    of PySimpleGUI and pymunk could be used to build games.
    Note this exact same demo runs with PySimpleGUIWeb by changing the import statement
"""


class Ball():
    def __init__(self, x, y, r, *args, **kwargs):
        mass = 10
        # Create a Body with mass and moment
        self.body = pymunk.Body(
            mass, pymunk.moment_for_circle(mass, 0, r, (0, 0)))
        self.body.position = x, y
        # Create a box shape and attach to body
        self.shape = pymunk.Circle(self.body, r, offset=(0, 0))
        self.shape.elasticity = 0.99999
        self.shape.friction = 0.8
        self.gui_circle_figure = None


class Playfield():
    def __init__(self, graph_elem):
        self.graph_elem = graph_elem
        self.space = pymunk.Space()
        self.space.gravity = 0, 200
        self.add_wall((0, 400), (600, 400))  # ground
        self.add_wall((0, 0), (0, 600))  # Left side
        self.add_wall((600, 0), (600, 400))  # right side

    def add_wall(self, pt_from, pt_to):
        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        ground_shape = pymunk.Segment(body, pt_from, pt_to, 0.0)
        ground_shape.friction = 0.8
        ground_shape.elasticity = .99
        self.space.add(ground_shape)

    def add_balls(self):
        self.arena_balls = []
        for i in range(1, 200):
            x = random.randint(0, 600)
            y = random.randint(0, 400)
            r = random.randint(1, 10)
            ball = Ball(x, y, r)
            self.arena_balls.append(ball)
            self.space.add(ball.body, ball.shape)
            ball.gui_circle_figure = self.graph_elem.draw_circle(
                (x, y), r, fill_color='black', line_width=0)


def main():



    # -------------------  Build and show the GUI Window -------------------
    graph_elem = sg.Graph((600, 400), (0, 400), (600, 0),
                          enable_events=True, key='-GRAPH-', background_color='lightblue')

    hostname = socket.gethostbyname(socket.gethostname())
    layout = [[sg.Text('Ball Test'), sg.Text('My IP '+hostname)],
              [graph_elem],
              # [sg.Up(), sg.Down()],
              [sg.Button('Kick'), sg.Button('Exit')]]

    window = sg.Window('Window Title', layout, finalize=True)

    area = Playfield(graph_elem)
    area.add_balls()

    # ------------------- GUI Event Loop -------------------
    while True:  # Event Loop
        event, values = window.read(timeout=0)
        # print(event, values)
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        area.space.step(0.02)

        for ball in area.arena_balls:
            if event == 'Kick':
                ball.body.position = ball.body.position[0], ball.body.position[1]-random.randint(
                    1, 200)
            graph_elem.RelocateFigure(
                ball.gui_circle_figure, ball.body.position[0], ball.body.position[1])

    window.close()

if __name__ == '__main__':
    main()