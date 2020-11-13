## Snake Game in python , I call it Snakeuela ..
## Use ARROWS KEYS to play, Choose diffcult level ,P for pauseing, Enter name and Press Enter to start play.
## Can Enter Description Press -> Use Instructions
## Dont Need to run all over again ,if death and want to keep going -> Press Retry 
## Hold a dictionary of ten bests players in game  


import pygame
import random
import sys
import os

pygame.init()
pause = False

## Set colors
black = (0, 0, 0)
red = (128, 0, 0)
green = (0, 128, 0)
blue = (0, 0, 128)
white = (255, 255, 255)
purple = (128, 0, 128)
light_purple = (255, 0, 255)
light_red = (255, 0, 0)
light_green = (0, 255, 0)
light_blue = (0, 0, 255)

## Set screen size
screenS_width = 800
screenS_height = 600
screenS_game = 500

## set font
smallFont = pygame.font.SysFont("Comicsansms", 20)
medFont = pygame.font.SysFont("Comicsansms", 45)
largeFont = pygame.font.SysFont("Comicsansms", 55)

## Initial window and title
game = pygame.display.set_mode((screenS_width, screenS_height))
pygame.display.set_caption("WOW SNAKEUEL")

## Frame per second
fps = pygame.time.Clock()


                            ###Screens###


## Screen level, Choose the difficulty that suits you 

def levelScreen(name, dic):
    game = pygame.display.set_mode((screenS_width, screenS_height))
    while True:
        game.fill(white)
        messageToScreen("Select Level", black, 0, -200, size="large")
        button("Begineer", name, dic, 325, 210, 150, 50, light_red, red, action="beginner")
        button("Medium", name, dic, 325, 270, 150, 50, light_blue, blue, action="medium")
        button("Expert", name, dic, 325, 330, 150, 50, light_green, green, action="expert")
        button("Back", name, dic, 150, 500, 150, 50, light_purple, purple, action="back")
        button("Quit", name, dic, 500, 500, 150, 50, light_purple, purple, action="quit")
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOver(dic)


## Discreption screen, Game Instructions 

def explainScreen(dic):
    descri = pygame.display.set_mode((screenS_width, screenS_height))
    while True:
        descri.fill(white)
        messageToScreen("Description", red, 0, -260, size="medium")
        messageToScreen("Welcome to my game !! ", black, 0, -160, size="small")
        messageToScreen("In this game we will work with the arrows. ", black, 0, -130, size="small")
        messageToScreen("To move up you need to press the up arrow. ", black, 0, -100, size="small")
        messageToScreen("To move down you need to press the down arrow. ", black, 0, -70, size="small")
        messageToScreen("To move left you need to press the left arrow.", black, 0, -40, size="small")
        messageToScreen("To move right you need to press the right arrow. ", black, 0, -10, size="small")
        messageToScreen("Just promise me that you'll be carfull , one touch in the border and you are done. ", black, 0,50, size="small")
        messageToScreen("To pasue the game press p. ", black, 0, 20, size="small")
        messageToScreen("Enjoy, Author: Zackuel", green, 0, 150, size="small")
        button("Back", "", 150, 500, 150, 50, light_purple, purple, action="back")
        button("Quit", "", 500, 500, 150, 50, light_purple, purple, action="quit")
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOver(dic)


## Retry screen,in case your Snake died because a collision ,Press Retry (same Name)

def retryScreen(score, name, playerNames):
    tmp=None
    #add to dic 
    if (name in playerNames and playerNames[name] < score) or (name not in playerNames):
        #If I have 10 players saved and the new Player with better score , I want to delete the lower score and keep the new  
        if len(playerNames) < 10:
            playerNames[name] = score
        else:
            playerNames=sortDict(playerNames)
            for player in playerNames.keys():
                if playerNames[player] < score:
                    tmp=player
            if tmp is not None:
                playerNames.pop(tmp)
                playerNames[name]=score
    while True:
        game.fill(white)
        messageToScreen("Game Over !!", green, -150, -250, size="large")
        messageToScreen("score: " + str(score), green, -150, -200, size="medium")
        messageToScreen("The Best:", black, -200, -75, size="medium")

        if playerNames is not None:
            playerNames = sortDict(playerNames)
            ln = list(playerNames.keys())
            if len(ln) > 5:
                size = 5
            else:
                size = len(ln)
            for i in range(size):
                messageToScreen("user: " + ln[i] + " score: " + str(playerNames[ln[i]]), black, -200, -25 + (i * 25),size="small")

        button("Retry", name, playerNames, 0, 450, 150, 50, light_purple, purple, action="lvl")
        button("Quit", "", playerNames, 350, 450, 150, 50, light_red, red, action="quit")

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOver(playerNames)


