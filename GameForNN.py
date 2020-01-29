# здесь подключаются модули
import pygame
import random
from pygame.locals import *
import sys

# здесь происходит инициация, создание объектов и др.
WIN_WIDTH = 600
WIN_HEIGHT = 400
pygame.init()
sc = pygame.display.set_mode((600, 400))
pygame.display.set_caption('GameForNN')
clock = pygame.time.Clock()     

def main():
    # здесь определяются константы, классы и функции
    
    FPS = 60
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    x = 10
    y = 50
    r = 10
    rTank = 30
    # если надо до цикла отобразить объекты на экране (уберите решотку ниже)
    #pygame.display.update()
    while True:
        sc.fill(BLACK)
        # цикл обработки событий
        for i in pygame.event.get():
            #print(i)
            if i.type == pygame.QUIT:
                return

        # --------
        # изменение объектов и многое др.
        #pygame.draw.rect(sc, (255, 255, 255), (20, 20, 100, 75))
        #pygame.draw.rect(sc, (64, 128, 255), (150, 20, 100, 75), 8)
        pygame.draw.circle(sc, GREEN, (WIN_WIDTH // 2, WIN_HEIGHT), rTank)

        #----Движение шарика в доль оси х----
        pygame.draw.circle(sc, RED, (x, y), r)
        if (x <= WIN_WIDTH + r):
            x += 4
        else:
            x = 0
            y = random.randint(10, 200)
        # --------
 
        # обновление экрана
        pygame.display.update()
        # задержка
        clock.tick(FPS)


if __name__ == "__main__":
    main()
