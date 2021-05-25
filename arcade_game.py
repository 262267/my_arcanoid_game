import pygame
from pygame.locals import *
import random

# initialize the pygame
pygame.init()
#create the screen
screen = pygame.display.set_mode((800, 600))

#initializing color for rectangle
color = (255,255,255)

# Title and Icon
my_image = pygame.image.load('tło.png')
pygame.display.set_caption("arcade game created by Jakub Muzyka")
icon = pygame.image.load('arcanoid.png')
pygame.display.set_icon(icon)

#arcanoid
arcade_paddleImg = pygame.image.load("arcanoid.png")
arcade_paddleX = 320
arcade_paddleY = 470
change_paddleX = 0

# ball
arcade_ballImg = pygame.image.load("ball1.png")
arcade_ballX = -20
arcade_ballY = 235
change_ballY = 0
change_ballX = 0

# add arcanoid without white places around
def arcanoid(x, y):
    screen.blit(arcade_paddleImg, (x, y))
    colorkey = arcade_paddleImg.get_at((0,0))
    arcade_paddleImg.set_colorkey(colorkey, RLEACCEL)

# add ball without white places around
def arcanoid_ball(x,y):
    screen.blit(arcade_ballImg, (x, y))
    colorkey1 = arcade_ballImg.get_at((0, 0))
    arcade_ballImg.set_colorkey(colorkey1, RLEACCEL)


# Game Loop
running = True
while running:

    # background
    screen.blit(my_image, (0, 0))

    # Drawing Rectangles
    x = 0
    while x < 800:

        pygame.draw.rect(screen, color, pygame.Rect(x, 5, 75, 40))
        pygame.draw.rect(screen, color, pygame.Rect(x, 50, 75, 40))
        pygame.draw.rect(screen, color, pygame.Rect(x, 95, 75, 40))
        pygame.draw.rect(screen, color, pygame.Rect(x, 140, 75, 40))

        x += 80

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # set the movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                change_paddleX = -0.3
            if event.key == pygame.K_RIGHT:
                change_paddleX = 0.3
            if event.key == K_SPACE:
                p = 0.5
                if random.random() < p:
                    change_ballY = 0.4
                    change_ballX = 0.4
                else:
                    change_ballY = 0.4
                    change_ballX = -0.4


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT and event.key == pygame.K_RIGHT:
                change_paddleX = 0

    arcade_paddleX += change_paddleX
    arcade_ballY -= change_ballY
    arcade_ballX += change_ballX

    #set the bounders of map
    if arcade_paddleX <= -30:
        change_paddleX = 0
    elif arcade_paddleX >= 680:
        change_paddleX = 0

    # set the ball X and Y bounders
    if arcade_ballX <= -403:
        change_ballX = 0.3
    elif arcade_ballX >= 370:
        change_ballX =  -0.3
    elif arcade_ballY <= -265:
        change_ballY = -0.3


    arcanoid(arcade_paddleX, arcade_paddleY)
    arcanoid_ball(arcade_ballX, arcade_ballY)
    pygame.display.update()
    pygame.display.flip()
      
