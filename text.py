# เปิดใช้งาน pygame
import pygame
from pygame.sprite import *
pygame.init()

import database as b

# เรียกใช้ font โดยใช้ font type comicsans ขนาด 50 pixel
level_font = pygame.font.SysFont('comicsans', 40)
score_font = pygame.font.SysFont('comicsans', 40)

def draw_text():
    level_label = level_font.render('Level : %02d'%b.level_game, 1, (255, 255, 255))
    level_label_width = level_label.get_width()

    score_label = score_font.render('Score : %05d'%b.score_game, 1, (255, 255, 255))
    score_label_width = score_label.get_width()

    b.screen.blit(level_label, (10, 10))
    b.screen.blit(score_label, (score_label_width+10, 10))