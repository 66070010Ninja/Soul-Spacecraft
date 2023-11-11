# เปิดใช้งาน pygame
import pygame
from pygame.locals import *
pygame.mixer.init()

# เสียงหน้าหลัก
def main_sound():
    main_sound = pygame.mixer.Sound("Sound/main_sound") # ใส่เสียง
    main_sound.play()
    main_sound.set_volume(0.3)
