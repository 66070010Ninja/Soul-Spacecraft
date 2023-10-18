# เรียกใช้งาน pygame
import pygame
from pygame.sprite import *

# เริ่มการทำงานของ pygame
pygame.init()

# กำหนด game variables
rows = 4
cols = 7

# กำหนด FPS
clock = pygame.time.Clock()
FPS = 60

# กำหนดขนาดของหน้าจอ
SCREEN_W = 750
SCREEN_H = 750

# ตั้งค่าสี (RGB)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# สร้างหน้าจอเกม
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))

# กำหนดข้อความที่ Titlebar
pygame.display.set_caption('Space Of Arcana')

# แสดงรูปพื้นหลังในหน้าจอ
bg = pygame.image.load("Image/background-black.png") # ดึงภาพจาก Image มาใช้งาน
bg = pygame.transform.scale(bg, (SCREEN_W, SCREEN_H)) # ปรับขนาดของ bg

def draw_bg():
    screen.blit(bg, (0, 0))

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
        if (key[pygame.K_d] or key[pygame.K_RIGHT]) and self.rect.right <= SCREEN_W:
            self.rect.x += speed

        # draw health bar
        pygame.draw.rect(screen, RED, (self.rect.x, (self.rect.bottom + 10), self.rect.width, 10))
        if self.health_remaining > 0:
            pygame.draw.rect(screen, GREEN, (self.rect.x, (self.rect.bottom + 10), self.rect.width*(self.health_remaining//self.health_start), 10))

        # cool dowe bullet
        time_now = pygame.time.get_ticks()
        check_cooldown = time_now - self.last_shot > cooldown
        check_cooldown_flast = time_now - self.last_shot > cooldown_fast
        check_cooldown_slow = time_now - self.last_shot > cooldown_slow

        # shoot
        if (key[pygame.K_1]) and check_cooldown:
            # ทำกระสุนกำหนดดังนี้ (ตำแหน่งเริ่มต้นของ x, ตำแหน่งเริ่มต้นของ y, ความเร็วของกระสุน)
            bullet = Bullets(self.rect.centerx, self.rect.top, 5)
            bullet_group.add(bullet)
            self.last_shot = time_now
        if (key[pygame.K_2]) and check_cooldown:
            for i in range(-1, 2, 1):
                # ทำกระสุนกำหนดดังนี้ (ตำแหน่งเริ่มต้นของ x, ตำแหน่งเริ่มต้นของ y, ระยะการกระจาย, ความเร็วของกระสุน)
                bullet = Bullets_Ball(self.rect.centerx, self.rect.top, i, 5)
                bullet_group.add(bullet)
            self.last_shot = time_now
        if (key[pygame.K_3]) and check_cooldown_flast:
            # ทำกระสุนกำหนดดังนี้ (ตำแหน่งเริ่มต้นของ x, ตำแหน่งเริ่มต้นของ y, ความเร็วของกระสุน)
            bullet = Bullets_Short(self.rect.centerx, self.rect.top, 10)
            bullet_group.add(bullet)
            self.last_shot = time_now
        if (key[pygame.K_4]) and check_cooldown_slow:
            # ทำกระสุนกำหนดดังนี้ (ตำแหน่งเริ่มต้นของ x, ตำแหน่งเริ่มต้นของ y, ความเร็วของกระสุน)
            bullet = Bullets_Cannon(self.rect.centerx, self.rect.top, 2)
            bullet_group.add(bullet)
            self.last_shot = time_now

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
        if pygame.sprite.spritecollide(self, enemy_group, True):
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
        if self.rect.bottom <= 0 or self.rect.left <= 0 or self.rect.right >= SCREEN_W:
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

# สร้าง Enemys class
class Enemys(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Image/Flameow.png')
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.move_counter = 0
        self.move_direction = 1
        self.last_time = pygame.time.get_ticks()
        self.down = 10 * 1000

    def update(self):
        self.rect.x += self.move_direction
        self.move_counter += 1
        self.now_time = pygame.time.get_ticks()
        if abs(self.move_counter) >= self.rect.width//2:
            self.move_direction *= -1
            self.move_counter *= self.move_direction
        if self.now_time - self.last_time > self.down:
            self.rect.y += 50
            self.last_time = pygame.time.get_ticks()

# สร้าง sprite groups
spaceship_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()

def create_enemys():
    # generate enemys
    for row in range(rows):
        for item in range(cols):
            enemy = Enemys(80 + item * 100,50 + row * 80)
            enemy_group.add(enemy)

create_enemys()

# สร้าง player
spaceship = Spaceship((SCREEN_W//2), SCREEN_H-100, 3)
spaceship_group.add(spaceship)

def main_game():
    running = True
    while running: # วนลูป while เพื่อควบคุมกิจกรรมในการรันเกม

        clock.tick(FPS)

        # draw background
        draw_bg()

        for event in pygame.event.get(): # ตวรจสอบ event ระหว่างรันเกม
            if event.type == pygame.QUIT: # ถ้าเกิด event ปิดหน้าจอเกม
                running = False # หยุดการวนลูป while

        # update spaceship
        spaceship.update()

        # update sprite groups
        bullet_group.update()
        enemy_group.update()

        # draw sprite groups
        spaceship_group.draw(screen)
        bullet_group.draw(screen)
        enemy_group.draw(screen)

        pygame.display.update()

    pygame.quit() # ออกจากโปรกแกรม
main_game()