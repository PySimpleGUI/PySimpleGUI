import PySimpleGUI as sg
import pymunk
import random

"""
    Demo that shows integrating PySimpleGUI with the pymunk library.  This combination
    of PySimpleGUI and pymynk could be used to build games.
    Note this exact same demo runs with PySimpleGUIWeb by changing the import statement
"""

class Ball():
    def __init__(self, x, y, r, *args, **kwargs):
        mass = 10
        self.body = pymunk.Body(mass,
                                pymunk.moment_for_circle(mass, 0, r, (0, 0)))  # Create a Body with mass and moment
        self.body.position = x, y
        self.shape = pymunk.Circle(self.body, r, offset=(0, 0))  # Create a box shape and attach to body
        self.shape.elasticity = 0.95
        self.shape.friction = 0.9
        self.gui_circle_figure = None


graph_elem = sg.Graph((400, 400), (0, 400), (400, 0), enable_events=True, key='_GRAPH_', background_color='lightblue')

layout = [[sg.Text('Ball Test', tooltip='Tips')],
          [graph_elem],
          [sg.Button('Exit')]]

window = sg.Window('Window Title', layout, ).Finalize()

space = pymunk.Space()
space.gravity = 0, 1000

# ground
ground_body = pymunk.Body(body_type=pymunk.Body.STATIC)
ground_shape = pymunk.Segment(ground_body, (0, 400), (400, 400), 0.0)
ground_shape.friction = 0.9
ground_shape.elasticity = 0.95
space.add(ground_shape)

arena_balls = []
for i in range(1, 300):
    x = random.randint(100, 300)
    y = random.randint(100, 300)
    r = random.randint(5, 10)
    ball = Ball(x, y, r)
    ball.gui_circle_figure = graph_elem.DrawCircle((x, y), r, fill_color='black', line_color='red')
    arena_balls.append(ball)
    space.add(ball.body, ball.shape)

while True:  # Event Loop
    event, values = window.Read(timeout=0)
    # print(event, values)
    if event in (None, 'Exit'):
        break
    space.step(0.01)
    for ball in arena_balls:
        graph_elem.RelocateFigure(ball.gui_circle_figure, ball.body.position[0], ball.body.position[1])

window.Close()
