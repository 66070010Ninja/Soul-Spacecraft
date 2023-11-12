# เปิดใช้งาน pygame
import pygame
from pygame.locals import *
pygame.init()
pygame.mixer.init()

import database as b

# เสียงหน้าหลัก
def main_sound():
    if b.sound_title == False:
        main_sound = pygame.mixer.Sound("Sound/main_sound.mp3") # ใส่เสียง
        main_sound.set_volume(0.15)
        pygame.mixer.Sound.play(main_sound)
        b.play_sound_title = True
        b.sound_title = True
    if b.new_game == False:
        pygame.mixer.stop()

print(1)
