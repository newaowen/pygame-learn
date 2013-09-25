#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()
screen_size = (800, 600)
screen = pygame.display.set_mode(screen_size, RESIZABLE, 32)
pygame.display.set_caption("星空")

x, y = 0, 0
move_x, move_y = 0, 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.fill((0, 0, 0))

    num = 800*600/200
    for _ in xrange(num):
        rand_color = (randint(0, 255), randint(0,255), randint(0,255))
        rand_pos = (randint(0,799), randint(0,599))
        screen.set_at(rand_pos, rand_color)

    pygame.display.update()