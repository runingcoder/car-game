import pygame
import time
import sys
import itertools
import math
from pygame import mixer
import random
pygame.init()
gray=(119,118,110)
black=(0,0,0)
red=(255,0,0)
green=(0,200,0)
blue=(0,0,200)
bright_red=(255,0,0)
bright_green=(0,255,0)
bright_blue=(0,0,255)
backgroundpic= pygame.image.load("background.jpg")
instruction_background= pygame.image.load("background2.jpg")
display_width=800
display_height=600


screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Car game")
clock = pygame.time.Clock()
care = pygame.image.load('carer.png')
background = pygame.image.load('backk.jpg')

backgroundpic=pygame.image.load("download12.jpg")
yellow_strip=pygame.image.load("yellow strip.jpg")
strip=pygame.image.load("strip.jpg")

def car(x, y):
    screen.blit(care, (x, y))


def background():
    screen.blit(backgroundpic,(0,0))
    screen.blit(backgroundpic,(0,200))
    screen.blit(backgroundpic,(0,400))
    screen.blit(backgroundpic,(700,0))
    screen.blit(backgroundpic,(700,200))
    screen.blit(backgroundpic,(700,400))
    screen.blit(yellow_strip,(400,0))
    screen.blit(yellow_strip,(400,100))
    screen.blit(yellow_strip,(400,200))
    screen.blit(yellow_strip,(400,300))
    screen.blit(yellow_strip,(400,400))
    screen.blit(yellow_strip,(400,500))
    screen.blit(strip,(120,0))
    screen.blit(strip,(120,100))
    screen.blit(strip,(120,200))
    screen.blit(strip,(680,0))
    screen.blit(strip,(680,100))
    screen.blit(strip,(680,200))
over_font = pygame.font.Font("dak.otf", 128)

def crash():

     over_text = over_font.render("You crashed", True, (0, 0, 0))

     screen.blit(over_text, (200, 250))
     pygame.display.update()
     time.sleep(3)
     intro_loop()

def collide(m,n):
    distance = math.sqrt((math.pow(m - n, 2)))
    if distance < 150:
        return True
    else:
        return False


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))
enemyImg = []
enemyX = []
enemyY = [0,0,0,0,0,0]
enemyY_change = []
noe = 5
for i in range(noe):
    if i==0:
        enemyImg.append(pygame.image.load('car1.jpg'))
    if i==1:
        enemyImg.append(pygame.image.load('car2.jpg'))
    if i==2:
        enemyImg.append(pygame.image.load('car7.jpg'))
    if i==3:
        enemyImg.append(pygame.image.load('car4.jpg'))
    if i==4:
        enemyImg.append(pygame.image.load('car5.jpg'))
    if i == 5:
        enemyImg.append(pygame.image.load('car6.jpg'))


    enemyX.append(random.randint(119, 649))
    for m,n in itertools.combinations(enemyX,2):
        if collide(m,n):
            break
        enemyX.append(random.randint(119, 649))

    enemyY_change.append(i+2)
print(enemyX)

def score_systerm(passs, score):
    font=pygame.font.SysFont(None, 25,italic=True)
    text=font.render("Passed :" + str(passs), True, black)
    score=font.render("Score :" + str(score), True, green)
    screen.blit(text,(0,50))
    screen.blit(score,(0, 30))

def text_objects(text,font):
    textsurface=font.render(text,True,black)
    return textsurface,textsurface.get_rect()

def iscollision(enemyX, enemyY, x, y):
    distance = math.sqrt((math.pow(enemyX - x, 2)) + (math.pow(enemyY - y, 2)))
    if distance < 40:
        return True
    else:
        return False
def intro_loop():
    intro= True
    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        screen.blit(instruction_background,(0,0))
        largetext = pygame.font.Font('freesansbold.ttf', 90)
        TextSurf, TextRect = text_objects("Flying CAR GAME", largetext)
        TextRect.center = (400, 100)
        screen.blit(TextSurf, TextRect)
        button("START", 150, 520, 100, 50, green, bright_green, "play")
        button("QUIT", 550, 520, 100, 50, red, bright_red, "quit")
        button("INSTRUCTION", 300, 520, 200, 50, blue, bright_blue, "intro")
        pygame.display.update()
        clock.tick(50)


def button(msg,x,y,w,h,ic,ac,action=None):
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if x+w>mouse[0]>x and y+h>mouse[1]>y:
        pygame.draw.rect(screen,ac,(x,y,w,h))
        if click[0]==1 and action!=None:
            if action=="play":
                countdown()
            elif action=="quit":
                pygame.quit()
                quit()
                sys.exit()
            elif action=="intro":
                introduction()
            elif action=="menu":
                intro_loop()
            elif action=="pause":
                paused()
            elif action=="unpause":
                unpaused()


    else:
        pygame.draw.rect(screen,ic,(x,y,w,h))
    smalltext=pygame.font.Font("freesansbold.ttf",20)
    textsurf,textrect=text_objects(msg,smalltext)
    textrect.center=((x+(w/2)),(y+(h/2)))
    screen.blit(textsurf,textrect)



