import PySimpleGUI as sg
import os
import sys
import copy
try:
    import chess
    import chess.pgn
    import chess.uci
except ImportError:
    raise ImportError("Please pip install python-chess")

CHESS_PATH = '.'  # path to the chess pieces

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

initial_board = [[ROOKB, KNIGHTB, BISHOPB, QUEENB, KINGB, BISHOPB, KNIGHTB, ROOKB],
                 [PAWNB, ] * 8,
                 [BLANK, ] * 8,
                 [BLANK, ] * 8,
                 [BLANK, ] * 8,
                 [BLANK, ] * 8,
                 [PAWNW, ] * 8,
                 [ROOKW, KNIGHTW, BISHOPW, QUEENW, KINGW, BISHOPW, KNIGHTW, ROOKW]]

blank = os.path.join(CHESS_PATH, 'blank.png')
bishopB = os.path.join(CHESS_PATH, 'nbishopb.png')
bishopW = os.path.join(CHESS_PATH, 'nbishopw.png')
pawnB = os.path.join(CHESS_PATH, 'npawnb.png')
pawnW = os.path.join(CHESS_PATH, 'npawnw.png')
knightB = os.path.join(CHESS_PATH, 'nknightb.png')
knightW = os.path.join(CHESS_PATH, 'nknightw.png')
rookB = os.path.join(CHESS_PATH, 'nrookb.png')
rookW = os.path.join(CHESS_PATH, 'nrookw.png')
queenB = os.path.join(CHESS_PATH, 'nqueenb.png')
queenW = os.path.join(CHESS_PATH, 'nqueenw.png')
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
        color = '#B58863'
    else:
        color = '#F0D9B5'
    return sg.RButton('', image_filename=image, size=(1, 1), button_color=('white', color), pad=(0, 0), key=key)


def redraw_board(window, board):
    for i in range(8):
        for j in range(8):
            color = '#B58863' if (i + j) % 2 else '#F0D9B5'
            piece_image = images[board[i][j]]
            elem = window.FindElement(key=(i, j))
            elem.Update(button_color=('white', color),
                        image_filename=piece_image, )


