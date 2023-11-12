# เปิดใช้งาน pygame
import pygame
from pygame.sprite import *
pygame.init()

# import file
import database as b
import player as p
import bullet as bu
import enemy as e
import create_level as cl
import pause_game as pg
import random
import choose_a_card as ca
import text as t
import gameover as go
import sound as s

def next_level():
    if b.start == False:
        rows, cols, health = cl.level_game()
        b.enemy_game = rows*cols
        design = random.randint(1, 3)
        if b.level_game % 5 == 0:
            if b.turn_barrier > 0:
                b.turn_barrier = 0
            b.enemy_game = 1
            design = 4
        if design == 1:
            cl.create_enemys_01(rows, cols, health)
        elif design == 2:
            cl.create_enemy_02(rows, cols, health)
        elif design == 3:
            cl.create_ennemys_03(rows, cols, health)
        elif design == 4:
            cl.create_ennemys_boss(rows, cols, health)
        b.start = True
    bu.bullet_01_group.update()
    bu.bullet_02_group.update()
    bu.bullet_03_group.update()
    bu.bullet_04_group.update()
    bu.bullet_boss_group.update()
    bu.bullet_enemy_group.update()
    bu.bullet_enemy_01_group.update()
    e.enemy_group.update()
    b.clear_game = False

def start_game():
    next_level()
    play_running = True
    while play_running == True:
        s.main_sound()
        b.clock.tick(b.FPS)
        if b.title == True:
            return
        if b.exit_game == True:
            return
        # draw background
        b.draw_bg_game_play()
        t.draw_text()
        key = pygame.key.get_pressed()
        for event in pygame.event.get(): # ตวรจสอบ event ระหว่างรันเกม
            if event.type == pygame.QUIT or b.exit_game == True: # ถ้าเกิด event ปิดหน้าจอเกม
                b.exit_game = True
                play_running = False # หยุดการวนลูป while
            if key[pygame.K_ESCAPE]:
                b.pause = True
                pg.pause_game()
        if b.enemy_game == 0:
            b.clear_game = True
            cl.turn_up()
            b.start = False
            b.level_game += 1
            b.score_game += 100
            b.use_card = ca.choose_card()
            next_level()

        # update spaceship
        p.spaceship.update()

        # update sprite groups
        bu.bullet_01_group.update()
        bu.bullet_02_group.update()
        bu.bullet_03_group.update()
        bu.bullet_04_group.update()
        bu.bullet_boss_group.update()
        bu.bullet_enemy_group.update()
        bu.bullet_enemy_01_group.update()
        e.enemy_group.update()

        # draw sprite groups
        p.spaceship_group.draw(b.screen)
        bu.bullet_01_group.draw(b.screen)
        bu.bullet_02_group.draw(b.screen)
        bu.bullet_03_group.draw(b.screen)
        bu.bullet_04_group.draw(b.screen)
        bu.bullet_boss_group.draw(b.screen)
        bu.bullet_enemy_group.draw(b.screen)
        bu.bullet_enemy_01_group.draw(b.screen)
        e.enemy_group.draw(b.screen)

        # update display
        pygame.display.update()
    return True
