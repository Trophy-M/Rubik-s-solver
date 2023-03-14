import pygame
import time
from varstore import *
import transformations
import cube
import beginnersolver
from pygame.locals import *
import pocketcube
import pocketcubesolver
import copy


class Button():
    #x and y defines the position and sf defines the image scale factor
    def __init__(self,x,y,image,sf):
        img_width = image.get_width()
        img_height = image.get_height()
        self.image = pygame.transform.scale(image, (int(img_width*sf),int(img_height*sf)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False

    def initialise(self,window):
        mousepos = pygame.mouse.get_pos()
        beenclicked = False

        if self.rect.collidepoint(mousepos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                beenclicked = True
                self.clicked = beenclicked

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        window.blit(self.image, (self.rect.x, self.rect.y))
        return beenclicked      

def displaytext(text, coordinate, font, size,window,color):
    my_font = pygame.font.SysFont(font, size)
    displayedtext = my_font.render(text,True,color)
    window.blit(displayedtext, coordinate)


    
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
    
    
            x = posx[d] + transformx + 150
            y = posy[d] + transformy + 100
            pygame.draw.rect(window, color,(x,y ,width, height))
            pygame.draw.rect(window, black,(x,y ,width, height),2)
            text_surface = my_font.render(str(int(jtems[1])), False, (0, 0, 0))
            window.blit(text_surface, (x+10,y))
            pygame.display.update()
def solvingcubedisplay(Rubikcube, delay):
    Rubikcube.updatedata()
    gridcoordinates = [[350,400,450,350,400,450,350,400,450],[50,50,50,100,100,100,150,150,150]]
    my_font = pygame.font.SysFont('Open Sans', 30)
    window = pygame.display.set_mode((1280,720))
    window.fill(white)
    displaytext('Solving...', (450,50),'Open Sans',60,window,(0,0,0))
    time.sleep(delay)
    placecube(Rubikcube.cu,gridcoordinates, window, my_font)

#In this mode, players can freely interact with the cube 
def Rubikinteract():
    clock = pygame.time.Clock()
    run = True
    window = pygame.display.set_mode((1280,720))
    window.fill(white)
    displaytext('Freeplay mode', (450,50),'Open Sans',60,window,(0,0,0))
    cube_font = pygame.font.SysFont('Open Sans', 30)
    pygame.display.flip()
    quitbtn = Button(300,450,(pygame.image.load('images/button_quit.png').convert_alpha()),1)
    solvebtn = Button(600,450,(pygame.image.load('images/button_solve.png').convert_alpha()),1)
    Rubikcube = beginnersolver.beginnersolver([['u1', 'u2', 'u3', 'u4', 'u5', 'u6', 'u7', 'u8', 'u9']
    ,['l1', 'l2', 'l3', 'l4', 'l5', 'l6', 'l7', 'l8', 'l9']
    ,['f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9']
    ,['r1', 'r2', 'r3', 'r4', 'r5', 'r6', 'r7', 'r8', 'r9']
    ,['b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'b9']
    ,['d1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9']])
    placecube(Rubikcube.cu,[[350,400,450,350,400,450,350,400,450],[50,50,50,100,100,100,150,150,150]], window, cube_font)
    returnbtn = Button(500,620,(pygame.image.load('images/button_return.png').convert_alpha()),1)
    while run:
        if returnbtn.initialise(window):
            run = False
            returnmenubool = True
        clock.tick(40)
        placecube(Rubikcube.cu,[[350,400,450,350,400,450,350,400,450],[50,50,50,100,100,100,150,150,150]], window, cube_font)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                menu()
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
                if event.key == K_s:
                    Rubikcube.solvecube()
                if event.key == K_0:
                    Rubikcube.shufflecube()
                if event.key == K_1:
                    Rubikcube.cubereset()
                if event.key == K_x:
                    Rubikcube.rotcube('x')
                if event.key == K_y:
                    Rubikcube.rotcube('y')
                if event.key == K_z:
                    Rubikcube.rotcube('z')

    if returnmenubool == True:
        menu()
def instructionscreen():
    clock = pygame.time.Clock()
    run = True
    window = pygame.display.set_mode((1280,720))
    window.fill(white)
    displaytext('Instructions', (450,50),'Open Sans',60,window,(255,0,0))
    displaytext('Press U/L/F/R/D/B to turn U/L/F/R/D/B faces', (450,100),'Open Sans',30,window,(0,0,0))
    displaytext('Press S to solve the cube', (450,150),'Open Sans',30,window,(0,0,0))
    displaytext('Press 0 to scramble the cube', (450,200),'Open Sans',30,window,(0,0,0))
    displaytext('Press 1 to reset the cube', (450,250),'Open Sans',30,window,(0,0,0))
    displaytext('Press enter to continue', (450,300),'Open Sans',30,window,(0,0,100))
    rubiklogo = pygame.transform.scale((pygame.image.load('images/rubik_logo.png').convert_alpha()), (int(1200*0.25),int(1200*0.25)))
    window.blit(rubiklogo, (450, 350))
    pygame.display.flip() 
    while run:
        clock.tick(40)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == K_RETURN:
                    run = False

        

def Pocketinteract():
    clock = pygame.time.Clock()
    run = True
    window = pygame.display.set_mode((1280,720))
    window.fill(white)
    displaytext('Freeplay mode', (450,50),'Open Sans',60,window,(0,0,0))
    cube_font = pygame.font.SysFont('Open Sans', 30)
    pygame.display.flip()
    pktcube = pocketcube.pocketcube([['u1', 'u2', 'u3', 'u4']
    ,['l1', 'l2', 'l3', 'l4']
    ,['f1', 'f2', 'f3', 'f4']
    ,['r1', 'r2', 'r3', 'r4']
    ,['b1', 'b2', 'b3', 'b4']
    ,['d1', 'd2', 'd3', 'd4']])
    pktcube.placepocket([[350,400,350,400],[50,50,100,100]],window,cube_font)
    returnbtn = Button(500,550,(pygame.image.load('images/button_return.png').convert_alpha()),1)
    while run:
        if pktcube.isSolved():
            pygame.draw.rect(window, (255,255,255),pygame.Rect(50,95,1000,50))
        if returnbtn.initialise(window):
            run = False
            menu()
        clock.tick(40)
        pktcube.placepocket([[350,400,350,400],[50,50,100,100]],window,cube_font)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                returnmenubool = True
            if event.type == pygame.KEYDOWN:
                if event.key == K_r:
                    pktcube.transformation('r')
                if event.key == K_u:
                    pktcube.transformation('u')
                if event.key == K_d:
                    pktcube.transformation('d')
                if event.key == K_b:
                    pktcube.transformation('b')
                if event.key == K_l:
                    pktcube.transformation('l')
                if event.key == K_f:
                    pktcube.transformation('f')
                if event.key == K_s:
                    spktcube = pocketcubesolver.bfsPocketcube(copy.deepcopy(pktcube.returnstate()))
                    solution = spktcube.UFRsolve()
                    spktcube.transformation(solution)
                    invsol = spktcube.inversemove(solution.copy())
                    solution += spktcube.bibfssearch()
                    displaytext(('Solution is '+ str(solution)), (100,100),'Open Sans',20,window,(0,0,0))
                if event.key == K_0:
                    pktcube.shufflecube()
                if event.key == K_1:
                    pktcube.resetcube()
                if event.key == K_x:
                    pass
                if event.key == K_y:
                    pass
                if event.key == K_z:
                    pass
        

def menu():
    pygame.font.init()
    window = pygame.display.set_mode((1280,720))
    window.fill(white)
    rubikbg = pygame.image.load('images/Rubikbg.jpg').convert_alpha()
    window.blit(pygame.image.load('images/Rubikbg.jpg').convert_alpha(),(-200,-300))
    displaytext('Rubik Cube Solver', (270,100),'Impact',100,window,(255,255,255))
    run = True
    pygame.display.flip()
    pocketbtn = Button(540,300,(pygame.image.load('images/pocketbutton.png').convert_alpha()),1)
    rubikbtn = Button(540,400,(pygame.image.load('images/rubikbutton.png').convert_alpha()),1)
    quitbtn = Button(545,500,(pygame.image.load('images/button_quit.png').convert_alpha()),1)
    while run == True:
        if rubikbtn.initialise(window):
            run = False
            instructionscreen()
            Rubikinteract()
        if pocketbtn.initialise(window):
            run = False
            instructionscreen()
            Pocketinteract()
        if quitbtn.initialise(window):
            exit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
        pygame.display.update()
    
