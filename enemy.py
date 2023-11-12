# เปิดใช้งาน pygame
import pygame
from pygame.sprite import *
pygame.init()

# import file
import database as b
import bullet as bu
import random

# สร้าง Enemys_Flameow class
class Enemys_Flameow(pygame.sprite.Sprite):
    def __init__(self, x, y, health):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Image/Enemy/Flameow.png')
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
        if abs(self.move_counter) >= self.rect.width/2: # เคลื่อนย้ายซ้าย-ขวา
            self.move_direction *= -1
            self.move_counter *= self.move_direction
        if self.now_time - self.last_time > self.down: # ตกลงมา
            self.rect.y += 80
            self.last_time = pygame.time.get_ticks()

        # draw health bar
        pygame.draw.rect(b.screen, b.RED, (self.rect.x, (self.rect.bottom - 3), self.rect.width, 10))
        if self.health_remaining > 0:
            pygame.draw.rect(b.screen, b.GREEN, (self.rect.x, (self.rect.bottom - 3), self.rect.width*(self.health_remaining/self.health_start), 10))
        if self.health_remaining <= 0:
            b.enemy_game -= 1
            b.score_game += 10
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
        
        if b.new_game == True:
            self.kill()

# สร้าง Enemy_FireFly class
class Enemys_FireFly(pygame.sprite.Sprite):
    def __init__(self, x, y, health, second):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Image/Enemy/FireFly.png')
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
        if abs(self.move_counter) >= self.rect.width/2: # เคลื่อนย้ายซ้าย-ขวา
            self.move_direction *= -1
            self.move_counter *= self.move_direction
        if self.now_time - self.last_time > self.down: # ตกลงมา
            self.rect.y += 80
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
        if self.health_remaining <= 0 or self.rect.y >= b.SCREEN_H:
            b.enemy_game -= 1
            b.score_game += 30
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
        
        if b.new_game == True:
            self.kill()

# Enemys_Flame_Boy class
class Enemys_Flame_Boy(pygame.sprite.Sprite):
    def __init__(self, x, y, health, second):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Image/Enemy/Flame Boy.png')
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
        if abs(self.move_counter) >= self.rect.width/2: # เคลื่อนย้ายซ้าย-ขวา
            self.move_direction *= -1
            self.move_counter *= self.move_direction
        if self.now_time - self.last_time > self.down: # ตกลงมา
            self.rect.y += 80
            self.last_time = pygame.time.get_ticks()

        # set a cooldown
        cooldown = self.second*1000 # milliseconds
        time_now = pygame.time.get_ticks()
        check_cooldown = time_now - self.last_shot > cooldown
        if check_cooldown:
            # ทำกระสุนกำหนดดังนี้ (ตำแหน่งเริ่มต้นของ x, ตำแหน่งเริ่มต้นของ y, ความเร็วของกระสุน)
            bullet = bu.Bullets_Flame_Boy(self.rect.centerx, self.rect.bottom, 3)
            bu.bullet_enemy_01_group.add(bullet)
            self.last_shot = time_now

        # draw health bar
        if self.health_remaining > 0:
            pygame.draw.rect(b.screen, b.RED, (self.rect.x, (self.rect.bottom - 3), self.rect.width, 10))
            pygame.draw.rect(b.screen, b.GREEN, (self.rect.x, (self.rect.bottom - 3), self.rect.width*(self.health_remaining/self.health_start), 10))
        if self.health_remaining <= 0 or self.rect.y >= b.SCREEN_H:
            b.enemy_game -= 1
            b.score_game += 50
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

        if b.new_game == True:
            self.kill()

