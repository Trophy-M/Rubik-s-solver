import pygame
from cube import *
from transformations import *
from varstore import *
from interface import displaycube
import time
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 30)
window = pygame.display.set_mode((1000,800))
window.fill(white)

class solver(cube):
    def __init__(self,uface, lface, fface, rface, bface, dface):
        super().__init__(uface, lface, fface, rface, bface, dface)
        
    
    
    def whitecross(self):
      whiteedgemap = {
        'uf': self.searchedge('uf'),
        'ul': self.searchedge('ul'),
        'ub': self.searchedge('ub'),
        'ur': self.searchedge('ur')
        }
      for key in whiteedgemap:
        print('Working on', key, 'from',whiteedgemap[key] )
        displaycube(self, turntime)
        rottimes = 0
        print(whiteedgemap[key])
        while 'f' not in whiteedgemap[key] and rottimes < 3:
          rottimes += 1
          maketurns(self,['UP'])
          rotcube(self,'y')
          self.updatedata()
          whiteedgemap[key] = self.searchedge(key)
          #print(whiteedgemap)
          displaycube(self, turntime)
        if rottimes >= 3:
          print('white on up face')
          while whiteedgemap[key] != self.searchedge(key):
            print('switching edge')
            maketurns(self,['R','U','RP','U','R','U2','RP','U'])
            self.updatedata()
            whiteedgemap[key] = self.searchedge(key)
            displaycube(self, turntime)
        elif rottimes < 3:
          print('white not on up face')
          match self.searchedge(key):
            case 'uf':
              pass
            case 'fl':
              maketurns(self, ['U', 'LP', 'UP'])
              displaycube(self, turntime)
            case 'fr':
              maketurns(self, ['UP', 'R', 'U'])
              displaycube(self, turntime)
            case 'df':
              maketurns(self, ['F2'])
              displaycube(self, turntime)
          self.updatedata()
          whiteedgemap[key] = self.searchedge(key)
        if self.edges['uf'][1][0] == 'u':
          maketurns(self,['F', 'UP', 'R', 'U'])
        maketurns(self, ['U'])
        





solver.maketurns = maketurns
solvetempcube = solver(['u1', 'u2', 'u3', 'u4', 'u5', 'u6', 'u7', 'u8', 'u9']
,['l1', 'l2', 'l3', 'l4', 'l5', 'l6', 'l7', 'l8', 'l9']
,['f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9']
,['r1', 'r2', 'r3', 'r4', 'r5', 'r6', 'r7', 'r8', 'r9']
,['b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'b9']
,['d1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9'])
solvetempcube.maketurns(['R', 'U', 'L','R2','LP', 'UP','U','RP','U','R','F', 'UP', 'R'])
solvetempcube.whitecross()
while True:
  displaycube(solvetempcube,0.5)