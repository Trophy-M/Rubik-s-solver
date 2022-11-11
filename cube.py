import random
from transformations import *


# change coordinate in arr2 in that position to be arr1 in the other position
# rotates a 3x3 matrix CW



# Stores data as an array with multiple subarrays. Each subarrays represent a face on the cube.
class cube:
    def __init__(self, uface, lface, fface, rface, bface, dface):
        self.uface = uface  # 0
        self.lface = lface  # 1
        self.fface = fface  # 2
        self.rface = rface  # 3
        self.bface = bface  # 4
        self.dface = dface  # 5
        self.cu = [uface, lface, fface, rface, bface, dface]
        self.edges = {
            'ub':[self.uface[1],self.bface[1]],
            'ul':[self.uface[3],self.lface[1]],
            'uf':[self.uface[7],self.fface[1]],
            'ur':[self.uface[5],self.rface[1]],
            'fl':[self.fface[3],self.lface[5]],
            'fr':[self.fface[5],self.rface[3]],
            'bl':[self.bface[5],self.lface[3]], #check bface connections
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
        

    def updatedata(self):
        self.edges = {
        'ub':[self.uface[1],self.bface[1]],
        'ul':[self.uface[3],self.lface[1]],
        'uf':[self.uface[7],self.fface[1]],
        'ur':[self.uface[5],self.rface[1]],
        'fl':[self.fface[3],self.lface[5]],
        'fr':[self.fface[5],self.rface[3]],
        'bl':[self.bface[5],self.lface[3]], #check bface connections
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
    # prints cube in the console
    def displaycube(self):
        for i in range(6): print(self.cu[i])

    # do random moves on the cube randomly totalling from 50-100
    def shufflecube(self):
        times = random.randint(50, 100)
        turns = [turnB(self), turnD(self), turnD(self), turnL(self), turnR(self), turnU(self)]
        for i in range(times):
            random.choice(turns)()

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








