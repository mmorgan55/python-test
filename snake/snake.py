import math
import random
import sys
import tkinter as tk
from tkinter import messagebox
import pygame

pygame.init()

size = 500
rows = 20


class Cube(object):
    rows = 0
    cubeSize = 0

    def __init__(self, start, dirX=1, dirY=0, color=(255, 0, 0)):
        pass

    def move(self, dirX, dirY):
        pass

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
        pass

    def reset(self, pos):
        pass

    def addCube(self):
        pass

    def draw(self, surface):
        pass


def drawGrid(gridSize, numRows, surface):
    blockSize = gridSize // numRows

    x = 0
    y = 0

    for line in range(rows):
        x = x + blockSize
        y = y + blockSize

        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, gridSize))
        pygame.draw.line(surface, (255, 255, 255), (0, y), (gridSize, y))


def redrawWindow(surface):
    drawGrid(size, rows, surface)
    pygame.display.update()


def randomSnack(rows, items):
    pass


def messageBox(subject, contect):
    pass


def main():
    window = pygame.display.set_mode((size, size))
    snake = Snake((255, 0, 0), (10, 10))
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
