import pygame as pg

pg.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

object = pg.Rect(300, 250, 50, 50)

# game loop
run = True
while run:

    #EVENT HANDLER

    key = pg.key.get_pressed()
    if key[pg.K_a] == True:
        object.x = max(0, object.x - 1)
    elif key[pg.K_d] == True:
        object.x = min(SCREEN_WIDTH - object.width, object.x + 1)
    elif key[pg.K_w] == True:
        object.y = max(0, object.y - 1)
    elif key[pg.K_s] == True:
        object.y = min(SCREEN_HEIGHT - object.height, object.y + 1)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    
    screen.fill((0, 0, 0)) # fill screen with black

    pg.draw.rect(screen, (255, 0, 0), object) # draw rectangle

    pg.draw.line(screen, (255, 255, 255), (0, 0), (SCREEN_WIDTH, SCREEN_HEIGHT)) # draw line

    pg.display.update() # update screen

pg.quit()
