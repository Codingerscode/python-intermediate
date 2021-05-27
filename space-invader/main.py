import pygame
import random
import math

# intializing the pygame
pygame.init()

# creation of screen
screen = pygame.display.set_mode((800, 600))

#background
background = pygame.image.load("background.png")


#title and Icon
pygame.display.set_caption("Space Invadors")
icon = pygame.image.load("spaceship.png")
pygame.display.set_icon(icon)

# player image
playerImg = pygame.image.load("space-invaders.png")
X = 370
Y = 480
playerex = 0
playery = 10

# Enemy image
enemyImg = []
eX = []
eY = [] 
enemyx = []
enemyy = []
num_of_enemies = 6 

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load("ghost.png"))
    eX.append(random.randint(64,735))
    eY.append(random.randint(50,150))
    enemyx.append(0.2)
    enemyy.append(0)


#bullet img
bulletImg = pygame.image.load("bullet.png")
bulletx = 0
bullety = 480
bulletchangeX = 0
bulletchangeY = 1

bulletstate = "ready"
score = 0


def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(enex, eney,eneir):
    screen.blit(enemyImg[eneir], (enex[eneir], eney[eneir]))

def fire_bullet(x,y):
    global bulletstate
    bulletstate = "fire"
    screen.blit(bulletImg,(x+16,y+10))

def isCollision(enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt((math.pow(enemyX-bulletX,2))+ (math.pow(enemyY-bulletY,2))) 
    if distance < 27:
        return True
    else:
        return False


# game loop
running = True

while running:
    screen.fill((0, 0, 0))
    screen.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerex = -0.5
            if event.key == pygame.K_RIGHT:
                playerex = 0.5
            if event.key == pygame.K_UP:
                playery = -0.3
            if event.key == pygame.K_DOWN:
                playery = 0.3
            if event.key == pygame.K_SPACE:
                if bulletstate is "ready":
                    bulletx = X
                    fire_bullet(bulletx,bullety)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerex = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playery = 0
            

    X += playerex
    Y += playery

    if X <= 0:
        X = 0
    elif X >= 736:
        X = 736
    elif Y <= 0:
        Y = 0
    elif Y >= 536:
        Y = 536


    if bullety <=0:
        bullety = 480
        bulletstate = "ready"


    #bullet movement
    if bulletstate is "fire":
        fire_bullet(bulletx,bullety)
        bullety -= bulletchangeY

    for ir in range(num_of_enemies):
        eX[ir] += enemyx[ir]
        eY[ir] += enemyy[ir]

        if eX[ir] <= 0:
            enemyx[ir] = 0.3
            eY[ir] +=5
        elif eX[ir] >= 736:
            enemyx[ir] = -0.3
            eY[ir] +=5
    
        #collision
        collision = isCollision(eX[ir],eY[ir],bulletx,bullety)
        if collision:
            bullety = 480
            bulletstate = "ready"
            score += 1
            print(score)
            eX = random.randint(64,735)
            eY = random.randint(50,150)
        print(ir)
        enemy(eX, eY, ir)


    player(X, Y)
    
    pygame.display.update()
