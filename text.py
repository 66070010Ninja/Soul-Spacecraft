# เปิดใช้งาน pygame
import pygame
from pygame.sprite import *
pygame.init()

import database as b

# เรียกใช้ font โดยใช้ font type comicsans ขนาด 50 pixel
score_font = pygame.font.SysFont('comicsans', 40)

def draw_text():
    level_label = score_font.render('Level : %02d'%b.level_game, 1, (255, 255, 255))

    score_label = score_font.render('Score : %05d'%b.score_game, 1, (255, 255, 255))
    score_label_width = score_label.get_width()

    b.screen.blit(level_label, (10, 10))
    b.screen.blit(score_label, (score_label_width+10, 10))

def score_game():
    score_label = score_font.render('Your Score : %05d'%b.score_game, 1, (255, 255, 255))
    score_label_width = score_label.get_width()

    height_score_label = score_font.render('Height Score : %05d'%b.height_score_game, 1, (255, 255, 255))
    height_score_label_width = height_score_label.get_width()

    b.screen.blit(score_label, ((b.SCREEN_W-score_label_width)/2, 300))
    b.screen.blit(height_score_label, ((b.SCREEN_W-height_score_label_width)/2, 200))