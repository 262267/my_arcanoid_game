import pygame
from pygame.locals import *

def arcade_ball_movement():
    global arcade_ball_speed_x, arcade_ball_speed_y, arcade_paddle_speed_x, score_value, lifes_value
    arcade_ball.y -= arcade_ball_speed_y
    arcade_ball.x -= arcade_ball_speed_x

    if arcade_ball.top <= 0:
        arcade_ball_speed_y *= -1
    if arcade_ball.left <= 0 or arcade_ball.right >= screen_width:
        arcade_ball_speed_x *= -1

    # collision - ball with paddle
    collision_tolerance = 10
    if arcade_ball.colliderect(arcade_paddle):
        if abs(arcade_paddle.top - arcade_ball.bottom) < collision_tolerance:
            arcade_ball_speed_y *= -1


    # bounders
    if arcade_paddle.left <= 0:
        arcade_paddle.left = 0
    if arcade_paddle.right >= screen_width:
        arcade_paddle.right = screen_width
    if arcade_ball.bottom >= screen_height:
        arcade_ball_speed_x = 0
        arcade_ball_speed_y = 0
        arcade_ball.x = arcade_paddle.x + 25
        arcade_ball.y = arcade_paddle.y - 30
        pygame.mixer.music.load("roblox.mp3")
        pygame.mixer.music.play()
        pygame.mixer.music.rewind()
        score_value = 0
        lifes_value -= 1


def draw_rectangulars():
    # Drawing Rectangles
    x = 0
    while x < 800:
        global arcade_ball_speed_y, user_points, score_value
        pygame.draw.rect(screen, color, pygame.Rect(x, 5, 75, 40))
        pygame.draw.rect(screen, color, pygame.Rect(x, 50, 75, 40))
        pygame.draw.rect(screen, color, pygame.Rect(x, 95, 75, 40))
        pygame.draw.rect(screen, color, pygame.Rect(x, 140, 75, 40))

        # colision - ball with block
        r1 = pygame.Rect(x, 5, 75, 40)
        r2 = pygame.Rect(x, 50, 75, 40)
        r3 = pygame.Rect(x, 95, 75, 40)
        r4 = pygame.Rect(x, 140, 75, 40)
        if arcade_ball.colliderect(r4):
            # ball collision with top rectangular size
            if arcade_ball.top >= r4.top:
                arcade_ball_speed_y *= -1
                pygame.mixer.music.load("click.wav")
                pygame.mixer.music.play()
                pygame.mixer.music.rewind()
                score_value += 1
            if arcade_ball.top >= r4.left:
                arcade_ball_speed_y *= -1
                pygame.mixer.music.load("click.wav")
                pygame.mixer.music.play()
                pygame.mixer.music.rewind()
            if arcade_ball.top >= r4.right:
                arcade_ball_speed_y *= -1
                pygame.mixer.music.load("click.wav")
                pygame.mixer.music.play()
                pygame.mixer.music.rewind()
            #ball collision with bottom rectangular size
            if arcade_ball.top >= r4.bottom:
                arcade_ball_speed_y *= -1
                pygame.mixer.music.load("click.wav")
                pygame.mixer.music.play()
                pygame.mixer.music.rewind()
        if arcade_ball.colliderect(r3):
            if arcade_ball.top >= r3.top:
                arcade_ball_speed_y *= -1
                pygame.mixer.music.load("click.wav")
                pygame.mixer.music.play()
                pygame.mixer.music.rewind()
        if arcade_ball.colliderect(r2):
            if arcade_ball.top >= r2.top:
                arcade_ball_speed_y *= -1
                pygame.mixer.music.load("click.wav")
                pygame.mixer.music.play()
                pygame.mixer.music.rewind()
        if arcade_ball.colliderect(r1):
            if arcade_ball.top >= r1.top:
                arcade_ball_speed_y *= -1
                pygame.mixer.music.load("click.wav")
                pygame.mixer.music.play()
                pygame.mixer.music.rewind()


        x += 80

# score
pygame.font.init()
score_value = 0
fontObj = pygame.font.SysFont('calibri', 28)
scoreX = 620
scoreY = 400

def show_score():
    user_score_view = fontObj.render("Total score: " + str(score_value), True, (255, 255, 255))
    screen.blit(user_score_view, (scoreX,scoreY))

# life
lifes_value = 3
fontObj1 = pygame.font.SysFont('calibri', 28)
lifeX = 620
lifeY = 430

def show_lifes():
    user_lifes_view = fontObj1.render("Total lifes: " + str(lifes_value), True, (255,255,255))
    screen.blit(user_lifes_view, (lifeX, lifeY))

# end of the game
fontObj2 = pygame.font.SysFont('calibri', 36)
endX = 170
endY = 300

def game_over():
    global lifes_value, user_value
    if lifes_value == 0:
        if event.type == pygame.KEYUP:
            end_view = fontObj2.render("Game Over! Click SPACE try again!", True, (255, 255, 255))
            screen.blit(end_view, (endX, endY))
            if event.key == K_SPACE:
                user_value = 0
                lifes_value = 3


# initialize the pygame
pygame.init()
clock = pygame.time.Clock()
#create the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
#initializing color for rectangle
color = (255,0,255)
color2 = (255,255,255)
color1 = (255,0,0)

# Title and Icon
my_image = pygame.image.load('tło.png')
pygame.display.set_caption("arcade game created by Jakub Muzyka")
icon = pygame.image.load('arcanoid.png')
pygame.display.set_icon(icon)

#arcanoid
arcade_paddle = pygame.Rect(355,530, 80, 10)
arcade_paddle_speed_x = 0

# ball
arcade_ball = pygame.Rect(380,495,30,30)
arcade_ball_speed_x = 0
arcade_ball_speed_y = 0

# Game Loop
running = True
while running:

    # background
    screen.blit(my_image, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # set the movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                arcade_paddle_speed_x -= 3
            if event.key == pygame.K_RIGHT:
                arcade_paddle_speed_x += 3
            if event.key == K_SPACE:
                arcade_ball_speed_x += 5
                arcade_ball_speed_y += 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                arcade_paddle_speed_x += 3
            if event.key == pygame.K_RIGHT:
                arcade_paddle_speed_x -= 3

    arcade_ball_movement()
    draw_rectangulars()
    show_score()
    show_lifes()
    game_over()
    arcade_paddle.x += arcade_paddle_speed_x
    pygame.draw.ellipse(screen, color2, arcade_ball)
    pygame.draw.rect(screen, color, arcade_paddle)
    pygame.display.update()
    pygame.display.flip()
    clock.tick(60)

