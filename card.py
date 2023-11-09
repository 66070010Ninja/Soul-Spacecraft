# เปิดใช้งาน pygame
import pygame
from pygame.sprite import *
pygame.init()

# สร้างลิสต์ของการ์ด (รูปภาพการ์ด) และความถี่เป็นเปอร์เซ็นต์
card_list_1 = [
    ("Card 1", pygame.image.load("Image/Card frame/nomal.png"), 70),  # 50% ความถี่
    ("Card 2", pygame.image.load("Image/Card frame/bad.png"), 10),    # 25% ความถี่
    ("Card 3", pygame.image.load("Image/Card frame/luck.png"), 20),  # 25% ความถี่
]

card_list_nomal = [
    ("BBASE", pygame.image.load("Image/Card png/BBASE.png"), 10),  # 50% ความถี่
    ("BBIG", pygame.image.load("Image/Card png/BBIG.png"), 10),  # 25% ความถี่
    ("BGAT", pygame.image.load("Image/Card png/BGAT.png"), 10),  # 25% ความถี่
    # ("HH", pygame.image.load("Image/Card png/HH.png"), 7.5),  # 50% ความถี่
    # ("sma", pygame.image.load("Image/Card png/sma.png"), 7.5),  # 25% ความถี่
    # ("sklp", pygame.image.load("Image/Card png/sklp.png"), 15),
    # ("B2", pygame.image.load("Image/Card png/B2.png"), 5),
    # ("BIGS", pygame.image.load("Image/Card png/BIGS.png"), 5),
    # ("BR", pygame.image.load("Image/Card png/BR.png"), 1),
    ("BSPA", pygame.image.load("Image/Card png/BSPA.png"), 10)
    # ("BDS", pygame.image.load("Image/Card png/but down spd.png"), 8),
    # ("DES", pygame.image.load("Image/Card png/DESTROY.png"), 0.01),
    # ("DS", pygame.image.load("Image/Card png/down spd.png"), 8),
    # ("HB", pygame.image.load("Image/Card png/HB.png"), 5),
    # ("L2", pygame.image.load("Image/Card png/L2.png"), 7.5),
    # ("NO", pygame.image.load("Image/Card png/NO.png"), 15),
    # ("SUP", pygame.image.load("Image/Card png/SPD UP BUL.png"), 5),
    # ("SU", pygame.image.load("Image/Card png/SPD UP.png"), 5),
]

card_list_luck = [
    ("HH", pygame.image.load("Image/Card png/HH.png"), 20),  # 50% ความถี่
    ("sma", pygame.image.load("Image/Card png/sma.png"), 10),  # 25% ความถี่
    ("sklp", pygame.image.load("Image/Card png/sklp.png"), 15),  # 25% ความถี่
    ("BR", pygame.image.load("Image/Card png/BR.png"), 0.5),
    ("DS", pygame.image.load("Image/Card png/down spd.png"), 10),
    ("L2", pygame.image.load("Image/Card png/L2.png"), 10),
    ("BDS", pygame.image.load("Image/Card png/but down spd.png"), 10),
]

card_list_bad = [
    ("B2", pygame.image.load("Image/Card png/B2.png"), 10),
    ("BIGS", pygame.image.load("Image/Card png/BIGS.png"), 15),
    ("DES", pygame.image.load("Image/Card png/DESTROY.png"), 0.01),
    ("HB", pygame.image.load("Image/Card png/HB.png"), 20),
    ("SUP", pygame.image.load("Image/Card png/SPD UP BUL.png"), 10),
    ("SU", pygame.image.load("Image/Card png/SPD UP.png"), 10),
]