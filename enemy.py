# เปิดใช้งาน pygame
import pygame
from pygame.sprite import *
pygame.init()

import os
import sys
import database as b
import random
import bullet as bu
sys.path.append('level_game')
import z_level_01 as level_01

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
            pygame.draw.rect(b.screen, b.GREEN, (self.rect.x, (self.rect.bottom - 3), self.rect.width*(self.health_remaining/self.health_start), 10))
        if self.health_remaining <= 0:
            level_01.enemy_game -= 1
            self.kill()

                # hit damage
        if pygame.sprite.spritecollide(self, bu.bullet_01_group, True):
            self.health_remaining -= b.damage_01
        if pygame.sprite.spritecollide(self, bu.bullet_02_group, True):
            self.health_remaining -= b.damage_02
        if pygame.sprite.spritecollide(self, bu.bullet_03_group, True):
            self.health_remaining -= b.damage_03
        if pygame.sprite.spritecollide(self, bu.bullet_04_group, False):
            self.health_remaining -= b.damage_04

# Enemy_FireFly class
class Enemys_FireFly(pygame.sprite.Sprite):
    def __init__(self, x, y, health, second):
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
        self.last_shot = pygame.time.get_ticks()
        self.second = second

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

        # set a cooldown
        cooldown = self.second*1000 # milliseconds
        time_now = pygame.time.get_ticks()
        check_cooldown = time_now - self.last_shot > cooldown

        if check_cooldown:
            # ทำกระสุนกำหนดดังนี้ (ตำแหน่งเริ่มต้นของ x, ตำแหน่งเริ่มต้นของ y, ความเร็วของกระสุน)
            bullet = bu.Bullets_FireFly(self.rect.centerx, self.rect.bottom, 3)
            bu.bullet_enemy_group.add(bullet)
            self.last_shot = time_now

        # draw health bar
        if self.health_remaining > 0:
            pygame.draw.rect(b.screen, b.RED, (self.rect.x, (self.rect.bottom - 3), self.rect.width, 10))
            pygame.draw.rect(b.screen, b.GREEN, (self.rect.x, (self.rect.bottom - 3), self.rect.width*(self.health_remaining/self.health_start), 10))
        if self.health_remaining <= 0:
            level_01.enemy_game -= 1
            self.kill()

        # hit damage
        if pygame.sprite.spritecollide(self, bu.bullet_01_group, True):
            self.health_remaining -= b.damage_01
        if pygame.sprite.spritecollide(self, bu.bullet_02_group, True):
            self.health_remaining -= b.damage_02
        if pygame.sprite.spritecollide(self, bu.bullet_03_group, True):
            self.health_remaining -= b.damage_03
        if pygame.sprite.spritecollide(self, bu.bullet_04_group, False):
            self.health_remaining -= b.damage_04

enemy_group = pygame.sprite.Group()

def create_enemys_01(rows, cols, health):
    # generate enemys
    for row in range(rows):
        for item in range(cols):
            enemy = Enemys_Flameow(80 + item * 100, 50 + row * 80, health)
            # elif num == 2:
            #     enemy = Enemys_FireFly(80 + item * 100, 50 + row * 80, health, random.randint(3, 6))
            enemy_group.add(enemy)

def create_enemy_02(rows, cols, health):
    # generate enemys
    for row in range(rows):
        for item in range(cols):
            num = random.randint(1, 3)
            if num == 1:
                enemy = Enemys_Flameow(80 + item * 100, 50 + row * 80, health)
            elif num == 2:
                enemy = Enemys_FireFly(80 + item * 100, 50 + row * 80, health, random.randint(3, 6))
            enemy_group.add(enemy)
