# เปิดใช้งาน pygame
import pygame
from pygame.sprite import *
pygame.init()

# import
import basic as b
import player as p
import bullet as bu
import enemy as e
import z_level_02 as level_02

if b.start == False:
    enemy_game = 4*7

def game_level_01():
    if b.start == False:
        e.create_enemys_01(4, 7, 100)
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
                return
        
        if enemy_game == 0:
            b.start = False
            level_02.game_level_02()

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
