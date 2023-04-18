'''
This file contains class pocketcube which contains information about the 2x2 cube and its functions. It uses copy library to
deep copy an array within an array. This is to prevent separate arrays from affecting each other.
'''

#2x2 cube called pocket cube
import pygame
import random
import copy
import ast

class pocketcube:
    def __init__(self, cu):
        #data structure is [[a,b,c,d],[a,b,c,d],[a,b,c,d],[a,b,c,d],[a,b,c,d],[a,b,c,d]]; (u,l,f,r,b,d)
        self.cu = cu
    
    #rotates a 2x2 array cw
    def rotpocket(self,arr):
        arr[1], arr[3], arr[0], arr[2] = arr[0], arr[1], arr[2], arr[3]
        return arr
    
    #returns a facelet given its face and position
    def returnfacelet(self, face, position):
        return self.cu[face][position]

    #Reset the cube back to solved state
    def resetcube(self):
        self.cu = [['u1', 'u2', 'u3', 'u4']
        ,['l1', 'l2', 'l3', 'l4']
        ,['f1', 'f2', 'f3', 'f4']
        ,['r1', 'r2', 'r3', 'r4']
        ,['b1', 'b2', 'b3', 'b4']
        ,['d1', 'd2', 'd3', 'd4']].copy()
    
    #check if cube is solved
    def isSolved(self):
        if self.cu == [['u1', 'u2', 'u3', 'u4']
        ,['l1', 'l2', 'l3', 'l4']
        ,['f1', 'f2', 'f3', 'f4']
        ,['r1', 'r2', 'r3', 'r4']
        ,['b1', 'b2', 'b3', 'b4']
        ,['d1', 'd2', 'd3', 'd4']]:
            return True
        else:
            return False
    
    def logstate(self):
        self.cubelog = open('pocketlog.txt','w')
        for rows in self.cu:
            self.cubelog.writelines(str(rows) + '\n')
        self.cubelog.close()
    
    def loadstate(self):
        self.cubelog = open('pocketlog.txt','r')
        cubestate = []
        for lines in self.cubelog: 
            cubestate.append(ast.literal_eval(lines[0:-1]))
        self.cu = copy.deepcopy(cubestate)

    #return self.cu
    def returnstate(self):
        return self.cu
    
    #Perform various faces turn on the cube
    def transformation(self, moves):
        for transform in moves:
            transform = transform.lower()
            match transform:
                case 'u':
                    self.rotpocket(self.cu[0])
                    tempf = self.cu[2][0], self.cu[2][1]
                    templ = self.cu[1][0], self.cu[1][1]
                    tempr = self.cu[3][0], self.cu[3][1]
                    tempb = self.cu[4][0], self.cu[4][1]

                    templ, tempb,tempf, tempr = tempf,templ,tempr,tempb
                    self.cu[2][0], self.cu[2][1] = tempf
                    self.cu[1][0], self.cu[1][1] = templ
                    self.cu[3][0], self.cu[3][1] = tempr
                    self.cu[4][0], self.cu[4][1] = tempb
                case 'l':
                    self.rotpocket(self.cu[1])
                    tempf = self.cu[2][0], self.cu[2][2]
                    tempd = self.cu[5][0], self.cu[5][2]
                    tempu = self.cu[0][0], self.cu[0][2]
                    tempb = self.cu[4][1], self.cu[4][3]

                    tempd,tempb,tempf,tempu = tempf,tempd,tempu,tempb
                    self.cu[2][0], self.cu[2][2] = tempf
                    self.cu[5][0], self.cu[5][2] = tempd
                    self.cu[0][2], self.cu[0][0] = tempu
                    self.cu[4][3], self.cu[4][1] = tempb
                case 'f':
                    self.rotpocket(self.cu[2])
                    tempd = self.cu[5][0], self.cu[5][1]
                    tempu = self.cu[0][2], self.cu[0][3]
                    templ = self.cu[1][1], self.cu[1][3]
                    tempr = self.cu[3][0], self.cu[3][2]

                    templ, tempr,tempu,tempd = tempd,tempu,templ,tempr
                    self.cu[5][1], self.cu[5][0] = tempd
                    self.cu[0][3], self.cu[0][2] = tempu
                    self.cu[1][1], self.cu[1][3] = templ
                    self.cu[3][0], self.cu[3][2] = tempr
                case 'r':
                    self.rotpocket(self.cu[3])
                    tempf = self.cu[2][1], self.cu[2][3]
                    tempd = self.cu[5][1], self.cu[5][3]
                    tempu = self.cu[0][1], self.cu[0][3]
                    tempb = self.cu[4][0], self.cu[4][2]

                    tempu ,tempf, tempb, tempd = tempf,tempd,tempu,tempb
                    self.cu[2][1], self.cu[2][3] = tempf
                    self.cu[5][3], self.cu[5][1] = tempd
                    self.cu[0][1], self.cu[0][3] = tempu
                    self.cu[4][2], self.cu[4][0] = tempb
                case 'b':
                    self.rotpocket(self.cu[4])
                    tempd = self.cu[5][2], self.cu[5][3]
                    tempu = self.cu[0][0], self.cu[0][1]
                    templ = self.cu[1][0], self.cu[1][2]
                    tempr = self.cu[3][1], self.cu[3][3]

                    tempd,tempu,templ,tempr = templ,tempr,tempu,tempd
                    self.cu[5][2], self.cu[5][3] = tempd
                    self.cu[0][0], self.cu[0][1] = tempu
                    self.cu[1][2], self.cu[1][0] = templ
                    self.cu[3][3], self.cu[3][1] = tempr
                case 'd':
                    self.rotpocket(self.cu[5])
                    tempf = self.cu[2][2], self.cu[2][3]
                    templ = self.cu[1][2], self.cu[1][3]
                    tempr = self.cu[3][2], self.cu[3][3]
                    tempb = self.cu[4][2], self.cu[4][3]

                    tempr,tempf,tempb,templ = tempf,templ,tempr,tempb
                    self.cu[2][2], self.cu[2][3] = tempf
                    self.cu[1][2], self.cu[1][3] = templ
                    self.cu[3][2], self.cu[3][3] = tempr
                    self.cu[4][2], self.cu[4][3 ] = tempb
                case 'u2':
                    for i in range(0,2): self.transformation('u')
                case 'l2':
                    for i in range(0,2): self.transformation('l')
                case 'f2':
                    for i in range(0,2): self.transformation('f')
                case 'r2':
                    for i in range(0,2): self.transformation('r')
                case 'b2':
                    for i in range(0,2): self.transformation('b')
                case 'd2':
                    for i in range(0,2): self.transformation('d')
                case 'up':
                    for i in range(0,3): self.transformation('u')
                case 'lp':
                    for i in range(0,3): self.transformation('l')
                case 'fp':
                    for i in range(0,3): self.transformation('f')
                case 'rp':
                    for i in range(0,3): self.transformation('r')
                case 'bp':
                    for i in range(0,3): self.transformation('b')
                case 'd2':
                    for i in range(0,3): self.transformation('d')
    
    #Display the pocket cube given its position, font, and window surface
    def placepocket(self, pos,window,my_font):
        red = (255,0,0)
        green = (0,255,0)
        blue = (0,0,255)
        orange = (255, 165, 0)
        white = (255,255,255)
        yellow = (255,255,0)
        black = (0,0,0)
        posx = pos[0]
        posy = pos[1]
        width = 50; height = 50
        for c,items in enumerate(self.cu):
            for d,jtems in enumerate(items):
                position = (c*4) + d + 1
                if position <= 4:
                    transformx,transformy = 0,0
                elif position <= 8:
                    transformx,transformy = -100,100
                elif position <= 12:
                    transformx,transformy = 0,100
                elif position <= 16:
                    transformx,transformy = 100,100
                elif position <= 20:
                    transformx,transformy = 200,100
                elif position <= 24:
                    transformx,transformy = 0,200
            
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
        
        
                x = posx[d] + transformx + 150
                y = posy[d] + transformy + 100
                pygame.draw.rect(window, color,(x,y ,width, height))
                pygame.draw.rect(window, black,(x,y ,width, height),2)
                text_surface = my_font.render(str(int(jtems[1])), False, (0, 0, 0))
                window.blit(text_surface, (x+10,y))
                pygame.display.update()

    #Shuffles the cube
    def shufflecube(self):
        times = random.randint(50, 100)
        randommoves = []
        for i in range(0, times):
            #Generates a random list containing random moves
            randommoves.append(random.choice(['u','l','f','r','b','d','u2','l2','f2','r2','b2','d2','up','lp','fp','rp','bp','dp']))
        self.transformation(randommoves)




            
            
                



