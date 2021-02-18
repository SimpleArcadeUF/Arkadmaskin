from libs.SimpleArcade import Game, Arcade, SpriteSheet
import pygame
from games.Faestone import HutoPie as game
import os
import random
from games.Faestone.Maps import devMap1 

class Faestone(Game.Game):

    def __init__(self):
        super().__init__("Faestone", (pygame.image.load("res/images/logo.png")))

    def onPlay(self):
        ###Setting Vars and EddePie settings
        self.currentMap=devMap1.dev_Map
        self.gameScale=1
        game.init("PieRangers", int(Arcade.SCREEN_WIDTH*1.5*self.gameScale), int(Arcade.SCREEN_HEIGHT*1.5*self.gameScale))
        game.MAX_FPS=120
        #Import sprites
        gameSpriteSheet=SpriteSheet.SpriteSheet("games/Faestone/Spritesheets/Normal.png",16)
        gameSpriteSheet.scaleImages(64*self.gameScale)
        #Map Tiles
        grassTile1=gameSpriteSheet.getImage(0,1) #ID:1
        #
        grassTile2=gameSpriteSheet.getImage(1,1)
        #
        grassTile3=gameSpriteSheet.getImage(2,1)
        #
        grassTile4=gameSpriteSheet.getImage(3,1)
        #
        stoneTile1=gameSpriteSheet.getImage(0,2) #ID: 2
        #
        stoneTile2=gameSpriteSheet.getImage(1,2)
        #
        stoneTile3=gameSpriteSheet.getImage(2,2) 
        #
        bushTile=gameSpriteSheet.getImage(3,2) #ID:3
        #
        campFire1=gameSpriteSheet.getImage(1,4) #ID: 4
        #
        campFire2=gameSpriteSheet.getImage(2,4)
        #
        campFire3=gameSpriteSheet.getImage(3,4)
        #
        unlitCampfire=gameSpriteSheet.getImage(0,4) #ID: 5
        #
        unopenedChest=gameSpriteSheet.getImage(1,3) #ID: 6
        #
        openedChest=gameSpriteSheet.getImage(0,3) #ID: 7
        #
        caveExit=gameSpriteSheet.getImage(2,3) #ID: 8
        #
        darkness=gameSpriteSheet.getImage(0,2) #darkness for darkness purposes
        darkness=pygame.transform.scale(darkness, (int(320*self.gameScale/4), int(320*self.gameScale/4)))
        ##Characters
        #kobold
        koboldSprite==gameSpriteSheet(0,0)
        koboldSprite=game.scaleImage(koboldSprite, int(64*self.gameScale), int(64*self.gameScale))
        #ranger
        rangerSprite==gameSpriteSheet(0,1)
        rangerSprite=game.scaleImage(rangerSprite, int(64*self.gameScale), int(64*self.gameScale))
        #///#

        #creating player from class
        player=PlayerCharacter("Darabunga", [2,2], 12, 12, [], 30, rangerSprite)

        #Game Loop
        if(game.isRunning()==True):
            print("Game is Running")
        else:
            print("Game isn't running")

        font = game.getFont("arial", 20)

        tileObjectCreator(currentMap)

    def update(self, screen):
        game.drawRect(0, 0, screenWidth*1.5*self.gameScale, screenHeight*1.5*self.gameScale, [0,0,0])
        if(mapLoop==True):
            mapRenderer(tileList)
            player.characterRenderer()
            game.drawImage(player.currentLocation[0]*64*self.gameScale-128*self.gameScale, player.currentLocation[1]*64*self.gameScale-128*self.gameScale, darkness)
        key_Presses()
        if(devMode==True):
            game.drawRect(8,8,90,30, [60,60,60])
            text = game.createText("FPS: "+str(round(game.FPS)), font, (200,200,200))
            game.drawText(10,10, text)

    def mapRenderer(tileObjectList):
        for Z in range(0,len(tileList)):
            if(tileObjectList[Z].X >= player.currentLocation[0]-2 and tileObjectList[Z].X <= player.currentLocation[0]+2):
                if(tileObjectList[Z].Y >= player.currentLocation[1]-2 and tileObjectList[Z].Y <= player.currentLocation[1]+2):
                    tileObjectList[Z].renderTile()
        player.characterRenderer()
    
    def tileObjectCreator(currentMap):
        for Y in range(0, len(currentMap)):
            currentRow=currentMap[Y]
            for X in range(0, len(currentRow)):
                tileName=str(str(X)+"x_"+str(Y)+"y")
                #
                if(currentRow[X==0]): #Empty Tile
                    pass
                #
                if(currentRow[X]==1 or currentRow[X]==2): #Not animated, seeded
                    #
                    if(currentRow[X]==1):#Stone
                        tileName=TileClass(X,Y,[stoneTile1,stoneTile2,stoneTile2],random.randint(0,2),tileList)
                    #
                    if(currentRow[X]==2): #grass
                        tileName=TileClass(X,Y,[grassTile1,grassTile2,grassTile3,grassTile4],random.randint(0,3),tileList)
                    #
                if(currentRow[X]==3 or currentRow[X]==5 or currentRow[X]==6 or currentRow[X]==7 or currentRow[X]==8): #Not animated, not seeded
                    #
                    if(currentRow[X]==3): #bush
                        tileName=TileClass(X,Y,[bushTile],-1,tileList)
                    #
                    if(currentRow[X]==5): #unlit campfire
                        tileName=TileClass(X,Y,[unlitCampfire],-1,tileList)
                    #
                    if(currentRow[X]==6): #unopened chest
                        tileName=TileClass(X,Y,[unopenedChest],-1,tileList)
                    #
                    if(currentRow[X]==7): #opened chest
                        tileName=TileClass(X,Y,[openedChest],-1,tileList)
                    #
                    if(currentRow[X]==8): #cave exit
                        tileName=TileClass(X,Y,[caveExit],-1,tileList)
                    #
                if(currentRow[X]==4): #Animated, not seeded
                    #
                    if(currentRow[X]==4): #Campfire
                        tileName=TileClass(X,Y,[campFire1, campFire2, campFire3],-1,tileList)


