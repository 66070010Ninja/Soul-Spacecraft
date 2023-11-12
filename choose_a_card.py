# เปิดใช้งาน pygame
import pygame
from pygame.sprite import *
pygame.init()

# import file
import random
import database as b
import card as c

def choose_card():
    # ตัวแปรสำหรับเลือกลิสต์การ์ด
    current_card_list = c.card_list_1

    # แปลงลิสต์นี้ให้เป็นลิสต์ของรายการการ์ดที่แยกออกมาเท่ากับความถี่
    cards, images, weights = zip(*current_card_list)

    # ตำแหน่งการ์ดบนหน้าต่าง
    x, y = 60, 170
    x2, y2 = 410, 170

    # ...
    # สุ่มการ์ดเริ่มต้น
    current_card = random.choices(images, weights=weights, k=1)[0]
    current_card_name = [card[0] for card in current_card_list if card[1] == current_card][0]
    current_card2 = random.choices(images, weights=weights, k=1)[0]  # สุ่ม current_card2 อิสระ
    current_card2_name = [card[0] for card in current_card_list if card[1] == current_card2][0]

    # ตัวแปรสำหรับติดตามการคลิก
    clicked_card1 = 0
    clicked_card2 = 0

    # เริ่มลูปหลัก
    running = True
    set_card = []
    while running:
        if b.exit_game == True:
            running = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                b.exit_game = True
            if event.type == pygame.MOUSEBUTTONDOWN and not (clicked_card1 == 2 and clicked_card2 == 2):
                if x <= event.pos[0] <= x + current_card.get_width() and y <= event.pos[1] <= y + current_card.get_height() and not clicked_card1 == 2:
                    if current_card_name == "Card 1":
                        current_card_list = c.card_list_nomal
                    elif current_card_name == "Card 3":
                        current_card_list = c.card_list_luck
                    elif current_card_name == "Card 2":
                        current_card_list = c.card_list_bad

                    cards, images, weights = zip(*current_card_list)
                    current_card = random.choices(images, weights=weights, k=1)[0]
                    current_card_name = [card[0] for card in current_card_list if card[1] == current_card][0]

                    clicked_card1 += 1

                    if clicked_card1 == 1:
                        set_card.insert(0, current_card_name)
                    elif clicked_card1 == 2 and len(set_card) == 2:
                        b.use_card = set_card[0]
                        c.usd_card()
                        return
                    elif clicked_card1 == 2 and len(set_card) == 1:
                        b.use_card = set_card[0]
                        c.usd_card()
                        return

                if x2 <= event.pos[0] <= x2 + current_card2.get_width() and y2 <= event.pos[1] <= y2 + current_card2.get_height() and not clicked_card2 == 2:
                    if current_card2_name == "Card 1":
                        current_card_list = c.card_list_nomal
                    elif current_card2_name == "Card 3":
                        current_card_list = c.card_list_luck
                    elif current_card2_name == "Card 2":
                        current_card_list = c.card_list_bad

                    cards, images, weights = zip(*current_card_list)
                    current_card2 = random.choices(images, weights=weights, k=1)[0]  # สุ่ม current_card2 อิสระ
                    current_card2_name = [card[0] for card in current_card_list if card[1] == current_card2][0]

                    clicked_card2 += 1

                    if clicked_card2 == 1:
                        set_card.insert(1, current_card2_name)
                    elif clicked_card2 == 2 and len(set_card) == 2:
                        b.use_card = set_card[1]
                        c.usd_card()
                        return
                    elif clicked_card2 == 2 and len(set_card) == 1:
                        b.use_card = set_card[0]
                        c.usd_card()
                        return

        # แสดงการ์ดปัจจุบัน
        b.screen.blit(current_card, (x, y))
        b.screen.blit(current_card2, (x2, y2))
        pygame.display.update()
    return
