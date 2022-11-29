import sys
import pygame
from transformations import *
from cube import cube
from interface import *
from beginnersolver import *
import time
from varstore import *
#from solver import *

uface = ['u1', 'u2', 'u3', 'u4', 'u5', 'u6', 'u7', 'u8', 'u9']
lface = ['l1', 'l2', 'l3', 'l4', 'l5', 'l6', 'l7', 'l8', 'l9']
fface = ['f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9']
rface = ['r1', 'r2', 'r3', 'r4', 'r5', 'r6', 'r7', 'r8', 'r9']
bface = ['b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'b9']
dface = ['d1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9']

pygame.font.init()
my_font = pygame.font.SysFont('Arial', 30)
Rubikcube = cube(uface, lface, fface, rface, bface, dface)


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
                if event.key == K_x:
                    rotcube(Rubikcube,'x')
                if event.key == K_y:
                    rotcube(Rubikcube,'y')
                if event.key == K_z:
                    rotcube(Rubikcube,'z')
        
            
        #check if the cube has been updated//True then updates interface
        if lastinstance != Rubikcube.cu:
            placecube(Rubikcube.cu, gridcoordinates,window, my_font)
            lastinstance = getlastinstance(Rubikcube)
            
    pygame.quit()

    

