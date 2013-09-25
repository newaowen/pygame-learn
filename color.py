#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = 'zhanqu'

def scale_color(color, scale):
    reg, green, blue = color
    red = int(red*scale)
    green = int(green*scale)
    blue = int(blue*scale)
    return red,green, blue

#颜色范围限制
def saturate_color(color):
    r, g, b = color
    r = min(r, 255)
    g = min(g, 255)
    b = min(b, 255)
    return r, g, b

#颜色插值
def blend_color(color1, color2, factor):
    r1, g1, b1 = color1
    r2, g2, b2 = color2

    if r2 < r1:
        r1, r2 = r2, r1
    if g2 < g1:
        g1, g2 = g2, g1
    if b2 < b1:
        b1, b2 = b2, b1

    r =  r1 + (r2 - r1) * factor
    g = g1 + (g2 - g1) * factor
    b = b1 + (b2 - b1) * factor
    return int(r), int(g), int(b)