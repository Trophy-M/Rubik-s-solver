import sys
import pygame
from pygame.locals import *
from interface import *
import collections

gridcoordinates = [[350,400,450,350,400,450,350,400,450],[50,50,50,100,100,100,150,150,150]]
def placecube(face, pos):
    posx = pos[0]
    posy = pos[1]
    width = 50; height = 50
    match face:
        case 'u':
            color = white
            transformx, transformy = 0,0
        case 'l':
            color = green
            transformx, transformy = -150,150
        case 'f':
            color = red
            transformx, transformy = 0,150
        case 'r':
            color = blue
            transformx, transformy = 150,150
        case 'b':
            color = orange
            transformx, transformy = 300,150
        case 'd':
            color = yellow
            transformx, transformy = 0,300
    
    for i in range (0,len(posx)):
        x = posx[i] + transformx
        y = posy[i] + transformy
        pygame.draw.rect(window, color,(x,y ,width, height))
        pygame.draw.rect(window, black,(x,y ,width, height),2)
        pygame.display.update()



'''def placeface(gridcoordinates, pos1, pos2):
    for m,x in enumerate(gridcoordinates):
        for n,y in enumerate(x):  
            y += vars('pos' +str(m+1))
            gridcoordinates[n] = y
        print(gridcoordinates)
        return gridcoordinates

#display the cube in solved state
def initcube():
    gridcoordinates = [[450,500,550,450,500,550,450,500,550],[50,50,50,100,100,100,150,150,150]]
    placecube('u',gridcoordinates)
    placeface(gridcoordinates, -150, 100)'''

def initialisecube(Rubikcube):
    print('initialised')
    for items in Rubikcube:
            for c,x in enumerate(items):
                placecube(x[0],gridcoordinates)

'''def updatecube(old,new):
    if old != new:
        initialisecube(new)
        old = new
    return old'''


if __name__ == '__main__':
    window = pygame.display.set_mode((1000,800))
    window.fill(white)
    run = True
    pygame.display.flip()
    initialisecube(Rubikcube.cu)
    while run == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == K_r:
                    print(Rubikcube.lastinstance != Rubikcube.cu)
                    Rubikcube.turnR()
                    Rubikcube.lastinstance != Rubikcube.cu
                    print('r')
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
        if Rubikcube.lastinstance != Rubikcube.cu:
            initialisecube(Rubikcube.cu)
            

        
    pygame.quit()
    

