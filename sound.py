# เปิดใช้งาน pygame
import pygame
from pygame.locals import *
pygame.init()
pygame.mixer.init()

import database as b

# เสียงหน้าหลัก
def main_sound():
    if b.sound_boss == True or b.sound_game_play == True:
        pygame.mixer.stop()
        b.sound_boss = False
        b.sound_game_play = False
    if b.sound_title == False:
        pygame.mixer.Sound.play(b.main_sound) # เล่นเสียง
        b.sound_title = True
    if b.new_game == False:
        b.sound_boss = False
        b.sound_game_play = False
        pygame.mixer.stop() # หยุดเสียง

# เสียงเจอบอส
def boss_sound():
    if b.sound_game_play == True:
        pygame.mixer.stop()
        b.sound_game_play = False
    if b.sound_boss == False:
        pygame.mixer.Sound.play(b.boss_sound) # เล่นเสียง
        b.sound_boss = True

# เสียงเกมหลัก
def enemy_sound():
    if b.sound_boss == True:
        pygame.mixer.stop()
        b.sound_boss = False
    if b.sound_game_play == False:
        pygame.mixer.Sound.play(b.enemy_sound) # เล่นเสียง
        b.sound_game_play = True
