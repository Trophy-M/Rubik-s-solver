#implementing bfs on solving 2x2x2
import pocketcube

class bfsPocketcube(pocketcube):
    def __init__(self, cu):
        super.__init__(self, cu)
    
    #search from current state to goal node using bfs and other way round
    def bibfssearch(self):
        depthlimit = 6
        queue = []
        visitted = []
        startnode = self.cu.copy()
        goalnode = [['u1', 'u2', 'u3', 'u4']
        ,['l1', 'l2', 'l3', 'l4']
        ,['f1', 'f2', 'f3', 'f4']
        ,['r1', 'r2', 'r3', 'r4']
        ,['b1', 'b2', 'b3', 'b4']
        ,['d1', 'd2', 'd3', 'd4']].copy()
        




