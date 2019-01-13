import numpy as np

COLUMN_COUNT = 7
ROW_COUNT = 6


def create_board():
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    return board


def drop_piece(board, row, col, piece):
    board[row][col] = piece


def is_valid_move(board, col):
    return board[ROW_COUNT - 1][col] == 0


def get_next_open_row(board, col):
    for row in range(ROW_COUNT):
        if board[row][col] == 0:
            return row


def find_win(board, piece):
    for col in range(COLUMN_COUNT - 3):
        for row in range(ROW_COUNT):
            if (board[row][col]) == piece and board[row][col + 1] and board[row][col + 2] and board[row][col + 3]:
                return True

    for col in range(COLUMN_COUNT):
        for row in range(ROW_COUNT - 3):
            if (board[row][col]) == piece and board[row + 1][col] and board[row + 2][col] and board[row + 3][col]:
                return True


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

            if find_win(game_board, 1):
                print("Worked")
                game_over = True

    else:
        column = int(input("Player 2 Make your Selection (0-6):"))
        if is_valid_move(game_board, column):
            row = get_next_open_row(game_board, column)
            drop_piece(game_board, row, column, 2)

    print(np.flip(game_board, 0))

    turn += 1
    turn = turn % 2
