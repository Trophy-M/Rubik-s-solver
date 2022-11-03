from cube import *
from movelibrary import *

def maketurns(theturn):
    for turn in theturn:
        match turn:
            case 'R':
                Rubikcube.turnR()
            case 'L':
                Rubikcube.turnL()
            case 'U':
                Rubikcube.turnU()
            case 'D':
                Rubikcube.turnD()
            case 'F':
                Rubikcube.turnF()
            case 'B':
                Rubikcube.turnB()
            case 'RP':
                for x in range(0,3): Rubikcube.turnR()
            case 'LP':
                for x in range(0,3):Rubikcube.turnL()
            case 'UP':
                for x in range(0,3):Rubikcube.turnU()
            case 'DP':
                for x in range(0,3):Rubikcube.turnD()
            case 'FP':
                for x in range(0,3):Rubikcube.turnF()
            case 'BP':
                for x in range(0,3):Rubikcube.turnB()
            case 'R2':
                for x in range(0,2): Rubikcube.turnR()
            case 'L2':
                for x in range(0,2):Rubikcube.turnL()
            case 'U2':
                for x in range(0,2):Rubikcube.turnU()
            case 'D2':
                for x in range(0,2):Rubikcube.turnD()
            case 'F2':
                for x in range(0,2):Rubikcube.turnF()
            case 'B2':
                for x in range(0,2):Rubikcube.turnB()

def getcoord(Rubikcube, solved, face):
    for c,x in enumerate(Rubikcube.cu):
        for d,y in enumerate(x):
            e = d+1
            if y == face:
                coord = [c,d]
    colorcoord = solved[coord[0]][coord[1]]
    return colorcoord



def findsolution(Rubikcube):

    print(standardmove)
    #whitecross
    whitecrossmoves = standardmove + [['RP','DP','R'],['F','D','FP'],['F','L','D2','LP','FP']]
    graph = [
        [Rubikcube.cu,'']
        ]
    print(graph)

Rubikcube.shufflecube()
findsolution(Rubikcube)