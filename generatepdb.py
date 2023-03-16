import pocketcube
import copy
import csv

#hashes the pattern of the rubik cube for storage. Cant be shared between rubik and pocket
def hashstate(cu):
    #Each coord is represented by primes which are not the same as prime for colors
    primelist = [7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,
                151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233] 
    colors = {'u':0,'l':1,'f':2,'r':3,'b':4,'d':5,} #Each faces colors represented by prime arrays
    hashvalues = []
    finalhash = 1
    for c,faces in enumerate(cu):
        for d,facelets in enumerate(faces):
            hashvalues.append(primelist[c*9+d-1]**colors[facelets[0]])
    for i in hashvalues:
        finalhash = finalhash*i
    
    return finalhash


                



#input in the start state of the cube
def generatecorners(startcube):
    n = 0
    allmoves = ['u','l','f','r','b','d','u2','l2','f2','r2','b2','d2','up','lp','fp','rp','bp','dp']
    queue  = [(copy.deepcopy(startcube.returnstate()),0)]
    searchtree = {}
    n = 0
    cornerpdb = open('cornerpdb.csv', mode = 'a')
    cornerpdb = csv.DictWriter(cornerpdb,fieldnames=['state','depth'],lineterminator = '\n')
    cornerpdb.writeheader()
        

    #queue contains a tuple of the state and its distance
    while queue != []:
        n += 1
        currentnode = queue.pop(0)
        currentstate = copy.deepcopy(currentnode[0])
        if str(currentstate) in searchtree:
            continue
        else:
            temppkt = pocketcube.pocketcube(copy.deepcopy(currentnode[0]))
            for items in allmoves:
                searchtree[str(currentstate)] = currentnode
                temppkt.transformation([items])
                if str(copy.deepcopy(temppkt.returnstate())) in searchtree:
                    continue
                else:
                    queue.append((copy.deepcopy(temppkt.returnstate()),currentnode[1]+1))
            cornerpdb.writerow({'state': hashstate(currentstate),'depth': currentnode[1]})
            if n%10000 == 0:
                print(n)
    cornerpdb.close()
        

solvedpkt = pocketcube.pocketcube([['u1', 'u2', 'u3', 'u4']
    ,['l1', 'l2', 'l3', 'l4']
    ,['f1', 'f2', 'f3', 'f4']
    ,['r1', 'r2', 'r3', 'r4']
    ,['b1', 'b2', 'b3', 'b4']
    ,['d1', 'd2', 'd3', 'd4']])

generatecorners(solvedpkt)
print('done')



