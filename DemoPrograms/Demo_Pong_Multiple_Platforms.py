# !/usr/bin/env python
# Based on work by - Siddharth Natamai
# At the moment, this source file runs on TWO of the 4 PySimpleGUI ports with a third one coming soon (Qt).
import PySimpleGUI as sg
import random

GAMEPLAY_SIZE = (700, 400)
BAT_SIZE = (20, 110)
STARTING_BALL_POSITION = (327, 200)
player_1_Starting_Score = 0
player_2_Starting_Score = 0
BALL_RADIUS = 12
# BACKGROUND_COLOR = 'lightblue'          # if running on PySimpleGUIWeb
BACKGROUND_COLOR = 'black'
# BALL_COLOR = 'black'                    # if running on PySimpleGUIWeb
BALL_COLOR = 'green1'
num_rounds = 0
while num_rounds == 0:
    try:
        num_rounds = int(sg.popup_get_text(
            'How many rounds would you like to play?'))
    except Exception as e:
        num_rounds = 0


class Ball:
    def __init__(self, graph, bat_1, bat_2, colour):
        self.graph = graph              # type: sg.Graph
        self.bat_1 = bat_1
        self.bat_2 = bat_2
        self.player_1_Score = player_1_Starting_Score
        self.player_2_Score = player_2_Starting_Score
        self.draw_P1 = None
        self.draw_P2 = None
        self.id = self.graph.draw_circle(
            STARTING_BALL_POSITION, BALL_RADIUS, line_color=colour, fill_color=colour)
        self.curx, self.cury = STARTING_BALL_POSITION
        # self.graph.relocate_figure(self.id, STARTING_BALL_POSITION[0], STARTING_BALL_POSITION[1])
        self.x = random.choice([-2.5, 2.5])
        self.y = -2.5

    def win_loss_check(self):
        winner = None
        if self.player_1_Score >= num_rounds:
            winner = 'Player Right Wins'
        if self.player_2_Score >= num_rounds:
            winner = 'Player Left Wins'
        return winner

    def update_player1_score(self, val):
        self.graph.delete_figure(self.draw_P1)
        self.draw_P1 = self.graph.draw_text(
            str(val), (170, 50), font=('Courier 60'), color='white')

    def update_player2_score(self, val):
        self.graph.delete_figure(self.draw_P2)
        self.draw_P2 = self.graph.draw_text(
            str(val), (550, 50), font=('courier 40'), color='white')

    def hit_bat(self, pos):
        bat_pos = (self.bat_1.curx, self.bat_1.cury)
        if pos[0] >= bat_pos[0] and pos[0] <= bat_pos[0]+BAT_SIZE[0]:
            if bat_pos[1] <= pos[1] <= bat_pos[1]+BAT_SIZE[1]:
                return True
            return False

    def hit_bat2(self, pos):
        bat_pos = (self.bat_2.curx, self.bat_2.cury)
        if pos[0] >= bat_pos[0] and pos[0] <= bat_pos[0]+BAT_SIZE[0]:
            if bat_pos[1] <= pos[1] <= bat_pos[1]+BAT_SIZE[1]:
                return True
            return False

    def draw(self):
        self.curx += self.x
        self.cury += self.y
        self.graph.relocate_figure(self.id, self.curx, self.cury)
        if self.cury <= 0:            # see if hit top or bottom of play area. If so, reverse y direction
            self.y = 4
            self.cury = 0
        if self.cury >= GAMEPLAY_SIZE[1]-BALL_RADIUS/2:
            self.y = -4
            self.cury = GAMEPLAY_SIZE[1]-BALL_RADIUS/2
        if self.curx <= 0:                     # see if beyond player
            self.player_1_Score += 1
            self.graph.relocate_figure(
                self.id, STARTING_BALL_POSITION[0], STARTING_BALL_POSITION[1])
            self.x = 4
            self.update_player2_score(self.player_1_Score)
            self.curx, self.cury = STARTING_BALL_POSITION
        if self.curx >= GAMEPLAY_SIZE[0]:
            self.player_2_Score += 1
            self.graph.relocate_figure(
                self.id, STARTING_BALL_POSITION[0], STARTING_BALL_POSITION[1])
            self.x = -4
            self.update_player1_score(self.player_2_Score)
            self.curx, self.cury = STARTING_BALL_POSITION
        if self.hit_bat((self.curx, self.cury)):
            self.x = 4
        if self.hit_bat2((self.curx, self.cury)):
            self.x = -4


class PongBall():
    def __init__(self, graph: sg.Graph, colour, x, width=BAT_SIZE[0], height=BAT_SIZE[1]):
        self.graph = graph
        self.id = graph.draw_rectangle(
            (x - width / 2, 200), (x + width / 2, 200 + height), fill_color=colour)
        self.y = 0
        self.x = x
        self.curx = x
        self.cury = height/2

    def up(self, amount):
        self.y = -amount

    def down(self, amount):
        self.y = amount

    @property
    def curr_pos(self):
        pos = self.cury
        return pos

    def draw(self):
        self.graph.relocate_figure(self.id, self.curx, self.cury)
        if self.cury + self.y + BAT_SIZE[1] <= GAMEPLAY_SIZE[1] and self.cury + self.y + BAT_SIZE[1] >= 0:
            self.cury += self.y
        if self.cury <= 0:
            self.cury = 0
            self.y = 0
        if self.cury >= GAMEPLAY_SIZE[1]:
            self.cury = GAMEPLAY_SIZE[1]
            self.y = 0


def pong():
    layout = [[sg.Graph(GAMEPLAY_SIZE,
                        (0, GAMEPLAY_SIZE[1]),
                        (GAMEPLAY_SIZE[0], 0),
                        background_color=BACKGROUND_COLOR,
                        key='-GRAPH-')],
              [sg.Text(''),
               sg.Button('Exit'),
               sg.Text('Speed'),
               sg.Slider((0, 20),
                         default_value=10,
                         orientation='h',
                         enable_events=True,
                         key='-SPEED-')]
              ]

    window = sg.Window(
        'Pong', layout, return_keyboard_events=True, finalize=True)

    graph_elem = window['-GRAPH-']                  # type: sg.Graph

    bat_1 = PongBall(graph_elem, 'red', 30)
    bat_2 = PongBall(graph_elem, 'blue', 670)
    ball_1 = Ball(graph_elem, bat_1, bat_2, 'green1')
    sleep_time = 10

    while True:
        ball_1.draw()
        bat_1.draw()
        bat_2.draw()

        event, values = window.read(
            timeout=sleep_time)         # type: str, str
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        elif event.startswith('Up') or event.endswith('Up'):
            bat_2.up(5)
        elif event.startswith('Down') or event.endswith('Down'):
            bat_2.down(5)
        elif event == 'w':
            bat_1.up(5)
        elif event == 's':
            bat_1.down(5)
        elif event == '-SPEED-':
            sleep_time = int(values['-SPEED-'])

        if ball_1.win_loss_check():
            sg.popup('Game Over', ball_1.win_loss_check() + ' won!!')
            break
    window.close()


if __name__ == '__main__':
    pong()
