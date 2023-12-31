# เปิดใช้งาน pygame
import pygame
from pygame.sprite import *
pygame.init()

# import file
import database as b
import create_level as cl

# สร้างลิสต์ของการ์ด (รูปภาพการ์ด) และความถี่เป็นเปอร์เซ็นต์
# ประเภทของการ์ด
card_list_1 = [
    ("Card 1", pygame.image.load("Image/Card frame/nomal.png"), 70),  # 50% ความถี่
    ("Card 2", pygame.image.load("Image/Card frame/bad.png"), 10),    # 25% ความถี่
    ("Card 3", pygame.image.load("Image/Card frame/luck.png"), 20),  # 25% ความถี่
]

# การ์ดกลาง
card_list_nomal = [
    ("BBASE", pygame.image.load("Image/Card png/BBASE.png"), 10),  # 50% ความถี่
    ("BBIG", pygame.image.load("Image/Card png/BBIG.png"), 10),  # 25% ความถี่
    ("BGAT", pygame.image.load("Image/Card png/BGAT.png"), 10),  # 25% ความถี่
    ("HH", pygame.image.load("Image/Card png/HH.png"), 7.5),  # 50% ความถี่
    ("sma", pygame.image.load("Image/Card png/sma.png"), 7.5),  # 25% ความถี่
    ("skip", pygame.image.load("Image/Card png/skip.png"), 15),
    ("BIGS", pygame.image.load("Image/Card png/BIGS.png"), 5),
    ("BR", pygame.image.load("Image/Card png/BR.png"), 1),
    ("BSPA", pygame.image.load("Image/Card png/BSPA.png"), 10),
    ("DES", pygame.image.load("Image/Card png/DESTROY.png"), 0.01),
    ("HB", pygame.image.load("Image/Card png/HB.png"), 5),
    ("L2", pygame.image.load("Image/Card png/L2.png"), 5),
    ("NO", pygame.image.load("Image/Card png/NO.png"), 15),
]

# การ์ดโชคดี
card_list_luck = [
    ("HH", pygame.image.load("Image/Card png/HH.png"), 20),  # 50% ความถี่
    ("sma", pygame.image.load("Image/Card png/sma.png"), 10),  # 25% ความถี่
    ("skip", pygame.image.load("Image/Card png/skip.png"), 15),  # 25% ความถี่
    ("BR", pygame.image.load("Image/Card png/BR.png"), 0.5),
    ("L2", pygame.image.load("Image/Card png/L2.png"), 5),
]

# การ์ดโชคร้าย
card_list_bad = [
    ("BIGS", pygame.image.load("Image/Card png/BIGS.png"), 15),
    ("DES", pygame.image.load("Image/Card png/DESTROY.png"), 0.01),
    ("HB", pygame.image.load("Image/Card png/HB.png"), 20),
]

# เช็คเงื่อนการ์ดที่เปิดได้
def usd_card():
    if b.use_card == 'BBASE':
        b.type_bullet = 1
    elif b.use_card == 'BBIG':
        b.type_bullet = 4
    elif b.use_card == 'BGAT':
        b.type_bullet = 3
    elif b.use_card == 'BSPA':
        b.type_bullet = 2
    elif b.use_card == 'HH':
        b.restore_blood += 30
    elif b.use_card == 'sma':
        b.size_player = 'small'
        b.turn_size_player = 3
    elif b.use_card == 'BIGS':
        b.size_player = 'big'
        b.turn_size_player = 3
    elif b.use_card == 'skip':
        b.level_game += 1
        cl.turn_up() # ข้ามเลเวล
    elif b.use_card == 'BR':
        b.turn_barrier = 2
    elif b.use_card == 'HB':
        b.restore_blood -= 30
    elif b.use_card == 'L2':
        b.turn_cool_down_atk = 1
    elif b.use_card == 'NO':
        pass
    elif b.use_card == 'DES':
        b.restore_blood -= 500
