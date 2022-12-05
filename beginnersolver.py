import pygame
from cube import *
from transformations import *
from varstore import *
from interface import *
import time
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 30)
window = pygame.display.set_mode((1000,800))
window.fill(white)

#check if top layer forms a cross
def checkifcross(Rubikcube):
  isCross = True
  for i in range(1,5):
    if Rubikcube.cu[i][1][0] != Rubikcube.cu[i][4][0]:
      isCross = False
      break
    
    if not (Rubikcube.cu[0][1][0] == Rubikcube.cu[0][3][0] == Rubikcube.cu[0][5][0] == Rubikcube.cu[0][7][0]):
      isCross = False
  return isCross

#returns current positions of faces inputted as list as list
def facemapping(Rubikcube, face):
  facemap = []
  for items in face:
    facepos = Rubikcube.getfaceletpos(items)
    facemap.append(facepos)
  return facemap


#arrange white faces on up face
class solver(cube):
  def __init__(self,uface, lface, fface, rface, bface, dface):
    super().__init__(uface, lface, fface, rface, bface, dface)
  
  def solvefrontedge(self, i, whitefacemap):
    if whitefacemap[i][1] == '2':
      maketurns(self, ['F', 'UP', 'R', 'U'])
    elif whitefacemap[i][1] == '4':
      maketurns(self, ['U', 'LP', 'UP'])
    elif whitefacemap[i][1] == '6':
      maketurns(self, ['UP', 'R', 'U'])
    elif whitefacemap[i][1] == '8':
      maketurns(self, ['F2'])
      maketurns(self, ['F', 'UP', 'R', 'U'])
    
  #assuming we already have an arrangement of the up faces. We can begin rearranging the edges such that it is in the correct place.
  def crosssolve(self):
    edgeswapalg = ['R', 'U', 'RP', 'U', 'R', 'U2', 'RP', 'U']
    #in a acw direction == y axis direction
    while not (checkifcross(self)):
      displaycube(self,0.5)
      unsolvededgesmap = [self.fface[1],self.rface[1],self.bface[1],self.lface[1]]
      while self.fface[1][0] != self.fface[4][0]:
        displaycube(self,0.5)
        maketurns(self, edgeswapalg)
        if self.fface[1][0] == self.fface[4][0]:
          break
        rotcube(self,'y')
      rotcube(self,'y')

  def crossarrange(self):
    while not (self.cu[0][1][0] == self.cu[0][3][0] == self.cu[0][5][0] == self.cu[0][7][0]):
      if (self.cu[0][1][0] == self.cu[0][3][0] == self.cu[0][5][0] == self.cu[0][7][0]):
        break
      whitefacemap = facemapping(self, ['u2', 'u4', 'u6', 'u8'])
      #faceindex - index of face are we currently looking at/ items - face we're looking at
      for i in range(0,len(whitefacemap)):
        c = 0
        while self.edges['uf'][0][0] == 'u' and c < 4:
          c += 1
          maketurns(self, ['U'])
        whitefacemap = facemapping(self, ['u2', 'u4', 'u6', 'u8'])
        displaycube(self,0.5)
        match whitefacemap[i][0]:
          case 'u':
            pass
          case 'f':
            self.solvefrontedge(i,whitefacemap)
          case 'd':
            #keep rotating until its is in d1 then f2
            while whitefacemap[i] != 'd2':
              maketurns(self, ['D'])
              whitefacemap[i] = self.getfaceletpos(['u2', 'u4', 'u6', 'u8'][i])
            maketurns(self, ['F2'])
          case 'r':
            maketurns(self, ['UP'])
            rotcube(self, 'y')
            self.solvefrontedge(i,whitefacemap)
          case 'b':
            for i in range(0,2):
              maketurns(self, ['UP'])
              rotcube(self, 'y')
            self.solvefrontedge(i,whitefacemap)
          case 'l':
            for i in range(0,3):
              maketurns(self, ['UP'])
              rotcube(self, 'y')
            self.solvefrontedge(i,whitefacemap)
           
      whitefacemap = facemapping(self, ['u2', 'u4', 'u6', 'u8'])

solver.maketurns = maketurns
solvecube = solver(['u1', 'u2', 'u3', 'u4', 'u5', 'u6', 'u7', 'u8', 'u9']
,['l1', 'l2', 'l3', 'l4', 'l5', 'l6', 'l7', 'l8', 'l9']
,['f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9']
,['r1', 'r2', 'r3', 'r4', 'r5', 'r6', 'r7', 'r8', 'r9']
,['b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'b9']
,['d1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9'])
solvecube.shufflecube()
solvecube.crossarrange()
solvecube.crosssolve()
while True:
  displaycube(solvecube,0.5)
