# เปิดใช้งาน pygame
import pygame
from pygame.sprite import *
pygame.init()

# import
import basic as b
import bullet as bu

# สร้าง Spachip class
class Spaceship(pygame.sprite.Sprite):
    def __init__(self, x, y, health):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Image/Protagonist Ship.png')
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.last_shot = pygame.time.get_ticks()
        self.health_start = health
        self.health_remaining = health

    def update(self):
        # set movement speed
        speed = 8
        
        # set a cooldown
        cooldown = 250 # milliseconds
        cooldown_fast = cooldown//3 # milliseconds
        cooldown_slow = cooldown*4 # milliseconds

        # get key press
        key = pygame.key.get_pressed()
        if (key[pygame.K_a] or key[pygame.K_LEFT]) and self.rect.left >= 0:
            self.rect.x -= speed
        if (key[pygame.K_d] or key[pygame.K_RIGHT]) and self.rect.right <= b.SCREEN_W:
            self.rect.x += speed

        # draw health bar
        pygame.draw.rect(b.screen, b.RED, (self.rect.x, (self.rect.bottom + 5), self.rect.width, 10))
        if self.health_remaining > 0:
            pygame.draw.rect(b.screen, b.GREEN, (self.rect.x, (self.rect.bottom + 5), self.rect.width*(self.health_remaining//self.health_start), 10))

        # cool dowe bullet
        time_now = pygame.time.get_ticks()
        check_cooldown = time_now - self.last_shot > cooldown
        check_cooldown_flast = time_now - self.last_shot > cooldown_fast
        check_cooldown_slow = time_now - self.last_shot > cooldown_slow

        # shoot
        if (key[pygame.K_1]) and check_cooldown:
            # ทำกระสุนกำหนดดังนี้ (ตำแหน่งเริ่มต้นของ x, ตำแหน่งเริ่มต้นของ y, ความเร็วของกระสุน)
            bullet = bu.Bullets(self.rect.centerx, self.rect.top, 5)
            bu.bullet_group.add(bullet)
            self.last_shot = time_now
        if (key[pygame.K_2]) and check_cooldown:
            for i in range(-1, 2, 1):
                # ทำกระสุนกำหนดดังนี้ (ตำแหน่งเริ่มต้นของ x, ตำแหน่งเริ่มต้นของ y, ระยะการกระจาย, ความเร็วของกระสุน)
                bullet = bu.Bullets_Ball(self.rect.centerx, self.rect.top, i, 5)
                bu.bullet_group.add(bullet)
            self.last_shot = time_now
        if (key[pygame.K_3]) and check_cooldown_flast:
            # ทำกระสุนกำหนดดังนี้ (ตำแหน่งเริ่มต้นของ x, ตำแหน่งเริ่มต้นของ y, ความเร็วของกระสุน)
            bullet = bu.Bullets_Short(self.rect.centerx, self.rect.top, 10)
            bu.bullet_group.add(bullet)
            self.last_shot = time_now
        if (key[pygame.K_4]) and check_cooldown_slow:
            # ทำกระสุนกำหนดดังนี้ (ตำแหน่งเริ่มต้นของ x, ตำแหน่งเริ่มต้นของ y, ความเร็วของกระสุน)
            bullet = bu.Bullets_Cannon(self.rect.centerx, self.rect.top, 2)
            bu.bullet_group.add(bullet)
            self.last_shot = time_now

spaceship_group = pygame.sprite.Group()

# สร้าง player
spaceship = Spaceship((b.SCREEN_W//2), b.SCREEN_H-100, 3)
spaceship_group.add(spaceship)
