import numpy as np
import pygame
import sys
import math

COLUMN_COUNT = 7
ROW_COUNT = 6
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)


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
            if (board[row][col]) == piece and board[row][col + 1] == piece and board[row][col + 2] == piece and \
                    board[row][col + 3] == piece:
                return True

    for col in range(COLUMN_COUNT):
        for row in range(ROW_COUNT - 3):
            if (board[row][col]) == piece and board[row + 1][col] == piece and board[row + 2][col] == piece and \
                    board[row + 3][col] == piece:
                return True

    for col in range(COLUMN_COUNT - 3):
        for row in range(ROW_COUNT - 3):
            if (board[row][col]) == piece and board[row + 1][col + 1] == piece and board[row + 2][col + 2] == piece \
                    and board[row + 3][col + 3] == piece:
                return True

    for col in range(COLUMN_COUNT - 3):
        for row in range(3, ROW_COUNT):
            if (board[row][col]) == piece and board[row - 1][col + 1] == piece and board[row - 2][col + 2] == piece \
                    and board[row - 3][col + 3] == piece:
                return True


def draw_board(board):
    for col in range(COLUMN_COUNT):
        for row in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE,
                             (col * SQUARE_SIZE, row * SQUARE_SIZE + SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            pygame.draw.circle(screen, BLACK,
                               (col * SQUARE_SIZE + SQUARE_SIZE // 2,
                                row * SQUARE_SIZE + SQUARE_SIZE + SQUARE_SIZE // 2), RADIUS)

    for col in range(COLUMN_COUNT):
        for row in range(ROW_COUNT):
            if board[row][col] == 1:
                pygame.draw.circle(screen, RED,
                                   (col * SQUARE_SIZE + SQUARE_SIZE // 2,
                                    height - (row * SQUARE_SIZE + SQUARE_SIZE // 2)), RADIUS)
            elif board[row][col] == 2:
                pygame.draw.circle(screen, YELLOW,
                                   (col * SQUARE_SIZE + SQUARE_SIZE // 2,
                                    height - (row * SQUARE_SIZE + SQUARE_SIZE // 2)), RADIUS)
    pygame.display.update()


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

            if turn == 0:
                posx = event.pos[0]
                column = math.floor(posx // SQUARE_SIZE)

                if is_valid_move(game_board, column):
                    row = get_next_open_row(game_board, column)
                    drop_piece(game_board, row, column, 1)

                    if find_win(game_board, 1):
                        game_over = True

            else:
                posx = event.pos[0]
                column = math.floor(posx // SQUARE_SIZE)
                if is_valid_move(game_board, column):
                    row = get_next_open_row(game_board, column)
                    drop_piece(game_board, row, column, 2)

                    if find_win(game_board, 2):
                        game_over = True

            print(np.flip(game_board, 0))
            draw_board(game_board)

            turn += 1
            turn = turn % 2
