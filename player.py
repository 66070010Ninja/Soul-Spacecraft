# เปิดใช้งาน pygame
import pygame
from pygame.sprite import *
pygame.init()

# import file
import database as b
import bullet as bu
import enemy as e

# สร้าง Spachip class
class Spaceship(pygame.sprite.Sprite):
    def __init__(self, x, y, health):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Image/Ship/Protagonist Ship.png')
        if b.size_player == 'normal':
            self.image = pygame.transform.scale(self.image, (70, 70))
            self.rect = self.image.get_rect()
        self.last_shot = pygame.time.get_ticks()
        self.rect.center = [x, y]
        self.health_start = health
        self.health_remaining = health

    def update(self):
        if b.size_player == 'small' and b.turn_size_player != 0:
            self.image = pygame.transform.scale(self.image, (50, 50))
            self.rect = self.image.get_rect()
            self.rect.centerx = b.SCREEN_W//2
            self.rect.centery = b.SCREEN_H-100
            b.speed_player = 10
            b.size_player = ''
        elif b.size_player == 'normal' and b.turn_size_player == 0:
            self.image = pygame.transform.scale(self.image, (70, 70))
            self.rect = self.image.get_rect()
            self.rect.centerx = b.SCREEN_W//2
            self.rect.centery = b.SCREEN_H-100
            b.speed_player = 8
            b.size_player = ''
        elif b.size_player == 'big' and b.turn_size_player != 0:
            self.image = pygame.transform.scale(self.image, (90, 90))
            self.rect = self.image.get_rect()
            self.rect.centerx = b.SCREEN_W//2
            self.rect.centery = b.SCREEN_H-100
            b.speed_player = 6
            b.size_player = ''
        b.player_x = self.rect.centerx
        b.player_y = self.rect.centery
        # set a cooldown
        cooldown = 250 # milliseconds
        cooldown_fast = cooldown//3 # milliseconds
        cooldown_slow = cooldown*4 # milliseconds

        # get key press
        key = pygame.key.get_pressed()
        if (key[pygame.K_a] or key[pygame.K_LEFT]) and self.rect.left >= 0:
            self.rect.x -= b.speed_player
        if (key[pygame.K_d] or key[pygame.K_RIGHT]) and self.rect.right <= b.SCREEN_W:
            self.rect.x += b.speed_player

        # draw health bar
        if b.restore_blood != 0:
            self.health_remaining += b.restore_blood
            b.restore_blood = 0
        if self.health_remaining >= 100:
            self.health_remaining = 100
        if self.health_remaining > 0:
            pygame.draw.rect(b.screen, b.RED, (self.rect.x, (self.rect.bottom + 5), self.rect.width, 10))
            pygame.draw.rect(b.screen, b.GREEN, (self.rect.x, (self.rect.bottom + 5), self.rect.width*(self.health_remaining/self.health_start), 10))
        if self.health_remaining <= 0:
            self.kill()

        # hit damage
        if pygame.sprite.spritecollide(self, bu.bullet_enemy_group, True) and b.turn_barrier == 0:
            self.health_remaining -= b.damage_enemy
        if pygame.sprite.spritecollide(self, bu.bullet_enemy_01_group, True) and b.turn_barrier == 0:
            self.health_remaining -= b.damage_enemy_01
        if pygame.sprite.spritecollide(self, e.enemy_group, True) and b.turn_barrier == 0:
            self.health_remaining -= b.damage_enemy_boom
            b.enemy_game -= 1

        # cool dowe bullet
        time_now = pygame.time.get_ticks()
        check_cooldown = time_now - self.last_shot > cooldown
        check_cooldown_flast = time_now - self.last_shot > cooldown_fast
        check_cooldown_slow = time_now - self.last_shot > cooldown_slow

        if b.turn_cool_down_atk == 1:
            check_cooldown = time_now - self.last_shot > cooldown/2
            check_cooldown_flast = time_now - self.last_shot > cooldown_fast/2
            check_cooldown_slow = time_now - self.last_shot > cooldown_slow/2

        # shoot
        if b.type_bullet == 1 and check_cooldown:
            # ทำกระสุนกำหนดดังนี้ (ตำแหน่งเริ่มต้นของ x, ตำแหน่งเริ่มต้นของ y, ความเร็วของกระสุน)
            bullet = bu.Bullets(self.rect.centerx, self.rect.top, 5)
            bu.bullet_01_group.add(bullet)
            self.last_shot = time_now

        if b.type_bullet == 2 and check_cooldown:
            for i in range(-1, 2, 1):
                # ทำกระสุนกำหนดดังนี้ (ตำแหน่งเริ่มต้นของ x, ตำแหน่งเริ่มต้นของ y, ระยะการกระจาย, ความเร็วของกระสุน)
                bullet = bu.Bullets_Ball(self.rect.centerx, self.rect.top, i, 5)
                bu.bullet_02_group.add(bullet)
            self.last_shot = time_now

        if b.type_bullet == 3 and check_cooldown_flast:
            # ทำกระสุนกำหนดดังนี้ (ตำแหน่งเริ่มต้นของ x, ตำแหน่งเริ่มต้นของ y, ความเร็วของกระสุน)
            bullet = bu.Bullets_Short(self.rect.centerx, self.rect.top, 10)
            bu.bullet_03_group.add(bullet)
            self.last_shot = time_now

        if b.type_bullet == 4 and check_cooldown_slow:
            # ทำกระสุนกำหนดดังนี้ (ตำแหน่งเริ่มต้นของ x, ตำแหน่งเริ่มต้นของ y, ความเร็วของกระสุน)
            bullet = bu.Bullets_Cannon(self.rect.centerx, self.rect.top, 2)
            bu.bullet_04_group.add(bullet)
            self.last_shot = time_now

spaceship_group = pygame.sprite.Group()

# สร้าง player
spaceship = Spaceship((b.SCREEN_W//2), b.SCREEN_H-100, 100)
spaceship_group.add(spaceship)
