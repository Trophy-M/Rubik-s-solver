#implementing bfs on solving 2x2x2
import pocketcube
import copy
import time

class bfsPocketcube(pocketcube.pocketcube):
    def __init__(self, cu):
        super().__init__(cu)
    
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
        #moves = [['l'],['b'],['d'],['l2'],['b2'],['d2'],['lp'],['bp'],['dp']]
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
                print('Depth limit reached')
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
            
            print(str([currentnode[0][3],currentnode[2][1],currentnode[3][0]]))
            print(goalUFR)
            if bool(searchstate&goalUFR) == True:
                search = False
                solution = searchtree[str(currentnode)]
                solution = list(solution)
            n+=1
        
        print(solution)
        return solution

            
            









    #search from current state to goal node using bfs and other way round
    def bibfssearch(self):
        depthlimit = 8
        queue = []
        visittedstart = {}
        visittedgoal = {}
        startnode = list(self.returnstate())
        goalnode = list([['u1', 'u2', 'u3', 'u4']
        ,['l1', 'l2', 'l3', 'l4']
        ,['f1', 'f2', 'f3', 'f4']
        ,['r1', 'r2', 'r3', 'r4']
        ,['b1', 'b2', 'b3', 'b4']
        ,['d1', 'd2', 'd3', 'd4']])
        #moves = [['u'],['l'],['f'],['r'],['b'],['d'],['up'],['lp'],['fp'],['rp'],['bp'],['dp']]
        moves = [['l'],['b'],['d'],['l2'],['b2'],['d2'],['lp'],['bp'],['dp']]
        #moves = [['u'],['l'],['f'],['r'],['b'],['d'],['u2'],['l2'],['f2'],['r2'],['b2'],['d2'],['up'],['lp'],['fp'],['rp'],['bp'],['dp']]
        queue = copy.deepcopy(moves)
        search = True
        searchtreestart, searchtreegoal = {}, {}
        searchstatestart, searchstategoal = {'a'}, {'b'}
        prevdepth = 1
        #n counts number of iterations
        n = 0
        start = time.time()
        if startnode == goalnode:
            search = False
        while search:
            path = queue.pop(0)
            if len(path) > depthlimit:
                search = False
                print('Depth limit reached')
            for items in moves:
                #if turns are repeated (e.g. r r2) they are redundant
                if path[len(path)-1][0] != items[0][0] and len(path+items) <= depthlimit:
                    queue.append(path+items)
            #for start node
            tempcube = pocketcube.pocketcube(copy.deepcopy(startnode))
            tempcube.transformation(path)

            currentnode = tempcube.returnstate()
            if tempcube in visittedstart:
                continue
            else:
                visittedstart[str(currentnode)] = n
                searchtreestart[str(currentnode)] = path
                searchstatestart.add(str(currentnode))
            
            #for end node
            tempcube = pocketcube.pocketcube(copy.deepcopy(goalnode))
            tempcube.transformation(path)

            currentnode = tempcube.returnstate()
            if tempcube in visittedgoal:
                continue
            else:
                visittedgoal[str(currentnode)] = n
                searchtreegoal[str(currentnode)] = path
                searchstategoal.add(str(currentnode))

            #if the node from goal is in visittedstart then a solution is found
            if bool(searchstatestart&searchstategoal) == True:
                print('Solution is found in', n)
                end = time.time()
                print('Time taken: ', end-start)
                middlenode = list(searchstatestart&searchstategoal)[0]
                print(searchtreegoal[middlenode])
                solution = searchtreestart[middlenode] + self.inversemove(searchtreegoal[middlenode]) #need to reverse solution from goal
                search = False
            
            
            #count iterations
            n += 1
            if len(path) != prevdepth:
                pass
            print('Current path bi: ', path)
            prevdepth = len(path)
            #print(searchstatestart,searchstategoal)
   
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

       
                

        




