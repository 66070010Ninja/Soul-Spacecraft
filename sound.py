# เปิดใช้งาน pygame
import pygame
from pygame.locals import *
pygame.init()
pygame.mixer.init()

# เสียงหน้าหลัก
def main_sound():
    main_sound = pygame.mixer.Sound("Sound/main_sound.mp3") # ใส่เสียง
    main_sound.set_volume(0.15)
    pygame.mixer.Sound.play(main_sound)
    pygame.mixer.music.stop()
