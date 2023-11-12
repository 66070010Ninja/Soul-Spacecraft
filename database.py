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
logo_game = pygame.transform.scale(logo_game, (617.5, 313.5)) # ปรับขนาดของ logo

# สร้างภาพ gameover
gameover_img = pygame.image.load("Image/Game/Gameover.png") # ดึงภาพจาก Image มาใช้งาน
gameover_img = pygame.transform.scale(gameover_img, (525, 112.5)) # ปรับขนาดของภาพ Gameover

# สร้างภาพ game pause
game_pause_img = pygame.image.load("Image/Game/Game Pause.png")
game_pause_img = pygame.transform.scale(game_pause_img, (487, 316))

def draw_bg_game_play():
    screen.blit(bg_game_play, (0, 0))

def draw_logo_game():
    screen.blit(logo_game, ((SCREEN_W-logo_game.get_width())/2, 0))

def draw_game_over():
    screen.blit(gameover_img, ((SCREEN_W-gameover_img.get_width())/2, 50))

def draw_game_papse():
    screen.blit(game_pause_img, ((SCREEN_W-game_pause_img.get_width())/2, 0))

# เช็คปิดโปรแกรม
enemy_game = 0 # จำนวนศัตรูของเลเวลนั้นๆ
start = False
exit_game = False
title = False
pause = False
gameover = False
new_game = True
clear_game = False


# damage
damage_01 = 40
damage_02 = 18
damage_03 = 20
damage_04 = 2

speed_player = 8

damage_enemy = 20
damage_enemy_01 = 10
damage_boss = 0.5
damage_enemy_boom = 50

level_game = 1
score_game = 0
height_score_game = 0

use_card = ''

# player
type_bullet = 1
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

# ตำแหน่ง player
player_x = 0
player_y = 0

main_sound = pygame.mixer.Sound("Sound/Game/main.mp3") # ใส่เสียง
main_sound.set_volume(0.15) # ปรับเสียง

boss_sound = pygame.mixer.Sound("Sound/Gmae/boss.mp3") # ใส่เสียง
boss_sound.set_volume(0.15) # ปรับเสียง

enemy_sound = pygame.mixer.Sound("Sound/Game/enemy.mp3") # ใส่เสียง
enemy_sound.set_volume(0.15) # ปรับเสียง

gameover_sound = pygame.mixer.Sound("Sound/Game/gameover.wav") # ใส่เสียง
gameover_sound.set_volume(0.15) # ปรับเสียง

sound_title = False
sound_enemy = False
sound_boss = False
sound_gameover = False
