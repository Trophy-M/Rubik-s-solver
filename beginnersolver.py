import cube
from varstore import *
import interface

#arrange white faces on up face
class beginnersolver(cube.cube):
  def __init__(self,cu):
    super().__init__(cu)

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

  #assuming we already have an arrangement of the up faces. We can begin rearranging the edges such that it is in the correct place.
  def crosssolve(self):
    edgeswapalg = ['R', 'U', 'RP', 'U', 'R', 'U2', 'RP', 'U']
    #in a acw direction == y axis direction
    while not (self.checkifcross()):
      if self.cu[2][1][0] != self.cu[2][4][0]:
        self.maketurns( ['R', 'U', 'RP', 'U', 'R', 'U2', 'RP', 'U'])
        for i in range(0,3): self.rotcube('y')
      else:
        for i in range(0,3): self.rotcube('y')
      unsolvededgesmap = [self.fface[1],self.rface[1],self.bface[1],self.lface[1]]
      while self.fface[1][0] != self.fface[4][0]:
        self.maketurns( edgeswapalg)
        if self.fface[1][0] == self.fface[4][0]:
          break
        for i in range(0,3): self.rotcube('y')

  #assuming edge is already in second or third layer fron edge; also flips the edge once if misoriented
  def crosssolvefrontface(self,thefacelet):
    self.updatedata()
    if thefacelet in self.edges['fl']:
      self.maketurns(['U','LP','UP','L'])
    elif thefacelet in self.edges['fr']:
      self.maketurns(['UP','R','U','RP'])
    elif thefacelet in self.edges['df']:
      self.maketurns(['FP','UP','R','U','RP'])
    
    if self.cu[2][1][0] == self.cu[5][4][0]:
      self.maketurns(['F', 'UP', 'R', 'U','RP'])

  def crosssolveFL(self):
    upedgesfacelet = [self.cu[0][4][0]+'2',self.cu[0][4][0]+'4',self.cu[0][4][0]+'6',self.cu[0][4][0]+'8']
    upedgesmap = {}
    for i in range(0,2): self.rotcube('x')
    for facelet in upedgesfacelet:
      upedgesmap[facelet] = self.getfaceletpos(facelet)
    while not (self.cu[5][1][0] == self.cu[5][3][0] == self.cu[5][5][0] == self.cu[5][7][0]):
      for keys in upedgesfacelet:
        if self.findlayer(keys) == 1:
          if keys in self.cu[0]:
            while self.getfaceletpos(keys) != 'u8':
              self.rotcube('y')
          else:
            while self.getfaceletpos(keys) != 'f2':
              self.rotcube('y')
            self.maketurns(['F', 'UP', 'R', 'U'])
          while self.cu[2][1][0] != self.cu[2][4][0]:
            self.maketurns(['UP'])
            self.rotcube('y')
        elif self.findlayer(keys) == 2:
          while keys not in self.cu[2]:
            self.rotcube('y')
          self.crosssolvefrontface(keys)     
          while self.cu[2][1][0] != self.cu[2][4][0]:
              self.maketurns(['UP'])
              self.rotcube('y')
        elif self.findlayer(keys) == 3:
          if keys in self.cu[5]:
            while self.getfaceletpos(keys) != 'd2':
              self.rotcube('y')
            if self.cu[2][4][0] == self.cu[2][7][0]:
              continue
            self.crosssolvefrontface(keys)
          else:
            while self.getfaceletpos(keys) != 'f8':
              self.rotcube('y')
            self.crosssolvefrontface(keys)
          while self.cu[2][1][0] != self.cu[2][4][0]:
            self.maketurns(['UP'])
            self.rotcube('y')
        self.maketurns(['F2'])
        c = 0
        ''''while self.cu[2][4][0] == self.cu[2][7][0] and c < 4:
          self.rotcube('y')
          c += 1'''
    for i in range(0,2): self.rotcube('x')    
  
  def checkifufrright(self):
    self.updatedata()
    cornersright = False
    cornersupright = False
    cornersmatchingright = False
    if self.uface[4][0] in [self.uface[8][0],self.fface[2][0],self.rface[0][0]]:
      cornersupright = True

    #print([self.fface[4][0],self.rface[4][0]],'and', [self.uface[8][0],self.fface[2][0],self.rface[0][0]])
    if set([self.fface[4][0],self.rface[4][0]]).issubset(set([self.uface[8][0],self.fface[2][0],self.rface[0][0]])):
      cornersmatchingright = True

    if cornersmatchingright == True and cornersupright == True:
      cornersright = True
    
    return cornersright

  def checkufrlineswithdfr(self):
    self.updatedata()
    linesup = False
    if self.fface[4][0] in [self.dface[2][0],self.fface[8][0],self.rface[6][0]] and self.rface[4][0] in [self.dface[2][0],self.fface[8][0],self.rface[6][0]]\
          and self.uface[4][0] in [self.dface[2][0],self.fface[8][0],self.rface[6][0]]:
      linesup = True
    return linesup
  #assuming the target corner is already in dfr, to ufr, white facing up
  def cornersolve(self):
    self.updatedata()
    if self.uface[4][0] == self.fface[8][0]:
      for i in range(0,5): self.maketurns( ['RP', 'DP', 'R', 'D'])
    elif self.uface[4][0] == self.rface[6][0]:
      self.maketurns( ['RP', 'DP', 'R', 'D'])
    elif self.uface[4][0] == self.dface[2][0]:
      for i in range(0,3): self.maketurns( ['RP', 'DP', 'R', 'D'])

  def cornersarrange(self):
    cornersmap = {}
    adjacent = {
      'u1':['u2','u4'],
      'u3':['u2','u6'],
      'u7':['u4','u8'],
      'u9':['u6','u8'],
    }
    for facelets in [self.cu[0][4][0]+'1',self.cu[0][4][0]+'3',self.cu[0][4][0]+'7',self.cu[0][4][0]+'9']:
      cornersmap[facelets] = self.getfaceletpos(facelets)
    
    #keys are u1.... and cornermaps[keys] are the position of those faces
    for keys in cornersmap:
      #print('at',keys)
      #first in U Layer
      self.updatedata()
      ##displaycube(self,0.5)
      if keys in self.uface or keys in [self.cu[1][0],self.cu[1][2],self.cu[2][0],self.cu[2][2],\
      self.cu[3][0],self.cu[3][2],self.cu[4][0],self.cu[4][2]]:
        #print('In U layer',keys not in self.corners['ufl'],self.checkufrlineswithdfr() == False)
        while keys not in self.corners['ufl']:
          self.updatedata()
          #print(keys,self.corners['ufl'])
          if keys in self.corners['ufl']:
            break
          #print('get face in ufl')
          ##displaycube(self,0.5)
          self.rotcube('y')
          #print(keys, ':', self.corners['ufl'])
          self.updatedata()
        self.maketurns(['L','D','LP'])
        
        while self.checkufrlineswithdfr() == False:
          if self.checkufrlineswithdfr() == True:
            break
          #print('get the right corner above U')
          ##displaycube(self,0.5)
          self.maketurns(['D'])
          self.rotcube('y')
        self.cornersolve()
      elif keys in self.dface or keys in [self.cu[1][6],self.cu[1][8],self.cu[2][6],self.cu[2][8],\
      self.cu[3][6],self.cu[3][8],self.cu[4][6],self.cu[4][8]]:
        #print('In D layer',keys not in self.corners,self.checkufrlineswithdfr() == False)
        while keys not in self.corners['dfr']:
          self.updatedata()
          if keys in self.corners['dfr']:
            break
          #print('get face in dfr')
          ##displaycube(self,0.5)
          self.rotcube('y')
          #print(keys, ':', self.corners['dfr'] )
          self.updatedata()

        while self.checkufrlineswithdfr() == False:
          if self.checkufrlineswithdfr() == True:
            break
          #print('get the right corner above D')
          ##displaycube(self,0.5)
          self.maketurns(['D'])
          self.rotcube('y')
        self.cornersolve()
      ##displaycube(self,0.5)
  
  #assuming the third layer edge already matched with the face
  def secondlayeredgeinsert(self):
    if self.cu[0][7][0] == self.cu[3][4][0]:
      self.maketurns(['U','R','UP','RP','UP','FP','U','F'])
    elif self.cu[0][7][0] == self.cu[1][4][0]:
      self.maketurns(['UP','LP','U','L','U','F','UP','FP'])

  def isSecondLayerSolved(self):
    solved = False
    facessolved = 0
    for i in range(1,5):
      if self.cu[i][3][0] == self.cu[i][4][0] == self.cu[i][5][0] == self.cu[i][6][0] == self.cu[i][7][0] == self.cu[i][8][0]:
        facessolved += 1
    if facessolved == 4:
      solved = True
    
    return solved

  def secondlayersolve(self):
    for i in range(0,2): self.rotcube( 'x')
    faceletmap = {}
    secondlayerfacelet = [self.cu[1][4][0] + '4',self.cu[1][4][0] + '6',self.cu[2][4][0] + '4',self.cu[2][4][0] + '6',\
    self.cu[3][4][0] + '4',self.cu[3][4][0] + '6',self.cu[4][4][0] + '4',self.cu[4][4][0] + '6']
    while self.isSecondLayerSolved() == False:
      for facelet in secondlayerfacelet:
        faceletmap[facelet] = self.getfaceletpos(facelet)
      for keys in faceletmap:
        faceletmap[keys] = self.getfaceletpos(keys)
        #skip if position is an up edge
        if faceletmap[keys][0] == self.cu[0][4][0] or faceletmap[keys][0] == self.cu[5][4][0]:
          continue
        if faceletmap[keys] in secondlayerfacelet:
          if faceletmap[keys] == keys:
            pass
          elif faceletmap[keys] != keys:
            while faceletmap[keys][0] != 'f':
              self.rotcube('y')
              faceletmap[keys] = self.getfaceletpos(keys)
            #to right
            if faceletmap[keys][1] == '6':
              self.maketurns(['U','R','UP','RP','UP','FP','U','F','U2'])
            elif faceletmap[keys][1] == '4':
              self.maketurns(['UP','LP','U','L','U','F','UP','FP','U2'])
            
            if faceletmap[keys][0] == self.cu[0][4][0]:
              continue
            while self.cu[2][1][0] != self.cu[2][4][0]:
              #displaycube(self,0.5)
              self.maketurns(['UP'])
              self.rotcube('y')
            self.secondlayeredgeinsert()
        else:
          while faceletmap[keys][0] != 'f':
            self.rotcube('y')
            faceletmap[keys] = self.getfaceletpos(keys)
          while self.cu[2][1][0] != self.cu[2][4][0]:
            self.maketurns(['UP'])
            self.rotcube('y')
          self.secondlayeredgeinsert()

  def lastlayercornerssolve(self):
    solvedcornersbool = [False,False,False,False]
    while solvedcornersbool != [True, True, True, True]:
      for i in range(0,4):
        solvedcornersbool[i] = self.checkifufrright()
        self.rotcube('y')
      if solvedcornersbool == [True, True, True, True]:
        break
      if True in solvedcornersbool:
          for i in range(0,solvedcornersbool.index(True)): self.rotcube('y')
          self.maketurns(['U', 'R', 'UP', 'LP', 'U', 'RP', 'UP', 'L'])
          for i in range(0,4-solvedcornersbool.index(True)): self.rotcube('y')
      else:
        self.maketurns(['U', 'R', 'UP', 'LP', 'U', 'RP', 'UP', 'L'])
    self.updatedata()
    for i in range(0,4):
      while self.cu[0][8][0] != self.cu[0][4][0]:
        self.maketurns(['RP', 'DP', 'R', 'D'])
      self.maketurns(['U'])
    
          
  def lastlayercross(self):
    #cross arrange alg
    while (self.cu[0][1][0] == self.cu[0][3][0] == self.cu[0][4][0] == self.cu[0][5][0] == self.cu[0][7][0]) == False:
      #make sure it is L shaped
      if ((self.cu[0][4][0] == self.cu[0][5][0] == self.cu[0][7][0]) and (self.cu[0][1][0] != self.cu[0][3][0]))\
        or ((self.cu[0][4][0] == self.cu[0][3][0] == self.cu[0][7][0]) and (self.cu[0][1][0] != self.cu[0][5][0]))\
        or ((self.cu[0][4][0] == self.cu[0][1][0] == self.cu[0][5][0]) and (self.cu[0][3][0] != self.cu[0][7][0]))== True:
        while (self.cu[0][4][0] == self.cu[0][1][0] == self.cu[0][3][0]) == False:
          self.rotcube('y')
      #make sure it is horizontal line
      elif ((self.cu[0][1][0] == self.cu[0][4][0] == self.cu[0][7][0]) and (self.cu[0][3][0] != self.cu[0][5][0])) == True:
        for i in range(0,2): self.rotcube('y')
      self.maketurns( ['F','R','U','RP','UP','FP'])
    self.crosssolve()
    self.lastlayercornerssolve()
    for i in range(0,2): self.rotcube('x')
    while self.cu[2][4][0] != 'f':
      self.rotcube('y')
    
    #last corner swap

  def solvecube(self):
    self.crosssolveFL()
    print('Cross solved')
    self.cornersarrange()
    print('Corners solved')
    self.secondlayersolve()
    print('Second Layer solved')
    self.lastlayercross()
    print('Cube solved')
    interface.Rubikinteract()

