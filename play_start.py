# เปิดใช้งาน pygame
import pygame
from pygame.sprite import *
pygame.init()

# import
import database as b
import player as p
import bullet as bu
import enemy as e
import create_level as cl
import pause_game as pg
import random

def start_game():
    if b.start == False:
        rows, cols = cl.level_game()
        health = (random.randint(10, 26))*10
        b.enemy_game = rows*cols
        design = random.randint(1, 2)
        if design == 1:
            cl.create_enemys_01(rows, cols, health)
        if design == 2:
            cl.create_enemy_02(rows, cols, health)
        b.start = True
    play_running = True
    while play_running == True:
        b.clock.tick(b.FPS)

        # draw background
        b.draw_bg_game_play()
        key = pygame.key.get_pressed()
        for event in pygame.event.get(): # ตวรจสอบ event ระหว่างรันเกม
            if event.type == pygame.QUIT: # ถ้าเกิด event ปิดหน้าจอเกม
                b.exit_game = True
                play_running = False # หยุดการวนลูป while
            if key[pygame.K_ESCAPE]:
                pg.pause_game()
            if b.enemy_game == 0:
                b.level_game += 1
                b.start = False
                start_game()

        # update spaceship
        p.spaceship.update()

        # update sprite groups
        bu.bullet_01_group.update()
        bu.bullet_02_group.update()
        bu.bullet_03_group.update()
        bu.bullet_04_group.update()
        bu.bullet_enemy_group.update()
        e.enemy_group.update()

        # draw sprite groups
        p.spaceship_group.draw(b.screen)
        bu.bullet_01_group.draw(b.screen)
        bu.bullet_02_group.draw(b.screen)
        bu.bullet_03_group.draw(b.screen)
        bu.bullet_04_group.draw(b.screen)
        bu.bullet_enemy_group.draw(b.screen)
        e.enemy_group.draw(b.screen)

        # update display
        pygame.display.update()
    return True