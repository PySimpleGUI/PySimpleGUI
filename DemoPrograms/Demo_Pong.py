# !/usr/bin/env python

"""
    Pong

    One of the most important video games.
    Pong was created by Al Alcorn and it did not use a microprocessor

    This demo is based on some initial code by Siddharth Natamai

    In 2021, it was reworked by Jay Nabaonne into this version you see today.

    A big

     ###### ##  ## ###### ##  ## ##  ##   ##  ## ###### ##  ##    ##
       ##   ##  ## ##  ## ### ## ## ##    ##  ## ##  ## ##  ##    ##
       ##   ###### ##  ## ###### ####     ##  ## ##  ## ##  ##    ##
       ##   ##  ## ###### ## ### ####     ###### ##  ## ##  ##    ##
       ##   ##  ## ##  ## ##  ## ## ##      ##   ##  ## ##  ##
       ##   ##  ## ##  ## ##  ## ##  ##    ####  ###### ######    ##

    to Jay for making it a smooth playing game.
    @jaynabonne https://github.com/jaynabonne

    Copyright 2021 PySimpleGUI, Jay Nabonne
"""

import PySimpleGUI as sg
import random
import datetime


GAMEPLAY_SIZE = (700, 400)
BAT_SIZE = (20, 110)
STARTING_BALL_POSITION = (327, 200)
BALL_RADIUS = 12
BACKGROUND_COLOR = 'black'
BALL_COLOR = 'green1'
BALL_SPEED = 300
BAT_SPEED = 400

UP_ARROW = 38
DOWN_ARROW = 40

player1_up_keycode = ord('W')
player1_down_keycode = ord('S')
player2_up_keycode = UP_ARROW
player2_down_keycode = DOWN_ARROW

num_rounds = 10


class Bat:
    def __init__(self, graph: sg.Graph, colour, x, field_height):
        self.graph = graph
        self.field_height = field_height
        self.width = BAT_SIZE[0]
        self.height = BAT_SIZE[1]
        self.current_x = x
        self.current_y = self.field_height / 2 - self.height / 2
        self.id = graph.draw_rectangle(
            (self.current_x, self.current_y),
            (self.current_x + self.width, self.current_y + self.height),
            fill_color=colour
        )
        self.vy = 0

    def stop(self):
        self.vy = 0

    def up(self):
        self.vy = -BAT_SPEED

    def down(self):
        self.vy = BAT_SPEED

    def is_hit_by(self, pos):
        bat_p0 = (self.current_x, self.current_y)
        bat_p1 = (bat_p0[0] + self.width, bat_p0[1] + self.height)
        return bat_p0[0] <= pos[0] <= bat_p1[0] and bat_p0[1] <= pos[1] <= bat_p1[1]

    def update(self, delta: float):
        new_y = self.current_y + self.vy * delta
        if new_y <= 0:
            new_y = 0
            self.stop()
        if new_y + self.height >= self.field_height:
            new_y = self.field_height - self.height
            self.stop()
        self.current_y = new_y

        self.graph.relocate_figure(self.id, self.current_x, self.current_y)


class Ball:
    def __init__(self, graph: sg.Graph, bat_1: Bat, bat_2: Bat, colour):
        self.graph = graph              # type: sg.Graph
        self.bat_1 = bat_1
        self.bat_2 = bat_2
        self.id = self.graph.draw_circle(
            STARTING_BALL_POSITION, BALL_RADIUS, line_color=colour, fill_color=colour)
        self.current_x, self.current_y = STARTING_BALL_POSITION
        self.vx = random.choice([-BALL_SPEED, BALL_SPEED])
        self.vy = -BALL_SPEED

    def hit_left_bat(self):
        return self.bat_1.is_hit_by((self.current_x - BALL_RADIUS, self.current_y))

    def hit_right_bat(self):
        return self.bat_2.is_hit_by((self.current_x + BALL_RADIUS, self.current_y))

    def update(self, delta: float):
        self.current_x += self.vx * delta
        self.current_y += self.vy * delta
        if self.current_y <= BALL_RADIUS:            # see if hit top or bottom of play area. If so, reverse y direction
            self.vy = -self.vy
            self.current_y = BALL_RADIUS
        if self.current_y >= GAMEPLAY_SIZE[1] - BALL_RADIUS:
            self.vy = -self.vy
            self.current_y = GAMEPLAY_SIZE[1] - BALL_RADIUS
        if self.hit_left_bat():
            self.vx = abs(self.vx)
        if self.hit_right_bat():
            self.vx = -abs(self.vx)

        self.position_to_current()

    def position_to_current(self):
        self.graph.relocate_figure(self.id, self.current_x - BALL_RADIUS, self.current_y - BALL_RADIUS)

    def restart(self):
        self.current_x, self.current_y = STARTING_BALL_POSITION
        self.position_to_current()


class Scores:
    def __init__(self, graph: sg.Graph):
        self.player_1_score = 0
        self.player_2_score = 0
        self.score_1_element = None
        self.score_2_element = None
        self.graph = graph

        self.draw_player1_score()
        self.draw_player2_score()

    def draw_player1_score(self):
        if self.score_1_element:
            self.graph.delete_figure(self.score_1_element)
        self.score_1_element = self.graph.draw_text(
            str(self.player_1_score), (170, 50), font='Courier 40', color='white')

    def draw_player2_score(self):
        if self.score_2_element:
            self.graph.delete_figure(self.score_2_element)
        self.score_2_element = self.graph.draw_text(
            str(self.player_2_score), (550, 50), font='Courier 40', color='white')

    def win_loss_check(self):
        if self.player_1_score >= num_rounds:
            return 'Left player'
        if self.player_2_score >= num_rounds:
            return 'Right player'
        return None

    def increment_player_1(self):
        self.player_1_score += 1
        self.draw_player1_score()

    def increment_player_2(self):
        self.player_2_score += 1
        self.draw_player2_score()

    def reset(self):
        self.player_1_score = 0
        self.player_2_score = 0
        self.draw_player1_score()
        self.draw_player2_score()


