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








