# здесь подключаются модули
import pygame
import random
from pygame.locals import *
import sys
import math

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
    BLUE = (0, 0, 255)
    x2 = 10
    y2 = 50
    r = 10
    #Переменные танка
    rTank = 30
    angle = -1.5
    Speed = 1
    x = WIN_WIDTH // 2 
    y = WIN_HEIGHT - 70
    L_D = True
    R_D = False
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
        '''try:
            k = (WIN_HEIGHT - y2) // (WIN_WIDTH // 2 - x2)
            #b = y2 - k*x2
        except ZeroDivisionError as e:
            print("Error! " + str(e))
        '''
        
        pygame.draw.circle(sc, GREEN, (WIN_WIDTH // 2, WIN_HEIGHT), rTank)
        pygame.draw.line(sc, GREEN, [WIN_WIDTH // 2, WIN_HEIGHT], [x, y], 3)
        #pygame.draw.circle(sc, GREEN, (x, y), 2)
        x = int(math.cos(angle) * 70) + WIN_WIDTH // 2
        y = int(math.sin(angle) * 70) + WIN_HEIGHT
        print(angle)

        #348 202
        if (angle >= -3) and (L_D == True):
            angle -= 0.02
        else:
            L_D = False
            R_D = True
        if (angle <= -0.2) and (R_D == True):
            angle += 0.02
        else:
            L_D = True
            R_D = False
        

        
        #pygame.draw.line(sc, GREEN, [WIN_WIDTH // 2, WIN_HEIGHT], [WIN_WIDTH // 2 -angle, WIN_HEIGHT-45], 3)
        
        
        #if (int(k) != 0) or (int(b) != 0):
         #   pygame.draw.circle(sc, BLUE, (b, WIN_HEIGHT), 5)





        #----Движение вражеского обьекта в доль оси х и случайное появление в доль оси y----
        pygame.draw.circle(sc, RED, (x2, y2), r)
        if (x2 <= WIN_WIDTH + r):
            x2 += Speed
        else:
            Speed = random.randint(1, 4)
            x2 = 10
            y2 = random.randint(10, 200)
        # --------
 
        # обновление экрана
        pygame.display.update()
        # задержка
        clock.tick(FPS)


if __name__ == "__main__":
    main()
