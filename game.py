import sys
import random

import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
SPEED = 10
BACKGROUND_COLOR = (0, 0, 0)
score = 0

player_size = 50
player_pos = [WIDTH / 2, HEIGHT - 2 * player_size]

enemy_size = 50
enemy_pos = [random.randint(0, WIDTH - enemy_size), 0]
enemy_list = [enemy_pos]

RECTANGLE = (player_pos[0], player_pos[1], 50, 50)

screen = pygame.display.set_mode((WIDTH, HEIGHT))

game_over = False

clock = pygame.time.Clock()

myFont = pygame.font.SysFont("monospace", 35)


def set_level(game_score):
    if game_score < 20:
        speed = 5
    elif game_score < 40:
        speed = 7
    elif game_score < 60:
        speed = 9
    else:
        speed = 13

    return speed


def drop_enemies(e_list):
    delay = random.random()
    if len(enemy_list) < 10 and delay < 0.1:
        x_pos = random.randint(0, WIDTH - enemy_size)
        y_pos = 0
        e_list.append([x_pos, y_pos])


def draw_enemies(e_list):
    for e_pos in e_list:
        pygame.draw.rect(screen, BLUE, (e_pos[0], e_pos[1], enemy_size, enemy_size))


def update_enemy_positions(e_list, game_score):
    for idx, e_pos in enumerate(enemy_list):
        if 0 <= e_pos[1] < HEIGHT:
            e_pos[1] += SPEED
        else:
            game_score += 1
            e_list.pop(idx)
    return game_score


def collision_check(e_list, p_pos):
    for e_pos in e_list:
        if detect_collision(e_pos, p_pos):
            return True
    return False


def detect_collision(p_pos, e_pos):
    p_x = p_pos[0]
    p_y = p_pos[1]

    e_x = e_pos[0]
    e_y = e_pos[1]

    if (p_x <= e_x < (p_x + player_size)) or (e_x <= p_x < (e_x + enemy_size)):
        if (p_y <= e_y < (p_y + player_size)) or (e_y <= p_y < (e_y + enemy_size)):
            return True
    return False


while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            x = player_pos[0]
            y = player_pos[1]
            if event.key == pygame.K_LEFT:
                x -= 25
            elif event.key == pygame.K_RIGHT:
                x += 25
            elif event.key == pygame.K_DOWN:
                y += 25
            elif event.key == pygame.K_UP:
                y -= 25
            player_pos = [x, y]

    screen.fill(BACKGROUND_COLOR)

    drop_enemies(enemy_list)
    score = update_enemy_positions(enemy_list, score)
    SPEED = set_level(score)
    text = "Score: " + str(score)
    label = myFont.render(text, 1, YELLOW)
    screen.blit(label, (WIDTH - 220, HEIGHT - 40))

    if collision_check(enemy_list, player_pos):
        game_over = True
        break
    draw_enemies(enemy_list)

    pygame.draw.rect(screen, RED, (player_pos[0], player_pos[1], player_size, player_size))

    clock.tick(30)

    pygame.display.update()
