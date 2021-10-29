#pygame RPG test (this will go wrong)


#These import different things that i need, pygame for pygame, mixer for music, time is for timers(also for fixing issues with fps changing speed), copy for copying variables to new variables without making them change when the other changes later in the code(important with time) and random to generate random numbers
import pygame 
from pygame import mixer 
import time
import copy 
import random

pygame.init()

pygame.font.init()
    
#screen size is 800, 600. Might change later
screen = pygame.display.set_mode((800, 600))


#old enemy values, needs fixing soon (not that soon)
enemyX = False
enemyY = False

#This is for dialouge. It opens a text file and reads it
class TR():
    lines = open('TextForRpg.txt')
    Read = lines.readlines()
    
#class text boxes and control of menus
class TextCon():
    MBox = ''
    Box1 = ''
    Box2 = ''
    Box3 = ''
    Box4 = ''
    select = 0
    enterPress = False
    textMode = False 
    textNum = 0
    EDown = False
    whereText = [4, 4, 4]
    whoText = [0, 0, 1, 1, 0, 1, 0, 1, 0, 1]
    whenSwitch = [2, 1, 1, 1, 1, 1, 1]
    switchTalk = 0 
    diaNum = 0
    curText = ''
    whoTalking = 0
    iGotToGo = 0

#rendering text font and caption. Might change it from comic sans later
TextBox = pygame.font.SysFont('Comic Sans MS', 32)
TextBox1 = pygame.font.SysFont('Cmic Sans MS', 25)
pygame.display.set_caption('RPG')

#music, might make into class if i add enough songs
mixer.music.load('testSong.wav')

#makes the game exit when exiting, kinda glitched with windows, might look into later
running = True

#pressing E cant happen more than once, not really necessary anymore so might remove if it feels necessary 
eAgain = False


#rendering sprites, all sprites are in the pygame folder
class Sprites():
    playerBullet = pygame.image.load('CoolBallThing.png')
    playerCha = pygame.image.load('Main.png')
    bullet = pygame.image.load('enemyBullet.png')
    RPGBox = pygame.image.load('RPGBox.png')
    testEnemy = pygame.image.load('testEnemy.png')
    defense = pygame.image.load('MainShielded.png')
    mainOver = pygame.image.load('overworldGuy.png')
    mainTalk = pygame.image.load('MainTalk.png')
    testEnemyTalk = pygame.image.load('TestEnemyTalk.png')
    enemyOverSprite = pygame.image.load('EnemyOver.png')
    BP = pygame.image.load('BattlePass.png')

yo = True

#is a def that loads all sprites
def LoadSprites():
    if(BHMOn == True):
        screen.blit(Sprites.playerBullet, (playerBHM.x, playerBHM.y))
        screen.blit(Sprites.bullet, (testEnemy.x, testEnemy.y))
        screen.blit(Sprites.RPGBox, (250, 200))
    
    if(Switch.RPGMode == False):
        screen.blit(Sprites.mainOver, (playerOver.x, playerOver.y))
        screen.blit(Sprites.enemyOverSprite, (enemyOver.x, enemyOver.y))
        
    if(BHMOn == True and TextCon.select == 1):
        screen.blit(Sprites.defense, (100, 100))
    elif(Switch.RPGMode == True and yo == False):
        screen.blit(Sprites.playerCha, (100, 100))
    elif(Switch.RPGMode and yo): 
        screen.blit(Sprites.BP, (100, 100))
        
    if(TextCon.textMode):
        screen.blit(TextCon.MBox,(200, 500))
        
        #this sees what portrait should be in play using a list as reference 
        if(TextCon.whoText[TextCon.whoTalking] == 0):
            screen.blit(Sprites.mainTalk,(100, 400))
        
        if(TextCon.whoText[TextCon.whoTalking] == 1):
            screen.blit(Sprites.testEnemyTalk, (100, 400))

    if(Switch.RPGMode == True):
        screen.blit(Sprites.testEnemy, (700, 135))
        screen.blit(TextCon.Box1,(70, 400))
        screen.blit(TextCon.Box2, (600, 400))
        screen.blit(TextCon.Box3, (700, 0))
        screen.blit(TextCon.Box4, (0, 0))
