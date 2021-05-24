import pygame



# initialize the pygame
pygame.init()
#create the screen
screen = pygame.display.set_mode((800, 600))

# Title and Icon
my_image = pygame.image.load('tło.png')
pygame.display.set_caption("arcade game created by Jakub Muzyka")
icon = pygame.image.load('arcanoid.png')
pygame.display.set_icon(icon)


# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # screen color
    sc_height = 800
    sc_width = 600
    screen.blit(my_image, (0,0))
    pygame.display.update()