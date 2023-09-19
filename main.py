# เรียกใช้ mudule pygame os time และ random
import pygame
import os
import time
import random
# เรียกใช้งานใช้ font
pygame.font.init()

# กำหนดขนาด windows หน่วย pixel
width, height = 750, 750
windows = pygame.display.set_mode((width, height))

# ตั้งชื่อ caption_display
pygame.display.set_caption('Soul-Spacecraft')

# ดึงรูปภาพจากไฟล์ เพื่อนำมาใช้งาน (โดยที่นี้จะทดสอบโดย โหลดไฟล์จาก Flie Foloder ที่มีชื่อว่า assets เพื่อลองทำการดึงภาพมาใช้งาน)

# space_ship ฝั่งศัตรู
red_space_ship = pygame.image.load(os.path.join('assets', 'pixel_ship_red_small.png'))
green_space_ship = pygame.image.load(os.path.join('assets', 'pixel_ship_green_small.png'))
blue_space_ship = pygame.image.load(os.path.join('assets', 'pixel_ship_blue_small.png'))

# space_ship_player
yellow_space_ship = pygame.image.load(os.path.join('assets', 'pixel_ship_yellow.png'))

# Lasers
red_laser = pygame.image.load(os.path.join('assets', 'pixel_laser_red.png'))
green_laser = pygame.image.load(os.path.join('assets', 'pixel_laser_green.png'))
blue_laser = pygame.image.load(os.path.join('assets', 'pixel_laser_blue.png'))
yellow_laser = pygame.image.load(os.path.join('assets', 'pixel_laser_yellow.png'))

# Background (เรียกใช้ background-black.png และปรับขนาด ให้เท่ากับ width, height)
background = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'background-black.png')), (width, height))

# กำหนดลักษณะของ ship
class ship:
    def __init__(self, x, y, health = 100):
        '''Object'''
        self.x = x # ตำแหน่ง x
        self.y = y # ตำแหน่ง y
        self.health = health # เลือดตัวละคร
        self.ship_img = None # ภาพของ ship
        self.laser_img = None # ภาพ laser
        self.lasers = [] # จำนวน laser
        self.cool_down_counter = 0 # ระยะเวลาที่ใช้ยิง

    def draw(self, window):
        '''draw Object'''
        # ให้วาดรูปจาก ship_img
        window.blit(self.ship_img, (self.x, self.y))
    
    # เก็บค่าความกว้าง
    def get_width(self):
        return self.ship_img.get_width()

    # เก็บค่าความสูง
    def get_height(self):
        return self.ship_img.get_height()

# กำหนดลักษณะ player
class player(ship):
    def __init__(self, x, y, health=100):
        '''Player'''
        super().__init__(x, y, health)
        self.ship_img = yellow_space_ship
        self.laser_img = yellow_laser
        self.mask = pygame.mask.from_surface(self.ship_img) # สร้าง hitbox
        self.max_health = health

def main():
    '''run game'''
    run = True
    fps = 60
    level = 1
    lives = 5
    # เรียกใช้ font โดยใช้ font type comicsans ขนาด 50 pixel
    main_font = pygame.font.SysFont('comicsans', 50)

    # กำหนดระยะการเดิน
    player_vel = 5
    
    # กำหนดตัว players
    players = player(300, 650)

    clock = pygame.time.Clock()

    def redraw_window():
        '''วาด background'''
        # ให้ดาวรูปจาก background ในตำแหน่ง (0, 0)
        windows.blit(background, (0, 0))
        
        # วาด text
        lives_label = main_font.render(f'Lives : {lives}', 1, (255, 255, 255))
        leve_label = main_font.render(f'Level : {level}', 1, (255, 255, 255))

        # ให้วาด text livse ในตำแหน่ง (10, 10)
        windows.blit(lives_label, (10, 10))
        # ให้วาด text leve ในตำแหน่ง (width - width ของ text level - 10, 10)
        windows.blit(leve_label, (width - leve_label.get_width()-10, 10))

        # วาด players
        players.draw(windows)

        pygame.display.update()

    # เปิด windows
    while run:
        # run fps/time
        clock.tick(fps)
        redraw_window()
        for event in pygame.event.get():
            # เช็คว่า เมื่อกดปุ่ม QUIT ให้ออกจากเกม
            if event.type == pygame.QUIT:
                run = False

        # การเคลื่อนโดยใช้ keyboard
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and players.x - player_vel > 0:
            # key a = left
            players.x -= player_vel
        if keys[pygame.K_d] and players.x + player_vel + players.get_width() < width:
            # key d = right
            players.x += player_vel
        if keys[pygame.K_w] and players.y - player_vel > 0:
            # key w = up
            players.y -= player_vel
        if keys[pygame.K_s] and players.y + player_vel + players.get_height() < height:
            # key s = down
            players.y += player_vel
main()