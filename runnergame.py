from tkinter import E
import pygame
from sys import exit
import random

def displayScore():
    currentTime = int(pygame.time.get_ticks() / 1000) - startTime
    scoreSurface = font.render(f'Score: {currentTime}', True, (255, 0, 0))
    scoreRect = scoreSurface.get_rect(center = (400, 50))
    screen.blit(scoreSurface, scoreRect)
    return currentTime

def obstacleMovement(obstacleList):
    if obstacleList:
        for obstacleRect in obstacleList:
            obstacleRect.x -= 5
            if obstacleRect.bottom == 300:
                screen.blit(snail, obstacleRect)
            else:
                screen.blit(fly, obstacleRect)

        obstacleList = [obstacle for obstacle in obstacleList if obstacle.x > -100]
    
        return obstacleList
    else:
        return []

def collisions(player, obstacles):
    if obstacles:
        for obstacleRect in obstacles:
            if player.colliderect(obstacleRect):
                return False
    return True

def playerAnimation():
    global playerSurface, playerIndex

    if playerRect.bottom < 300:
        playerSurface = playerJump
    else:
        playerIndex += 0.1

        if playerIndex >= len(playerWalk):
            playerIndex = 0
        playerSurface = playerWalk[int(playerIndex)]








pygame.init()

currentTime = pygame.time.get_ticks()




screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()
font = pygame.font.Font("college.ttf", 50)

gameActive = False
startTime = 0

score = 0

background = pygame.image.load("Graphics/Sky.png").convert()
ground = pygame.image.load("Graphics/ground.png").convert()


snailFrame1 = pygame.image.load("Graphics/snail1.png").convert_alpha()
snailFrame2 = pygame.image.load("Graphics/snail2.png").convert_alpha()
snailFrames = [snailFrame1, snailFrame2]


flyFrame1 = pygame.image.load("Graphics/Fly1.png").convert_alpha()
flyFrame2 = pygame.image.load("Graphics/Fly2.png").convert_alpha()
flyFrames = [flyFrame1, flyFrame2]

snailFrameIndex = 0
flyFrameIndex = 0

snail = snailFrames[snailFrameIndex]
fly = flyFrames[flyFrameIndex]


obstacleRectList = []

playerWalk1 = pygame.image.load("Graphics/player_walk_1.png").convert_alpha()
playerWalk2 = pygame.image.load("Graphics/player_walk_2.png").convert_alpha()

playerWalk = [playerWalk1, playerWalk2]

playerIndex = 0

playerSurface = playerWalk[playerIndex]

playerJump = pygame.image.load("Graphics/jump.png").convert_alpha()

playerRect = playerSurface.get_rect(midbottom = (80, 300))
playerGravity = 0


playerStand = pygame.image.load("Graphics/player_stand.png").convert_alpha()
playerStand = pygame.transform.rotozoom(playerStand, 0, 2)
playerStandRect = playerStand.get_rect(center = (400, 200))

pygame.display.set_icon(playerStand)


title = font.render("Runner", True, (200, 0, 0))
titleRect = title.get_rect(center = (400, 50))

instructions = font.render("Press 'Space' to start the game", True, (200, 0, 0))
instructions = pygame.transform.rotozoom(instructions, 0, 0.5)

instructionsRect = instructions.get_rect(center = (400, 350))

obstacleTimer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacleTimer, 1450)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if gameActive:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
                if playerRect.bottom == 300:
                    playerGravity = -20
            if event.type == pygame.MOUSEBUTTONDOWN and playerRect.collidepoint(mousePos):
                if playerRect.bottom == 300:
                    playerGravity = -20


        else: 
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                gameActive = True
                startTime = int(pygame.time.get_ticks() / 1000)
        
        if event.type == obstacleTimer and gameActive == True:
            if random.randint(0, 2):
                obstacleRectList.append(snail.get_rect(bottomright = (random.randint(900, 1100), 300)))
            else:
                obstacleRectList.append(fly.get_rect(bottomright = (random.randint(900, 1100), 210)))


 


    if gameActive == True:


        screen.blit(background, (0,0))
        screen.blit(ground, (0, 300))

     #   snailRect.left -= 5
      #  if snailRect.left < -100:
      #      snailRect.left = 900
    #    screen.blit(snail, snailRect)

            
        


        playerGravity += 1
        playerRect.y += playerGravity
        if playerRect.bottom >= 300:
            playerRect.bottom = 300

        playerAnimation()


        screen.blit(playerSurface, playerRect)
        score = displayScore()
        obstacleRectList = obstacleMovement(obstacleRectList)

        gameActive = collisions(playerRect, obstacleRectList)



        #if snailRect.colliderect(playerRect):



    else:
        screen.fill((94, 129, 162))
        playerRect.midbottom = (80, 300)
        playerGravity = 0
        screen.blit(playerStand, playerStandRect)
        screen.blit(title, titleRect)
        obstacleRectList.clear()
        scoreMessage = font.render(f"Your score: {score}", False, (200, 0, 0))
        scoreMessageRect = scoreMessage.get_rect(center = (400, 330))
        screen.blit(instructions, instructionsRect)





        mousePos = pygame.mouse.get_pos()


    

        



    pygame.display.update()
    clock.tick(60)



