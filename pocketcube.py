#2x2 cube called pocket cube

class pocketcube:
    def __init__(self, cu):
        #data structure is [[a,b,c,d],[a,b,c,d],[a,b,c,d],[a,b,c,d],[a,b,c,d],[a,b,c,d]]; (u,l,f,r,b,d)
        self.cu = cu.copy()
    
    def rotpocket(arr):
        arr[0], arr[1], arr[2], arr[3] = arr[2], arr[0], arr[1], arr[3]
        return arr
    
    def transformation(self, moves):
        for transform in moves:
            transform = transform.lower()
            if transform == 'u':
                self.rotpocket(self.cu[0])
                tempf = self.cu[2][0], self.cu[2][1]
                templ = self.cu[1][0], self.cu[1][1]
                tempr = self.cu[3][0], self.cu[3][1]
                tempb = self.cu[4][0], self.cu[4][1]

                templ, tempb,tempf, tempr = tempf,templ,tempr,tempb
                self.cu[2][0], self.cu[2][1] = tempf
                self.cu[1][0], self.cu[1][1] = templ
                self.cu[3][0], self.cu[3][1] = tempr
                self.cu[4][0], self.cu[4][1] = tempb
            elif transform == 'l':
                self.rotpocket(self.cu[1])
                tempf = self.cu[2][0], self.cu[2][2]
                tempd = self.cu[5][0], self.cu[5][2]
                tempu = self.cu[0][0], self.cu[0][2]
                tempb = self.cu[4][1], self.cu[4][3]

                tempd,tempb,tempf,tempu = tempf,tempd,tempu,tempb
                self.cu[2][0], self.cu[2][2] = tempf
                self.cu[5][0], self.cu[5][2] = tempd
                self.cu[0][2], self.cu[0][0] = tempu
                self.cu[4][3], self.cu[4][1] = tempb
            elif transform == 'f':
                self.rotpocket(self.cu[2])
                tempd = self.cu[5][0], self.cu[5][1]
                tempu = self.cu[0][2], self.cu[0][3]
                templ = self.cu[1][1], self.cu[1][3]
                tempr = self.cu[3][0], self.cu[3][2]

                templ, tempr,tempu,tempd = tempd,tempu,templ,tempr
                self.cu[5][1], self.cu[5][0] = tempd
                self.cu[0][3], self.cu[0][2] = tempu
                self.cu[1][1], self.cu[1][3] = templ
                self.cu[3][0], self.cu[3][2] = tempr
            elif transform == 'r':
                self.rotpocket(self.cu[3])
                tempf = self.cu[2][1], self.cu[2][3]
                tempd = self.cu[5][1], self.cu[5][3]
                tempu = self.cu[0][1], self.cu[0][3]
                tempb = self.cu[4][0], self.cu[4][2]

                tempu ,tempf, tempb, tempd = tempf,tempd,tempu,tempb
                self.cu[2][1], self.cu[2][3] = tempf
                self.cu[5][3], self.cu[5][1] = tempd
                self.cu[0][1], self.cu[0][3] = tempu
                self.cu[4][2], self.cu[4][0] = tempb
            elif transform == 'b':
                self.rotpocket(self.cu[4])
                tempd = self.cu[5][2], self.cu[5][3]
                tempu = self.cu[0][0], self.cu[0][1]
                templ = self.cu[1][0], self.cu[1][2]
                tempr = self.cu[3][1], self.cu[3][3]

                tempd,tempu,templ,tempr = templ,tempr,tempu,tempd
                self.cu[5][2], self.cu[5][3] = tempd
                self.cu[0][0], self.cu[0][1] = tempu
                self.cu[1][2], self.cu[1][0] = templ
                self.cu[3][3], self.cu[3][1] = tempr
            elif transform == 'd':
                self.rotpocket(self.cu[5])
                tempf = self.cu[2][2], self.cu[2][3]
                templ = self.cu[1][2], self.cu[1][3]
                tempr = self.cu[3][2], self.cu[3][3]
                tempb = self.cu[4][2], self.cu[4][3]

                tempr,tempf,tempb,templ = tempf,templ,tempr,tempb
                self.cu[2][2], self.cu[2][3] = tempf
                self.cu[1][2], self.cu[1][3] = templ
                self.cu[3][2], self.cu[3][3] = tempr
                self.cu[4][2], self.cu[4][3] = tempb

            
            
                



