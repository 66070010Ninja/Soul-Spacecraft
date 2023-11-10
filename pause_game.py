# เปิดใช้งาน pygame
import pygame
from pygame.sprite import *
pygame.init()

# import file
import database as b

def pause_game():
    play_running = True
    while play_running == True:
        b.clock.tick(b.FPS)
        b.draw_bg_game_play()
        key = pygame.key.get_pressed()
        for event in pygame.event.get(): # ตรวจสอบ event ระหว่างรันเกม
            if event.type == pygame.QUIT: # ถ้าเกิด event ปิดหน้าจอเกม
                b.exit_game = True # หยุดการวนลูป while
            if key[pygame.K_ESCAPE]:
                return
        pygame.display.update()
    return True
