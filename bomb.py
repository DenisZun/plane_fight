# 爆炸效果测试
import pygame

WINDOW_WIDTH, WINDOW_HEIGHT = 500, 500
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))


def bomb():
    animax = 0
    while True:
        if animax >= 21:
            return
        pygame.init()
        print(animax)
        pic = pygame.image.load("res/bomb-%d.png" % (animax//3 + 1))
        print("res/bomb-%d.png" % (animax//3 + 1))
        window.blit(pic, (250, 250))
        animax += 1
        pygame.display.update()


if __name__ == '__main__':
    bomb()