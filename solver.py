from cube import *
from transformations import *
from varstore import *

class solver(cube):
    def __init__(self,uface, lface, fface, rface, bface, dface):
        super().__init__(uface, lface, fface, rface, bface, dface)
    
    def whitecross(self):
        print([self.edges['ub'],self.edges['ul'],self.edges['uf'],self.edges['ur']],[['u2', 'b2'],['u4', 'l2'], ['u8', 'f2'], ['u6', 'r2']])
        while self.edges['ub'] != ['u2', 'b2'] or self.edges['ul'] != ['u4', 'l2'] or self.edges['uf'] != ['u8', 'f2'] or self.edges['ur']\
        != ['u6', 'r2']:
            print('yes')

solvetempcube = solver(uface, lface, fface, rface, bface, dface)
solvetempcube.whitecross()
