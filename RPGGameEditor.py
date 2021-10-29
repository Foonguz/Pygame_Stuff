#RPG editor (this will go wrong)

import pygame 
import time
import copy

pygame.init()

screen = pygame.display.set_mode((800,600))

pygame.display.set_caption('RPG Editor')


enemies = []

enemyText = []

newText = []


class Sprites():
    icon = pygame.image.load('Editor.png')
    testEnemy = pygame.image.load('EnemyOver.png')
    
pygame.display.set_icon(Sprites.icon)

running = True


class Cords():
    x = 0
    y = 0
    def __init__ (self, x, y):
        self.x = x
        self.y = y
    

class Timer():
    saveTime = copy.deepcopy(time.time()) - 15
    
mouse = Cords(0, 0)
testEnemy = Cords(0, 0)
deletion = Cords(0, 0)

readLine = open('test.txt', 'r')  
readText = open('textForRpg.txt', 'r')    
stop = False

enemyPlus = 0

value = readLine.readlines()
valueText = readText.readlines()

test = False

deletionOfText = []

rangeOnce = True


def Save(enemies):
    writeLine = open('test.txt', 'w')
    writeText = open('textForRpg.txt', 'w')
    print('saving')
    for x in range(len(enemies)):
        
        if(deletion.x == enemies[x].x and deletion.y == enemies[x].y):
            enemies[x].x = - 200
        elif(enemies[x].x >= 0):
            writeLine.write(str(enemies[x].x) + '\n')
            writeLine.write(str(enemies[x].y) + '\n')
            
    
    for x in range(len(enemyText)): 
        
        deletionOfText.append('')
    
        if(str(enemyText[x][x].strip('\n' + 'cord ')) == str(deletion.x) + str(deletion.y)):
            
            for y in range(x):
                    deletionOfText.append(enemyText[x])
                    deletionOfText.append(enemyText[x + 1])
                    for z in range(enemyText[x + 1]):
                        deletionOfText.append(enemyText[x + z])
        elif(deletionOfText[x] != enemyText[x]):
            if(enemyText[x][1].strip('\n').isnumeric()):
                for y in range(len(enemyText[x])):
                    writeText.write(str(enemyText[x][y]))
                    writeText.write(str('')) 
            
            
    deletion.x = -200
    deletion.y = -200


            
    
            
            

for i in range(int(len(value)*0.5)):
    

    newEnemy = Cords(int(value[i * 2]), int(value[i * 2 + 1]))
    enemies.append(newEnemy) 


writeLine = open('test.txt', 'w')
writeText = open('textForRpg.txt', 'w')



writeEnemy = False

testTest = True

enemyTextCount = 0
addedTextCount = 0


overAgain = True

while(running):
    
    
    mouseValue = pygame.mouse.get_pos()
    
    mouse.x = round(mouseValue[0]/100) * 100
    mouse.y = round(mouseValue[1]/100) * 100
    
    for event in pygame.event.get():
        
        if(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_q):
                deletion.x = mouse.x
                deletion.y = mouse.y
                Save(enemies)
                
        if(event.type == pygame.MOUSEBUTTONDOWN):
            
            newEnemy = Cords(mouse.x, mouse.y)
            enemies.append(newEnemy) 
            
            newText.append('')
            newText[0] = 'cord '+ str(mouse.x) + str(mouse.y) + '\n'
            newText.append('')
            
            newText[1] = input('how many lines: ') + '\n'
            for x in range(int(newText[1])):
                newText.append('')
                newText[x + 2] = input(f'line {x + 1}: ') + '\n'
                
            enemyText.append('')
            enemyText[addedTextCount] = copy.deepcopy(newText)
            newText = [] 
            addedTextCount =+ 1
            
            Save(enemies)
            
            test = True
               
        if(event.type == pygame.QUIT):
                
            running = False
          
    screen.fill((0,0,0))  

    if(testTest):
        for x in range(len(valueText)):
            
            if(valueText[x].strip('\n').isnumeric() == True):
                print('True')
                for y in range(int(valueText[x]) + 2):
                    
                    
                    newText.append('')
                    newText[y] = valueText[x + y - 1]
                    
                    if(y == int(valueText[x]) + 1):
                        
                        if(overAgain):
                            enemyText.append('')
                            
                        enemyText[enemyTextCount] = newText 
                        print(enemyText)
                        enemyTextCount += 1
                        addedTextCount = copy.deepcopy(enemyTextCount)
                        newText = []
        overAgain = False
        testTest = False
        enemyTextCount = 0
    
    if(time.time() - Timer.saveTime > 5):
        testTest = True
        Save(enemies)
        Timer.saveTime = copy.deepcopy(time.time())
        
        
    for x in range(len(enemies)):
        screen.blit(Sprites.testEnemy, (enemies[x].x, enemies[x].y))
        
     
    pygame.display.update()
    
    