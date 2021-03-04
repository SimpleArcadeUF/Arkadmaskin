from libs.SimpleArcade import Game, Arcade, SpriteSheet
from libs.SimpleArcade.gui import Label
import pygame
import os
import random
from games.Faestone.Maps import devMap1 

gameScale=0.75
mapLoop = True
devMode = False
currentMap=devMap1.dev_Map

class Faestone(Game.Game):
    
    def __init__(self):
        super().__init__("Faestone", (pygame.image.load("res/images/logo.png")))

    def onPlay(self):
        ###Setting Vars and EddePie settings
        #Import sprites
        gameSpriteSheet=SpriteSheet.SpriteSheet("games/Faestone/Spritesheets/Normal.png",16)
        gameSpriteSheet.scaleImages(64*gameScale)
        #Map Tiles
        self.grassTile1=gameSpriteSheet.getImage(0,1) #ID:1
        #
        self.grassTile2=gameSpriteSheet.getImage(1,1)
        #
        self.grassTile3=gameSpriteSheet.getImage(2,1)
        #
        self.grassTile4=gameSpriteSheet.getImage(3,1)
        #
        self.stoneTile1=gameSpriteSheet.getImage(0,2) #ID: 2
        #
        self.stoneTile2=gameSpriteSheet.getImage(1,2)
        #
        self.stoneTile3=gameSpriteSheet.getImage(2,2) 
        #
        self.stoneTile4=gameSpriteSheet.getImage(3,2) #ID:3

        self.bushTile = gameSpriteSheet.getImage(2,3)
        #
        self.campFire1=gameSpriteSheet.getImage(1,4) #ID: 4
        #
        self.campFire2=gameSpriteSheet.getImage(2,4)
        #
        self.campFire3=gameSpriteSheet.getImage(3,4)
        #
        self.unlitCampfire=gameSpriteSheet.getImage(0,4) #ID: 5
        #
        self.unopenedChest=gameSpriteSheet.getImage(1,3) #ID: 6
        #
        self.openedChest=gameSpriteSheet.getImage(0,3) #ID: 7
        #
        self.caveExit=gameSpriteSheet.getImage(2,3) #ID: 8
        #
        self.darkness=gameSpriteSheet.getImage(2,0) #darkness for darkness purposes
        self.darkness=pygame.transform.scale(self.darkness, (int(320*gameScale/4), int(320*gameScale/4)))
        ##Characters
        #kobold
        self.koboldSprite=gameSpriteSheet.getImage(0,0)
        #ranger
        self.rangerSprite=gameSpriteSheet.getImage(1,0)
        #///#

        #creating player from class
        self.player=PlayerCharacter("Darabunga", [2,2], 12, 12, [], 30, self.rangerSprite)
        self.tileList = []

        self.lblFPS = Label.Label()
        self.lblFPS.addText("FPS: "+str(round(Arcade._FPS)), Arcade.FONT, (200,200,200), 50)


        self.tileObjectCreator(currentMap)

    def update(self, screen):
        pygame.draw.rect(screen, (0,0,0), (0, 0, Arcade.SCREEN_WIDTH*1.5*gameScale, Arcade.SCREEN_HEIGHT*1.5*gameScale))
        if(mapLoop==True):
            self.mapRenderer(screen, self.tileList)
            self.player.characterRenderer(screen)
            screen.blit(self.darkness, (self.player.currentLocation[0]*64*gameScale-128*gameScale, self.player.currentLocation[1]*64*gameScale-128*gameScale))
            self.player.key_Presses()
        if(devMode==True):
            pygame.draw.rect(screen, (60,60,60), (8,8,90,30))
            
            self.lblFPS.setText("FPS: "+str(round(Arcade._FPS)))
            self.lblFPS.update(screen)

    def mapRenderer(self, screen, tileObjectList):
        for Z in range(0,len(self.tileList)):
            if(tileObjectList[Z].X >= self.player.currentLocation[0]-2 and tileObjectList[Z].X <= self.player.currentLocation[0]+2):
                if(tileObjectList[Z].Y >= self.player.currentLocation[1]-2 and tileObjectList[Z].Y <= self.player.currentLocation[1]+2):
                    tileObjectList[Z].renderTile(screen)
        self.player.characterRenderer(screen)
    
    def tileObjectCreator(self, currentMap):
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
                        tileName=TileClass(X,Y,[self.stoneTile1,self.stoneTile2,self.stoneTile2],random.randint(0,2),self.tileList)
                    #
                    if(currentRow[X]==2): #grass
                        tileName=TileClass(X,Y,[self.grassTile1,self.grassTile2,self.grassTile3,self.grassTile4],random.randint(0,3),self.tileList)
                    #
                if(currentRow[X]==3 or currentRow[X]==5 or currentRow[X]==6 or currentRow[X]==7 or currentRow[X]==8): #Not animated, not seeded
                    #
                    if(currentRow[X]==3): #bush
                        tileName=TileClass(X,Y,[self.bushTile],-1,self.tileList)
                    #
                    if(currentRow[X]==5): #unlit campfire
                        tileName=TileClass(X,Y,[self.unlitCampfire],-1,self.tileList)
                    #
                    if(currentRow[X]==6): #unopened chest
                        tileName=TileClass(X,Y,[self.unopenedChest],-1,self.tileList)
                    #
                    if(currentRow[X]==7): #opened chest
                        tileName=TileClass(X,Y,[self.openedChest],-1,self.tileList)
                    #
                    if(currentRow[X]==8): #cave exit
                        tileName=TileClass(X,Y,[self.caveExit],-1,self.tileList)
                    #
                if(currentRow[X]==4): #Animated, not seeded
                    #
                    if(currentRow[X]==4): #Campfire
                        tileName=TileClass(X,Y,[self.campFire1, self.campFire2, self.campFire3],-1,self.tileList)


