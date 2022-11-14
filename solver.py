from cube import *
from transformations import *
from varstore import *

class solver(cube):
    def __init__(self,uface, lface, fface, rface, bface, dface):
        super().__init__(uface, lface, fface, rface, bface, dface)
    def whitecross(self):
        upedges = ['ub','ul','uf','ur']
        downedges = ['db','dl','df','dr']
        while self.edges['ub'] != ['u2', 'b2'] or self.edges['ul'] != ['u4', 'l2'] or self.edges['uf'] != ['u8', 'f2'] or self.edges['ur']\
        != ['u6', 'r2']:
            for items in upedges:
                edgenow = self.edges[items]
                for c, jtems in enumerate(edgenow):
                    if c == 0:
                        while self.uface.index(jtems) + 1 != int(jtems[1]):
                            maketurns(self,['U'])
                    elif c == 1:
                            maketurns(self,['F','UP','R','U'])
            for items in downedges:
                edgenow = self.edges[items]
                for c, jtems in enumerate(edgenow):
                    if jtems[0] == 'u':
                        print(edgenow)
                        print(edgenow[1-c][0], items[1])
                        while edgenow[1-c][0] != self.uface.index(jtems):
                            print(edgenow[1-c][0], items[1])
                            maketurns(self,['D'])



            
        
solver.maketurns = maketurns
solvetempcube = solver(uface, lface, fface, rface, bface, dface)
maketurns(solvetempcube,['u','r','d'])
solvetempcube.whitecross()
print(solvetempcube.cu)
