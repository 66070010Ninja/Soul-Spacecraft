# เปิดใช้งาน pygame
from typing import Any
import pygame
from pygame.sprite import *
pygame.init()

# import
import basic as b
import enemy as e
import player as p

# สร้าง Bullets class
class Bullets(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        self.speed = speed
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Image/Laser.png')
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def update(self):
        self.rect.y -= self.speed
        if self.rect.bottom <= 0:
            self.kill()
        if pygame.sprite.spritecollide(self, e.enemy_group, True):
            self.kill()

# สร้าง Bullets_Ball class
class Bullets_Ball(pygame.sprite.Sprite):
    def __init__(self, x ,y, distance, speed):
        self.distance = distance
        self.speed = speed
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Image/Laser_Ball.png')
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def update(self):
        self.rect.y -= self.speed
        self.rect.x += self.distance
        if self.rect.bottom <= 0 or self.rect.left <= 0 or self.rect.right >= b.SCREEN_W:
            self.kill()
        if pygame.sprite.spritecollide(self, e.enemy_group, True):
            self.kill()

# สร้าง Bullets_Short class
class Bullets_Short(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        self.speed = speed
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Image/Laser_Short.png')
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def update(self):
        self.rect.y -= self.speed
        if self.rect.bottom <= 0:
            self.kill()
        if pygame.sprite.spritecollide(self, e.enemy_group, True):
            self.kill()

# สร้าง Bullets_Cannon class
class Bullets_Cannon(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        self.speed = speed
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Image/Laser_Big.png')
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def update(self):
        self.rect.y -= self.speed
        if self.rect.bottom <= 0:
            self.kill()
        if pygame.sprite.spritecollide(self, e.enemy_group, True):
            pass

# สร้าง Bullets_FireFly
class Bullets_FireFly(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        self.speed = speed
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('/Image/Laser_FireFly.png')
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
    
    def update(self):
        self.rect.y += self.speed
        if self.rect.bottom <= b.SCREEN_H:
            self.kill()
        if pygame.sprite.spritecollide(self, p.spaceship_group, True):
            pass

bullet_group = pygame.sprite.Group()