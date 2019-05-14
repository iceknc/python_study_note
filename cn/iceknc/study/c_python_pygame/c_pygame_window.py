import pygame

pygame.init()

# 创建游戏窗口
screen = pygame.display.set_mode((480, 700))

bg = pygame.image.load("./images/background.png")
screen.blit(bg, (0, 0))
hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (200, 500))

pygame.display.update()

pygame.quit()
