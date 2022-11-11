import sys
import pygame
from transformations import *
from cube import cube
from interface import *
from varstore import *
#from solver import *

pygame.font.init()
my_font = pygame.font.SysFont('Arial', 30)
Rubikcube = cube(uface, lface, fface, rface, bface, dface)
for items in ['ub','ul','uf','ur']: print(Rubikcube.edges[items])


lastinstance = getlastinstance(Rubikcube)

if __name__ == '__main__':
    window = pygame.display.set_mode((1000,800))
    window.fill(white)
    run = True
    pygame.display.flip()
    placecube(Rubikcube.cu, gridcoordinates,window,my_font)
    
    #maketurns(Rubikcube, ['UP', 'R2', 'L2', 'F2', 'B2', 'UP', 'R', 'L', 'F', 'BP', 'U', 'F2', 'D2', 'R2', 'L2', 'F2', 'U2', 'F2', 'UP', 'F2'])
    while run == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == K_r:
                    turnR(Rubikcube)
                if event.key == K_u:
                    turnU(Rubikcube)
                if event.key == K_d:
                    turnD(Rubikcube)
                if event.key == K_b:
                    turnB(Rubikcube)
                if event.key == K_l:
                    turnL(Rubikcube)
                if event.key == K_f:
                    turnF(Rubikcube)
                if event.key == K_0:
                    Rubikcube.shufflecube()
                if event.key == K_1:
                    Rubikcube.cubereset()
                print(Rubikcube.cu)

        
            
        #check if the cube has been updated//True then updates interface
        if lastinstance != Rubikcube.cu:
            placecube(Rubikcube.cu, gridcoordinates,window, my_font)
            lastinstance = getlastinstance(Rubikcube)
            
    pygame.quit()

    

