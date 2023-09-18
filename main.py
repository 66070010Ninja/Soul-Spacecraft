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

def main():
    '''run game'''
    run = True
    fps = 60
    level = 1
    lives = 5
    # เรียกใช้ font โดยใช้ font type comicsans ขนาด 50 pixel
    main_font = pygame.font.SysFont('comicsans', 50)

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
main()