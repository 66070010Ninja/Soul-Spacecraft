# เปิดใช้งาน pygame
import pygame
from pygame.locals import *
pygame.init()
pygame.mixer.init()

import database as b

# เสียงหน้าหลัก
def main_sound():
    if b.sound_title == False:
        pygame.mixer.Sound.play(b.main_sound) # เล่นเสียง
        b.sound_title = True
    if b.new_game == False:
        pygame.mixer.stop() # หยุดเสียง

# เสียงในเกม
def boss_sound():
    #if b.sound_title == False:
        pygame.mixer.Sound.play(b.boss_sound) # เล่นเสียง
        b.sound_title = True
    #if b.new_game == False:
        pygame.mixer.stop() # หยุดเสียง

# เสียงเจอบอส
def enemy_sound():
    #if b.sound_title == False:
        pygame.mixer.Sound.play(b.enemy_sound) # เล่นเสียง
        b.sound_title = True
    #if b.new_game == False:
        pygame.mixer.stop() # หยุดเสียง
