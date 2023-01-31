#Only for 2x2 as search space for 3x3 is too large. 

class Rubikgraph:
    def __init__(self, startnode, goalnode):
        #data structure is [[a,b,c,d],[a,b,c,d],[a,b,c,d],[a,b,c,d],[a,b,c,d],[a,b,c,d]]; (u,l,f,r,b,d)
        self.startnode = startnode
        self.goalnode = goalnode
    
    def rot2x2(arr):
        arr[0], arr[1], arr[2], arr[3] = arr[2], arr[0], arr[1], arr[3]
        return arr
    
    def transformation(self, cubestate, moves):
        for transform in moves:
            transform = transform.lower()
            if transform == 'u':
                self.rot2x2(cubestate[0])
                tempf = cubestate[2][0], cubestate[2][1]
                templ = cubestate[1][0], cubestate[1][1]
                tempr = cubestate[3][0], cubestate[3][1]
                tempb = cubestate[4][0], cubestate[4][1]

                templ, tempb,tempf, tempr = tempf,templ,tempr,tempb
                cubestate[2][0], cubestate[2][1] = tempf
                cubestate[1][0], cubestate[1][1] = templ
                cubestate[3][0], cubestate[3][1] = tempr
                cubestate[4][0], cubestate[4][1] = tempb
            elif transform == 'l':
                self.rot2x2(cubestate[1])
                tempf = cubestate[2][0], cubestate[2][2]
                tempd = cubestate[5][0], cubestate[5][3] #
                tempu = cubestate[0][0], cubestate[0][3]
                tempb = cubestate[4][2], cubestate[4][5]

                tempd,tempb,tempf,tempu = tempf,tempd,tempu,tempb
                cubestate[2][0], cubestate[2][3], cubestate[2][6] = tempf
                cubestate[5][0], cubestate[5][3], cubestate[5][6] = tempd
                cubestate[0][6], cubestate[0][3], cubestate[0][0] = tempu
                cubestate[4][8], cubestate[4][5], cubestate[4][2] = tempb
                



