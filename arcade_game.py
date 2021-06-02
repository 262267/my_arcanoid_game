import pygame
from pygame.locals import *
import pygame_menu
import random



def arcade_ball_movement():
    global arcade_ball_speed_x, arcade_ball_speed_y, arcade_paddle_speed_x, score_value, lifes_value, best_value
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
        if abs(arcade_paddle.left - arcade_ball.right) < collision_tolerance:
            arcade_ball_speed_x *= -1
        if abs(arcade_paddle.right - arcade_ball.left) < collision_tolerance:
            arcade_ball_speed_x *= -1

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
        lifes_value -= 1
        if lifes_value == 0:
            pygame.mixer.music.load("end_game.wav")
            pygame.mixer.music.play()
            pygame.mixer.music.rewind()
            if score_value > best_value:
                best_value = score_value

def draw_rectangulars():
    # Drawing Rectangles
    x = 0
    while x < 800:
        global arcade_ball_speed_y, score_value
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
            collision_tolerance = 10
            # ball collision with top rectangular size
            if abs(r4.bottom - arcade_ball.top) < collision_tolerance:
                arcade_ball_speed_y *= -1
                pygame.mixer.music.load("click.wav")
                pygame.mixer.music.play()
                pygame.mixer.music.rewind()
                score_value += 1
            if abs(r4.left - arcade_ball.right) < collision_tolerance:
                arcade_ball_speed_y *= -1
                pygame.mixer.music.load("click.wav")
                pygame.mixer.music.play()
                pygame.mixer.music.rewind()
                score_value += 1
            if abs(r4.right - arcade_ball.left) < collision_tolerance:
                arcade_ball_speed_y *= -1
                pygame.mixer.music.load("click.wav")
                pygame.mixer.music.play()
                pygame.mixer.music.rewind()
                score_value += 1
            if abs(r4.top - arcade_ball.bottom) < collision_tolerance:
                arcade_ball_speed_y *= -1
                pygame.mixer.music.load("click.wav")
                pygame.mixer.music.play()
                pygame.mixer.music.rewind()
                score_value += 1

        # ball collision with bottom rectangular size
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
scoreX = 640
scoreY = 400

def show_score():
    user_score_view = fontObj.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(user_score_view, (scoreX, scoreY))

# life
lifes_value = 3
fontObj1 = pygame.font.SysFont('calibri', 28)
lifeX = 640
lifeY = 430

def show_lifes():
    user_lifes_view = fontObj1.render("Lifes: " + str(lifes_value), True, (255,255,255))
    screen.blit(user_lifes_view, (lifeX, lifeY))

# best score
best_value = 0
bestX = 640
bestY = 460
def best_score():
    user_best_value_view = fontObj1.render("Best score: " + str(best_value), True, (255, 255, 255))
    screen.blit(user_best_value_view, (bestX, bestY))

# end of the game
fontObj2 = pygame.font.SysFont('calibri', 36)
endX = 170
endY = 250
endX1 = 225
endY1 = 290

def game_over():
    global lifes_value, score_value
    if lifes_value == 0:
        end_view = fontObj2.render("Game Over! Your total score: " + str(score_value),
                                   True, (255, 255, 255))
        end_view1 = fontObj2.render("Click SPACE and try again!", True, (255, 255, 255))
        screen.blit(end_view, (endX, endY))
        screen.blit(end_view1, (endX1, endY1))
        score_value = 0
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

# adding music to menu
begin = pygame_menu.sound.Sound()
# begin.set_sound(pygame_menu.sound.SOUND_TYPE_EVENT, "menu_music.wav")
pygame.mixer.music.load("menu_music.wav")
pygame.mixer.music.play(-1)
begin.set_sound(pygame_menu.sound.SOUND_TYPE_WIDGET_SELECTION, "click.wav")

