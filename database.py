# เปิดใช้งาน pygame
import pygame
from pygame.sprite import *
pygame.init()

# ขนาดหน้าจอ
SCREEN_W = 800
SCREEN_H = 800

# ตั้งค่าสี (RGB)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# กำหนด FPS
clock = pygame.time.Clock()
FPS = 60

# สร้างหน้าจอเกม
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))

# แสดงรูปพื้นหลังในหน้าจอ
bg_game_play = pygame.image.load("Image/background-black.png") # ดึงภาพจาก Image มาใช้งาน
bg_game_play = pygame.transform.scale(bg_game_play, (SCREEN_W, SCREEN_H)) # ปรับขนาดของ bg

def draw_bg_game_play():
    screen.blit(bg_game_play, (0, 0))

# เช็คปิดโปรแกรม
start = False
exit_game = False
enemy_game = 0

# damage
damage_01 = 30
damage_02 = 20
damage_03 = 20
damage_04 = 0.5

damage_enemy = 20
damage_enemy_boom = 50