# เรียกใช้ module
import pygame, sys, os
from pygame.locals import *

# เริ่มใช้ pygame
pygame.init()

# ชื่อเกม
pygame.display.set_caption("Space of Arcana")

# ขนาดหน้าจอ
monitor_size = [pygame.display.Info().current_w, pygame.display.Info().current_h]

# หน้าจอ
screen = pygame.display.set_mode(monitor_size, pygame.FULLSCREEN)

# การแสดงภาพต่อวินาที
clock = pygame.time.Clock()

# หน้าจอ Fullscreen
fullscreen = True

# แสดงรูปพื้นหลังในหน้าจอ
bg = pygame.image.load(os.path.join("assets", "background-black.png"))
bg = pygame.transform.scale(bg, (monitor_size))

# แสดงรูปปุ่ม
start_image = pygame.image.load(os.path.join("assets", "start_button.jpg")).convert_alpha()
exit_image = pygame.image.load(os.path.join("assets", "exit_button.jpg")).convert_alpha()

# เก็บพื้นหลัง
def draw_bg():
    screen.blit(bg, (0, 0))

# คลาสปุ่ม
class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw_button(self):
        # ตัวกระทำ
        action = False

        # ตำแหน่งเมาส์
        pos = pygame.mouse.get_pos()

        # เช็คตำแหน่งและการคลิ๊ก
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # วาดปุ่ม
        screen.blit(self.image, (self.rect.x, self.rect.y))

        # คืนค่าตัวกระทำ
        return action

# สร้างปุ่ม
start_button = Button(685, 500 ,start_image, 0.23)
exit_button = Button(685, 600 ,exit_image, 0.25)

# แสดงหน้าจอ
while True:

    for event in pygame.event.get():

        draw_bg()

        if start_button.draw_button(): # กดปุ่มเพื่อเริ่มเกม
            print("Start")

        if exit_button.draw_button(): # กดปุ่มเพื่อออกเกม
            pygame.quit()
            sys.exit()

        if event.type == QUIT: # กดปุ่มกากบาท มุมขวาบน
            pygame.quit()
            sys.exit()

        if event.type == VIDEORESIZE: # ยืด-หด ตัวหน้าตจอ
            if not fullscreen:
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

        if event.type == KEYDOWN: # กดปุ่ม
            if event.key == K_ESCAPE: # กดปุ่ม ESC
                pygame.quit()
                sys.exit()
            if event.key == K_F12: # กดปุ่ม F12
                fullscreen = not fullscreen
                if fullscreen:
                    screen = pygame.display.set_mode(monitor_size, pygame.FULLSCREEN)
                else:
                    screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)

    pygame.display.update() # อัปเดตหน้าจอ
    clock.tick(60) # fps หน้าจอ