def check_ball_exit(ball: Ball, scores: Scores):
    if ball.current_x <= 0:
        scores.increment_player_2()
        ball.restart()
    if ball.current_x >= GAMEPLAY_SIZE[0]:
        scores.increment_player_1()
        ball.restart()


def goto_menu(window):
    window['-MAIN_MENU-'].update(visible=True)
    window['-GAME-'].update(visible=False)


def pong():
    sleep_time = 10

    inner_layout = [[sg.Graph(GAMEPLAY_SIZE,
                        (0, GAMEPLAY_SIZE[1]),
                        (GAMEPLAY_SIZE[0], 0),
                        background_color=BACKGROUND_COLOR,
                        key='-GRAPH-')],
              [sg.Button('Back to Menu', key="-MENU-")]]

    main_menu_layout = [[sg.Text("Pong", font="Courier 40", justification="center", size=(None, 1))],
                        [sg.Text("-- Instructions --", font="Courier 16")],
                        [sg.Text("Left player controls: W and S", font="Courier 12")],
                        [sg.Text("Right player controls: \u2191 and \u2193", font="Courier 12")],
                        [sg.Text("Escape to pause game", font="Courier 12")],
                        [sg.Text("", font="Courier 8")],
                        [sg.Text("Winner is first to 10 points", font="Courier 12")],
                        [sg.Text("", font="Courier 8")],
                        [sg.Button("Start", key='-START-', font="Courier 24"),
                        sg.Button("Quit", key='-QUIT-', font="Courier 24")]]

    layout = [[sg.pin(sg.Column(main_menu_layout, key='-MAIN_MENU-', size=GAMEPLAY_SIZE)),
               sg.pin(sg.Column(inner_layout, key='-GAME-', visible=False))]]

    window = sg.Window('Pong', layout, finalize=True, use_default_focus=False)

    window.bind("<Key>", "+KEY+")
    window.bind("<KeyRelease>", "-KEY-")

    graph_elem = window['-GRAPH-']                  # type: sg.Graph

    scores = Scores(graph_elem)
    bat_1 = Bat(graph_elem, 'red', 30, GAMEPLAY_SIZE[1])
    bat_2 = Bat(graph_elem, 'blue', GAMEPLAY_SIZE[0] - 30 - BAT_SIZE[0], GAMEPLAY_SIZE[1])
    ball_1 = Ball(graph_elem, bat_1, bat_2, 'green1')

    start = datetime.datetime.now()
    last_post_read_time = start

    game_playing = False

    while True:
        pre_read_time = datetime.datetime.now()
        processing_time = (pre_read_time - last_post_read_time).total_seconds()
        time_to_sleep = sleep_time - int(processing_time*1000)
        time_to_sleep = max(time_to_sleep, 0)

        event, values = window.read(time_to_sleep)
        now = datetime.datetime.now()
        delta = (now-last_post_read_time).total_seconds()
        # read_delta = (now-pre_read_time).total_seconds()
        last_post_read_time = now
        # print("**", event, delta, time_to_sleep, processing_time, read_delta)
        if event in (sg.WIN_CLOSED, "-QUIT-"):
            break
        elif event == "-START-":
            scores.reset()
            ball_1.restart()
            window['-MAIN_MENU-'].update(visible=False)
            window['-GAME-'].update(visible=True)
            sg.popup('\nPress a key to begin.\n',
                     no_titlebar=True,
                     font="Courier 12",
                     text_color=sg.BLUES[0],
                     background_color=sg.YELLOWS[1],
                     any_key_closes=True,
                     button_type=sg.POPUP_BUTTONS_NO_BUTTONS)
            last_post_read_time = datetime.datetime.now()
            game_playing = True
        elif event == "-MENU-":
            game_playing = False
            goto_menu(window)
        elif game_playing:
            if event == "+KEY+":
                if window.user_bind_event.keycode == player1_up_keycode:
                    bat_1.up()
                elif window.user_bind_event.keycode == player1_down_keycode:
                    bat_1.down()
                elif window.user_bind_event.keycode == player2_up_keycode:
                    bat_2.up()
                elif window.user_bind_event.keycode == player2_down_keycode:
                    bat_2.down()
            elif event == "-KEY-":
                if window.user_bind_event.keycode in [player1_up_keycode, player1_down_keycode]:
                    bat_1.stop()
                elif window.user_bind_event.keycode in [player2_up_keycode, player2_down_keycode]:
                    bat_2.stop()
                elif window.user_bind_event.keycode == 27:
                    sg.popup('\nPaused. Press a key to resume.\n',
                             no_titlebar=True,
                             font="Courier 12",
                             text_color=sg.BLUES[0],
                             background_color=sg.YELLOWS[1],
                             any_key_closes=True,
                             button_type=sg.POPUP_BUTTONS_NO_BUTTONS)
                    last_post_read_time = datetime.datetime.now()

        if game_playing:
            ball_1.update(delta)
            bat_1.update(delta)
            bat_2.update(delta)

            check_ball_exit(ball_1, scores)

            winner = scores.win_loss_check()
            if winner is not None:
                sg.popup('Game Over', winner + ' won!!', no_titlebar=True)
                game_playing = False
                goto_menu(window)

    window.close()


if __name__ == '__main__':
    pong()