def PlayGame():
    menu_def = [['&File', ['&Open PGN File', 'E&xit']],
                ['&Help', '&About...'], ]

    # sg.SetOptions(margins=(0,0))
    sg.ChangeLookAndFeel('GreenTan')
    # create initial board setup
    psg_board = copy.deepcopy(initial_board)
    # the main board display layout
    board_layout = [[sg.T('     ')] + [sg.T('{}'.format(a), pad=((23, 27), 0), font='Any 13') for a in 'abcdefgh']]
    # loop though board and create buttons with images
    for i in range(8):
        row = [sg.T(str(8 - i) + '   ', font='Any 13')]
        for j in range(8):
            piece_image = images[psg_board[i][j]]
            row.append(render_square(piece_image, key=(i, j), location=(i, j)))
        row.append(sg.T(str(8 - i) + '   ', font='Any 13'))
        board_layout.append(row)
    # add the labels across bottom of board
    board_layout.append([sg.T('     ')] + [sg.T('{}'.format(a), pad=((23, 27), 0), font='Any 13') for a in 'abcdefgh'])

    # setup the controls on the right side of screen
    openings = (
        'Any', 'Defense', 'Attack', 'Trap', 'Gambit', 'Counter', 'Sicillian', 'English', 'French', 'Queen\'s openings',
        'King\'s Openings', 'Indian Openings')

    board_controls = [[sg.RButton('New Game', key='New Game'), sg.RButton('Draw')],
                      [sg.RButton('Resign Game'), sg.RButton('Set FEN')],
                      [sg.RButton('Player Odds'), sg.RButton('Training')],
                      [sg.Drop(openings), sg.Text('Opening/Style')],
                      [sg.CBox('Play As White', key='_white_')],
                      [sg.Drop([2, 3, 4, 5, 6, 7, 8, 9, 10], size=(3, 1), key='_level_'), sg.Text('Difficulty Level')],
                      [sg.Text('Move List')],
                      [sg.Multiline([], do_not_clear=True, autoscroll=True, size=(15, 10), key='_movelist_')],
                      ]

    # layouts for the tabs
    controls_layout = [[sg.Text('Performance Parameters', font='_ 20')],
                       [sg.T('Put stuff like AI engine tuning parms on this tab')]]

    statistics_layout = [[sg.Text('Statistics', font=('_ 20'))],
                         [sg.T('Game statistics go here?')]]

    board_tab = [[sg.Column(board_layout)]]

    # the main window layout
    layout = [[sg.Menu(menu_def, tearoff=False)],
              [sg.TabGroup([[sg.Tab('Board', board_tab),
                             sg.Tab('Controls', controls_layout),
                             sg.Tab('Statistics', statistics_layout)]], title_color='red'),
               sg.Column(board_controls)],
              [sg.Text('Click anywhere on board for next move', font='_ 14')]]

    window = sg.Window('Chess',
                       default_button_element_size=(12, 1),
                       auto_size_buttons=False,
                       icon='kingb.ico').Layout(layout)

    filename = sg.PopupGetFile('\n'.join(('To begin, set location of AI EXE file',
                                          'If you have not done so already, download the engine',
                                          'Download the StockFish Chess engine at: https://stockfishchess.org/download/')),
                               file_types=(('Chess AI Engine EXE File', '*.exe'),))
    if filename is None:
        sys.exit()
    engine = chess.uci.popen_engine(filename)
    engine.uci()
    info_handler = chess.uci.InfoHandler()
    engine.info_handlers.append(info_handler)

    board = chess.Board()
    move_count = 1
    move_state = move_from = move_to = 0
    # ---===--- Loop taking in user input --- #
    while not board.is_game_over():

        if board.turn == chess.WHITE:
            engine.position(board)

            # human_player(board)
            move_state = 0
            while True:
                button, value = window.Read()
                if button in (None, 'Exit'):
                    exit()
                if button == 'New Game':
                    sg.Popup('You have to restart the program to start a new game... sorry....')
                    break
                    psg_board = copy.deepcopy(initial_board)
                    redraw_board(window, psg_board)
                    move_state = 0
                    break
                level = value['_level_']
                if type(button) is tuple:
                    if move_state == 0:
                        move_from = button
                        row, col = move_from
                        piece = psg_board[row][col]  # get the move-from piece
                        button_square = window.FindElement(key=(row, col))
                        button_square.Update(button_color=('white', 'red'))
                        move_state = 1
                    elif move_state == 1:
                        move_to = button
                        row, col = move_to
                        if move_to == move_from:  # cancelled move
                            color = '#B58863' if (row + col) % 2 else '#F0D9B5'
                            button_square.Update(button_color=('white', color))
                            move_state = 0
                            continue

                        picked_move = '{}{}{}{}'.format('abcdefgh'[move_from[1]], 8 - move_from[0],
                                                        'abcdefgh'[move_to[1]], 8 - move_to[0])

                        if picked_move in [str(move) for move in board.legal_moves]:
                            board.push(chess.Move.from_uci(picked_move))
                        else:
                            print('Illegal move')
                            move_state = 0
                            color = '#B58863' if (move_from[0] + move_from[1]) % 2 else '#F0D9B5'
                            button_square.Update(button_color=('white', color))
                            continue

                        psg_board[move_from[0]][move_from[1]] = BLANK  # place blank where piece was
                        psg_board[row][col] = piece  # place piece in the move-to square
                        redraw_board(window, psg_board)
                        move_count += 1

                        window.FindElement('_movelist_').Update(picked_move + '\n', append=True)

                        break
        else:
            engine.position(board)
            best_move = engine.go(searchmoves=board.legal_moves, depth=level, movetime=(level * 100)).bestmove
            move_str = str(best_move)
            from_col = ord(move_str[0]) - ord('a')
            from_row = 8 - int(move_str[1])
            to_col = ord(move_str[2]) - ord('a')
            to_row = 8 - int(move_str[3])

            window.FindElement('_movelist_').Update(move_str + '\n', append=True)

            piece = psg_board[from_row][from_col]
            psg_board[from_row][from_col] = BLANK
            psg_board[to_row][to_col] = piece
            redraw_board(window, psg_board)

            board.push(best_move)
            move_count += 1
    sg.Popup('Game over!', 'Thank you for playing')


# Download the StockFish Chess engine at: https://stockfishchess.org/download/
# engine = chess.uci.popen_engine(r'E:\DownloadsE\stockfish-9-win\Windows\stockfish_9_x64.exe')
# engine.uci()
# info_handler = chess.uci.InfoHandler()
# engine.info_handlers.append(info_handler)
# level = 2
PlayGame()
