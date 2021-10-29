import pygame 

#intialize the program 
pygame.init()

#create the screen
screen = pygame.display.set_mode((800,600))

left = False
right = False

pygame.display.set_caption('space invaders')

icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

playerImg = icon = pygame.image.load('spaceship.png')
playerX = 370
playerY = 480 

def player():
    screen.blit(playerImg, (playerX, playerY))
    
running = True

while running:

    for event in pygame.event.get():
        
        if(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_a):
                left = True 
            if(event.key == pygame.K_d):
                right = True
        if(event.type == pygame.KEYUP):
            if(event.key == pygame.K_a):
                left = False
            if(event.key == pygame.K_d):
                right = False
    
 
        if (event.type == pygame.QUIT):
            running = False  
            
    if(left):
        playerX += -1
    
    if(right):
       playerX += 1
           
    
    screen.fill((0, 0, 0)) 

    player()
       
    pygame.display.update()