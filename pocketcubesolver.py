#implementing bfs on solving 2x2x2
import pocketcube
import copy
import time

#Class inherits from pocketcube but added additional methods which solves the cube
class bfsPocketcube(pocketcube.pocketcube):
    def __init__(self, cu):
        super().__init__(cu)
    
    #inverses moves given in an array (i.e. [FP,L,R2] --> [R2,LP,F])
    def inversemove(self,moves):
        moves.reverse()
        inversedmove = []
        for items in moves:
            items = items.lower()
            #if item is one letter then it is a single turn
            if len(items) == 1:
                inversedmove.append(items + 'p')
            #if item is two letter and ends with P then it is a triple turn
            elif len(items) == 2 and items[1] == 'p':
                inversedmove.append(items[0])
            else:
                inversedmove.append(items)
        return inversedmove
    
    #search for a solved state of corner DFR using bfs
    def UFRsolve(self):
        initialUFR = copy.deepcopy([self.cu[0][3],self.cu[2][1],self.cu[3][0]])
        goalUFR = {'a',str(['u4','f2','r1'])}
        moves = [['u'],['l'],['f'],['r'],['b'],['d'],['u2'],['l2'],['f2'],['r2'],['b2'],['d2'],['up'],['lp'],['fp'],['rp'],['bp'],['dp']]
        queue = []
        depthlimit = 8
        n=0
        visited, searchtree,searchstate = {},{},{'b'}
        startnode = self.cu
        search = True
        queue = copy.deepcopy(moves)
        while search:
            path = queue.pop(0)
            if len(path) > depthlimit:
                search = False
            for items in moves:
                #if turns are repeated (e.g. r r2) they are redundant
                if path[len(path)-1][0] != items[0][0] and len(path+items) <= depthlimit:
                    queue.append(path+items)

            tempcube = pocketcube.pocketcube(copy.deepcopy(startnode))
            tempcube.transformation(path)

            currentnode = tempcube.returnstate()
            if tempcube in visited:
                continue
            else:
                visited[str(currentnode)] = n
                searchtree[str(currentnode)] = path
                searchstate.add(str([currentnode[0][3],currentnode[2][1],currentnode[3][0]]))
            
            if bool(searchstate&goalUFR) == True:
                search = False
                solution = searchtree[str(currentnode)]
                solution = list(solution)
            n+=1

        return solution

            
            









    #search from current state to goal node using bfs and other way round
    def bibfssearch(self):
        #limits the search depth
        depthlimit = 8
        queue = []
        #Both dictionary will contain {state:moves made to reach the state}
        visittedstart = {}
        visittedgoal = {}
        #Defines the start and the goal state
        startnode = list(self.returnstate())
        goalnode = list([['u1', 'u2', 'u3', 'u4']
        ,['l1', 'l2', 'l3', 'l4']
        ,['f1', 'f2', 'f3', 'f4']
        ,['r1', 'r2', 'r3', 'r4']
        ,['b1', 'b2', 'b3', 'b4']
        ,['d1', 'd2', 'd3', 'd4']])
        #moves reduced to these
        moves = [['l'],['b'],['d'],['l2'],['b2'],['d2'],['lp'],['bp'],['dp']]
        queue = copy.deepcopy(moves)
        search = True
        searchtreestart, searchtreegoal = {}, {}
        #Sets that contains states for each of the search direction
        searchstatestart, searchstategoal = {'a'}, {'b'}
        prevdepth = 1
        #n counts number of iterations
        n = 0
        start = time.time()
        if startnode == goalnode:
            search = False
        while search:
            #path is the transformation to be performed/next in queue
            path = queue.pop(0)
            if len(path) > depthlimit:
                search = False
            for items in moves:
                #if turns are repeated (e.g. r r2) they are redundant hence we dont append them in the queue
                if path[len(path)-1][0] != items[0][0] and len(path+items) <= depthlimit:
                    queue.append(path+items)
            #for start node; we use tempcube to temporary be applied the transformation. Same state as start.
            tempcube = pocketcube.pocketcube(copy.deepcopy(startnode))
            tempcube.transformation(path)

            currentnode = tempcube.returnstate()
            if tempcube in visittedstart:
                continue
            else:
                #Add to dict visited to see if the nodes are visited and dict for search tree containing the path. Also added to a set
                visittedstart[str(currentnode)] = n
                searchtreestart[str(currentnode)] = path
                searchstatestart.add(str(currentnode))
            
            #for end node; same state as solved.
            tempcube = pocketcube.pocketcube(copy.deepcopy(goalnode))
            tempcube.transformation(path)

            currentnode = tempcube.returnstate()
            if tempcube in visittedgoal:
                continue
            else:
                visittedgoal[str(currentnode)] = n
                searchtreegoal[str(currentnode)] = path
                searchstategoal.add(str(currentnode))

            #Performs set intersection to find out if a solution has been found.
            if bool(searchstatestart&searchstategoal) == True:
                end = time.time()
                middlenode = list(searchstatestart&searchstategoal)[0]
                #Have to inverse moves made from goal. Then add those two together we have the solution.
                solution = searchtreestart[middlenode] + self.inversemove(searchtreegoal[middlenode])
                search = False
            
            
            #count iterations
            n += 1
            if len(path) != prevdepth:
                pass
            prevdepth = len(path)
            #print(searchstatestart,searchstategoal)
        #Don't return the solution if these are no iterations of the search.
        if n == 0:
            pass
        else:
            return solution

'''temppocket = bfsPocketcube([['u1', 'u2', 'u3', 'u4']
,['l1', 'l2', 'l3', 'l4']
,['f1', 'f2', 'f3', 'f4']
,['r1', 'r2', 'r3', 'r4']
,['b1', 'b2', 'b3', 'b4']
,['d1', 'd2', 'd3', 'd4']])
temppocket.transformation(['R','UP','D2','F',"B2"])
firstsol = temppocket.UFRsolve()
temppocket.transformation(firstsol)
temppocket.bibfssearch()'''

       
                

        




