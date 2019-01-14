import numpy as np
import pygame
import sys

COLUMN_COUNT = 7
ROW_COUNT = 6
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)


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

    for col in range(COLUMN_COUNT - 3):
        for row in range(ROW_COUNT - 3):
            if (board[row][col]) == piece and board[row + 1][col + 1] and board[row + 2][col + 2] \
                    and board[row + 3][col + 3]:
                return True

    for col in range(COLUMN_COUNT - 3):
        for row in range(3, ROW_COUNT):
            if (board[row][col]) == piece and board[row - 1][col + 1] and board[row - 2][col + 2] \
                    and board[row - 3][col + 3]:
                return True


def draw_board(board):
    for col in range(COLUMN_COUNT):
        for row in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE,
                             (col * SQUARE_SIZE, row * SQUARE_SIZE + SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            pygame.draw.circle(screen, BLACK,
                               (col * SQUARE_SIZE + SQUARE_SIZE // 2,
                                row * SQUARE_SIZE + SQUARE_SIZE + SQUARE_SIZE // 2), RADIUS)


game_board = create_board()
print(game_board)
game_over = False
turn = 0

pygame.init()

SQUARE_SIZE = 100
width = COLUMN_COUNT * SQUARE_SIZE
height = (ROW_COUNT + 1) * SQUARE_SIZE
RADIUS = SQUARE_SIZE // 2 - 5

size = (width, height)

screen = pygame.display.set_mode(size)
draw_board(game_board)
pygame.display.update()

while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            print()

    # if turn == 0:
    #     column = int(input("Player 1 Make your Selection (0-6):"))
    #     if is_valid_move(game_board, column):
    #         row = get_next_open_row(game_board, column)
    #         drop_piece(game_board, row, column, 1)
    #
    #         if find_win(game_board, 1):
    #             print("Worked")
    #             game_over = True
    #
    # else:
    #     column = int(input("Player 2 Make your Selection (0-6):"))
    #     if is_valid_move(game_board, column):
    #         row = get_next_open_row(game_board, column)
    #         drop_piece(game_board, row, column, 2)
    #
    #         if find_win(game_board, 1):
    #             print("Worked")
    #             game_over = True
    #
    # print(np.flip(game_board, 0))
    #
    # turn += 1
    # turn = turn % 2
