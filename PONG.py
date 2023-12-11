#Import the pygame libary and initialise the game engine
import pygame
pygame.init()

#open a new window, caption it "Pong"
screen = pygame.display.set_mode((700, 500))
pygame.display.set_caption("Pong")

#Here's the variable that runs our game loop
doExit = False

#The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

#Variables to hold paddle positions
p1x = 20
p1y = 100

#P2 paddle position
p2x = 650
p2y = 100

#Ball variables
bx = 350 #xposition
by = 250 #yposition
bVx = 5 #x velocity (horizontal speed)
bVy = 5 #y velocity (vertical speed)

p2Score = 0
p1Score = 0
while not doExit: #GAME LOOP-----------------------------------

    #Event queue stuff------------------------
    clock.tick(60) #set the FPS
    
    for event in pygame.event.get(): #check if user did something
        if event.type == pygame.QUIT: #check if user clicked close
            doExit = True #Flag that we are done so we exit game loop
            
    #game logic will go here----------------
    Keys = pygame.key.get_pressed()
    if Keys[pygame.K_w]:
       p1y-=5
    if Keys[pygame.K_s]:
      p1y+=5
     
    #Second player key inputs
    if Keys[pygame.K_UP]:
       p2y-=5
    if Keys[pygame.K_DOWN]:
      p2y+=5
    
    #ball movement
    bx += bVx
    by += bVy
     
    #reflect ball off side walls of screen
    #if bx < 0 or bx + 20 > 700:
    #    bVx *= -1
    
    
    #reflect ball off top and bottom    
    if by < 0 or by + 20 > 500:
        bVy *= -1
        
    #ball-paddle reflection    
    if bx < p1x + 20 and by + 20 > p1y and by < p1y + 100:
         bVx *= -1
     
    if bx + 20 > p2x  and by + 20 > p2y and by < p2y + 100:
         bVx *= -1
    
    
    #reflect ball off side walls of screen, change score 
    if bx < 0: #this has been split up from right wall collision so we can increase scores
        bVx *= -1
        p2Score += 1 #python doesn't do ++ because it's DUMB
   
    #add score for the right wall here
    if bx + 20 > 700:
        bVx*= -1
        p1Score += 1

    #render section will go here--------------
   
    screen.fill((0,0,0)) #wipe screen black
    #draw a rectangle
    pygame.draw.rect(screen, (255, 255, 255), (p1x, p1y, 20, 100), 4)
    
    #second paddle
    pygame.draw.rect(screen, (255, 255, 255), (p2x, p2y, 20, 100), 4)
            
    #Ball
    pygame.draw.circle(screen, (255, 255, 255), (bx, by), 10)
     
    #draw a line down the middle
    pygame.draw.line(screen, (255, 255, 255), [349, 0], [349, 500], 5)

        
    #display scores
    font = pygame.font.Font(None, 74)
    text = font.render(str(p2Score), 1, (255, 255, 255))
    screen.blit(text, (420,10))
    
    font = pygame.font.Font(None, 74)
    text = font.render(str(p1Score), 1, (255, 255, 255))
    screen.blit(text, (220,10))


 
    #update the screen
    pygame.display.flip()
            
            
#END GAME LOOP------------------------------------------------

pygame.quit()#when game is done close down pygame
