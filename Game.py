import sys
from random import randint
import pygame




pygame.init()

height = 600
width = 600



screen = pygame.display.set_mode((width, height))

Blue = (0,0,225)
White = (255,255,255)
Red = (225, 0, 0)

Green = (0,225,0)

screen.fill(White)
pygame.display.update()

playerpos = [200,300]

playersize = 50


enemypos = [randint(0,600),0]
enemysize = 50


enemypos2 = [randint(0,600),0]
enemysize2 = 50

clock = pygame.time.Clock()

timer_event = pygame.USEREVENT + 1
pygame.time.set_timer(timer_event,25)


Playersprite = pygame.image.load("spaceship.png").convert_alpha()
enemysprite = pygame.image.load("Meteor.png").convert_alpha()
backround = pygame.image.load("backround.png").convert_alpha()


game_over= False

while not game_over:

    for event in pygame.event.get():




        if event.type == pygame.QUIT:
            sys.exit()



        if event.type == pygame.KEYDOWN:

            x = playerpos[0]
            y = playerpos[1]

            if event.key == pygame.K_s:
               y += 20
            elif event.key == pygame.K_a:
                x -= 20
            elif event.key == pygame.K_w:
                y -= 20
            elif event.key == pygame.K_d:
                x += 20
            playerpos = [x,y]
        screen.fill((225,225,225))
        if  enemypos[1] >= 0 and enemypos[1] < height:
           enemypos[1] += 5
        else:aa
            enemypos[1] = 0
            enemypos[0] = randint(1,width)
        if event.type == timer_event:
            enemypos[1] += 5
        if  enemypos2[1] >= 0 and enemypos2[1] < height:
           enemypos2[1] += 5
        else:
            enemypos2[1] = 0
            enemypos2[0] = randint(1,width)
        if event.type == timer_event:
            enemypos2[1] += 5

    screen.blit(backround, (0, 0))
    screen.blit(Playersprite,(playerpos[0],playerpos[1]))
    screen.blit(enemysprite,(enemypos[0],enemypos[1]))
    screen.blit(enemysprite, (enemypos2[0], enemypos2[1]))

    player = pygame.Rect(playerpos[0],playerpos[1], playersize, playersize)
    enemy = pygame.Rect(enemypos[0],enemypos[1], enemysize, enemysize)
    enemy2 = pygame.Rect(enemypos2[0],enemypos2[1], enemysize, enemysize)


    if player.colliderect(enemy) or player.colliderect(enemy2):
        sys.exit()

    clock.tick(100)

    pygame.display.update()














