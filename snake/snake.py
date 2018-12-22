import math
import random
import tkinter as tk
from tkinter import messagebox
import pygame


class Cube(object):
    rows = 0
    w = 0

    def __init__(self, start, dirX=1, dirY=0, color=(255, 0, 0)):
        pass

    def move(self, dirX, dirY):
        pass

    def draw(self, surface, eyes=False):
        pass


class Snake(object):
    def __init__(self, color, pos):
        pass

    def move(self):
        pass

    def reset(self, pos):
        pass

    def addCube(self):
        pass

    def draw(self, surface):
        pass


def drawGrid(w, rows, surface):
    pass


def redrawWindow(surface):
    pass


def randomSnack(rows, items):
    pass


def messageBox(subject, contect):
    pass


def main():
    width = 500
    height = 500
    rows = 20
    window = pygame.display.set_mode((width, height))

