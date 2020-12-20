# import PySimpleGUIWeb as sg
import PySimpleGUI as sg
import pymunk
import random
import socket

"""
    python -m pip install pymunk==5.7.0
    Demo that shows integrating PySimpleGUI with the pymunk library.  This combination
    of PySimpleGUI and pymunk could be used to build games.
    Note this exact same demo runs with PySimpleGUIWeb by changing the import statement
"""


class Ball():
    def __init__(self, x, y, r, graph_elem, *args, **kwargs):
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
        self.graph_elem = graph_elem

    def move(self):
        self.graph_elem.RelocateFigure(
            self.gui_circle_figure, self.body.position[0], ball.body.position[1])


class Playfield():
    def __init__(self, graph_elem):
        self.space = pymunk.Space()
        self.space.gravity = 0, 200
        self.add_wall((0, 400), (600, 400))  # ground
        self.add_wall((0, 0), (0, 600))  # Left side
        self.add_wall((600, 0), (600, 400))  # right side
        self.arena_balls = []               # type: List[Ball]
        self.graph_elem = graph_elem        # type: sg.Graph

    def add_wall(self, pt_from, pt_to):
        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        ground_shape = pymunk.Segment(body, pt_from, pt_to, 0.0)
        ground_shape.friction = 0.8
        ground_shape.elasticity = .99
        ground_shape.mass = pymunk.inf
        self.space.add(ground_shape)

    def add_random_balls(self):
        for i in range(1, 200):
            x = random.randint(0, 600)
            y = random.randint(0, 400)
            r = random.randint(1, 10)
            self.add_ball(x, y, r)

    def add_ball(self, x, y, r, fill_color='black', line_color='red'):
        ball = Ball(x, y, r, self.graph_elem)
        self.arena_balls.append(ball)
        area.space.add(ball.body, ball.shape)
        ball.gui_circle_figure = self.graph_elem.draw_circle(
            (x, y), r, fill_color=fill_color, line_color=line_color)
        return ball

    def shoot_a_ball(self, x, y, r, vector=(-10, 0), fill_color='black', line_color='red'):
        ball = self.add_ball(
            x, y, r, fill_color=fill_color, line_color=line_color)
        # ball.shape.surface_velocity=10
        ball.body.apply_impulse_at_local_point(100*pymunk.Vec2d(vector))


# -------------------  Build and show the GUI Window -------------------
graph_elem = sg.Graph((600, 400), (0, 400), (600, 0),
                      enable_events=True,
                      key='-GRAPH-',
                      background_color='lightblue')

hostname = socket.gethostbyname(socket.gethostname())
layout = [[sg.Text('Ball Test'), sg.Text('My IP {}'.format(hostname))],
          [graph_elem],
          [sg.Button('Kick'), sg.Button('Player 1 Shoot', size=(15, 2)),
           sg.Button('Player 2 Shoot', size=(15, 2)), sg.Button('Exit')]
          ]

window = sg.Window('Window Title', layout, disable_close=True, finalize=True)

area = Playfield(graph_elem)
area.add_wall((0,300), (300,300))
graph_elem.draw_line((0,300),(300,300))
# area.add_random_balls()

# ------------------- GUI Event Loop -------------------
while True:  # Event Loop
    event, values = window.read(timeout=10)
    # print(event, values)
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    
    area.space.step(0.01)

    if event == 'Player 2 Shoot':
        area.shoot_a_ball(555, 200, 5, (-10, 0),
                          fill_color='green', line_color='green')
    elif event == 'Player 1 Shoot':
        area.shoot_a_ball(10, 200, 5, (10, 0))

    for ball in area.arena_balls:
        if event == 'Kick':
            pos = ball.body.position[0], ball.body.position[1]-random.randint(1, 200)
            ball.body.position = pos
        ball.move()

window.close()
