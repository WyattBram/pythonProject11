import random

import pygame, sys
from pygame.locals import *

resolution = (400,400)

pygame.init()
clock = pygame.time.Clock()

disp = pygame.display.set_mode(resolution)

pos = True
i=0
while True:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit(0)
        elif keys[pygame.K_ESCAPE]:
            sys.exit(0)


    if pos:
        disp.fill((i,i,i))
        i+=1
    else:
        i -= 1
        disp.fill((i, i, i))

    if i == 255: pos = False
    if i == 0: pos = True

    clock.tick(30)
    pygame.display.flip()
