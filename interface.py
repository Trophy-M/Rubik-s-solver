import pygame
import time
from varstore import *
from pygame.locals import *

def getlastinstance(Rubikcube):
    lastinstance = []
    for x in Rubikcube.cu:
        lastface = []
        for y in x:
            lastface.append(y)
        lastinstance.append(lastface)
    return lastinstance
    
#places color in the window according to their position in the array (face) and subarray (1-9)
def placecube(Rubikcube, pos,window,my_font):
    posx = pos[0]
    posy = pos[1]
    width = 50; height = 50
    for c,items in enumerate(Rubikcube):
        for d,jtems in enumerate(items):
            position = (c*9) + d + 1
            if position <= 9:
                transformx,transformy = 0,0
            elif position <= 18:
                transformx,transformy = -150,150
            elif position <= 27:
                transformx,transformy = 0,150
            elif position <= 36:
                transformx,transformy = 150,150
            elif position <= 45:
                transformx,transformy = 300,150
            elif position <= 54:
                transformx,transformy = 0,300
        
            match jtems[0]:
                case 'u':
                    color = white
                case 'l':
                    color = green
                case 'f':
                    color = red
                case 'r':
                    color = blue
                case 'b':
                    color = orange
                case 'd':
                    color = yellow         
    
    
            x = posx[d] + transformx
            y = posy[d] + transformy
            pygame.draw.rect(window, color,(x,y ,width, height))
            pygame.draw.rect(window, black,(x,y ,width, height),2)
            text_surface = my_font.render(str(int(jtems[1])), False, (0, 0, 0))
            window.blit(text_surface, (x+10,y))
            pygame.display.update()
def displaycube(Rubikcube, delay):
    Rubikcube.updatedata()
    gridcoordinates = [[350,400,450,350,400,450,350,400,450],[50,50,50,100,100,100,150,150,150]]
    my_font = pygame.font.SysFont('Arial', 30)
    window = pygame.display.set_mode((1000,800))
    window.fill(white)
    time.sleep(delay)
    placecube(Rubikcube.cu,gridcoordinates, window, my_font)
