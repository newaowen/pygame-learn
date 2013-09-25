#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#fps比较demo

import pygame
from pygame.locals import *
from sys import exit

background_image_filename = 'res/background.png'
mouse_image_filename = 'res/mouse.png'

pygame.init()

screen = pygame.display.set_mode((800, 600), 0, 32)
pygame.display.set_caption("fps比较")

background = pygame.image.load(background_image_filename).convert()
sprite = pygame.image.load('res/kakaxi.png').convert_alpha()

clock = pygame.time.Clock()
x1 = 0
x2 = 0
speed = 200
frame_no = 0
time_passed_sec = 0
factor = 4
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    distance = speed * time_passed_sec

    x1 += distance


    if (frame_no % factor) == 0:
        distance = time_passed_sec * speed
        x2 += distance * factor

    if x1 > 800 :
        x1 -= 800
    if x2 > 800:
        x2 -= 800

    screen.blit(background, (0,0))
    screen.blit(sprite, (x1, 50))
    screen.blit(sprite, (x2, 250))

    frame_no += 1
    pygame.display.update()

    time_passed = clock.tick(30)
    time_passed_sec = time_passed / 1000.0
