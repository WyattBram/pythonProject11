import random

import pygame, sys
from pygame.locals import *

pygame.init()

iFuckingHatePyGame = 1

resolution = ((800,800))
screen = pygame.display.set_mode(resolution)

clock = pygame.time.Clock()

playerRect = pygame.Rect(380,380, 40,40)
playerSurf = pygame.Surface((40,40))
playerSurf.fill((200,200,200))
pygame.font.init()

myFont = pygame.font.SysFont('Comic Sans Ms', 30)

def createMetor(size, speed, x, y, dir):
    metRect = pygame.Rect(x, y, size, size)
    metSurf = pygame.Surface((size, size))
    metSurf.fill((random.randint(50,256),random.randint(50,256),random.randint(50,256)))
    return [metRect, metSurf, speed, dir]


fon = pygame.font.SysFont('Arial', 12)
def draw(text, text_col, x, y):
    img = fon.render(text, True, text_col)
    screen.blit(img, (x,y))




metR = []
metS = []
metSpeed = []
dir = []
timeCheck = 1

allowed = 2000
total = 0
flag = True
i = 0
while True:


    screen.fill(color=(0,0,0))

    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit(0)
        if keys[pygame.K_ESCAPE]:
            sys.exit(0)
        if keys[pygame.K_w]:
            if not playerRect.y ==0:
                playerRect = playerRect.move(0,-5)
        if keys[pygame.K_a]:
            if not playerRect.x == 0:
                playerRect = playerRect.move(-5,0)
        if keys[pygame.K_s]:
            if not playerRect.y ==800:
                playerRect = playerRect.move(0,5)
        if keys[pygame.K_d]:
            if not playerRect.x ==-800:
                playerRect = playerRect.move(5, 0)


    if pygame.time.get_ticks() // 1000 == timeCheck:
        timeCheck+=1


    draw(str(timeCheck), (255, 255, 255), 50, 50)


    if timeCheck % 5 == 0 and flag:
        rint = random.randint(1,4)
        print(rint)
        match rint:

            case 1:
                lst = createMetor(random.randint(20, 60), iFuckingHatePyGame, random.randint(0, 760), -40, 'y')
            case 2:
                lst = createMetor(random.randint(20, 60), -1 * iFuckingHatePyGame,  random.randint(0, 760), 800, 'y')
            case 3:
                lst = createMetor(random.randint(20, 60), iFuckingHatePyGame, -40, random.randint(0, 760), 'x')
            case 4:
                lst = createMetor(random.randint(20, 60), -1 * iFuckingHatePyGame, 800, random.randint(0, 760), 'x')

        metR.append(lst[0])
        metS.append(lst[1])
        metSpeed.append(lst[2])
        dir.append(lst[3])
        flag = False
        iFuckingHatePyGame += .5

    if timeCheck % 5 != 0:
        flag = True

    for i in range(len(metR)):

        if dir[i] == 'y':
            metR[i] = metR[i].move(0, metSpeed[i])
        if dir[i] == 'x':
            metR[i] = metR[i].move(metSpeed[i], 0)
        screen.blit(metS[i], metR[i].topleft)
        if metR[i].colliderect(playerRect):
            sys.exit(0)



    screen.blit(playerSurf, playerRect.topleft)




    pygame.display.flip()
    clock.tick(60)

