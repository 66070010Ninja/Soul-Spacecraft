# เปิดใช้งาน pygame
import pygame
from pygame.sprite import *
pygame.init()

# import file
import database as b
import button as bt

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
    if b.exit_game == True:
        return False
    bt.button_start_group.update()
    bt.button_start_group.draw(b.screen)
    pygame.display.update()
    return True

running = True
while running == True:
    running = title()
pygame.quit() # ออกจากโปรกแกรม
