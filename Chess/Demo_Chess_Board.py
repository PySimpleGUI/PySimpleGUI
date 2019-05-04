import PySimpleGUI as sg
import os
import chess
import chess.pgn
import copy
import time

button_names = ('close', 'cookbook', 'cpu', 'github', 'pysimplegui', 'run', 'storage', 'timer')

CHESS_PATH = os.path.dirname(os.path.abspath(__file__))  # path to the chess pieces

BLANK = 0  # piece names
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
                [PAWNB,]*8,
                [BLANK,]*8,
                [BLANK,]*8,
                [BLANK,]*8,
                [BLANK,]*8,
                [PAWNW,]*8,
                [ROOKW, KNIGHTW, BISHOPW, KINGW, QUEENW, BISHOPW, KNIGHTW, ROOKW]]

blank = os.path.join(CHESS_PATH, 'blank.png')
bishopB = os.path.join(CHESS_PATH, 'nbishopb.png')
bishopW = os.path.join(CHESS_PATH, 'nbishopw.png')
pawnB = os.path.join(CHESS_PATH, 'npawnb.png')
pawnW = os.path.join(CHESS_PATH, 'npawnw.png')
knightB = os.path.join(CHESS_PATH, 'nknightb.png')
knightW = os.path.join(CHESS_PATH, 'nknightw.png')
rookB = os.path.join(CHESS_PATH, 'nrookb.png')
rookW = os.path.join(CHESS_PATH, 'nrookw.png')
queenB = os.path.join(CHESS_PATH, 'nqueenB.png')
queenW = os.path.join(CHESS_PATH, 'nqueenW.png')
kingB = os.path.join(CHESS_PATH, 'nkingb.png')
kingW = os.path.join(CHESS_PATH, 'nkingw.png')

images = {BISHOPB: bishopB, BISHOPW: bishopW, PAWNB: pawnB, PAWNW: pawnW, KNIGHTB: knightB, KNIGHTW: knightW,
          ROOKB: rookB, ROOKW: rookW, KINGB: kingB, KINGW: kingW, QUEENB: queenB, QUEENW: queenW, BLANK: blank}

def open_pgn_file(filename):
    pgn = open(filename)
    first_game = chess.pgn.read_game(pgn)
    moves = [move for move in first_game.main_line()]
    return moves

def render_square(image, key, location):
    if (location[0] + location[1]) % 2:
        color =  '#B58863'
    else:
        color = '#F0D9B5'
    return sg.RButton('', image_filename=image, size=(1, 1), button_color=('white', color), pad=(0, 0), key=key)

def redraw_board(window, board):
    for i in range(8):
        for j in range(8):
            color = '#B58863' if (i+j) % 2 else '#F0D9B5'
            piece_image = images[board[i][j]]
            elem = window.FindElement(key=(i,j))
            elem.Update(button_color = ('white', color),
                        image_filename=piece_image,)

def PlayGame():

    menu_def = [['&File', ['&Open PGN File', 'E&xit' ]],
                ['&Help', '&About...'],]

    # sg.SetOptions(margins=(0,0))
    sg.ChangeLookAndFeel('GreenTan')
    # create initial board setup
    board = copy.deepcopy(initial_board)
    # the main board display layout
    board_layout = [[sg.T('     ')] + [sg.T('{}'.format(a), pad=((23,27),0), font='Any 13') for a in 'abcdefgh']]
    # loop though board and create buttons with images
    for i in range(8):
        row = [sg.T(str(8-i)+'   ', font='Any 13')]
        for j in range(8):
            piece_image = images[board[i][j]]
            row.append(render_square(piece_image, key=(i,j), location=(i,j)))
        row.append(sg.T(str(8-i)+'   ', font='Any 13'))
        board_layout.append(row)
    # add the labels across bottom of board
    board_layout.append([sg.T('     ')] + [sg.T('{}'.format(a), pad=((23,27),0), font='Any 13') for a in 'abcdefgh'])

    # setup the controls on the right side of screen
    openings = ('Any', 'Defense', 'Attack', 'Trap', 'Gambit','Counter', 'Sicillian', 'English','French', 'Queen\'s openings', 'King\'s Openings','Indian Openings')

    board_controls = [[sg.RButton('New Game', key='Open PGN File'), sg.RButton('Draw')],
                      [sg.RButton('Resign Game'), sg.RButton('Set FEN')],
                      [sg.RButton('Player Odds'),sg.RButton('Training') ],
                      [sg.Drop(openings),sg.Text('Opening/Style')],
                      [sg.CBox('Play a White', key='_white_')],
                      [sg.Text('Move List')],
                      [sg.Multiline([], do_not_clear=True, autoscroll=True, size=(15,10),key='_movelist_')],]

    # layouts for the tabs
    controls_layout = [[sg.Text('Performance Parameters', font='_ 20')],
                       [sg.T('Put stuff like AI engine tuning parms on this tab')]]

    statistics_layout = [[sg.Text('Statistics', font=('_ 20'))],
                         [sg.T('Game statistics go here?')]]

    board_tab = [[sg.Column(board_layout)]]

    # the main window layout
    layout = [[sg.Menu(menu_def, tearoff=False)],
              [sg.TabGroup([[sg.Tab('Board',board_tab),
                             sg.Tab('Controls', controls_layout),
                             sg.Tab('Statistics', statistics_layout)]], title_color='red'),
               sg.Column(board_controls)],
              [sg.Text('Click anywhere on board for next move', font='_ 14')]]

    window = sg.Window('Chess', default_button_element_size=(12,1), auto_size_buttons=False, icon='kingb.ico').Layout(layout)

    # ---===--- Loop taking in user input --- #
    i = 0
    moves = None
    while True:
        button, value = window.Read()
        if button in (None, 'Exit'):
            break
        if button == 'Open PGN File':
            filename = sg.PopupGetFile('', no_window=True)
            if filename is not None:
                moves = open_pgn_file(filename)
                i = 0
                board = copy.deepcopy(initial_board)
                window.FindElement('_movelist_').Update(value='')
        if button == 'About...':
            sg.Popup('Powerd by Engine Kibitz Chess Engine')
        if type(button) is tuple and moves is not None and i < len(moves):
            move = moves[i]                 # get the current move
            window.FindElement('_movelist_').Update(value='{}   {}\n'.format(i+1, str(move)), append=True)
            move_from = move.from_square    # parse the move-from and move-to squares
            move_to = move.to_square
            row, col = move_from // 8, move_from % 8
            piece = board[row][col]         # get the move-from piece
            button = window.FindElement(key=(row,col))
            for x in range(3):
                button.Update(button_color = ('white' , 'red' if x % 2 else 'white'))
                window.Refresh()
                time.sleep(.05)
            board[row][col] = BLANK         # place blank where piece was
            row, col = move_to // 8, move_to % 8  # compute move-to square
            board[row][col] = piece         # place piece in the move-to square
            redraw_board(window, board)
            i += 1

PlayGame()
