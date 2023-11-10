# เปิดใช้งาน pygame
import pygame
pygame.init()

# import file
import database as b

# สร้าง Button class
class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw_button(self):
        # ตัวกระทำ
        action = False

        # ตำแหน่งเมาส์
        pos = pygame.mouse.get_pos()

        # เช็คตำแหน่งและการคลิ๊ก
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # วาดปุ่ม
        b.screen.blit(self.image, (self.rect.x, self.rect.y))

        # คืนค่าตัวกระทำ
        return action
