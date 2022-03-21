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
WINDOWWIDTH = 500
WINDOWHEIGHT = 500
screen = pygame.display.set_mode([WINDOWWIDTH, WINDOWHEIGHT])


# set long term variables
running = True
# circle_pos = 250, 250
#------------------------------------------------------

# set up player

position = [WINDOWWIDTH / 2, WINDOWHEIGHT / 2]
PLAYERSIZE = 50
player = pygame.Rect(position[0], position[1], PLAYERSIZE, PLAYERSIZE)
# -----------------------------------------------------








#playerImg = pygame.image.load('game assets/graphics/player_tank_body_v3.png')
#playerImg.convert()
#playerRect = playerImg.get_rect()
#playerRect.center = 250, 250

# other graphics
#green_sandbagImg = pygame.image.load('game assets/graphics/green_sandbag.png')
#green_sandbagImg = 100, 100

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
                position[0] -= 10
            if event.key == pygame.K_RIGHT:
                position[0] += 10
            if event.key == pygame.K_UP:
                position[1] -= 10
            if event.key == pygame.K_DOWN:
                position[1] += 10



        #if event.type == pygame.KEYDOWN:
            #if event.key == pygame.K_LEFT:
                #playerRect.center = (playerRect.center[0]-10, playerRect.center[1])
            #if event.key == pygame.K_RIGHT:
                #playerRect.center = (playerRect.center[0]+10, playerRect.center[1])
            #if event.key == pygame.K_UP:
                #playerRect.center = (playerRect.center[0], playerRect.center[1]-10)
            #if event.key == pygame.K_DOWN:
                #playerRect.center = (playerRect.center[0], playerRect.center[1]+10)
            
            
        # and if keydown    
    #----------------------------------------------

    #----------------------------------------------
    # Update
    #----------------------------------------------
    player.left = position[0]
    player.top = position[1]
    #----------------------------------------------


    #----------------------------------------------
    # Draw
    #----------------------------------------------
    # fill background with colour
    screen.fill((0, 0, 0))
    #----------------------------------------------
    # draw everything
    pygame.draw.rect(screen, (125, 125, 125), player)




    #screen.blit(playerImg, playerRect)
 
   # pygame.draw.circle(screen, (125, 125, 125), (circle_pos), 75)

    # Flip the display
    pygame.display.flip()
    # ---------------------------------------------


# END of Game Loop
# -------------------------------------------------


# -------------------------------------------------
# Program Exit
# -------------------------------------------------
pygame.quit()
# -------------------------------------------------







