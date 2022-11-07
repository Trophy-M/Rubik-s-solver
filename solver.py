from queue import Queue
from cube import *
from movelibrary import *
import itertools
from varstore import *

tempcube = cube(uface, lface, fface, rface, bface, dface)

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


        