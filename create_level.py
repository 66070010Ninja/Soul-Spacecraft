# เปิดใช้งาน pygame
import pygame
from pygame.sprite import *
pygame.init()

# import file
import enemy as e
import database as b
import random

# เลเวลเกม แถว จำนวนศัตรูและเลือดศัตรูในแต่ละเลเวล
def level_game():
    if b.level_game % 5 == 0:
        if b.turn_barrier > 0:
            b.turn_barrier == 0
        return (b.SCREEN_W//2), 130, ((b.level_game/5)*500) + 500
    elif b.level_game <= 10:
        return 2, 7, 100
    elif b.level_game <= 20:
        return 3, 7, 150
    elif b.level_game <= 30:
        return 4, 7, 200
    else:
        return 5, 7, ((b.level_game//10)*50)+100

# สร้างศัตรูรูปแบบที่ 1
def create_enemys_01(rows, cols, health):
    # generate enemys
    for row in range(rows):
        for item in range(cols):
            enemy = e.Enemys_Flameow(80 + item * 100, 50 + (row+1) * 80, health)
            e.enemy_group.add(enemy)

# สร้างศัตรูรูปแบบที่ 2
def create_enemy_02(rows, cols, health):
    # generate enemys
    for row in range(rows):
        for item in range(cols):
            num = random.randint(1, 2)
            if num == 1:
                enemy = e.Enemys_Flameow(80 + item * 100, 50 + (row+1) * 80, health)
            elif num == 2:
                enemy = e.Enemys_FireFly(80 + item * 100, 50 + (row+1) * 80, health, random.randint(3, 9))
            e.enemy_group.add(enemy)

# สร้างศัตรูรูปแบบที่ 3
def create_ennemys_03(rows, cols, health):
    # generate enemys
    for row in range(rows):
        for item in range(cols):
            num = random.randint(1, 3)
            if num == 1:
                enemy = e.Enemys_Flameow(80 + item * 100, 50 + (row+1) * 80, health)
            elif num == 2:
                enemy = e.Enemys_FireFly(80 + item * 100, 50 + (row+1) * 80, health, random.randint(3, 9))
            elif num == 3:
                enemy = e.Enemys_Flame_Boy(80 + item * 100, 50 + (row+1) * 80, health, random.randint(3, 9))
            e.enemy_group.add(enemy)

# สร้างบอส
def create_ennemys_boss(rows, cols, health):
    enemy = e.Main_Boss(rows, cols, health)
    e.enemy_group.add(enemy)

# ข้ามเลเวล และลบจำนวนรอบความสามารถการ์ด
def turn_up():
    if b.turn_size_player != 0:
        b.turn_size_player -= 1
    if b.turn_barrier != 0:
        b.turn_barrier -= 1
    if b.turn_cool_down_atk != 0:
        b.turn_cool_down_atk -= 1
    if b.turn_size_player == 0:
        b.size_player = 'normal'
    b.restore_blood += 15
