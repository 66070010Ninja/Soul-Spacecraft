# เปิดใช้งาน pygame
import pygame
from pygame.sprite import *
pygame.init()

# import
import basic as b
import player as p
import bullet as bu
import enemy as e

def game_level_01():
    e.create_enemys(4, 7, 100)
    play_running = True
    while play_running == True:
        b.clock.tick(b.FPS)

        # draw background
        b.draw_bg_game_play()

        for event in pygame.event.get(): # ตวรจสอบ event ระหว่างรันเกม
            if event.type == pygame.QUIT: # ถ้าเกิด event ปิดหน้าจอเกม
                play_running = False # หยุดการวนลูป while

        # update spaceship
        p.spaceship.update()

        # update sprite groups
        bu.bullet_group.update()
        e.enemy_group.update()

        # draw sprite groups
        p.spaceship_group.draw(b.screen)
        bu.bullet_group.draw(b.screen)
        e.enemy_group.draw(b.screen)

        pygame.display.update()
    pygame.quit() # ออกจากโปรกแกรม
game_level_01()
