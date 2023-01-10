import pygame as pg
import os

black = (0, 0, 0)

x = 400
x = float(x)
y = 250
y = float(y)

screen = pg.display.set_mode((800, 600),pg.RESIZABLE)
sprite = pg.image.load("Jupiter.png")

running = True
while running:
    screen.fill(black)
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False
        if event.type == pg.QUIT:
            running = False
    screen.blit(sprite, (x, y))
    pg.display.flip()