#BHM stands for Bullet Hell Mode, reffering to the bullet hell gaming genre
class BHM():

    #x and y off 'bullets' in BHM mode
    x = 600
    y = 400
    
    #hp of player and enemy
    HP = 0
    
    #bools needed for control
    left = False
    right = False
    up = False
    down = False



    #made so any object can use all commands without needing to make a command for each
    def __init__(self, x, y, HP, left, right, up, down):
        self.x = x
        self.y = y
        self.hp = HP
        self.left = left
        self.right = right
        self.up = up
        self.down = down
        
#all objects, might make into a class if more are added
playerBHM = BHM(400, 300, 10, False, False, False, False)
testEnemy = BHM(700, 500, 3, False, False, False, False)

#this is the script which handles over world movement and such
class Overworld():
    x = 0 
    y = 0
    
    left = False
    right = False
    up = False
    down = False
    
    #made so any object can use all commands without needing to make a command for each
    def __init__(self, x, y, left, right, up, down):
        self.x = x
        self.y = y
        
        self.left = left
        self.right = right
        self.up = up
        self.down = down
    

#overworld objects
playerOver = Overworld(300, 200, False, False, False, False)
enemyOver = Overworld(400, 400, False, False, False, False)

#this class handles the switch between overworld mode and rpg mode
class Switch():
    RPGMode = False


#'enemySpawn' not used anywhere
enemySpawn = 3

#puts on BHM 
BHMOn = False

#makes enemy bullet timers not update every frame
once = False

#different 'timers' timing different things
class Timers():
    timerOld = copy.deepcopy(time.time()) - 0.067
    timerNew = 0
    timerRes = 0
    bulletTime = 0
    endTime = 0
    testTime = 0
    hitInv = 0
    musicTime = 0
    
#Sees if music is suppose to play, might change with more tracks
musicPlay = False

