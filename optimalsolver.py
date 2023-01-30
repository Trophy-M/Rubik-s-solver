'''from cube import *
from transformations import *
from varstore import *
import numpy as np
import itertools

class optimalsolver(cube):
    def __init__(self,uface, lface, fface, rface, bface, dface):
        super().__init__(uface, lface, fface, rface, bface, dface)

#Use EO detection for heuristic
    def edgescore(self,tempcube):
        #use a matrix to represent distance
        edgescore = 0
        tempcube.updatedata()
        faces = ['u','l','f','r','b','d']
        for keys in solvededges:
            #if facelet color is L or R then add one to score
            if tempcube.cu[faces.index(solvededges[keys][0][0])][int(solvededges[keys][0][1])-1][0] == tempcube.cu[1][4][0] or tempcube.cu[faces.index(solvededges[keys][0][0])]\
            [int(solvededges[keys][0][1])-1][0] == tempcube.cu[3][4][0]:
                edgescore += 1
            #otherwise if facelet color is F or B, check if its corresponding edge facelet is U or D, if yes, then add one to score
            elif tempcube.cu[faces.index(solvededges[keys][0][0])][int(solvededges[keys][0][1])-1][0] == tempcube.cu[2][4][0] or tempcube.cu[faces.index(solvededges[keys][0][0])]\
            [int(solvededges[keys][0][1])-1][0] == tempcube.cu[4][4][0]:
                if tempcube.cu[faces.index(solvededges[keys][1][0])][int(solvededges[keys][1][1])-1][0] == tempcube.cu[0][4][0] or tempcube.cu[faces.index(solvededges[keys][1][0])]\
                [int(solvededges[keys][1][1])-1][0] == tempcube.cu[5][4][0]:
                    edgescore += 1
        return edgescore
    def hscore(self, cube):
        edgescore = 0
        cornerscore = 0
        for keys in cube.edges:
            permedges = list(itertools.permutations(cube.edges[keys]))
            if tuple(solvededges[keys]) not in permedges:
                edgescore += 1
        for keys in cube.corners:
            permcorners = list(itertools.permutations(cube.corners[keys]))
            #print('corner: ', set(solvedcorners[keys]),'perm: ',permcorners)
            if tuple(solvedcorners[keys]) not in permcorners:
                cornerscore += 1
        #hscore = edgescore + cornerscore
        return [edgescore,cornerscore]
    
    #use ida search to find a state in which all corners are solved
    def firststatesearch(self):
        pass

kcube = optimalsolver(['u1', 'u2', 'u3', 'u4', 'u5', 'u6', 'u7', 'u8', 'u 9']
,['l1', 'l2', 'l3', 'l4', 'l5', 'l6', 'l7', 'l8', 'l9']
,['f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9']
,['r1', 'r2', 'r3', 'r4', 'r5', 'r6', 'r7', 'r8', 'r9']
,['b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'b9']
,['d1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9'])
kcube.shufflecube()
kcube.firststatesearch()











        
'''