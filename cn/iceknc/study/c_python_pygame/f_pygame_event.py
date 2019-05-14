import pygame

pygame.init()

# 创建游戏窗口
screen = pygame.display.set_mode((480, 700))

bg = pygame.image.load("./images/background.png")

hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (150, 300))

# 创建时钟对象
clock = pygame.time.Clock()

hero_rect = pygame.Rect(150, 300, 102, 126)

i = 0
while True:
    # 代码执行的频率
    clock.tick(60)

    # 捕获事件
    event_list = pygame.event.get()
    if len(event_list) > 0:
        print(event_list)

    # 修改飞机的位置
    hero_rect.y -= 1
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)

    print(i)
    i += 1
    pygame.display.update()

pygame.quit()
