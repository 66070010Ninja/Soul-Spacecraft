# เปิดใช้งาน pygame
import pygame
from pygame.sprite import *
pygame.init()

# import file
import database as b
import button as bt

def pause_game():
    pause_running = True
    while pause_running == True:
        b.clock.tick(b.FPS)
        b.draw_bg_game_play()
        key = pygame.key.get_pressed()
        for event in pygame.event.get(): # ตรวจสอบ event ระหว่างรันเกม
            if event.type == pygame.QUIT: # ถ้าเกิด event ปิดหน้าจอเกม
                b.exit_game = True # หยุดการวนลูป while
            if key[pygame.K_ESCAPE] or b.pause == False or b.title == True:
                pause_running = False
        if b.exit_game == True:
            pause_running = False
        bt.button_pause_group.update()
        bt.button_pause_group.draw(b.screen)
        pygame.display.update()
    return True
