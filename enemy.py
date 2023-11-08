# เปิดใช้งาน pygame
import pygame
from pygame.sprite import *
pygame.init()

import basic as b
import random

# สร้าง Enemys_Flameow class
class Enemys_Flameow(pygame.sprite.Sprite):
    def __init__(self, x, y, health):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Image/Flameow.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.move_counter = 0
        self.move_direction = 1
        self.last_time = pygame.time.get_ticks()
        self.down = 10 * 1000
        self.health_start = health
        self.health_remaining = health

    def update(self):
        self.rect.x += self.move_direction
        self.move_counter += 1
        self.now_time = pygame.time.get_ticks()
        if abs(self.move_counter) >= self.rect.width//2: # เคลื่อนย้ายซ้าย-ขวา
            self.move_direction *= -1
            self.move_counter *= self.move_direction
        if self.now_time - self.last_time > self.down: # ตกลงมา
            self.rect.y += 50
            self.last_time = pygame.time.get_ticks()

        # draw health bar
        pygame.draw.rect(b.screen, b.RED, (self.rect.x, (self.rect.bottom - 3), self.rect.width, 10))
        if self.health_remaining > 0:
            pygame.draw.rect(b.screen, b.GREEN, (self.rect.x, (self.rect.bottom - 3), self.rect.width*(self.health_remaining//self.health_start), 10))

# Enemy_FireFly class
class Enemys_FireFly(pygame.sprite.Sprite):
    def __init__(self, x, y, health):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Image/FireFly.png')
        self.image = pygame.transform.scale(self.image, (70, 50))
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.move_counter = 0
        self.move_direction = 1
        self.last_time = pygame.time.get_ticks()
        self.down = 10 * 1000
        self.health_start = health
        self.health_remaining = health

    def update(self):
        self.rect.x += self.move_direction
        self.move_counter += 1
        self.now_time = pygame.time.get_ticks()
        if abs(self.move_counter) >= self.rect.width//2: # เคลื่อนย้ายซ้าย-ขวา
            self.move_direction *= -1
            self.move_counter *= self.move_direction
        if self.now_time - self.last_time > self.down: # ตกลงมา
            self.rect.y += 50
            self.last_time = pygame.time.get_ticks()

        # draw health bar
        pygame.draw.rect(b.screen, b.RED, (self.rect.x, (self.rect.bottom - 3), self.rect.width, 10))
        if self.health_remaining > 0:
            pygame.draw.rect(b.screen, b.GREEN, (self.rect.x, (self.rect.bottom - 3), self.rect.width*(self.health_remaining//self.health_start), 10))

enemy_group = pygame.sprite.Group()

def create_enemys(rows, cols, health):
    # generate enemys
    moster = [1, 2]
    for row in range(rows):
        for item in range(cols):
            num = random.choice(moster)
            if num == 1:
                enemy = Enemys_Flameow(80 + item * 100, 50 + row * 80, health)
            elif num == 2:
                enemy = Enemys_FireFly(80 + item * 100, 50 + row * 80, health)
            enemy_group.add(enemy)
