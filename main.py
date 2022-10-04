import sys
import pygame
from pygame.locals import *
from interface import *
import collections

pygame.font.init()
my_font = pygame.font.SysFont('Arial', 30)
gridcoordinates = [[350,400,450,350,400,450,350,400,450],[50,50,50,100,100,100,150,150,150]]

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
                    print(Rubikcube.cu)
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
                
                placecube(Rubikcube.cu, gridcoordinates)
                #pygame.display.flip()


    pygame.quit()
    