# create a manu for our game
font = pygame_menu.font.FONT_8BIT
font1= pygame_menu.font.FONT_FRANCHISE
mytheme = pygame_menu.themes.Theme(widget_font=font1,
                                   title_font=font1,
                                   background_color=(255, 255, 255, 0), # transparent background
                                   title_background_color=(0, 0, 0, 0),
                                   title_font_shadow=True,
                                   widget_padding=25,
                                   readonly_color=(255,255,255),
                                   title_font_size=60,
                                   widget_font_color = (255,255,255),
                                   widget_font_size=24
                                   )

menu = pygame_menu.Menu(title='welcome to the arcanoid game!',
                        width=600,
                        height=550,
                        theme=mytheme)

menu.set_sound(begin, recursive=True)
myimage = pygame_menu.baseimage.BaseImage(
    image_path= "C:\\Users\\kubam\\OneDrive\\Desktop\\python_game\\tło.png"
)

def main_background():
    myimage.draw(screen)

# create a settings
# def sound_settings(value, enabled):
#     if enabled:
#         menu.set_sound(begin, recursive=True)
#         print("Menu sounds were enabled")
#     else:
#         menu.set_sound(None, recursive=True)
#         print("Menu sounds were disabled")
#
# def sound_effects_settings():
#     pass
settings_menu = pygame_menu.themes.Theme(
                            widget_font=font1,
                            background_color=(255, 255, 255, 0),
                            widget_padding=25,
                            readonly_color=(255,255,255),
                            widget_font_color = (255,255,255),
                            widget_font_size=24,
                            title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_TITLE_ONLY_DIAGONAL,
                            title_background_color=(0,0,0)
                            )

settings = pygame_menu.Menu(height=600,
                            width=800,
                            theme=settings_menu,
                            title='Settings'
                            )
settings.add.toggle_switch(title='Sound:',
                           default=True,
                           # onchange=sound_settings
                           )
settings.add.toggle_switch('Sound effects:',
                           True,
                           # onchange=sound_effects_settings
                           )
def add_settings():
    settings.add.vertical_margin(50)
    settings.add.button(
        'Return to main menu',
        pygame_menu.events.BACK,
        align=pygame_menu.locals.ALIGN_CENTER,
    )

# create a Author button
author_button = pygame_menu.themes.Theme(
                            widget_font=font1,
                            background_color=(255, 255, 255, 0),
                            widget_padding=25,
                            readonly_color=(255,255,255),
                            widget_font_color = (255,255,255,0),
                            widget_font_size=34,
                            title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_TITLE_ONLY_DIAGONAL,
                            title_background_color=(0,0,0)
                            )

author = pygame_menu.Menu(height=600,
                          width=800,
                          theme=author_button,
                          title='Author',
                          )

author.add.vertical_margin(1)
author.add.label('Introduction:',
                 align=pygame_menu.locals.ALIGN_LEFT,
                 font_name=pygame_menu.font.FONT_OPEN_SANS_BOLD,
                 font_size=44
                 )

info = ('Witam wszystkich czytających tę wiadomość! Znajdujemy się w grze, '
        'stworzonej przeze mnie, czyli Jakuba Muzykę. Została ona stworzona na '
        'potrzebę zaliczenia przedmiotu o nazwie "Programowanie". Po wszelkie '
        'wskazówki, dotyczące sterowania oraz resztę rzeczy, zapraszam do sekcji'
        '"Instruction", gdzie dokładnie omówię zasady. Mam nadzieje, że spędzicie miło czas,'
        ' grając w moją grę, pozdrawiam! :)')

author_info = author.add.label(info,
                               max_char=50,
                               align=pygame_menu.locals.ALIGN_CENTER,
                               margin=(29, 1),
                               font_size=28,
                               font_name=pygame_menu.font.FONT_OPEN_SANS_BOLD,
                               font_color=(255, 255, 255),
                               padding=0
                               )

image_path = pygame_menu.baseimage.BaseImage(
    image_path= "C:\\Users\\kubam\\OneDrive\\Pictures\\Camera Roll\\ja1.png"
)
author.add_image(image_path,
                 align=pygame_menu.locals.ALIGN_CENTER,
                 border_inflate=(383,250)
                 )

