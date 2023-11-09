# เปิดใช้งาน pygame
import pygame
from pygame.sprite import *
pygame.init()

# import
import enemy as e
import random

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
            print(num)
            if num == 1:
                enemy = e.Enemys_Flameow(80 + item * 100, 50 + row * 80, health)
            elif num == 2:
                enemy = e.Enemys_FireFly(80 + item * 100, 50 + row * 80, health, random.randint(3, 9))
            e.enemy_group.add(enemy)