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
bg_game_play = pygame.image.load("Image/Game/background-black.png") # ดึงภาพจาก Image มาใช้งาน
bg_game_play = pygame.transform.scale(bg_game_play, (SCREEN_W, SCREEN_H)) # ปรับขนาดของ bg

# แสดงรูป logo game
logo_game = pygame.image.load("Image/Game/Space of Arcana.png") # ดึงภาพจาก Image มาใช้งาน
logo_game = pygame.transform.scale(logo_game, (600, 400)) # ปรับขนาดของ logo

def draw_bg_game_play():
    screen.blit(bg_game_play, (0, 0))

def draw_logo_game():
    screen.blit(logo_game, (100, 0))

# เช็คปิดโปรแกรม
start = False
exit_game = False
enemy_game = 0

# damage
damage_01 = 40
damage_02 = 20
damage_03 = 20
damage_04 = 0.5

speed_player = 8

damage_enemy = 20
damage_enemy_boom = 50

level_game = 0

use_card = ''

# player
type_bullet = 3
restore_blood = 0
size_player = 'normal'
turn_size_player = 0
turn_barrier = 0
turn_cool_down_atk = 0

# enemy
turn_cool_up_enemy = 0
turn_cool_down_enemy = 0
turn_speed_move_up_enemy = 0
turn_speed_move_down_enemy = 0