for line in author_info:
    line.set_max_width(400)

# create instruction button
instruction_button = pygame_menu.themes.Theme(
                            widget_font=font1,
                            background_color=(0, 0, 0, 0),
                            widget_padding=25,
                            readonly_color=(255,255,255),
                            widget_font_color = (255,255,255),
                            widget_font_size=24,
                            title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_TITLE_ONLY_DIAGONAL,
                            title_background_color=(0,0,0)
                            )

instruction = pygame_menu.Menu(height=600,
                        width=800,
                        theme=instruction_button,
                        title='Instruction'
                        )

instruction.add.vertical_margin(1)
instruction.add.label('How to play?',
                 align=pygame_menu.locals.ALIGN_LEFT,
                 font_name=pygame_menu.font.FONT_OPEN_SANS_BOLD,
                 font_size=44
                 )
how_to_play = ('Gra polega na zbijaniu bloczków, które znikają i dają po 1 punkcie. Masz 3 życia. Nie da się '
               'wygrać - walczysz z samym sobą o najlepszy rezultat. Poruszasz się strzałkami (LEFT, RIGHT),'
               ' a piłkę wyrzucasz spacją (SPACE). Po dotarciu do górnej części ekranu te wracają'
               ' do postaci początkowej, wtedy prędkość piłki się zwiększa, a długość naszej paletki do odbijania się'
               'zmniejsza. Przegrywasz, gdy stracisz wszystkie życia. Są 3 poziomy trudności do wyboru: easy,'
               'medium, hard. W każadym z tych poziomów prędkość piłeczki oraz naszej paletki '
               'zwiększa się/zmniejsza się.\n'
               'Powodzenia!')

instruction_info = instruction.add.label(how_to_play,
                               max_char=45,
                               align=pygame_menu.locals.ALIGN_CENTER,
                               margin=(29, 1),
                               font_size=24,
                               font_name=pygame_menu.font.FONT_OPEN_SANS_BOLD,
                               font_color=(255, 255, 255),
                               padding=0
                               )

DIFFICULTY = ['EASY']
def set_difficulty(value, difficulty):
    selected,index = value
    DIFFICULTY[0] = difficulty


def start_the_game(difficulty):
    global arcade_paddle_speed_x, arcade_ball_speed_y, arcade_ball_speed_x, score_value, best_value,\
        lifes_value, arcade_paddle
    # Game Loop
    running = True
    while running:

        # background
        screen.blit(my_image, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            # set the movement

            difficulty = difficulty[0]
            if difficulty == 'EASY':
                arcade_paddle = pygame.Rect(355, 530, 130, 10)
            elif difficulty == 'MEDIUM':
                arcade_paddle = pygame.Rect(355, 530, 100, 10)
            elif difficulty == 'HARD':
                arcade_paddle = pygame.Rect(355, 530, 80, 10)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    arcade_paddle_speed_x -= 3
                if event.key == pygame.K_RIGHT:
                    arcade_paddle_speed_x += 3
                if event.key == K_SPACE:
                    p = 0.5
                    if random.random() < p:
                        arcade_ball_speed_x += 5
                        arcade_ball_speed_y += 5
                    else:
                        arcade_ball_speed_x -= 5
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
        best_score()
        game_over()
        arcade_paddle.x += arcade_paddle_speed_x
        pygame.draw.ellipse(screen, color2, arcade_ball)
        pygame.draw.rect(screen, color, arcade_paddle)
        pygame.display.update()
        pygame.display.flip()
        clock.tick(60)

menu.add.selector('Difficulty :', [('Easy', 'EASY'),
                                  ('Medium', 'MEDIUM'),
                                  ('Hard', 'HARD')],
                  onchange=set_difficulty
                  )
menu.add.button('Play', start_the_game, DIFFICULTY)
menu.add.button('Instruction', instruction)
menu.add.button('Author', author)
menu.add.button('Settings', settings)
menu.add.button('Quit', pygame_menu.events.EXIT)
menu.mainloop(screen, main_background)
