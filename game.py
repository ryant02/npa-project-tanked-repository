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
circle_pos = 250, 250
#------------------------------------



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
                circle_pos = (circle_pos[0]-10, circle_pos[1])
            if event.key == pygame.K_RIGHT:
                circle_pos = (circle_pos[0]+10, circle_pos[1])
            if event.key == pygame.K_UP:
                circle_pos = (circle_pos[0], circle_pos[1]-10)
            if event.key == pygame.K_DOWN:
                circle_pos = (circle_pos[0], circle_pos[1]+10)
            
            
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

    pygame.draw.circle(screen, (125, 125, 125), (circle_pos), 75)
    
    pygame.display.flip()
