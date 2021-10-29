import pygame
import random

pygame.init()

pygame.font.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption('move around screen killing bad guys')

myfont = pygame.font.SysFont('Comic Sans MS', 30)

class Sprite: 
    X = 0 
    Y = 0
    img = 0
    
    left = False
    right = False
    up = False
    down = False
    
    def __init__(self, x, y, img, left, right, up, down):
        self.X = x 
        self.Y = y 
        self.img = img 
        self.left = left
        self.right = right
        self.up = up
        self.down = down
    
    
class Sprites: 
    playerIconL = pygame.image.load('GuyL.png')
    playerIconR = pygame.image.load('GuyR.png')
    playerIconB = pygame.image.load('GuyB.png')
    playerIconF = pygame.image.load('GuyF.png')
    
    ball = pygame.image.load('ball.png')
    gameOver = pygame.image.load('gameOver.png')
    coinIcon = pygame.image.load('coin.png')

playerIcon = Sprites.playerIconL

pygame.display.set_icon(playerIcon)

running = True

player = Sprite(370, 480, playerIcon, False, False, False, False)

ball = Sprite(400, 400, Sprites.ball, False, False, False, False)

coin = Sprite(400, 400, Sprites.coinIcon, False, False, False, False)


gameOverOn = False
coinCount = 0

def Pos(): 
    screen.blit(player.img, (player.X, player.Y))
    screen.blit(ball.img, (ball.X, ball.Y))
    screen.blit(coin.img, (coin.X, coin.Y))
    
    screen.blit(textsurface,(0,550))
    
while(running == True): 
    
        
    textsurface = myfont.render(str(coinCount), False, (0, 0, 0))
    
    if(ball.X <= 770 and ball.left == False and gameOverOn == False):
        ball.X += 1 
    else:
        ball.left = True
        
    if(ball.X >= 0 and ball.left == True and gameOverOn == False):
        ball.X -= 1
    else:
        ball.left = False
        
    if(ball.Y <= 570 and ball.up == False and gameOverOn == False):
        ball.Y += 2 
    else:
        ball.up = True
        
    if(ball.Y >= 0 and ball.up == True and gameOverOn == False):
        ball.Y -= 2
    else:
        ball.up = False
    
    if(gameOverOn):
        player.up = False
        player.down = False
        player.left = False
        player.right = False
    
    for event in pygame.event.get():
        
        if(event.type == pygame.KEYDOWN and gameOverOn == False):
            if(event.key == pygame.K_w):
                player.up = True
            if(event.key == pygame.K_s):
                player.down = True
            if(event.key == pygame.K_a):
                player.left = True
            if(event.key == pygame.K_d):
                player.right = True
                
        if(event.type == pygame.KEYUP):
            
            if(event.key == pygame.K_w):
                player.up = False
            if(event.key == pygame.K_s):
                player.down = False
            if(event.key == pygame.K_a):
                player.left = False
            if(event.key == pygame.K_d):
                player.right = False
    
        if(event.type == pygame.QUIT):
            running = False
    
    screen.fill((0, 0, 150)) 
    
    Pos()
    

    
    if(gameOverOn == True):
        
        screen.blit(Sprites.gameOver, (400, 300))
    
    pygame.display.update()
    
    if(player.up):
        player.Y -= 1
        player.img = Sprites.playerIconB
        
    if(player.down):
        player.Y += 1
        player.img = Sprites.playerIconF
    
    if(player.right):
         player.X += 1
         player.img = Sprites.playerIconR
    
    
    if(player.left):
       player.X -= 1
       player.img = Sprites.playerIconL
        
    if(player.X > 770):
        player.X = 770
    elif(player.X < 0):
        player.X = 0
    if(player.Y > 570):
        player.Y = 570
    elif(player.Y < 0):
        player.Y = 0
        
    
    if(ball.X >= player.X and ball.X <= player.X + 32 and ball.Y <= player.Y and ball.Y >= player.Y - 32):
        gameOverOn = True
        
    if(coin.X > player.X - 32 and coin.X < player.X + 32 and coin.Y < player.Y + 32 and coin.Y > player.Y - 32):
        coin.X = random.randint(1, 780)
        coin.Y = random.randint(1, 580)
        coinCount += 1 
    
        
    
    
    
    