##Tile
class TileClass():
    def __init__(self, X, Y, textures, seed, mapTileList):
        self.X=int(X)
        self.Y=int(Y)
        self.seed=seed
        self.textures=list(textures)
        mapTileList.append(self)
    def renderTile(self, screen):
        if(len(self.textures)==1): #Non-animated un-seeded tiles
            screen.blit(self.textures[0], (self.X*64*gameScale,self.Y*64*gameScale))
        elif(self.seed!= -1): #Non-animated seeded tiles
            screen.blit(self.textures[self.seed], (self.X*64*gameScale,self.Y*64*gameScale))
        else: #Animated tiles
            textureRand=random.randint(0,len(self.textures))
            imageToDraw=self.textures[textureRand-1]
            screen.blit(imageToDraw, (self.X*64*gameScale,self.Y*64*gameScale))
    def changeTileTexture(self,newTexture):
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
        self.WIsPressed = False
        self.SIsPressed = False
        self.AIsPressed = False
        self.DIsPressed = False

    def setCoordinates(self, newX, newY):
        self.currentLocation=[newX, newY]
    def characterRenderer(self, screen):
        screen.blit(self.characterSprite, (self.currentLocation[0]*64*gameScale,self.currentLocation[1]*64*gameScale))
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
    
    def isObstructed(self, currentX, currentY, Heading):
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
    def key_Presses(self):
        if(mapLoop==True):
            if(pygame.mouse.get_pressed()[0]==True):
                pass
                #changeTile(2, 2, 5)
            if(pygame.mouse.get_pressed()[1]==True):
                pass
                #changeTile(2, 2, 8)
            keys = pygame.key.get_pressed()
            if(keys[pygame.K_w] and self.WIsPressed==False):
                self.moveCharacter("N")
                self.WIsPressed=True
            elif(keys[pygame.K_w]==False):
                self.WIsPressed=False
            if(keys[pygame.K_a] and self.AIsPressed==False):
                self.moveCharacter("W")
                self.AIsPressed=True
            elif(keys[pygame.K_a]==False):
                self.AIsPressed=False
            if(keys[pygame.K_s] and self.SIsPressed==False):
                self.moveCharacter("S")
                self.SIsPressed=True
            elif(keys[pygame.K_s]==False):
                self.SIsPressed=False
            if(keys[pygame.K_d] and self.DIsPressed==False):
                self.moveCharacter("E")
                self.DIsPressed=True
            elif(keys[pygame.K_d] ==False):
                self.DIsPressed=False
    def gameEvent(self, type): #1:Chest, 2: Combat, 3: New level,
        pass