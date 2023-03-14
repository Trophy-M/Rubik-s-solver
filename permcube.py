import cube

class permcube(cube.cube):
    def __init__(self,cu):
        super().__init__(cu)
        self.cu = self.changefaceletformat()
    
    #change from coordinate like u1 to 1 or l2 to 11
    def changefaceletformat(self):
        facesname = ['u','l','f','r','b','d']
        newcu = []
        for faces in self.cu:
            for facelet in faces:
                newcu.append(facesname.index(facelet[0])*9+int(facelet[1])-1)
        return newcu
    
    def lehmerencoding(self):
        pass

    def returnbitstring(self):
        return ','.join(str(x) for x in self.cu)

tempperm = permcube([['u1', 'u2', 'u3', 'u4', 'u5', 'u6', 'u7', 'u8', 'u9']
    ,['l1', 'l2', 'l3', 'l4', 'l5', 'l6', 'l7', 'l8', 'l9']
    ,['f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9']
    ,['r1', 'r2', 'r3', 'r4', 'r5', 'r6', 'r7', 'r8', 'r9']
    ,['b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'b9']
    ,['d1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9']])


print(tempperm.returnbitstring())