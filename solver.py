from queue import Queue
from cube import *
from movelibrary import *
import itertools

tempcube = cube(uface, lface, fface, rface, bface, dface)
def maketurns(theturn):
    for turn in theturn:
        match turn:
            case 'R':
                tempcube.turnR()
            case 'L':
                tempcube.turnL()
            case 'U':
                tempcube.turnU()
            case 'D':
                tempcube.turnD()
            case 'F':
                tempcube.turnF()
            case 'B':
                tempcube.turnB()
            case 'RP':
                for x in range(0,3): tempcube.turnR()
            case 'LP':
                for x in range(0,3):tempcube.turnL()
            case 'UP':
                for x in range(0,3):tempcube.turnU()
            case 'DP':
                for x in range(0,3):tempcube.turnD()
            case 'FP':
                for x in range(0,3):tempcube.turnF()
            case 'BP':
                for x in range(0,3):tempcube.turnB()
            case 'R2':
                for x in range(0,2): tempcube.turnR()
            case 'L2':
                for x in range(0,2):tempcube.turnL()
            case 'U2':
                for x in range(0,2):tempcube.turnU()
            case 'D2':
                for x in range(0,2):tempcube.turnD()
            case 'F2':
                for x in range(0,2):tempcube.turnF()
            case 'B2':
                for x in range(0,2):tempcube.turnB()

def getcoord(tempcube, solved, face):
    for c,x in enumerate(tempcube.cu):
        for d,y in enumerate(x):
            e = d+1
            if y == face:
                coord = [c,d]
    colorcoord = solved[coord[0]][coord[1]]
    return colorcoord

def checkpattern(tempcube):
    tempcube

def findsolution(tempcube):
    print(standardmove)
    #whitecross\
    lastinstance = tempcube.cu

def genmoves(moves, depth):
    return list(itertools.permutations(moves,r=depth))

def bfssearch(standardmoves):
    queue = []
    possiblemoves = []
    for i in range(0,len(standardmoves)):
        possiblemoves += genmoves(standardmoves, i)
    
    

    
'''    def bfssearch(vertex,moves,goal,depth):
        isVisitted = [False]*(len(moves)**depth)
        queue = []
        queue.append(vertex)
        counter = 0
        solution = None
        while len(queue) > 0 and counter < len(moves)**depth:
            counter += 1
            vertexnow = queue.pop(0)
            if isVisitted[queue.index(vertexnow)] == False:
                if vertexnow == goal:
                    solution = moves
                isVisitted[queue.index(vertexnow)] == True
                if moves[]'''


        