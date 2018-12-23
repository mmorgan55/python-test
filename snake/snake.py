import math
import random
import sys
import tkinter as tk
from tkinter import messagebox
import pygame

pygame.init()

RED = (255, 0, 0)
WHITE = (255, 255, 255)
STARTING_POSITION = (10, 10)
size = 500
rows = 20


class Cube(object):
    rows = 0
    cubeSize = 0

    def __init__(self, start, dirX=1, dirY=0, color=RED):
        self.pos = start
        self.dirX = 1
        self.dirY = 0
        self.color = color

    def move(self, dirX, dirY):
        self.dirX = dirX
        self.dirY = dirY
        self.pos(self.pos[0] + self.dirX, self.pos[1] + self.dirY)

    def draw(self, surface, eyes=False):
        pass


class Snake(object):
    body = []
    turns = []

    def __init__(self, color, pos):
        self.color = color
        self.head = Cube(pos)
        self.body.append(self.head)
        self.dirX = 0
        self.dirY = 1

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            keys = pygame.key.get_pressed()

            for key in keys:
                if key[pygame.K_LEFT]:
                    self.dirX = -1
                    self.dirY = 0
                    self.turns[self.head.pos[:]] = [self.dirX, self.dirY]
                elif key[pygame.K_RIGHT]:
                    self.dirX = 1
                    self.dirY = 0
                    self.turns[self.head.pos[:]] = [self.dirX, self.dirY]

                elif key[pygame.K_UP]:
                    self.dirX = 0
                    self.dirY = -1
                    self.turns[self.head.pos[:]] = [self.dirX, self.dirY]
                elif key[pygame.K_DOWN]:
                    self.dirX = 0
                    self.dirY = 1
                    self.turns[self.head.pos[:]] = [self.dirX, self.dirY]

            for index, cube in enumerate(self.body):
                position = cube.pos[:]
                if position in self.turns:
                    turn = self.turns[position]
                    cube.move(turn[0], turn[1])
                    if index == len(self.body) - 1:
                        self.turns.pop(position)
                else:
                    if cube.dirX == -1 and cube.pos[0] <= 0:
                        cube.pos = (cube.rows - 1, cube.pos[1])
                    elif cube.dirX == 1 and cube.pos[0] >= cube.rows - 1:
                        cube.pos = (0, cube.pos[1])
                    elif cube.dirY == 1 and cube.pos[1] >= cube.rows - 1:
                        cube.pos = (cube.pos[0], 0)
                    elif cube.dirY == -1 and cube.pos[1] <= 0:
                        cube.pos = (cube.pos[0], cube.rows - 1)
                    else:
                        cube.move(cube.dirX, cube.dirY)

    def reset(self, pos):
        pass

    def addCube(self):
        pass

    def draw(self, surface):
        for index, cube in enumerate(self.body):
            if index == 0:
                cube.draw(surface, True)
            else:
                cube.draw(surface)


snake = Snake(RED, STARTING_POSITION)


def drawGrid(gridSize, numRows, surface):
    blockSize = gridSize // numRows

    x = 0
    y = 0

    for line in range(rows):
        x = x + blockSize
        y = y + blockSize

        pygame.draw.line(surface, WHITE, (x, 0), (x, gridSize))
        pygame.draw.line(surface, WHITE, (0, y), (gridSize, y))


def redrawWindow(surface):
    snake.draw(surface)
    drawGrid(size, rows, surface)
    pygame.display.update()


def randomSnack(rows, items):
    pass


def messageBox(subject, contect):
    pass


def main():
    window = pygame.display.set_mode((size, size))
    flag = True

    clock = pygame.time.Clock()
    while flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.time.delay(50)
        clock.tick(10)
        redrawWindow(window)


main()
