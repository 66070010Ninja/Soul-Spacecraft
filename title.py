# เปิดใช้งาน pygame
import pygame
from pygame.sprite import *
pygame.init()

# import file
import os
import sys
import database as b
sys.path.append('level_game')
import level_01
import level_02
import level_03
import level_04
import level_05

# กำหนดข้อความที่ Titlebar
pygame.display.set_caption('Space Of Arcana')

def title():
    b.draw_bg_game_play()
    key = pygame.key.get_pressed()
    for event in pygame.event.get(): # ตรวจสอบ event ระหว่างรันเกม
        if event.type == pygame.QUIT: # ถ้าเกิด event ปิดหน้าจอเกม
            b.exit_game = True # หยุดการวนลูป while
        if key[pygame.K_KP_ENTER]:
            level_05.game_level_05()
    if b.exit_game == True:
        return False
    pygame.display.update()
    return True

running = True
while running == True:
    running = title()
pygame.quit() # ออกจากโปรกแกรม
