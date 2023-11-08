# เปิดใช้งาน pygame
import pygame
from pygame.sprite import *
pygame.init()

# import file
import basic as b

# กำหนดข้อความที่ Titlebar
pygame.display.set_caption('Space Of Arcana')

running = True
while running == True:
    b.draw_bg_game_play()
    for event in pygame.event.get(): # ตรวจสอบ event ระหว่างรันเกม
        if event.type == pygame.QUIT: # ถ้าเกิด event ปิดหน้าจอเกม
            running = False # หยุดการวนลูป while
    pygame.display.update()
pygame.quit() # ออกจากโปรกแกรม
