import itertools
from transformations import *
from itertools import chain
import random

#change coordinate in arr2 in that position to be arr1 in the other position
#rotates a 3x3 matrix CW
def rotate(arr):
    arr[0], arr[1], arr[2], arr[3], arr[4], arr[5], arr[6], arr[7], arr[8] = arr[6], arr[3], arr[0], arr[7], arr[4], arr[1], arr[8], arr[5], arr[2]
    return arr

class cube:
    def __init__(self, uface, lface, fface, rface, bface, dface):
        self.uface = uface #0
        self.lface = lface #1
        self.fface = fface #2
        self.rface = rface #3
        self.bface = bface #4
        self.dface = dface #5
        self.cu = [uface,lface,fface,rface,bface,dface]

    def turnR(self):
        rotate(self.cu[3])
        self.cu[2][2],self.cu[2][5],self.cu[2][8],self.cu[5][2],self.cu[5][5],self.cu[5][8]\
           ,self.cu[0][2],self.cu[0][5],self.cu[0][8],self.cu[4][0],self.cu[4][3],self.cu[4][6] \
         = self.cu[0][2],self.cu[0][5],self.cu[0][8],self.cu[2][2],self.cu[2][5],self.cu[2][8],\
            self.cu[4][6],self.cu[4][3],self.cu[4][0],self.cu[5][8],self.cu[5][5],self.cu[5][2]
    def turnL(self):
        rotate(self.cu[1])
        self.cu[2][0],self.cu[2][3],self.cu[2][6],self.cu[5][0],self.cu[5][3],self.cu[5][6]\
           ,self.cu[0][0],self.cu[0][3],self.cu[0][6],self.cu[4][2],self.cu[4][5],self.cu[4][8] \
         = self.cu[5][0],self.cu[5][3],self.cu[5][6],self.cu[4][2],self.cu[4][5],self.cu[4][2],\
            self.cu[2][6],self.cu[2][3],self.cu[2][0],self.cu[0][6],self.cu[0][3],self.cu[0][0]
    def turnU(self):
        rotate(self.cu[0])
        self.cu[2][0],self.cu[2][1],self.cu[2][2],self.cu[1][0],self.cu[1][1],self.cu[1][2]\
           ,self.cu[3][0],self.cu[3][1],self.cu[3][2],self.cu[4][0],self.cu[4][2],self.cu[4][3] \
         = self.cu[1][0],self.cu[1][1],self.cu[1][2],self.cu[4][0],self.cu[4][1],self.cu[4][2],\
            self.cu[2][0],self.cu[2][1],self.cu[2][2],self.cu[3][0],self.cu[3][1],self.cu[3][2]
    def turnD(self):
        rotate(self.cu[5])
        self.cu[2][6],self.cu[2][7],self.cu[2][8],self.cu[1][6],self.cu[1][7],self.cu[1][8]\
           ,self.cu[3][6],self.cu[3][7],self.cu[3][8],self.cu[4][6],self.cu[4][7],self.cu[4][8] \
         = self.cu[3][6],self.cu[3][7],self.cu[3][8],self.cu[2][6],self.cu[2][7],self.cu[2][8],\
            self.cu[4][6],self.cu[4][7],self.cu[4][8],self.cu[1][6],self.cu[1][7],self.cu[1][8]
    def turnF(self):
        rotate(self.cu[2])
        self.cu[5][0],self.cu[5][1],self.cu[5][2],self.cu[0][6],self.cu[0][7],self.cu[0][8]\
           ,self.cu[1][2],self.cu[1][5],self.cu[1][8],self.cu[3][0],self.cu[3][3],self.cu[3][6] \
         = self.cu[1][2],self.cu[1][5],self.cu[1][8],self.cu[3][0],self.cu[3][3],self.cu[3][6],\
            self.cu[0][8],self.cu[0][7],self.cu[0][6],self.cu[5][2],self.cu[5][1],self.cu[5][0]
    def turnB(self):
        rotate(self.cu[4])
        self.cu[5][6],self.cu[5][7],self.cu[5][8],self.cu[0][0],self.cu[0][1],self.cu[0][2]\
           ,self.cu[1][0],self.cu[1][3],self.cu[1][6],self.cu[3][2],self.cu[3][5],self.cu[3][8] \
         = self.cu[3][8],self.cu[3][5],self.cu[3][2],self.cu[1][6],self.cu[1][3],self.cu[1][0],\
            self.cu[5][6],self.cu[5][7],self.cu[5][8],self.cu[0][0],self.cu[0][1],self.cu[0][2]
    
    def displaycube(self):
        for items in self.cu:
            print(items)

    def shufflecube(self):
        coordinates = []
        for items in self.cu:
            for jtems in items:
                coordinates.append(jtems)

        n = len(coordinates)
        print(n)
        shuffledlist = []
        while n > 0:
            shuffle = random.randint(0, (n-1))
            shuffledlist.append(coordinates[shuffle])
            coordinates.remove(coordinates[shuffle])
            n -= 1
        facelist, finallist = [], []
        print(len(shuffledlist))
        for i in range(1,7):
            for j in range(1,10):
                facelist.append(shuffledlist[(9*(i-1) + j)-1])
                #print(facelist)
            finallist.append(facelist)
            facelist = []
        return finallist





uface = ['u1','u2','u3','u4','u5','u6','u7','u8','u9']
lface = ['l1','l2','l3','l4','l5','l6','l7','l8','l9']
fface = ['f1','f2','f3','f4','f5','f6','f7','f8','f9']
rface = ['r1','r2','r3','r4','r5','r6','r7','r8','r9']
bface = ['b1','b2','b3','b4','b5','b6','b7','b8','b9']
dface = ['d1','d2','d3','d4','d5','d6','d7','d8','d9']
Rubikcube = cube(uface, lface, fface, rface, bface, dface)

hello = Rubikcube.shufflecube()
print(hello)
