# เปิดใช้งาน pygame
import pygame, os
from pygame.locals import *
pygame.init()

# import file
import database as b
import button as bt
import play_start as ps

# ชื่อเกม
pygame.display.set_caption("Space of Arcana")

# หน้าจอ
screen = pygame.display.set_mode((b.SCREEN_W, b.SCREEN_H), pygame.RESIZABLE)

# ดึงภาพจาก Image รูปปุ่ม
start_image = pygame.image.load(os.path.join("Image/Game/start_button.jpg")).convert_alpha()
exit_image = pygame.image.load(os.path.join("Image/Game/exit_button.jpg")).convert_alpha()

# สร้างปุ่ม
start_button = bt.Button(325, 500 ,start_image, 0.23)
exit_button = bt.Button(325, 600 ,exit_image, 0.25)

# แสดงหน้าจอ
def start():
    button_running = True
    while button_running == True:

        for event in pygame.event.get():

            if start_button.draw_button(): # กดปุ่มเพื่อเริ่มเกม
                ps.start_game()

            if exit_button.draw_button(): # กดปุ่มเพื่อออกเกม
                pygame.quit()

            if event.type == QUIT: # กดปุ่มกากบาท มุมขวาบน
                pygame.quit()

            if event.type == KEYDOWN: # กดปุ่ม
                if event.key == K_ESCAPE: # กดปุ่ม ESC
                    pygame.quit()

        pygame.display.update() # อัปเดตหน้าจอ
        b.clock.tick(b.FPS) # fps หน้าจอ
    return True
