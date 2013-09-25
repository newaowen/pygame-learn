#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import pygame
from pygame.locals import *
from sys import exit

pygame.init()
screen_size = (800, 600)
screen = pygame.display.set_mode(screen_size, RESIZABLE, 32)
pygame.display.set_caption("move")

bg_image_filename = 'res/kakaxi.png'
background = pygame.image.load(bg_image_filename).convert_alpha()

x, y = 0, 0
move_x, move_y = 0, 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            print "key down"
            if event.key == K_LEFT:
                move_x = -1
            elif event.key == K_RIGHT:
                move_x = 1
            elif event.key == K_UP:
                move_y = -1
            elif event.key == K_DOWN:
                move_y = 1
        elif event.type == KEYUP:
            if event.key == K_LEFT:
                move_x = 0
            elif event.key == K_RIGHT:
                move_x = 0
            elif event.key == K_UP:
                move_y = 0
            elif event.key == K_DOWN:
                move_y = 0

    x += move_x
    y += move_y


    screen.fill((0, 0, 0))
    screen.blit(background, (x, y))

    pygame.display.update()