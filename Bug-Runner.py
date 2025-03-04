# Ehsan 

# upload game library  
from curses import KEY_LEFT, KEY_RIGHT
import pygame
import time 
import random

# Start game 
pygame.init()

# upload game music 
crash_sound = pygame.mixer.Sound('asset/lose-m.wav')
# pygame.mixer.music.load('asset/05 Without Me.ogg')

# display size 
display_width = 1000 
display_height = 700 

# Colors 
black = (51,0,0)
gray = (200,200,200)
dark_solid = (5,49,67)
red = (255,0,0)
bright_red = (255,64,0)
green = (0,100,0)
bright_green = (0,160,0)
box_color = (255,28,0)

gameDisplay = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption('Bug-Runner')

clock = pygame.time.Clock()

BugImg = pygame.image.load('asset/4.png')

Bug_width = 60 

# butthon start and quit 
def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y :
        pygame.draw.rect(gameDisplay,ac,(x,y,w,h))
        if click[0] == 1 and action != None : 
            if action == 'play' :
                game_loop()
            elif action == 'quit':
                pygame.quit()
                quit()
    else : 
        pygame.draw.rect(gameDisplay,ic,(x,y,w,h))
            
    smallText = pygame.font.Font('freesansbold.ttf', 20)
    TextSurf, TextRect = text_objects(msg, smallText)
    TextRect.center = ((x + (w/2)), (y + (h/2)))
    gameDisplay.blit(TextSurf, TextRect)    

def game_intro():
    intro = True 
    while intro :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(dark_solid)
        largeText = pygame.font.Font('freesansbold.ttf', 70)
        TextSurf , TextRect = text_objects('Wlcome to BugRunner', largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button('Start',250,450,100,50,green,bright_green,'play')
        button('Quit',650,450,100,50,red,bright_red,'quit')

        pygame.display.update()


def stuff_dodged(count):
    font = pygame.font.SysFont(None, 30)
    text = font.render('score : '+str(count), True, gray)
    gameDisplay.blit(text,(5,5))


def stuff(stuffx, stuffy,stuffw,stuffh,color):
    pygame.draw.rect(gameDisplay,color,[stuffx, stuffy, stuffw, stuffh])

def car(x,y):
    gameDisplay.blit(BugImg,(x,y))

def text_objects(text, font):
    textSurface = font.render(text ,True, gray)
    return textSurface, textSurface.get_rect()

# if you crashed this happened
def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 70)
    TextSurf , TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()

    time.sleep(2)
    game_loop()
    
# if you crashed     
def crash():
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)

    largeText = pygame.font.Font('freesansbold.ttf', 70)
    TextSurf , TextRect = text_objects('You Crashed !', largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    while True :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        button('Try again',250,450,100,50,green,bright_green,'play')
        button('Quit',650,450,100,50,red,bright_red,'quit')
        
        pygame.display.update()

def game_loop():
    # Start game music 
    # pygame.mixer.music.play(-1)

    x = (display_width * 0.45)
    y = (display_height * 0.8)
    x_change = 0 
    stuff_startx = random.randrange(0,display_width)
    stuff_starty = -700
    stuff_speed = 7
    stuff_width = 100
    stuff_height = 100
    dodged = 0

    Game_Exit = False

    while not Game_Exit :
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT :
                    x_change = -8 
                elif event.key == pygame.K_RIGHT:
                    x_change = 8    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT: 
                    x_change = 0 

        x += x_change

        gameDisplay.fill(dark_solid)

        # stuffx, stuffy,stuffw,stuffh,color
        stuff(stuff_startx, stuff_starty, stuff_width, stuff_height, box_color)
        stuff_starty += stuff_speed

        stuff_dodged(dodged)

        car(x,y)

        if x > display_width - Bug_width or x < 0 : 
            crash()

        if stuff_starty > display_height:
            stuff_starty = 0 - stuff_height
            stuff_startx = random.randrange(0, display_width)  
            dodged += 1

            if (dodged % 7 == 0):
                stuff_speed += 1
                stuff_width += 10
                stuff_height += 4
                
        if y < stuff_starty + stuff_height :        
            if x > stuff_startx and x < stuff_startx + stuff_width or x + Bug_width > stuff_startx and x + Bug_width < stuff_startx + stuff_width : 
                crash()
        
        pygame.display.update()
        clock.tick(60)
    pygame.display.flip()

game_intro()
game_loop()
pygame.quit()
quit()