## First screen, giving the user options ( Choose Diff Level , See Description, Quit)

def startScreen():
    dic = readFromFile("usersSnake.txt")
    input_box = pygame.Rect(400, 290, 140, 32)
    text = ''
    text1 = ""
    active = True
    afterRe = False
    color = green
    
    while True:
        game.fill(white)
        messageToScreen("SnakeUela", green, 0, -100, size="large")
        if not afterRe:
            messageToScreen("Enter name:", green, -150, 0, size="medium")
            pygame.draw.rect(game, color, input_box, 2)
        else:
            messageToScreen("Hello " + text1 + " GoodLuck", green, -150, 0, size="medium")
        
        button("Select Level", text1, dic, 100, 450, 150, 50, light_purple, purple, action="lvl")
        button("Use Instructions", text1, dic, 300, 450, 200, 50, light_green, green, action="des")
        button("Quit", text1, dic, 550, 450, 150, 50, light_red, red, action="quit")
        txt_surface = pygame.font.Font(None, 32).render(text, True, black)
        
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width
        game.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOver(dic)
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user want to add his name
                if input_box.collidepoint(event.pos):
                    # active varibles
                    active = not active
                else:
                    active = False
                color = light_green if active else green
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        afterRe = True
                        text1 = text
                        text = ""
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
            


## Play screen, responsible for the Keys and run the game , create Object of Snake and Food. 

def startplay(fps1, level, name, dic):
    global pause
    win = pygame.display.set_mode((screenS_game, screenS_game))

    score = 0
    snake = Snake()
    foodsp = FoodSp()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOver(dic)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake.changeDirTo("LEFT")
                if event.key == pygame.K_RIGHT:
                    snake.changeDirTo("RIGHT")
                if event.key == pygame.K_DOWN:
                    snake.changeDirTo("DOWN")
                if event.key == pygame.K_UP:
                    snake.changeDirTo("UP")
                if event.key == pygame.K_p:
                    pause = True
                    paused(dic)
        foodPos = foodsp.spawnFood()
        if snake.move(foodPos):
            score += 1
            foodsp.setFoodOnSc(False)
        win.fill(white)
        for pos in snake.getbody():
            pygame.draw.rect(win, red, pygame.Rect(pos[0], pos[1], 10, 10))
        pygame.draw.rect(win, green, pygame.Rect(foodPos[0], foodPos[1], 10, 10))
        if snake.checkCollision():
            retryScreen(score, name, dic)
        pygame.display.set_caption("SnakeUela |user: " + name + " | score: " + str(score) + "  |  Level: " + level)
        pygame.display.flip()
        fps.tick(fps1)



## Create buttons , design them and their place. Also responsible in case of action

def button(text, name, dic, x, y, width, height, inactiveColor, activeColor, textColor=black, action=None):
    currentPos = pygame.mouse.get_pos()
    isPressed = pygame.mouse.get_pressed()
    difLev = 0
    if x + width > currentPos[0] > x and y + height > currentPos[1] > y:
        pygame.draw.rect(game, activeColor, (x, y, width, height))
        if isPressed[0] == 1 and action != None:
            if action == "quit":
                gameOver(dic)
            if action == "con":
                unpaused()
            if action == "des":
                game.fill(white)
                pygame.display.update()
                explainScreen(dic)
            if action == "lvl":
                if len(name) == 0:
                    messageToScreen("please enter name", black, 100, 0, size="small")
                else:
                    game.fill(white)
                    pygame.display.update()
                    levelScreen(name, dic)
            if action == "beginner":
                difLev = 12
                startplay(difLev, "Easy", name, dic)
            if action == "medium":
                difLev = 22
                startplay(difLev, "Medium", name, dic)
            if action == "expert":
                difLev = 32
                startplay(difLev, "Expert", name, dic)
            if action == "back":
                game.fill(white)
                pygame.display.update()
                startScreen()
            if action == "retry":
                game.fill(white)
                pygame.display.update()
                levelScreen(name, dic)

    else:
        pygame.draw.rect(game, inactiveColor, (x, y, width, height))
    text_to_button(text, textColor, x, y, width, height)


## Write text on the button
def text_to_button(msg, color, buttonX, buttonY, buttonWidth, buttonHeight, size="small"):
    textSurface, textRec = text_objects(msg, color, size)
    textRec.center = (buttonX + (int(buttonWidth / 2)), buttonY + (int(buttonHeight / 2)))
    game.blit(textSurface, textRec)