##Tile
class TileClass():
    def __init__(self, X, Y, textures, seed, mapTileList):
        self.X=int(X)
        self.Y=int(Y)
        self.seed=seed
        self.textures=list(textures)
        mapTileList.append(self)
    def renderTile(self):
        if(len(self.textures)==1): #Non-animated un-seeded tiles
            game.drawImage(self.X*64*self.gameScale,self.Y*64*self.gameScale,self.textures[0])
        elif(self.seed!= -1): #Non-animated seeded tiles
            game.drawImage(self.X*64*self.gameScale,self.Y*64*self.gameScale, self.textures[self.seed])
        else: #Animated tiles
            textureRand=random.randint(0,len(self.textures))
            imageToDraw=self.textures[textureRand-1]
            game.drawImage(self.X*64*self.gameScale,self.Y*64*self.gameScale,imageToDraw)
    def changeTileTexture(newTexture):
        self.texture=newTexture

##PlayerCharacter
class PlayerCharacter():
    def __init__(self, name, currentLocation, hitPoints, maxhitPoints, inventory, gold, characterSprite):
        self.name=name
        self.currentLocation=currentLocation
        self.hitPoints=hitPoints
        self.maxhitPoints=maxhitPoints
        self.inventory=inventory
        self.gold=gold
        self.characterSprite=characterSprite
    def setCoordinates(self, newX, newY):
        self.currentLocation=[newX, newY]
    def characterRenderer(self):
        game.drawImage(self.currentLocation[0]*64*self.gameScale,self.currentLocation[1]*64*self.gameScale, self.characterSprite)
    def getCoordinates(self):
        return(self.currentLocation[0],self.currentLocation[1])
    def moveCharacter(self, direction): #Moves character in one of four cardinal directions. west, north, east, south
        direction=direction.upper()
        if(direction=="N" and self.isObstructed(self.currentLocation[0],self.currentLocation[1], "N")==False):
            self.setCoordinates(self.currentLocation[0], self.currentLocation[1]-1)
            # print("slide to the NORTH")
        if(direction=="W" and self.isObstructed(self.currentLocation[0],self.currentLocation[1], "W")==False):
            self.setCoordinates(self.currentLocation[0]-1, self.currentLocation[1])
            # print("slide to the WEST")
        if(direction=="E" and self.isObstructed(self.currentLocation[0],self.currentLocation[1], "E")==False):
            self.setCoordinates(self.currentLocation[0]+1, self.currentLocation[1])
            # print("slide to the EAST")
        if(direction=="S" and self.isObstructed(self.currentLocation[0],self.currentLocation[1], "S")==False):
            self.setCoordinates(self.currentLocation[0], self.currentLocation[1]+1)
            # print("slide to the SOUTH")    
    def isObstructed(currentX, currentY, Heading):
        print(currentY, currentX)
        if(Heading=="N"):
            if(currentMap[currentY-1][currentX]==1 or currentMap[currentY-1][currentX]==3):
                return(True)
            else:
                return(False)
        elif(Heading=="W"):
            if(currentMap[currentY][currentX-1]==1 or currentMap[currentY][currentX-1]==3): 
                return(True)
            else:
                return(False)
        elif(Heading=="S"):
            if(currentMap[currentY+1][currentX]==1 or currentMap[currentY+1][currentX]==3):
                return(True)
            else:
                return(False)
        elif(Heading=="E"):
            if(currentMap[currentY][currentX+1]==1 or currentMap[currentY][currentX+1]==3):
                return(True)
            else:
                return(False)
    def key_Presses():
        if(mapLoop==True):
            if(game.isLeftMouseDown()==True):
                pass
                #changeTile(2, 2, 5)
            if(game.isRightMouseDown()==True):
                pass
                #changeTile(2, 2, 8)
            if(game.isKeyDown(game.K_W) and WIsPressed==False):
                player.moveCharacter("N")
                WIsPressed=True
            elif(game.isKeyDown(game.K_W)==False):
                WIsPressed=False
            if(game.isKeyDown(game.K_A) and AIsPressed==False):
                player.moveCharacter("W")
                AIsPressed=True
            elif(game.isKeyDown(game.K_A)==False):
                AIsPressed=False
            if(game.isKeyDown(game.K_S) and SIsPressed==False):
                player.moveCharacter("S")
                SIsPressed=True
            elif(game.isKeyDown(game.K_S)==False):
                SIsPressed=False
            if(game.isKeyDown(game.K_D) and DIsPressed==False):
                player.moveCharacter("E")
                DIsPressed=True
            elif(game.isKeyDown(game.K_D)==False):
                DIsPressed=False
    def gameEvent(type): #1:Chest, 2: Combat, 3: New level,
        pass