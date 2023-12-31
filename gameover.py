# เปิดใช้งาน pygame
import pygame
from pygame.sprite import *
pygame.init()

# import file
import database as b
import button as bt
import text as t
import sound as s

# สร้างหน้าจบเกม
def gameover():
    s.gameover_sound()
    gameover_running = True
    if b.score_game > b.height_score_game:
        b.height_score_game = b.score_game
    while gameover_running == True:
        if b.exit_game == True:
            gameover_running = False
        b.clock.tick(b.FPS)
        b.draw_bg_game_play()
        b.draw_game_over()
        t.score_game()
        key = pygame.key.get_pressed()
        for event in pygame.event.get(): # ตรวจสอบ event ระหว่างรันเกม
            if event.type == pygame.QUIT: # ถ้าเกิด event ปิดหน้าจอเกม
                b.exit_game = True # หยุดการวนลูป while
            if key[pygame.K_SPACE] or b.title == True:
                gameover_running = False
        if b.exit_game == True:
            gameover_running = False
        bt.button_game_over_group.update()
        bt.button_game_over_group.draw(b.screen)
        pygame.display.update()
    return True
