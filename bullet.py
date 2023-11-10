# เปิดใช้งาน pygame
import pygame
from pygame.sprite import *
pygame.init()

# import file
import database as b

# สร้าง Bullets class
class Bullets(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        self.speed = speed
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Image/Laser/Laser.png')
        self.rect = self.image.get_rect()
        self.last_shot = pygame.time.get_ticks()
        self.rect.center = [x, y]

    def update(self):
        self.rect.y -= self.speed
        if (self.rect.bottom <= 0) or (b.start == False):
            self.kill()

# สร้าง Bullets_Ball class
class Bullets_Ball(pygame.sprite.Sprite):
    def __init__(self, x ,y, distance, speed):
        self.distance = distance
        self.speed = speed
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Image/Laser/Laser_Ball.png')
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def update(self):
        self.rect.y -= self.speed
        self.rect.x += self.distance
        if (self.rect.bottom <= 0 or self.rect.left <= 0) or (self.rect.right >= b.SCREEN_W or b.start == False):
            self.kill()

# สร้าง Bullets_Short class
class Bullets_Short(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        self.speed = speed
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Image/Laser/Laser_Short.png')
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def update(self):
        self.rect.y -= self.speed
        if (self.rect.bottom <= 0) or (b.start == False):
            self.kill()

# สร้าง Bullets_Cannon class
class Bullets_Cannon(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        self.speed = speed
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Image/Laser/Laser_Big.png')
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def update(self):
        self.rect.y -= self.speed
        if (self.rect.bottom <= 0) or (b.start == False):
            self.kill()

# สร้าง Bullets_FireFly
class Bullets_FireFly(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        self.speed = speed
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Image/Laser/Laser_FireFly.png')
        self.image = pygame.transform.scale(self.image, (6, 6))
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def update(self):
        self.rect.y += self.speed
        if (self.rect.top > b.SCREEN_H) or (b.start == False):
            self.kill()

# สร้าง Bullets_Flame_Boy
class Bullets_Flame_Boy(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        self.speed = speed
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Image/Laser/Laser_Flame Boy.png')
        self.image = pygame.transform.scale(self.image, (6, 6))
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def update(self):
        self.rect.y += self.speed
        if self.rect.x > b.player_x and self.rect.y <= b.SCREEN_H-300:
            self.rect.x -= self.speed/2
        elif self.rect.x < b.player_x and self.rect.y <= b.SCREEN_H-300:
            self.rect.x += self.speed/2
        if (self.rect.top > b.SCREEN_H) or (b.start == False):
            self.kill()

bullet_01_group = pygame.sprite.Group()
bullet_02_group = pygame.sprite.Group()
bullet_03_group = pygame.sprite.Group()
bullet_04_group = pygame.sprite.Group()
bullet_enemy_group = pygame.sprite.Group()
bullet_enemy_01_group = pygame.sprite.Group()
