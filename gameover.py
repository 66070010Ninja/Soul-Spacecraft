# เปิดใช้งาน pygame
import pygame
from pygame.sprite import *
pygame.init()

# import file
import database as b
import button as bt

def gameover():
    gameover_running = True
    while gameover_running == True:
        b.clock.tick(b.FPS)
        b.draw_bg_game_play()
        b.draw_game_over()
        key = pygame.key.get_pressed()
        for event in pygame.event.get(): # ตรวจสอบ event ระหว่างรันเกม
            if event.type == pygame.QUIT: # ถ้าเกิด event ปิดหน้าจอเกม
                b.exit_game = True # หยุดการวนลูป while
            if key[pygame.K_SPACE] or b.gameover == False:
                gameover_running = False
        if b.exit_game == True:
            gameover_running = False
        pygame.display.update()
    return True
gameover()
