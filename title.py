# เปิดใช้งาน pygame
import pygame
from pygame.sprite import *
pygame.init()

# import file
import database as b
import button as bt
import enemy as e
import bullet as bu

# กำหนดข้อความที่ Titlebar
pygame.display.set_caption('Space Of Arcana')

def title():
    b.draw_bg_game_play()
    b.draw_logo_game()
    b.clock.tick(b.FPS)
    for event in pygame.event.get(): # ตรวจสอบ event ระหว่างรันเกม
        if event.type == pygame.QUIT: # ถ้าเกิด event ปิดหน้าจอเกม
            b.exit_game = True # หยุดการวนลูป while
    b.title = False
    b.new_game = True
    b.start = False
    if b.exit_game == True:
        return False
    bu.bullet_01_group.update()
    bu.bullet_02_group.update()
    bu.bullet_03_group.update()
    bu.bullet_04_group.update()
    bu.bullet_enemy_group.update()
    bu.bullet_enemy_01_group.update()
    e.enemy_group.update()
    bt.button_start_group.update()
    bt.button_start_group.draw(b.screen)
    pygame.display.update()
    return True

running = True
while running == True:
    running = title()
pygame.quit() # ออกจากโปรกแกรม
