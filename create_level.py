# เปิดใช้งาน pygame
import pygame
from pygame.sprite import *
pygame.init()

# import file
import enemy as e
import database as b
import random

def level_game():
    if b.level_game <= 10:
        return 3, 7
    elif b.level_game <= 20:
        return 4, 7
    elif b.level_game <= 30:
        return 5, 7
    else:
        return 6, 7

def create_enemys_01(rows, cols, health):
    # generate enemys
    for row in range(rows):
        for item in range(cols):
            enemy = e.Enemys_Flameow(80 + item * 100, 50 + row * 80, health)
            e.enemy_group.add(enemy)

def create_enemy_02(rows, cols, health):
    # generate enemys
    for row in range(rows):
        for item in range(cols):
            num = random.randint(1, 2)
            if num == 1:
                enemy = e.Enemys_Flameow(80 + item * 100, 50 + row * 80, health)
            elif num == 2:
                enemy = e.Enemys_FireFly(80 + item * 100, 50 + row * 80, health, random.randint(3, 9)*(1 + (b.turn_cool_down_enemy > 0)))
            e.enemy_group.add(enemy)