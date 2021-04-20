import pygame as pg
import numpy as np
import math
import os
import random
import pygame_widgets as pgw

os.chdir("C:\\Users\\guilh\\Google Drive\\Cursos Online\\Projetos Python\\Aproximando PI")

os.environ['SDL_VIDEO_CENTERED'] = '1'

pg.init()
width, height = 800, 600
fps = 60
pg.display.set_caption("Aproximando PI")
screen = pg.display.set_mode((width, height))
clock = pg.time.Clock()

time = 0

xo = 50
yo = 50

size = 400

center = ((size/2)+xo,(size/2)+yo)

#cores
white = (255, 255, 255)
gray = (150, 150, 150)
black = (0, 0, 0)
crimson = (230, 20, 32)
green = (0, 128, 0)


textbox_pi = pgw.TextBox(screen, size + 100, 100, 200, 50, fontSize=20,
                  borderColour=(255, 0, 0), textColour=(0, 200, 0),
                  radius=10, borderThickness=5)
textbox_in = pgw.TextBox(screen, size + 100, 200, 200, 50, fontSize=20,
                  borderColour=(255, 0, 0), textColour=(0, 200, 0),
                  radius=10, borderThickness=5)
textbox_out = pgw.TextBox(screen, size + 100, 300, 200, 50, fontSize=20,
                  borderColour=(255, 0, 0), textColour=(0, 200, 0),
                  radius=10, borderThickness=5)

run = True

points = []
points_in = []
while run:
    clock.tick(fps)
    screen.fill(white)
    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            run = False    
    
    pg.draw.circle(screen, black, center, size/2, 1)
    pg.draw.polygon(screen, black, points=[(xo, yo), (xo, yo + size), (xo + size, yo + size), (xo + size, yo)], width=1)
    
    point = (random.randint(xo, xo+size), random.randint(yo, yo+size))
    if point not in points:
        points.append(point)
        d = math.sqrt((point[0] - center[0])**2 + (point[1] - center[1])**2)
        if d <= size/2:
            points_in.append(point)
    
    for p in points:
        d = math.sqrt((p[0] - center[0])**2 + (p[1] - center[1])**2)
        if d > size/2:
            pg.draw.circle(screen, green, p, 2)
        else:
            pg.draw.circle(screen, crimson, p, 2)
    
    if (len(points_in) > 0):
        pi = 4*len(points_in)/len(points)
        
    textbox_pi.listen(events)
    textbox_pi.setText("Pi aproximado: " + str(pi))
    textbox_pi.draw()
    
    textbox_in.listen(events)
    textbox_in.setText("len_in: " + str(len(points_in)))
    textbox_in.draw()
    
    textbox_out.listen(events)
    textbox_out.setText("len_out: " + str(len(points)))
    textbox_out.draw()
    
    pg.display.update()

pg.quit()