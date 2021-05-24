import pygame
from pygame.locals import *


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

# add arcanoid without white places around
def arcade(x, y):
    screen.blit(arcade_paddleImg, (x, y))
    colorkey = arcade_paddleImg.get_at((0,0))
    arcade_paddleImg.set_colorkey(colorkey, RLEACCEL)
    
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
                change_paddleX = -0.2
            if event.key == pygame.K_RIGHT:
                change_paddleX = 0.2

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT and event.key == pygame.K_RIGHT:
                change_paddleX = 0

    arcade_paddleX += change_paddleX
    
   #set the bounders of map
    if arcade_paddleX <= -30:
        change_paddleX = 0
    elif arcade_paddleX >= 680:
        change_paddleX = 0


    arcade(arcade_paddleX, arcade_paddleY)
    pygame.display.update()
    pygame.display.flip()
      