# Main Boss class
class Main_Boss(pygame.sprite.Sprite):
    def __init__(self, x, y, health):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Image/Enemy/Main Boss.png')
        self.image = pygame.transform.scale(self.image, (135, 150))
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.move_counter = 0
        self.move_direction = 1
        self.health_start = health
        self.health_remaining = health
        self.last_shot = pygame.time.get_ticks()
        self.second = 3
    
    def update(self):
        self.rect.x += self.move_direction
        self.move_counter += 1
        self.now_time = pygame.time.get_ticks()
        if abs(self.move_counter) >= self.rect.width/2: # เคลื่อนย้ายซ้าย-ขวา
            self.move_direction *= -1
            self.move_counter *= self.move_direction

        # set a cooldown
        cooldown = self.second*1000 # milliseconds
        time_now = pygame.time.get_ticks()
        check_cooldown = time_now - self.last_shot > cooldown
        if check_cooldown:
            pattern =  random.randint(1, 3)
            if pattern == 1:
                # ทำกระสุนกำหนดดังนี้ (ตำแหน่งเริ่มต้นของ x, ตำแหน่งเริ่มต้นของ y, ความเร็วของกระสุน)
                for i in range(0, 9):
                    bullet = bu.Bullets_FireFly(80+(i*80), 0-(i*115), 3)
                    bu.bullet_enemy_group.add(bullet)
                for i in range(0, 9):
                    bullet = bu.Bullets_FireFly(b.SCREEN_W-80-(i*80), 0-(i*115), 3)
                    bu.bullet_enemy_group.add(bullet)
                for i in range(0, 9):
                    bullet = bu.Bullets_FireFly(80+(i*80), -920-(i*115), 3)
                    bu.bullet_enemy_group.add(bullet)
                for i in range(0, 9):
                    bullet = bu.Bullets_FireFly(b.SCREEN_W-80-(i*80), -920-(i*115), 3)
                    bu.bullet_enemy_group.add(bullet)
                for i in range(0, 9):
                    bullet = bu.Bullets_FireFly(80+(i*80), -1840-(i*115), 3)
                    bu.bullet_enemy_group.add(bullet)
                for i in range(0, 9):
                    bullet = bu.Bullets_FireFly(b.SCREEN_W-80-(i*80), -1840-(i*115), 3)
                    bu.bullet_enemy_group.add(bullet)
                self.second = 15
                self.last_shot = time_now
            elif pattern == 2:
                for i in range(0, 9):
                    bullet = bu.Bullets_Flame_Boy(80+(i*80), -80, 3)
                    bu.bullet_enemy_01_group.add(bullet)
                for i in range(0, 9):
                    bullet = bu.Bullets_Flame_Boy(80+(i*80), -640, 3)
                    bu.bullet_enemy_01_group.add(bullet)
                for i in range(0, 9):
                    bullet = bu.Bullets_Flame_Boy(80+(i*80), -1280, 3)
                    bu.bullet_enemy_01_group.add(bullet)
                self.second = 8
                self.last_shot = time_now
            elif pattern == 3:
                num = random.randint(0, 8)
                for i in range(0, 9):
                    if i == num:
                        pass
                    else:
                        bullet = bu.Bullets_Boss(80+(i*80), -80, 2)
                        bu.bullet_boss_group.add(bullet)
                num = random.randint(0, 8)
                for i in range(0, 9):
                    if i == num:
                        pass
                    else:
                        bullet = bu.Bullets_Boss(80+(i*80), -640, 2)
                        bu.bullet_boss_group.add(bullet)
                num = random.randint(0, 8)
                for i in range(0, 9):
                    if i == num:
                        pass
                    else:
                        bullet = bu.Bullets_Boss(80+(i*80), -1280, 2)
                        bu.bullet_boss_group.add(bullet)
                self.second = 15
                self.last_shot = time_now

        # draw health bar
        if self.health_remaining > 0:
            pygame.draw.rect(b.screen, b.RED, (self.rect.x, (self.rect.bottom - 3), self.rect.width, 10))
            pygame.draw.rect(b.screen, b.GREEN, (self.rect.x, (self.rect.bottom - 3), self.rect.width*(self.health_remaining/self.health_start), 10))
        if self.health_remaining <= 0 or self.rect.y >= b.SCREEN_H:
            b.enemy_game -= 1
            b.score_game += 500
            b.damage_01 += 3
            b.damage_02 += 2
            b.damage_03 += 2
            b.damage_04 += 0.5
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

        if b.new_game == True:
            self.kill()

# เก็บกลุ่มของศัตรู
enemy_group = pygame.sprite.Group()
