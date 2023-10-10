import pygame

pygame.init()
pygame.display.set_caption('Space Of Arcana')

BLACK = (0, 0, 0)

SCREEN_W = 800
SCREEN_H = 600
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))

runing = True
while runing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runing = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_F4]:
        break
    screen.fill(BLACK)
    pygame.display.update()
pygame.quit()
