import PySimpleGUI as sg
import os
import io
from PIL import Image, ImageDraw, ImageTk, ImageFont
import sys
from random import randint as rand
import chess
import chess.pgn

button_names = ('close', 'cookbook', 'cpu', 'github', 'pysimplegui', 'run', 'storage', 'timer')

ROOT_PATH = './' if sys.platform == 'linux' else 'C:\\Python\\PycharmProjects\\GooeyGUI\\'
CHESS_PATH = 'C:/Python/PycharmProjects/GooeyGUI/Chess'

# piece names
BLANK = 0
PAWNB = 1
KNIGHTB = 2
BISHOPB = 3
ROOKB = 4
KINGB = 5
QUEENB = 6
PAWNW = 7
KNIGHTW = 8
BISHOPW = 9
ROOKW = 10
KINGW = 11
QUEENW = 12

initial_board = [[ROOKB, KNIGHTB,  BISHOPB, KINGB, QUEENB, BISHOPB, KNIGHTB, ROOKB ],
                [PAWNB for _ in range(8)],
                [BLANK for _ in range(8)],
                [BLANK for _ in range(8)],
                [BLANK for _ in range(8)],
                [BLANK for _ in range(8)],
                [PAWNW for _ in range(8)],
                 [ROOKW, KNIGHTW, BISHOPW, KINGW, QUEENW, BISHOPW, KNIGHTW, ROOKW]]

blank = os.path.join(CHESS_PATH, 'blank.png')
bishopB = os.path.join(CHESS_PATH, 'bishopb.png')
bishopW = os.path.join(CHESS_PATH, 'bishopw.png')
pawnB = os.path.join(CHESS_PATH, 'pawnb.png')
pawnW = os.path.join(CHESS_PATH, 'pawnw.png')
knightB = os.path.join(CHESS_PATH, 'knightb.png')
knightW = os.path.join(CHESS_PATH, 'knightw.png')
rookB = os.path.join(CHESS_PATH, 'rookb.png')
rookW = os.path.join(CHESS_PATH, 'rookw.png')
queenB = os.path.join(CHESS_PATH, 'queenB.png')
queenW = os.path.join(CHESS_PATH, 'queenW.png')
kingB = os.path.join(CHESS_PATH, 'kingb.png')
kingW = os.path.join(CHESS_PATH, 'kingw.png')


images = {BISHOPB: bishopB, BISHOPW: bishopW, PAWNB: pawnB, PAWNW: pawnW, KNIGHTB: knightB, KNIGHTW: knightW,
          ROOKB: rookB, ROOKW: rookW, KINGB: kingB, KINGW: kingW, QUEENB: queenB, QUEENW: queenW, BLANK: blank}

def get_a_move():
    board = chess.Board()
    pgn = open('C:/Python/PycharmProjects/GooeyGUI/Chess/game.pgn')
    first_game = chess.pgn.read_game(pgn)
    for move in first_game.main_line():
        print(move)
        yield move


def render_square(image, key, location):
    if (location[0] + location[1]) % 2:
        color =  '#B58863'
    else:
        color = '#F0D9B5'
    return sg.RButton('', image_filename=image, size=(1, 1), button_color=('white', color), pad=(0, 0), key=key)


def redraw_board(window, board):
    for i in range(8):
        for j in range(8):
            if (i+j) % 2:
                color = '#B58863'
            else:
                color = '#F0D9B5'
            piece_image = images[board[i][j]]
            elem = window.FindElement(key=(i,j))
            elem.Update(button_color = ('white', color),
                        image_filename=piece_image,)

def update_board(board):
    # board[5][5] = KINGB
    return board

def DrawBoard():


    sg.SetOptions(auto_size_buttons=True, margins=(0,0), button_color=sg.COLOR_SYSTEM_DEFAULT)

    brn = sg.RButton('',image_filename=blank, size=(1,1), button_color=('white','#B58863') ,pad=(0,0), key='_close_')
    tan = sg.RButton('', image_filename=blank, size=(4,3), button_color=('white','#F0D9B5') ,pad=(0,0))

    board = initial_board

    board_layout = [[sg.T('     ')] + [sg.T(f'{a}', pad=((23,27),0), font='Any 13') for a in 'abcdefgh']]

    for i in range(8):
        row = [sg.T(str(8-i)+'   ', font='Any 13')]
        for j in range(8):
            piece_image = images[board[i][j]]
            row.append(render_square(piece_image, key=(i,j), location=(i,j)))
            # if (i+j) % 2:
            #     row.append(render_tan(piece_image, key=(i,j)))
            # else:
            #     row.append(render_brn(piece_image, key=(i,j)))
        row.append(sg.T(str(8-i)+'   ', font='Any 13'))
        board_layout.append(row)

    board_layout.append([sg.T('     ')] + [sg.T(f'{a}', pad=((23,27),0), font='Any 13') for a in 'abcdefgh'])

    controls_layout = [[sg.Text('Performance Parameters', font='Any 20')]]
    statistics_layout = [[sg.Text('Statistics', font=('Any 20'))]]

    layout = [[sg.TabGroup([[sg.Tab('Board',board_layout),
                             sg.Tab('Controls', controls_layout),
                             sg.Tab('Statistics', statistics_layout)]])]]

    window = sg.Window('Chess',
                       no_titlebar=False,
                       grab_anywhere=True,
                       keep_on_top=True,
                       icon='kingb.ico').Layout(layout)

    pgn = open('C:/Python/PycharmProjects/GooeyGUI/Chess/game.pgn')
    first_game = chess.pgn.read_game(pgn)
    moves = [move for move in first_game.main_line()]
    # ---===--- Loop taking in user input --- #
    i = 0
    while True:
        board = update_board(board)
        button, value = window.Read()
        if button is None:
            break
        move = moves[i]
        move_from = move.from_square
        move_to = move.to_square
        print(move_from, move_to)
        row = move_from//8
        col = move_from%8
        print(row, col)
        piece = board[row][col]
        board[row][col] = BLANK
        row = move_to//8
        col = move_to % 8
        board[row][col] = piece
        print(piece)
        redraw_board(window, board)
        i += 1
DrawBoard()