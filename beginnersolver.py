import pygame
from cube import *
from transformations import *
from varstore import *
from interface import placecube
import time
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 30)
window = pygame.display.set_mode((1000,800))
window.fill(white)

class solver(cube):
    def __init__(self,uface, lface, fface, rface, bface, dface):
        super().__init__(uface, lface, fface, rface, bface, dface)
        
    
    
    def daisy(self):
      for i in range(0,2): rotcube(self, 'x')
      while not (self.edges['db'] == ['u2', 'b2'] and self.edges['dl'] == ['u4', 'l2'] and self.edges['df'] == ['u8', 'f2'] and self.edges['dr']\
        == ['u6', 'r2']):
        whiteedgesfaces = ['u2','u4','u6','u8']
        #check for dface if they have any whiteface
        while checkanyfacelets(self.dface, whiteedgesfaces) == True:
          placecube(self.cu, gridcoordinates,window,my_font)
          time.sleep(turntime)
          dseven = self.dface[7][0]
          while dseven != 'u':
            print(dseven)
            placecube(self.cu, gridcoordinates,window,my_font)
            time.sleep(turntime)
            maketurns(self, ['d'])
            dseven = self.dface[7][0]
          maketurns(self, ['f2'])
        
          
          
          if self.fface[7][0] == 'u':
            print('running whiteindface - because whiteOnfrontDF')
            maketurns(self,'f2')
          whiteInDface = any(x in self.dface for x in whiteedgesfaces)
        
        whiteInFface = any(x in self.fface for x in whiteedgesfaces)
        while whiteInFface == True:
          print('running whiteInFface')
          placecube(self.cu, gridcoordinates,window,my_font)
          time.sleep(turntime)
          if self.fface[1][0] == 'u':
            maketurns(self, ['F', 'UP', 'R', 'U'])
          elif self.fface[3][0] == 'u':
            maketurns(self, ['U', 'LP', 'UP'])
          elif self.fface[5][0] == 'u':
            maketurns(self, ['UP', 'R', 'U'])
          elif self.fface[7][0] == 'u':
            maketurns(self, ['F2'])
          rotcube(self,'y')
          whiteInFface = any(x in self.fface for x in whiteedgesfaces)
          print(whiteInFface)
          
        
        while self.uface[7][0] == 'u' and self.fface[1] != self.fface[4]:
          placecube(self.cu, gridcoordinates,window,my_font)
          time.sleep(turntime)
          print('running match front face')
          maketurns(self, 'UP')
          rotcube(self, 'y')
        
        maketurns(self, 'F2')
        maketurns(self, 'D')
        rotcube(self, 'y')
        print('white is inserted down and cube rotated')
      for i in range(0,2): rotcube(self, 'x')


solver.maketurns = maketurns
solvetempcube = solver(uface, lface, fface, rface, bface, dface)
solvetempcube.shufflecube()
solvetempcube.daisy()