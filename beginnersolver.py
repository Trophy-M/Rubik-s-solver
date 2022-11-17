from cube import *
from transformations import *
from varstore import *

class solver(cube):
    def __init__(self,uface, lface, fface, rface, bface, dface):
        super().__init__(uface, lface, fface, rface, bface, dface)
    
    
    def crosssolve(self):
        while not (self.edges['ub'] == ['u2', 'b2'] and self.edges['ul'] == ['u4', 'l2'] and self.edges['uf'] == ['u8', 'f2'] and self.edges['ur']\
        == ['u6', 'r2']):
            if self.edges['ul'] == ['u4', 'l2'] and self.edges['ur'] == ['u6', 'r2']:
                maketurns(self, ['F', 'R', 'U', 'RP', 'UP', 'FP'])
                print('horizontal')
            elif self.edges['ub'] == ['u2', 'b2'] and self.edges['uf'] == ['u8', 'f2']:
                maketurns(self, ['U', 'F', 'R', 'U', 'RP', 'UP', 'FP'])
                print('vertical')
            elif self.edges['ub'] != ['u2', 'b2'] and self.edges['ul'] != ['u4', 'l2'] and self.edges['uf'] != ['u8', 'f2'] and self.edges['ur']\
        != ['u6', 'r2']:
                maketurns(self, ['F', 'U', 'R', 'UP', 'RP', 'FP', 'U', 'F', 'R', 'U', 'RP', 'UP', 'FP'])
                print('dot')
            elif (self.edges['ub'] == ['u2', 'b2'] and self.edges['ul'] != ['u4', 'l2']) or self.edges['uf'] == ['u8', 'f2'] or self.edges['ur']\
        != ['u6', 'r2']:
                maketurns(self, ['F', 'R', 'U', 'RP', 'UP', 'FP'])
                print('L')
            else:
                maketurns(self, ['U'])
                print('neither')
            print(self.uface)

    def whitecross(self):
        while not (self.edges['ub'] == ['u2', 'b2'] and self.edges['ul'] == ['u4', 'l2'] and self.edges['uf'] == ['u8', 'f2'] and self.edges['ur']\
        == ['u6', 'r2']):
            whiteedgepos = []
            for edges in self.edges:
                if self.edges[edges] == ['u2', 'b2'] or self.edges[edges] == ['u4', 'l2'] or self.edges[edges] == ['u8', 'f2'] or self.edges[edges]\
                == ['u6', 'r2']:
                    whiteedgepos.append(edges)
'''            for items in whiteedgepos:
                match whiteedgepos:

            whiteedgepos = []'''


            
        
solver.maketurns = maketurns
solvetempcube = solver(uface, lface, fface, rface, bface, dface)
maketurns(solvetempcube,['u','r','d'])
#solvetempcube.whitecross()
print(solvetempcube.cu)