#Needed for BHM ending, might change
doneTrice = 0
while(running):
    
    #Plays music if it's in 'rpg' mode. it also doesn't allow it to be read more than once a battle
    if(Switch.RPGMode and musicPlay == False):
        mixer.music.play(-1)
        musicPlay = True
            
    if(Switch.RPGMode == False and musicPlay == True):
        musicPlay = False
        mixer.music.stop()
    
    #switches to rpg mode if enemy touches the player 
    if(enemyOver.x > playerOver.x and enemyOver.x < playerOver.x + 60 and enemyOver.y > playerOver.y and enemyOver.y < playerOver.y + 60): 
        TextCon.textMode = True 
    else: 
        TextCon.textMode = False
        
    #if enemy.hp is 0 or lower the battle ends
    if(testEnemy.hp <= 0):
        Switch.RPGMode = False
        BHMOn = False
        enemyOver.x = 1000 
        enemyOver.y = 1000
    
    #tells the game what text the text should load, also which color they should have
    TextCon.Box4 = TextBox.render(str(playerBHM.hp), False, (255,255,255))
    TextCon.Box3 = TextBox.render(str(testEnemy.hp), False, (255,255,255))
    
    if(TextCon.select == 0):
        TextCon.Box1 = TextBox.render('Attack', False, (255,255,255))
    else:
        TextCon.Box1 = TextBox.render('Attack', False, (100,100,100))
    if(TextCon.select == 1):
        TextCon.Box2 = TextBox.render('Defend', False, (255,255,255))
    else:
        TextCon.Box2 = TextBox.render('Defend', False, (100,100,100))
        
    #turns the game into bullet hell mode when e is pressed and when game is not already in bullet hell mode
    if(TextCon.select == 0 and TextCon.enterPress == True): 
        testEnemy.hp -= 2
        TextCon.enterPress = False
    elif(TextCon.select == 1 and TextCon.enterPress == True):
        testEnemy.hp -= 1
        TextCon.enterPress = False

    #explained down in movement 
    Timers.timerNew = copy.deepcopy(time.time())

    
    #This sees when a portrait should switch, it takes these from a list as reference
    if(TextCon.whenSwitch[TextCon.iGotToGo] == TextCon.switchTalk):
        TextCon.iGotToGo += 1   
        TextCon.whoTalking += 1 
        TextCon.switchTalk = 0


    #this makes a dialouge box apper when going into an enemy, and not just when you press E at one
    if(TextCon.textMode and yo == True):
        TextCon.curText = TR.Read[TextCon.textNum]
        TextCon.MBox = TextBox1.render(TextCon.curText, False, (255,255,255))
        TextCon.textNum += 1
        yo = False
        TextCon.switchTalk +=1
        
    #makes button controls possible in pygame
    for event in pygame.event.get():
        
        
        if(Switch.RPGMode == False):
            if(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_w):
                    playerOver.up = True
                if(event.key == pygame.K_s):
                    playerOver.down = True
                if(event.key == pygame.K_a):
                    playerOver.left = True
                if(event.key == pygame.K_d):
                    playerOver.right = True
    
        
        if(event.type == pygame.KEYUP):
                
            if(event.key == pygame.K_w):
                playerOver.up = False
            if(event.key == pygame.K_s):
                playerOver.down = False
            if(event.key == pygame.K_a):
                playerOver.left = False
            if(event.key == pygame.K_d):
                playerOver.right = False                  
        
        if(Switch.RPGMode):
            #keydown looks if a key is pressed down
            if(event.type == pygame.KEYDOWN):
            
                #in non BHM, text select changes once
                if(event.key == pygame.K_a and BHMOn == False):
                    if(TextCon.select > 0):
                        TextCon.select -= 1
            
                if(event.key == pygame.K_d and BHMOn == False):
                    if(TextCon.select < 1):
                        TextCon.select += 1
            
                #enters BHM
                if(event.key == pygame.K_e and BHMOn == False):
                
                    TextCon.enterPress = True
                    BHMOn = True

            #makes up, down, left and right true when in BHM mode. When these are true the player moves up, down, left and right respectively
                if(BHMOn == True):
                    if(event.key == pygame.K_w):
                        playerBHM.up = True
                    if(event.key == pygame.K_s):
                        playerBHM.down = True
                    if(event.key == pygame.K_a):
                        playerBHM.left = True
                    if(event.key == pygame.K_d):
                        playerBHM.right = True
                        
                
        
        #Takes away the affects of the KEYDOWN buttons, effectivly making the game read when a player is holding down a button
        if(event.type == pygame.KEYUP):
                
            if(event.key == pygame.K_w):
                    playerBHM.up = False
            if(event.key == pygame.K_s):
                    playerBHM.down = False
            if(event.key == pygame.K_a):
                    playerBHM.left = False
            if(event.key == pygame.K_d):
                    playerBHM.right = False
        
        #quits the game, as said before kinda broken
        if(event.type == pygame.QUIT): 
            running = False
        
        if(event.type == pygame.KEYDOWN):
            if(TextCon.textMode and event.key == pygame.K_e):
                    TextCon.curText = TR.Read[TextCon.textNum]
                    TextCon.MBox = TextBox1.render(TextCon.curText, False, (255,255,255))
                    TextCon.textNum += 1
                    TextCon.switchTalk +=1
                    if(TextCon.textNum == TextCon.whereText[TextCon.diaNum]):
                        TextCon.textMode = False
                        Switch.RPGMode = True
                        TextCon.diaNum += 1
                        enemyOver.x = -50
                        enemyOver.y = -50
            if(TextCon.textMode == False):
                TextCon.MBox = TextBox1.render('', False, (255,255,255))
            
            
     
    #The BHM player isn't suppose to be able to move out of a specific area, this makes that stay true
    #the timers are needed to make movement constant. 'timersOld' is how much time has passed since jan 1 1970 last frame, whilst 'timerNew' is how much time it was since jan 1 1970 this frame. subtracting tiemrNew with timerOld therefore gives the amount of time since last frame. if you then multiply your movement with it the movement is always constant
    if(playerBHM.up == True and playerBHM.y > 200):
            playerBHM.y -= 1.000000001  * Timers.timerNew - Timers.timerOld 
    if(playerBHM.down == True and playerBHM.y < 470):
            playerBHM.y +=  1.000000001  * Timers.timerNew - Timers.timerOld
    if(playerBHM.right == True and playerBHM.x < 520):
            playerBHM.x += 1.000000001  * Timers.timerNew - Timers.timerOld
    if(playerBHM.left == True and playerBHM.x > 250):
            playerBHM.x -= 1.000000001  * Timers.timerNew - Timers.timerOld
            
            
    if(playerOver.up == True and playerOver.y > 0 and TextCon.textMode == False):
            playerOver.y -= 1.000000001 * Timers.timerNew - Timers.timerOld
    if(playerOver.down == True and playerOver.y < 525 and TextCon.textMode == False):
            playerOver.y += 1.000000001  * Timers.timerNew - Timers.timerOld
    if(playerOver.right == True and playerOver.x < 736 and TextCon.textMode == False):
            playerOver.x += 1.000000001  * Timers.timerNew - Timers.timerOld
    if(playerOver.left == True and playerOver.x > 0 and TextCon.textMode == False):
            playerOver.x -= 1.000000001 * Timers.timerNew - Timers.timerOld
    
    if(BHMOn == True):
        #Says that 'bulletTime' is time.time, making it a timer
        Timers.bulletTime = time.time()
        if(once == False):
            #copies bulletTime to get the the exact time it was copied in, subtracting bulletTime with this time gives the time that has passed
            Timers.testTime = copy.deepcopy(Timers.bulletTime)
            Timers.hitInv = copy.deepcopy(Timers.bulletTime) - 3
            #makes this if statment only happen once, until the once command is used again
            once = True
    
        #makes bullets follow the player, with it reseting posistions every 5 seconds. Will add more bullet patterns at a later time
        if(Timers.bulletTime - Timers.testTime < 5):
            if(testEnemy.x > playerBHM.x and enemyY == False):
                testEnemy.x -= 1.0000000002 * Timers.timerNew - Timers.timerOld
            if(testEnemy.x < playerBHM.x and enemyY == False):
                testEnemy.x += 1.0000000002 * Timers.timerNew - Timers.timerOld
            if(testEnemy.y > playerBHM.y and enemyX == False):
                testEnemy.y -= 1.0000000002 * Timers.timerNew - Timers.timerOld
            if(testEnemy.y < playerBHM.y and enemyX == False):
                testEnemy.y  += 1.0000000002 * Timers.timerNew - Timers.timerOld
                
        if(Timers.bulletTime - Timers.testTime > 5):
            testEnemy.x = random.randint(0, 800)
            testEnemy.y = random.randint(0, 600)
            once = False
           
            #checks how many times this command is used, is used down below to reset the battle into menuMode (non BHM rpg mode) when 15 seconds have passed
            doneTrice += 1
            
        if(doneTrice >= 3):
            BHMOn = False
            doneTrice = 0 
            testTimeLarge = 0 
            
        #makes testEnemy.x and y be at 1000 when BHMOn is false, avoiding potential bugs
        if(BHMOn == False):
            testEnemy.x = 1000
            testEnemy.y = 1000
        
        #checks if the playerBHM and the testEnemy are at the same position relative to their sprites
        if(testEnemy.x > playerBHM.x and testEnemy.x < playerBHM.x + 30 and testEnemy.y > playerBHM.y and testEnemy.y < playerBHM.y + 30 and Timers.bulletTime - Timers.hitInv > 1.5):
            if(TextCon.select == 1):
                playerBHM.hp -= 1
            else: 
                playerBHM.hp -= 2
            #hitstun so your hp wont dissapear every frame
            Timers.hitInv = copy.deepcopy(Timers.bulletTime)
            
        
    
    #some values for testing
    if(testEnemy.y == playerBHM.y):
        enemyY = True 
            
    if(testEnemy.x == playerBHM.x):
        enemyX = True
        
        
    #avoids bugs with sprites being where they shouldn't, also switches background color in RPG mode and overworld mode 
    
    if(Switch.RPGMode == False):
        screen.fill((0,150,0))
    else: 
        screen.fill((0,0,0))
    
    #loads all sprites which should be loaded
    LoadSprites()
    
    #updates timerOld into this frame. it will be one frame outdated when its used in code
    Timers.timerOld = copy.deepcopy(time.time())
    
    #updates the sprites, also there for bug reasons
    pygame.display.update()