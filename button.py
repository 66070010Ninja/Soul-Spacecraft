# เปิดใช้งาน pygame
from typing import Any
import pygame
from pygame.sprite import *
pygame.init()

# import file
import database as b
import game as g
# import title as t

# สร้าง Button_Start class
class Button_Start(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Image/Game/Start.png')
        self.image = pygame.transform.scale(self.image, (208, 94))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.y = y
    def update(self):
        # ตำแหน่งเมาส์
        pos = pygame.mouse.get_pos()
        # เช็คตำแหน่งและการคลิ๊ก
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                b.new_game = False
                g.start_game()

# สร้าง Button_Exit class
class Button_Exit(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Image/Game/Exit.png')
        self.image = pygame.transform.scale(self.image, (208, 94))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.y = y
    def update(self):
        # ตำแหน่งเมาส์
        pos = pygame.mouse.get_pos()
        # เช็คตำแหน่งและการคลิ๊ก
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                b.exit_game = True

# สร้าง Button_Continue class
class Button_Continue(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Image/Game/Continue.png')
        self.image = pygame.transform.scale(self.image, (314, 104))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.y = y
    def update(self):
        # ตำแหน่งเมาส์
        pos = pygame.mouse.get_pos()
        # เช็คตำแหน่งและการคลิ๊ก
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                b.pause = False

#  Buttn_Title class
class Button_Title(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Image/Game/TITLE.png')
        self.image = pygame.transform.scale(self.image, (208, 94))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.y = y
    def update(self):
        # ตำแหน่งเมาส์
        pos = pygame.mouse.get_pos()
        # เช็คตำแหน่งและการคลิ๊ก
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                b.title = True

button_start_group = pygame.sprite.Group()
button_pause_group = pygame.sprite.Group()
button_game_over_group = pygame.sprite.Group()

# สร้างปุ่ม
button_start = Button_Start(b.SCREEN_W/2, 350)
button_exit = Button_Exit(b.SCREEN_W/2, 500)
button_continue = Button_Continue(b.SCREEN_W/2, 350)
button_title = Button_Title(b.SCREEN_W/2, 500)

button_pause_group.add(button_title)
button_pause_group.add(button_continue)

button_start_group.add(button_start)
button_start_group.add(button_exit)

button_game_over_group.add(button_title)