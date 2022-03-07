#------------------------------------
# NPA Game Project
# Coded by Ryan To
#------------------------------------

#------------------------------------
# import libraries
#------------------------------------
import pygame
#------------------------------------


#------------------------------------
# initialisation and setup
#------------------------------------
pygame.init()

# set up the window we'll use to draw our game
screen = pygame.display.set_mode([500,500])


# set long term variables
running = True
# circle_pos = 250, 250
#------------------------------------

# set up player image
playerImg = pygame.image.load('game assets/graphics/tankBody_blue.png')
playerImg.convert()
playerRect = playerImg.get_rect()
playerRect.center = 250, 250


#------------------------------------------------------------------------
# game loop
#------------------------------------------------------------------------
# run the loop forever until the user asks to quit
while running:


    #----------------------------------------------------------------------
    # Input
    # check if the user clicked the close button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerRect.center = (playerRect.center[0]-10, playerRect.center[1])
            if event.key == pygame.K_RIGHT:
                playerRect.center = (playerRect.center[0]+10, playerRect.center[1])
            if event.key == pygame.K_UP:
                playerRect.center = (playerRect.center[0], playerRect.center[1]-10)
            if event.key == pygame.K_DOWN:
                playerRect.center = (playerRect.center[0], playerRect.center[1]+10)
            
            
        # and if keydown    
    #----------------------------------------------

    #----------------------------------------------
    # Update
    #----------------------------------------------
    
    #----------------------------------------------


    #----------------------------------------------
    # Draw
    #----------------------------------------------
    # fill background with colour
    screen.fill((255, 255, 255))
    #----------------------------------------------
    # draw everything
    screen.blit(playerImg, playerRect)
 
   # pygame.draw.circle(screen, (125, 125, 125), (circle_pos), 75)
    
    pygame.display.flip()