def introduction():
    introduction=True
    while introduction:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        screen.blit(instruction_background,(0,0))
        largetext=pygame.font.Font('freesansbold.ttf',80)
        smalltext=pygame.font.Font('freesansbold.ttf',20)
        mediumtext=pygame.font.Font('freesansbold.ttf',40)
        textSurf,textRect=text_objects("This is an car game in which you need dodge the coming cars",smalltext)
        textRect.center=((350),(200))
        TextSurf,TextRect=text_objects("INSTRUCTION",largetext)
        TextRect.center=((400),(100))
        screen.blit(TextSurf,TextRect)
        screen.blit(textSurf,textRect)
        stextSurf,stextRect=text_objects("ARROW LEFT : LEFT TURN",smalltext)
        stextRect.center=((150),(400))
        hTextSurf,hTextRect=text_objects("ARROW RIGHT : RIGHT TURN" ,smalltext)
        hTextRect.center=((150),(450))
        sTextSurf,sTextRect=text_objects("CONTROLS",mediumtext)
        sTextRect.center=((350),(300))
        screen.blit(sTextSurf,sTextRect)
        screen.blit(stextSurf,stextRect)
        screen.blit(hTextSurf,hTextRect)

        button("BACK",600,450,100,50,blue,bright_blue,"menu")
        pygame.display.update()
        clock.tick(30)

def paused():
    global pause

    while pause:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
                    sys.exit()
            screen.blit(instruction_background,(0,0))
            largetext=pygame.font.Font('freesansbold.ttf',115)
            TextSurf,TextRect=text_objects("PAUSED",largetext)
            TextRect.center=((display_width/2),(display_height/2))
            screen.blit(TextSurf,TextRect)
            button("CONTINUE",150,450,150,50,green,bright_green,"unpause")
            button("RESTART",350,450,150,50,blue,bright_blue,"play")
            button("MAIN MENU",550,450,200,50,red,bright_red,"menu")
            pygame.display.update()
            clock.tick(30)

def unpaused():
    global pause
    pause=False


def countdown_background():
    font=pygame.font.SysFont(None,25)
    x=(display_width*0.45)
    y=(display_height*0.8)
    screen.blit(backgroundpic,(0,0))
    screen.blit(backgroundpic,(0,200))
    screen.blit(backgroundpic,(0,400))
    screen.blit(backgroundpic,(700,0))
    screen.blit(backgroundpic,(700,200))
    screen.blit(backgroundpic,(700,400))
    screen.blit(yellow_strip,(400,100))
    screen.blit(yellow_strip,(400,200))
    screen.blit(yellow_strip,(400,300))
    screen.blit(yellow_strip,(400,400))
    screen.blit(yellow_strip,(400,100))
    screen.blit(yellow_strip,(400,500))
    screen.blit(yellow_strip,(400,0))
    screen.blit(yellow_strip,(400,600))
    screen.blit(strip,(120,200))
    screen.blit(strip,(120,0))
    screen.blit(strip,(120,100))
    screen.blit(strip,(680,100))
    screen.blit(strip,(680,0))
    screen.blit(strip,(680,200))
    screen.blit(care,(x,y))
    text=font.render("DODGED: 0",True, black)
    score=font.render("SCORE: 0",True,red)
    screen.blit(text,(0,50))
    screen.blit(score,(0,30))
    button("PAUSE",650,0,150,50,blue,bright_blue,"pause")

def countdown():
    countdown=True

    while countdown:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
                    sys.exit()
            screen.fill(gray)
            countdown_background()
            largetext=pygame.font.Font('freesansbold.ttf',115)
            TextSurf,TextRect=text_objects("3",largetext)
            TextRect.center=((display_width/2),(display_height/2))
            screen.blit(TextSurf,TextRect)
            pygame.display.update()
            clock.tick(1)
            screen.fill(gray)
            countdown_background()
            largetext=pygame.font.Font('freesansbold.ttf',115)
            TextSurf,TextRect=text_objects("2",largetext)
            TextRect.center=((display_width/2),(display_height/2))
            screen.blit(TextSurf,TextRect)
            pygame.display.update()
            clock.tick(1)
            screen.fill(gray)
            countdown_background()
            largetext=pygame.font.Font('freesansbold.ttf',115)
            TextSurf,TextRect=text_objects("1",largetext)
            TextRect.center=((display_width/2),(display_height/2))
            screen.blit(TextSurf,TextRect)
            pygame.display.update()
            clock.tick(1)
            screen.fill(gray)
            countdown_background()
            largetext=pygame.font.Font('freesansbold.ttf',115)
            TextSurf,TextRect=text_objects("GO!!!",largetext)
            TextRect.center=((display_width/2),(display_height/2))
            screen.blit(TextSurf,TextRect)
            pygame.display.update()
            clock.tick(1)
            game_loop()




def game_loop():

    x = 370
    y = 540
    x_change = 0
    y_change =0
    passs=0
    score=0
    henry = True
    while henry:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                henry = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            if event.key == pygame.K_RIGHT:
                x_change = 5
            if event.key == pygame.K_UP:
                y_change = -2

            if event.key == pygame.K_DOWN:
                y_change = +2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                x_change = 0
                y_change=0
        x+=x_change
        y+=y_change

        screen.fill((10, 24, 45))

        background()
        car(x,y)
        score_systerm(passs, score)

        if x>650:
            crash()
        if x<120:
            crash()
        if y > 500:
            y= 500

        for i in range(noe):
            enemyY[i] += enemyY_change[i]



            # collision detection
            collision = iscollision(enemyX[i], enemyY[i], x, y)
            if collision:
                collision_sound = mixer.Sound("explosion.wav")
                collision_sound.play()

                crash()

            enemy(enemyX[i], enemyY[i], i)
            if enemyY[i] > 600:
                enemyX[i] = random.randint(119, 649)
                enemyY[i] = 0
                score+=10
                passs=score/10



        pygame.display.update()
        clock.tick(60)


intro_loop()
game_loop()
pygame.quit()
quit()
