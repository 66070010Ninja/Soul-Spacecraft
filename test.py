import pygame
import sys
import random

# กำหนดรูปภาพพื้นหลัง
background = pygame.image.load("Image/Game/background-black.png")

# กำหนดขนาดหน้าต่าง
screen_width = 800
screen_height = 600

# สร้างหน้าต่าง Pygame
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("สุ่มการ์ด Pygame")

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
    ("HH", pygame.image.load("Image/Card png/HH.png"), 7.5),  # 50% ความถี่
    ("sma", pygame.image.load("Image/Card png/sma.png"), 7.5),  # 25% ความถี่
    ("sklp", pygame.image.load("Image/Card png/sklp.png"), 15),
    ("B2", pygame.image.load("Image/Card png/B2.png"), 5),
    ("BIGS", pygame.image.load("Image/Card png/BIGS.png"), 5),
    ("BR", pygame.image.load("Image/Card png/BR.png"), 1),
    ("BSPA", pygame.image.load("Image/Card png/BSPA.png"), 10),
    ("BDS", pygame.image.load("Image/Card png/but down spd.png"), 8),
    ("DES", pygame.image.load("Image/Card png/DESTROY.png"), 0.01),
    ("DS", pygame.image.load("Image/Card png/down spd.png"), 8),
    ("HB", pygame.image.load("Image/Card png/HB.png"), 5),
    ("L2", pygame.image.load("Image/Card png/L2.png"), 7.5),
    ("NO", pygame.image.load("Image/Card png/NO.png"), 15),
    ("SUP", pygame.image.load("Image/Card png/SPD UP BUL.png"), 5),
    ("SU", pygame.image.load("Image/Card png/SPD UP.png"), 5),
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
# ตัวแปรสำหรับเลือกลิสต์การ์ด
current_card_list = card_list_1

# แปลงลิสต์นี้ให้เป็นลิสต์ของรายการการ์ดที่แยกออกมาเท่ากับความถี่
cards, images, weights = zip(*current_card_list)

# ตำแหน่งการ์ดบนหน้าต่าง
x, y = -50, 50
x2, y2 = 350, 50

# ...
# สุ่มการ์ดเริ่มต้น
current_card = random.choices(images, weights=weights, k=1)[0]
current_card_name = [card[0] for card in current_card_list if card[1] == current_card][0]
current_card2 = random.choices(images, weights=weights, k=1)[0]  # สุ่ม current_card2 อิสระ
current_card2_name = [card[0] for card in current_card_list if card[1] == current_card2][0]

# ตัวแปรสำหรับติดตามการคลิก
clicked_card1 = False
clicked_card2 = False

# เริ่มลูปหลัก
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and not (clicked_card1 and clicked_card2):
            if x <= event.pos[0] <= x + current_card.get_width() and y <= event.pos[1] <= y + current_card.get_height() and not clicked_card1:
                if current_card_name == "Card 1":
                    current_card_list = card_list_nomal
                elif current_card_name == "Card 3":
                    current_card_list = card_list_luck
                elif current_card_name == "Card 2":
                    current_card_list = card_list_bad

                cards, images, weights = zip(*current_card_list)
                current_card = random.choices(images, weights=weights, k=1)[0]
                current_card_name = [card[0] for card in current_card_list if card[1] == current_card][0]

                clicked_card1 = True

            if x2 <= event.pos[0] <= x2 + current_card2.get_width() and y2 <= event.pos[1] <= y2 + current_card2.get_height() and not clicked_card2:
                if current_card2_name == "Card 1":
                    current_card_list = card_list_nomal
                elif current_card2_name == "Card 3":
                    current_card_list = card_list_luck
                elif current_card2_name == "Card 2":
                    current_card_list = card_list_bad

                cards, images, weights = zip(*current_card_list)
                current_card2 = random.choices(images, weights=weights, k=1)[0]  # สุ่ม current_card2 อิสระ
                current_card2_name = [card[0] for card in current_card_list if card[1] == current_card2][0]

                clicked_card2 = True

    screen.blit(background, (0, 0))

    # แสดงการ์ดปัจจุบัน
    screen.blit(current_card, (x, y))
    screen.blit(current_card2, (x2, y2))

    pygame.display.flip()

# ออกจากโปรแกรม Pygame
pygame.quit()
sys.exit()
