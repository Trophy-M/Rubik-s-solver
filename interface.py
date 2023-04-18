import pygame
import time
from varstore import *
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

    #Returns bool when the button is pressed
    def initialise(self,window):
        mousepos = pygame.mouse.get_pos()
        beenclicked = False

        #checks if the mouse is at the button, is pressed, and the button hadn't been clicked before
        if self.rect.collidepoint(mousepos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                beenclicked = True
                self.clicked = beenclicked

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        window.blit(self.image, (self.rect.x, self.rect.y))
        return beenclicked      

#Given the text, position, font, size, window to put on, and the text color. This function will put a text on the surface of a given window.
def displaytext(text, coordinate, font, size,window,color):
    my_font = pygame.font.SysFont(font, size)
    displayedtext = my_font.render(text,True,color)
    window.blit(displayedtext, coordinate)


    
#places color in the window according to their position in the array (face) and subarray (1-9)
def placecube(Rubikcube, pos,window,my_font):
    posx = pos[0]
    posy = pos[1]
    #Each facelets are 50 pxl in width and height
    width = 50; height = 50
    #iterates through cube.cu and places the cube according to its position within the list
    for c,items in enumerate(Rubikcube):
        for d,jtems in enumerate(items):
            #c represents the face it is in, d represents its position in the face
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
            
            #Draws color according to which color is assigned initially (i.e. U2 - up face - is white)
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
        
#Display the cube when it is solving. Need a time delay as the changes occurs too fast for us to see.
def solvingcubedisplay(Rubikcube, delay):
    Rubikcube.updatedata()
    gridcoordinates = [[350,400,450,350,400,450,350,400,450],[50,50,50,100,100,100,150,150,150]]
    my_font = pygame.font.SysFont('Open Sans', 30)
    window = pygame.display.set_mode((1280,720))
    window.fill(white)
    displaytext('Solving...', (450,50),'Open Sans',60,window,(0,0,0))
    #stops the program for 'delay' seconds
    #time.sleep(delay)
    #use placecube subroutine from prior to display the cube on screen
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
    #initialising 3 buttons for the user to quit, solve, or return.
    quitbtn = Button(300,450,(pygame.image.load('images/button_quit.png').convert_alpha()),1)
    solvebtn = Button(600,450,(pygame.image.load('images/button_solve.png').convert_alpha()),1)
    #Initialise the cube as a solved cube
    Rubikcube = cube.cube([['u1', 'u2', 'u3', 'u4', 'u5', 'u6', 'u7', 'u8', 'u9']
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
        #Limits the FPS
        clock.tick(40)
        placecube(Rubikcube.cu,[[350,400,450,350,400,450,350,400,450],[50,50,50,100,100,100,150,150,150]], window, cube_font)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                menu()
            #Pressing keys will run a certain function
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
                    solvecube = beginnersolver.beginnersolver(copy.deepcopy(Rubikcube.returnstate()))
                    solvecube.solvecube()
                if event.key == K_0:
                    Rubikcube.shufflecube()
                if event.key == K_1:
                    Rubikcube.cubereset()
                if event.key == K_z:
                    Rubikcube.logstate()
                if event.key == K_x:
                    Rubikcube.loadstate()
    #Returns to menu if return button is pressed
    if returnmenubool == True:
        menu()

#This mode displays instruction to the users.
def instructionscreen():
    clock = pygame.time.Clock()
    run = True
    window = pygame.display.set_mode((1280,720))
    window.fill(white)
    #Code below add the text to the surface and put on a picture on the surface
    displaytext('Instructions', (450,50),'Open Sans',60,window,(255,0,0))
    displaytext('Press U/L/F/R/D/B to turn U/L/F/R/D/B faces', (450,100),'Open Sans',30,window,(0,0,0))
    displaytext('Press S to solve the cube', (450,150),'Open Sans',30,window,(0,0,0))
    displaytext('Press 0 to scramble the cube', (450,200),'Open Sans',30,window,(0,0,0))
    displaytext('Press 1 to reset the cube', (450,250),'Open Sans',30,window,(0,0,0))
    displaytext('Press z/x to save/load the cube', (450,300),'Open Sans',30,window,(0,0,0))
    displaytext('Press enter to continue', (450,350),'Open Sans',30,window,(0,0,100))
    rubiklogo = pygame.transform.scale((pygame.image.load('images/rubik_logo.png').convert_alpha()), (int(1200*0.20),int(1200*0.20)))
    window.blit(rubiklogo, (450, 400))
    pygame.display.flip() 
    while run:
        clock.tick(40)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == K_RETURN:
                    run = False

        
#In this mode, users can interact with a pocketcube.
def Pocketinteract():
    clock = pygame.time.Clock()
    run = True
    window = pygame.display.set_mode((1280,720))
    window.fill(white)
    displaytext('Freeplay mode', (450,50),'Open Sans',60,window,(0,0,0))
    cube_font = pygame.font.SysFont('Open Sans', 30)
    pygame.display.flip()
    #Initialise the pocketcube
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
                '''Solutions are obtained in two parts. The first part of the solution is sa solved UFR corner. This
                is stored in variable solution and used to transform the cube in to the second group. The second part
                is then obtained and appended to solution. The solution is then displayed on screen for the user. Also,
                the pocketcube is passed on to a temporary class variable a deepcopy of the array is made to prevent
                any changes made to the original.
                '''
                if event.key == K_s:
                    spktcube = pocketcubesolver.bfsPocketcube(copy.deepcopy(pktcube.returnstate()))
                    solution = spktcube.UFRsolve()
                    spktcube.transformation(solution)
                    invsol = spktcube.inversemove(solution.copy())
                    solution += spktcube.bibfssearch()
                    pygame.draw.rect(window, (255,255,255), pygame.Rect(100, 100, 500, 20))
                    displaytext(('Solution is '+ str(solution)), (100,100),'Open Sans',20,window,(0,0,0))
                if event.key == K_0:
                    pktcube.shufflecube()
                if event.key == K_1:
                    pktcube.resetcube()
                if event.key == K_z:
                    pktcube.logstate()
                if event.key == K_x:
                    pktcube.loadstate()
        
#In this mode, users can choose their options.
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
    
