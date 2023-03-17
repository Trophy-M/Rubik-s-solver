import random
import time
from varstore import *
import interface

'''
Class takes in an array in an array which represents a state of the Rubik's cube as a parameter. Each of the list is split in to self.uface, self.lface, etc;
in order to represent all of the faces. Edges and corners are also defined in a dict based on their name and their corresponding facelet within that edge or
corner currently.
'''

class cube:
    def __init__(self, cu):
        self.cu = cu
        self.uface = self.cu[0]
        self.lface = self.cu[1]
        self.fface = self.cu[2]
        self.rface = self.cu[3]
        self.bface = self.cu[4]
        self.dface = self.cu[5]
        self.prev = self.cu.copy()
        self.edges = {
            'ub':[self.uface[1],self.bface[1]],
            'ul':[self.uface[3],self.lface[1]],
            'uf':[self.uface[7],self.fface[1]],
            'ur':[self.uface[5],self.rface[1]],
            'fl':[self.fface[3],self.lface[5]],
            'fr':[self.fface[5],self.rface[3]],
            'bl':[self.bface[5],self.lface[3]],
            'br':[self.bface[3],self.rface[5]],
            'db':[self.dface[1],self.bface[7]],
            'dl':[self.dface[5],self.lface[7]],
            'df':[self.dface[7],self.fface[7]],
            'dr':[self.dface[3],self.rface[7]],
        }
        self.corners = {
            'ubl':[self.uface[0],self.bface[2],self.lface[0]],
            'ubr':[self.uface[2],self.bface[0],self.rface[2]],
            'ufl':[self.uface[6],self.fface[0],self.lface[2]],
            'ufr':[self.uface[8],self.fface[2],self.rface[0]],
            'dbl':[self.dface[2],self.bface[8],self.lface[6]],
            'dbr':[self.dface[0],self.bface[6],self.rface[8]],
            'dfl':[self.dface[8],self.fface[6],self.lface[8]],
            'dfr':[self.dface[6],self.fface[8],self.rface[6]],
        }
        self.solved = [['u1', 'u2', 'u3', 'u4', 'u5', 'u6', 'u7', 'u8', 'u9'],
                   ['l1', 'l2', 'l3', 'l4', 'l5', 'l6', 'l7', 'l8', 'l9'], \
                   ['f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9'],
                   ['r1', 'r2', 'r3', 'r4', 'r5', 'r6', 'r7', 'r8', 'r9'], \
                   ['b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'b9'],
                   ['d1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9']]
        self.cubelog = open('rubiklog.txt','w')
        self.cubelog.close()
        

    def checkchanges(self):
        if self.prev != self.cu:
            self.prev = self.cu.copy()
            return True
        else:
            return False

    def updatedata(self):
        self.edges = {
        'ub':[self.uface[1],self.bface[1]],
        'ul':[self.uface[3],self.lface[1]],
        'uf':[self.uface[7],self.fface[1]],
        'ur':[self.uface[5],self.rface[1]],
        'fl':[self.fface[3],self.lface[5]],
        'fr':[self.fface[5],self.rface[3]],
        'bl':[self.bface[5],self.lface[3]],
        'br':[self.bface[3],self.rface[5]],
        'db':[self.dface[7],self.bface[7]],
        'dl':[self.dface[3],self.lface[7]],
        'df':[self.dface[1],self.fface[7]],
        'dr':[self.dface[5],self.rface[7]],
        }
        self.corners = {
            'ubl':[self.uface[0],self.bface[2],self.lface[0]],
            'ubr':[self.uface[2],self.bface[0],self.rface[2]],
            'ufl':[self.uface[6],self.fface[0],self.lface[2]],
            'ufr':[self.uface[8],self.fface[2],self.rface[0]],
            'dbl':[self.dface[6],self.bface[8],self.lface[6]],
            'dbr':[self.dface[8],self.bface[6],self.rface[8]],
            'dfl':[self.dface[0],self.fface[6],self.lface[8]],
            'dfr':[self.dface[2],self.fface[8],self.rface[6]],
        }
        self.uface = self.cu[0]  # 0
        self.lface = self.cu[1]  # 1
        self.fface = self.cu[2]  # 2
        self.rface = self.cu[3]  # 3
        self.bface = self.cu[4]  # 4
        self.dface = self.cu[5]  # 5

    # prints cube in the console
    def returnstate(self):
        return self.cu

    # do random moves on the cube randomly totalling from 50-100
    def shufflecube(self):
        times = random.randint(50, 100)
        randommoves = []
        for i in range(0, times):
            randommoves.append(random.choice(['u','l','f','r','b','d','u2','l2','f2','r2','b2','d2','up','lp','fp','rp','bp','dp']))
        self.maketurns(randommoves)

    # import other oreintation of cubes
    def rubikchange(self, importcube):
        self.cu = importcube
    

    def cubereset(self):
        self.cu = [['u1', 'u2', 'u3', 'u4', 'u5', 'u6', 'u7', 'u8', 'u9'],
                   ['l1', 'l2', 'l3', 'l4', 'l5', 'l6', 'l7', 'l8', 'l9'], \
                   ['f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9'],
                   ['r1', 'r2', 'r3', 'r4', 'r5', 'r6', 'r7', 'r8', 'r9'], \
                   ['b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'b9'],
                   ['d1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9']]
    
    #input in face and get its position of where it would be if cube solved
    def getfaceletpos(self, facelet):
        self.updatedata()
        for c,items in enumerate(self.cu):
            if facelet in items:
                pos = items.index(facelet)
                facenum = c
        return self.solved[facenum][pos]
    
    #input in edge and get its position where it would be if cube solved (e.g. dl: ['f4','l6'] -> solved is fl: ['f4','l6'] so output fl)
    def getedgepos(self, thisedge):
        solvededge = None
        for items in solvededges:
            if any(x in solvededges[items] for x in self.edges[thisedge]):
                solvededge = items
                break
        return solvededge
    
    def getcornerpos(self, thiscorner):
        solvedcorner = None
        for items in solvedcorners:
            if any(x in solvedcorner[items] for x in self.corners[thiscorner]):
                solvedcorner = items
                break
        return solvedcorner

    #search for edge (solved) and find where it is (scrambled)
    def searchedge(self, thisedge):
        self.updatedata
        thisedgeat = 'k'
        thisedgefaces = solvededges[thisedge]
        for edges in self.edges:
            if (thisedgefaces[0][0] == self.edges[edges][0][0] and thisedgefaces[1][0] == self.edges[edges][1][0]) or (thisedgefaces[1][0] == self.edges[edges][0][0] and thisedgefaces[0][0] == self.edges[edges][1][0]):
                thisedgeat = edges
                break
        return thisedgeat
    #Finds the layer the facelet is in
    def findlayer(self, facelet):
        layer = 0
        self.updatedata()
        if facelet in (self.corners['ufl'] + self.corners['ufr'] + self.corners['ubl'] + self.corners['ubr'] + self.edges['ub']\
        + self.edges['ul'] + self.edges['uf'] + self.edges['ur']):
            layer = 1
        elif facelet in self.edges['fl'] + self.edges['fr'] + self.edges['bl'] + self.edges['br']:
            layer = 2
        elif facelet in (self.corners['dfl'] + self.corners['dfr'] + self.corners['dbl'] + self.corners['dbr'] + self.edges['db']\
        + self.edges['dl'] + self.edges['df'] + self.edges['dr']):
            layer = 3
        else:
            if facelet == self.cu[0][4]:
                layer = 1
            elif facelet == self.cu[5][4]:
                layer = 3
            else:
                layer = 2
        return layer
    
    '''
    Below are subroutines which perform transformations to the cube once it is turn. When the cube is turned, the face that is being turned is rotated
    and the facelets that are connected to the face is also translated to a different face. Hence we need to consider both the face rotation and the 
    translation of these faces.
    '''
    def rotate(self,arr):
        arr[0], arr[1], arr[2], arr[3], arr[4], arr[5], arr[6], arr[7], arr[8] = arr[6], arr[3], arr[0], arr[7], arr[4], \
                                                                                arr[1], arr[8], arr[5], arr[2]
        return arr

    
    def turnR(self):
        self.rotate(self.cu[3])
        tempf = self.cu[2][2], self.cu[2][5], self.cu[2][8]
        tempd = self.cu[5][2], self.cu[5][5], self.cu[5][8]
        tempu = self.cu[0][2], self.cu[0][5], self.cu[0][8]
        tempb = self.cu[4][0], self.cu[4][3], self.cu[4][6]

        tempu ,tempf, tempb, tempd = tempf,tempd,tempu,tempb
        self.cu[2][2], self.cu[2][5], self.cu[2][8] = tempf
        self.cu[5][8], self.cu[5][5], self.cu[5][2] = tempd
        self.cu[0][2], self.cu[0][5], self.cu[0][8] = tempu
        self.cu[4][6], self.cu[4][3], self.cu[4][0] = tempb
        self.updatedata()

    def turnL(self):
        self.rotate(self.cu[1])
        tempf = self.cu[2][0], self.cu[2][3], self.cu[2][6]
        tempd = self.cu[5][0], self.cu[5][3], self.cu[5][6]
        tempu = self.cu[0][0], self.cu[0][3], self.cu[0][6]
        tempb = self.cu[4][2], self.cu[4][5], self.cu[4][8]

        tempd,tempb,tempf,tempu = tempf,tempd,tempu,tempb
        self.cu[2][0], self.cu[2][3], self.cu[2][6] = tempf
        self.cu[5][0], self.cu[5][3], self.cu[5][6] = tempd
        self.cu[0][6], self.cu[0][3], self.cu[0][0] = tempu
        self.cu[4][8], self.cu[4][5], self.cu[4][2] = tempb
        self.updatedata()

    def turnU(self):
        self.rotate(self.cu[0])
        tempf = self.cu[2][0], self.cu[2][1], self.cu[2][2]
        templ = self.cu[1][0], self.cu[1][1], self.cu[1][2]
        tempr = self.cu[3][0], self.cu[3][1], self.cu[3][2]
        tempb = self.cu[4][0], self.cu[4][1], self.cu[4][2]

        templ, tempb,tempf, tempr = tempf,templ,tempr,tempb
        self.cu[2][0], self.cu[2][1], self.cu[2][2] = tempf
        self.cu[1][0], self.cu[1][1], self.cu[1][2] = templ
        self.cu[3][0], self.cu[3][1], self.cu[3][2] = tempr
        self.cu[4][0], self.cu[4][1], self.cu[4][2] = tempb
        self.updatedata()
        

    def turnD(self):
        self.rotate(self.cu[5])
        tempf = self.cu[2][6], self.cu[2][7], self.cu[2][8]
        templ = self.cu[1][6], self.cu[1][7], self.cu[1][8]
        tempr = self.cu[3][6], self.cu[3][7], self.cu[3][8]
        tempb = self.cu[4][6], self.cu[4][7], self.cu[4][8]

        tempr,tempf,tempb,templ = tempf,templ,tempr,tempb
        self.cu[2][6], self.cu[2][7], self.cu[2][8] = tempf
        self.cu[1][6], self.cu[1][7], self.cu[1][8] = templ
        self.cu[3][6], self.cu[3][7], self.cu[3][8] = tempr
        self.cu[4][6], self.cu[4][7], self.cu[4][8] = tempb
        self.updatedata()
        

    def turnF(self):
        self.rotate(self.cu[2])
        tempd = self.cu[5][0], self.cu[5][1], self.cu[5][2]
        tempu = self.cu[0][6], self.cu[0][7], self.cu[0][8]
        templ = self.cu[1][2], self.cu[1][5], self.cu[1][8]
        tempr = self.cu[3][0], self.cu[3][3], self.cu[3][6]

        templ, tempr,tempu,tempd = tempd,tempu,templ,tempr
        self.cu[5][2], self.cu[5][1], self.cu[5][0] = tempd
        self.cu[0][8], self.cu[0][7], self.cu[0][6] = tempu
        self.cu[1][2], self.cu[1][5], self.cu[1][8] = templ
        self.cu[3][0], self.cu[3][3], self.cu[3][6] = tempr
        self.updatedata()
        

    def turnB(self):
        self.rotate(self.cu[4])
        tempd = self.cu[5][6], self.cu[5][7], self.cu[5][8]
        tempu = self.cu[0][0], self.cu[0][1], self.cu[0][2]
        templ = self.cu[1][0], self.cu[1][3], self.cu[1][6]
        tempr = self.cu[3][2], self.cu[3][5], self.cu[3][8]

        tempd,tempu,templ,tempr = templ,tempr,tempu,tempd
        self.cu[5][6], self.cu[5][7], self.cu[5][8] = tempd
        self.cu[0][0], self.cu[0][1], self.cu[0][2] = tempu
        self.cu[1][6], self.cu[1][3], self.cu[1][0] = templ
        self.cu[3][8], self.cu[3][5], self.cu[3][2] = tempr
        self.updatedata()

    #Input in axis rotations as a string. The transformation will then be done.
    def rotcube(self, axis):
        with open('rubiklog.txt','a') as s:
            s.writelines(axis.lower() + '\n')
        tempu,templ,tempf,tempr,tempb,tempd = self.cu[0], self.cu[1], self.cu[2], self.cu[3], self.cu[4], self.cu[5]
        match axis:
            case 'x':
                self.cu[0], self.cu[1], self.cu[2], self.cu[3], self.cu[4], self.cu[5] = tempf,templ,tempd,tempr,tempu,tempb
                for i in range(0,2): self.rotate(self.cu[4])
                for i in range(0,2): self.rotate(self.cu[5])
                for i in range(0,3): self.rotate(self.cu[1])
                self.rotate(self.rface)
            case 'y':
                self.cu[0], self.cu[1], self.cu[2], self.cu[3], self.cu[4], self.cu[5] = tempu, tempf, tempr, tempb, templ, tempd
                for i in range(0,3): self.rotate(self.cu[5])
                self.rotate(self.cu[0])
            case 'z':
                self.cu[0], self.cu[1], self.cu[2], self.cu[3], self.cu[4], self.cu[5] = templ, tempd, tempf, tempu, tempb, tempr
                self.rotate(self.cu[0])
                self.rotate(self.cu[1])
                self.rotate(self.cu[2])
                self.rotate(self.cu[3])
                self.rotate(self.cu[5])
                for i in range(0,3):self.rotate(self.cu[4])
        
                
    #Take in an array which contains moves. These moves will then be done sequentially on the cube.
    def maketurns(self, theturn):
        self.updatedata()
        #Iterates through all the moves in the array
        for turn in theturn:
            turn = turn.upper()
            with open('rubiklog.txt','a') as s:
                s.writelines(turn + '\n')
            #interface.solvingcubedisplay(self, 0.1)
            match turn:
                case 'R':
                    self.turnR()
                case 'L':
                    self.turnL()
                case 'U':
                    self.turnU()
                case 'D':
                    self.turnD()
                case 'F':
                    self.turnF()
                case 'B':
                    self.turnB()
                case 'RP':
                    for x in range(0,3): self.turnR()
                case 'LP':
                    for x in range(0,3): self.turnL()
                case 'UP':
                    for x in range(0,3): self.turnU()
                case 'DP':
                    for x in range(0,3): self.turnD()
                case 'FP':
                    for x in range(0,3): self.turnF()
                case 'BP':
                    for x in range(0,3): self.turnB()
                case 'R2':
                    for x in range(0,2): self.turnR()
                case 'L2':
                    for x in range(0,2): self.turnL()
                case 'U2':
                    for x in range(0,2): self.turnU()
                case 'D2':
                    for x in range(0,2): self.turnD()
                case 'F2':
                    for x in range(0,2): self.turnF()
                case 'B2':
                    for x in range(0,2): self.turnB()

                







            










