import numpy as np

COLUMN_COUNT = 6
ROW_COUNT = 5


def create_board():
    board = np.zeros((6, 7))
    return board


def drop_piece(board, row, col, piece):
    board[row][col] = piece


def is_valid_move(board, col):
    return board[ROW_COUNT][col] == 0


def get_next_open_row(board, col):
    for row in range(ROW_COUNT):
        if board[row][col] == 0:
            return row


game_board = create_board()
print(game_board)
game_over = False
turn = 0

while not game_over:
    if turn == 0:
        column = int(input("Player 1 Make your Selection (0-6):"))
        if is_valid_move(game_board, column):
            row = get_next_open_row(game_board, column)
            drop_piece(game_board, row, column, 1)

    else:
        column = int(input("Player 2 Make your Selection (0-6):"))
        if is_valid_move(game_board, column):
            row = get_next_open_row(game_board, column)
            drop_piece(game_board, row, column, 2)

    print(np.flip(game_board, 0))

    turn += 1
    turn = turn % 2
