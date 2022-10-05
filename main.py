import sys
import pygame
from pygame.locals import *
from varstore import * 
import collections

pygame.font.init()
my_font = pygame.font.SysFont('Arial', 30)

#store the dynamic attribute value
def getlastinstance(Rubikcube):
    lastinstance = []
    for x in Rubikcube.cu:
        lastface = []
        for y in x:
            lastface.append(y)
        lastinstance.append(lastface)
    return lastinstance
    
#places color in the window according to their position in the array (face) and subarray (1-9)
def placecube(Rubikcube, pos):
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
            text_surface = my_font.render(str(jtems[1]), False, (0, 0, 0))
            window.blit(text_surface, (x+10,y))
            pygame.display.update()


lastinstance = getlastinstance(Rubikcube)

if __name__ == '__main__':
    window = pygame.display.set_mode((1000,800))
    window.fill(white)
    run = True
    pygame.display.flip()
    placecube(Rubikcube.cu, gridcoordinates)
    while run == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == K_r:
                    Rubikcube.turnR()
                if event.key == K_u:
                    Rubikcube.turnU()
                if event.key == K_d:
                    Rubikcube.turnD()
                if event.key == K_b:
                    Rubikcube.turnB()
                if event.key == K_l:
                    Rubikcube.turnL()
                if event.key == K_f:
                    Rubikcube.turnF()
                if event.key == K_0:
                    Rubikcube.shufflecube()
                if event.key == K_1:
                    Rubikcube.cubereset()
            
            #check if the cube has been updated//True then updates interface
            if lastinstance != Rubikcube.cu:
                placecube(Rubikcube.cu, gridcoordinates)
                lastinstance = getlastinstance(Rubikcube)


    pygame.quit()
    

