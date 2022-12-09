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
  
  #Solves the front edge to UF based on their current position on front face / Also flips UF to the correct position
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
      #unsolvededgesmap = [self.fface[1],self.rface[1],self.bface[1],self.lface[1]]
      displaycube(self,0.5)
      if self.cu[2][1][0] != self.cu[2][4][0]:
        maketurns(self, ['R', 'U', 'RP', 'U', 'R', 'U2', 'RP', 'U'])
        for i in range(0,3): rotcube(self,'y')
      else:
        for i in range(0,3): rotcube(self,'y')
      unsolvededgesmap = [self.fface[1],self.rface[1],self.bface[1],self.lface[1]]
      while self.fface[1][0] != self.fface[4][0]:
        displaycube(self,0.5)
        maketurns(self, edgeswapalg)
        if self.fface[1][0] == self.fface[4][0]:
          break
        for i in range(0,3): rotcube(self,'y')

  def crossarrange(self):
    while not (self.cu[0][1][0] == self.cu[0][3][0] == self.cu[0][5][0] == self.cu[0][7][0]):
      if (self.cu[0][1][0] == self.cu[0][3][0] == self.cu[0][5][0] == self.cu[0][7][0]):
        break
      whitefacemap = facemapping(self, ['u2', 'u4', 'u6', 'u8'])
      #faceindex - index of face are we currently looking at/ items - face we're looking at
      for i in range(0,len(whitefacemap)):
        c = 0
        while self.edges['uf'][0][0] == self.uface[4][0] and c < 4:
          c += 1
          maketurns(self, ['U'])
        whitefacemap = facemapping(self, ['u2', 'u4', 'u6', 'u8'])
        displaycube(self,0.5)
        #self.uface[4][0],self.fface[4][0],self.dface[4][0]
        if whitefacemap[i][0] == self.uface[4][0]:
          pass
        elif whitefacemap[i][0] == self.fface[4][0]:
          self.solvefrontedge(i,whitefacemap)
        elif whitefacemap[i][0] == self.dface[4][0]:
            #keep rotating until its is in d1 then f2
          while whitefacemap[i] != 'd2':
            maketurns(self, ['D'])
            whitefacemap[i] = self.getfaceletpos(['u2', 'u4', 'u6', 'u8'][i])
          maketurns(self, ['F2'])
        elif whitefacemap[i][0] == self.rface[4][0]:
          maketurns(self, ['UP'])
          rotcube(self, 'y')
          self.solvefrontedge(i,whitefacemap)
        elif whitefacemap[i][0] == self.bface[4][0]:
          for i in range(0,2):
            maketurns(self, ['UP'])
            rotcube(self, 'y')
          self.solvefrontedge(i,whitefacemap)
        elif whitefacemap[i][0] == self.lface[4][0]:
          for i in range(0,3):
            maketurns(self, ['UP'])
            rotcube(self, 'y')
          self.solvefrontedge(i,whitefacemap)
           
      whitefacemap = facemapping(self, ['u2', 'u4', 'u6', 'u8'])
    
  #solve corner in the bottom layer in DFR position to UFR
  def cornersfromdown(self):
    if self.fface[8][0] == self.uface[4][0]:
      maketurns(self, ['F', 'D' ,'FP'])
    elif self.rface[6][0] == self.uface[4][0]:
      maketurns(self, ['RP', 'DP' ,'R'])
    elif self.dface[2][0] == self.uface[4][0]:
      maketurns(self, ['F', 'L' ,'D2', 'LP', 'FP'])

  def checkifcrosscorners(self):
    self.updatedata()
    isCrossCorners = True
    crosscorners = ['dbl','dbr','dfl','dfr']
    for corners in crosscorners:
      cornersfacelets = self.corners[corners]
      print(cornersfacelets)
      for facelets in cornersfacelets:
        if self.uface[4][0] in facelets:
          crosscorners = False
    print(crosscorners)
    return crosscorners

  #check if corners in right place, doesn't matter the oreintation
  def checkifcornersright(self):
    cornersright = False
    if self.uface[4][0] in [self.cu[2][2][0], self.cu[3][0][0], self.cu[0][8][0]] and self.cu[2][4][0] in [self.cu[2][2][0], self.cu[3][0][0], self.cu[0][8][0]]:
      cornersright = True
    return cornersright


  def cornersarrange(self):
    while self.checkifcrosscorners() == False:
      displaycube(self,0.5)
      if self.uface[4][0] in [self.cu[2][8][0], self.cu[3][6][0], self.cu[5][2][0]]:
        while self.uface[4][0] in [self.cu[2][2][0], self.cu[3][0][0], self.cu[0][8][0]]:
          maketurns(self,['D'])
          rotcube(self,'y')
        self.cornersfromdown()
      else:
        rotcube(self,'y')
    
  def cornerssolve(self):
    amountofsolvedcorners = 0
    awayfromsolved = 0
    while amountofsolvedcorners < 4:
      displaycube(self, 0.5)
      #orient the corner correctly if the corners is in its correctposition but in the wrong oreintation
      #while (self.uface[8][0] != self.uface[4][0] or self.fface[2][0] != self.fface[4][0]) and self.checkifcornersright():
        #maketurns(self,['RP','DP','R','D'])
      #now we check if the corner is not right, then we return to previous right then apply alg. Right, add to amountofsolvedcorners.
      if self.checkifcornersright() == True:
         amountofsolvedcorners += 1
         awayfromsolved += 1
         rotcube(self,'y')
      elif self.checkifcornersright() == False:
        amountofsolvedcorners = 0
        if awayfromsolved > 0:
          for i in range(0, 4-awayfromsolved): rotcube(self,'y')
          maketurns(self,['U', 'R', 'UP', 'LP', 'U', 'RP', 'UP', 'L'])
          awayfromsolved = 0
        else:
          rotcube(self,'y')
        




    

  def solvecube(self):
    self.crossarrange()
    self.crosssolve()
    print('Cross solved')
    self.cornersarrange()
    print('Corners arranged')
    self.cornerssolve()

solver.maketurns = maketurns
solvecube = solver(['u1', 'u2', 'u3', 'u4', 'u5', 'u6', 'u7', 'u8', 'u9']
,['l1', 'l2', 'l3', 'l4', 'l5', 'l6', 'l7', 'l8', 'l9']
,['f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9']
,['r1', 'r2', 'r3', 'r4', 'r5', 'r6', 'r7', 'r8', 'r9']
,['b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'b9']
,['d1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9'])
solvecube.shufflecube()
solvecube.solvecube()
while True:
  displaycube(solvecube,0.5)