## Write Message on the screen
def messageToScreen(msg, color, x_displace=0, y_displace=0, size="small"):
    textSurface, textRec = text_objects(msg, color, size)
    textRec.center = ((int(screenS_width / 2)) + x_displace, y_displace + (int(screenS_height / 2)))
    game.blit(textSurface, textRec)

## Create the Font Size
def text_objects(text, color, size):
    if size == "small":
        textS = smallFont.render(text, True, color)
    elif size == "medium":
        textS = medFont.render(text, True, color)
    elif size == "large":
        textS = largeFont.render(text, True, color)

    return textS, textS.get_rect()


## Pause the game in the middle , and unpause when want to conitnue

def unpaused():
    global pause
    pause = False


def paused(dic):
    newwin = pygame.display.set_mode((screenS_game, screenS_game))
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOver(dic)
        newwin.fill(white)
        messageToScreen("Paused", black, -150, -200, size="large")
        button("Continue", "",dic, 175, 250, 150, 50, light_blue, blue, black, action="con")
        pygame.display.update()


## Game Over
def gameOver(dic):
    writeToFile("usersSnake.txt", len(dic), dic)
    pygame.quit()
    sys.exit()


## sort the dictionary by Score ,keep on the 10 best Players
def sortDict(dic):
    dict1 = {}
    li = [value for value in dic.values()]
    li = reversed(sorted(li))
    for i in li:
        for player in dic:
            if i == dic[player]:
                dict1[player] = i
    return dict1


## Save and Load from File , to keep the 10 best players .
def writeToFile(fileName, numOfPlayrs, dic):
    f = open(fileName, "w")
    f.write(str(numOfPlayrs))
    f.write("\n")
    for player in dic:
        f.write(player + " " + str(dic[player]))
        f.write("\n")

    f.close()


def readFromFile(fileName):
    if not os.path.exists(fileName):
        f = open(fileName, "x")
    dic = {}
    f = open(fileName, "r")
    if os.stat(fileName).st_size == 0:
        return {}
    size = int(f.readline())
    for i in range(int(size)):
        str1 = f.readline()
        li = str1.split()
        dic[li[0]] = int(li[1])
    f.close()
    return dic


                            #######SnakeUela Game######

class Snake:
## Initial the first position as (100,50),body size as 3 , start direction as Right  
    def __init__(self):  
        self.pos = [100, 50]
        self.body = [[100, 50], [90, 50], [80, 50]]
        self.dir = "RIGHT"
        self.chaDir = self.dir

    ## Change direction and check if user do something illegal , like going right and press left (illegal)
    def changeDirTo(self, dir1):
        if dir1 == "RIGHT" and not self.dir == "LEFT":
            self.dir = "RIGHT"
        if dir1 == "LEFT" and not self.dir == "RIGHT":
            self.dir = "LEFT"
        if dir1 == "UP" and not self.dir == "DOWN":
            self.dir = "UP"
        if dir1 == "DOWN" and not self.dir == "UP":
            self.dir = "DOWN"

    ## Move- change the position by adding or substract 10 from (x,y),when hit food then grow
    def move(self, foodpos):
        if self.dir == "RIGHT":
            self.pos[0] += 10
        if self.dir == "LEFT":
            self.pos[0] -= 10
        if self.dir == "UP":
            self.pos[1] -= 10
        if self.dir == "DOWN":
            self.pos[1] += 10
        self.body.insert(0, list(self.pos))
        if self.pos == foodpos:
            return 1
        else:
            self.body.pop()
            return 0

    ## Check collision(hit the bounderies)->dead
    def checkCollision(self):
        if self.pos[0] > 490 or self.pos[0] < 0:
            return 1
        if self.pos[1] > 490 or self.pos[1] < 0:
            return 1
        for bodypart in self.body[1:]:
            if self.pos == bodypart:
                return 1
        return 0

    def getpos(self):
        return self.pos

    def getbody(self):
        return self.body


                            ##############Food###############

class FoodSp:

## Set the food in a random place ,hold flag
    def __init__(self):  
        self.foodposit = [random.randrange(1, 50) * 10, random.randrange(1, 50) * 10]
        self.isFoodOnSc = True

## If there is no food on screen put some and change flag
    def spawnFood(self):
        if not self.isFoodOnSc:
            self.foodposit = [random.randrange(1, 50) * 10, random.randrange(1, 50) * 10]
            self.isFoodOnSc = True
        return self.foodposit

    def setFoodOnSc(self, B):
        self.isFoodOnSc = B

## Main
if __name__ == "__main__":
    startScreen()
