import time
from varstore import *

def rotate(arr):
    arr[0], arr[1], arr[2], arr[3], arr[4], arr[5], arr[6], arr[7], arr[8] = arr[6], arr[3], arr[0], arr[7], arr[4], \
                                                                             arr[1], arr[8], arr[5], arr[2]
    return arr

def turnR(Rubikcube):
    rotate(Rubikcube.cu[3])
    tempf = Rubikcube.cu[2][2], Rubikcube.cu[2][5], Rubikcube.cu[2][8]
    tempd = Rubikcube.cu[5][2], Rubikcube.cu[5][5], Rubikcube.cu[5][8]
    tempu = Rubikcube.cu[0][2], Rubikcube.cu[0][5], Rubikcube.cu[0][8]
    tempb = Rubikcube.cu[4][0], Rubikcube.cu[4][3], Rubikcube.cu[4][6]

    tempu ,tempf, tempb, tempd = tempf,tempd,tempu,tempb
    Rubikcube.cu[2][2], Rubikcube.cu[2][5], Rubikcube.cu[2][8] = tempf
    Rubikcube.cu[5][8], Rubikcube.cu[5][5], Rubikcube.cu[5][2] = tempd
    Rubikcube.cu[0][2], Rubikcube.cu[0][5], Rubikcube.cu[0][8] = tempu
    Rubikcube.cu[4][6], Rubikcube.cu[4][3], Rubikcube.cu[4][0] = tempb
    Rubikcube.updatedata()

def turnL(Rubikcube):
    rotate(Rubikcube.cu[1])
    tempf = Rubikcube.cu[2][0], Rubikcube.cu[2][3], Rubikcube.cu[2][6]
    tempd = Rubikcube.cu[5][0], Rubikcube.cu[5][3], Rubikcube.cu[5][6]
    tempu = Rubikcube.cu[0][0], Rubikcube.cu[0][3], Rubikcube.cu[0][6]
    tempb = Rubikcube.cu[4][2], Rubikcube.cu[4][5], Rubikcube.cu[4][8]

    tempd,tempb,tempf,tempu = tempf,tempd,tempu,tempb
    Rubikcube.cu[2][0], Rubikcube.cu[2][3], Rubikcube.cu[2][6] = tempf
    Rubikcube.cu[5][0], Rubikcube.cu[5][3], Rubikcube.cu[5][6] = tempd
    Rubikcube.cu[0][6], Rubikcube.cu[0][3], Rubikcube.cu[0][0] = tempu
    Rubikcube.cu[4][8], Rubikcube.cu[4][5], Rubikcube.cu[4][2] = tempb
    Rubikcube.updatedata()

def turnU(Rubikcube):
    rotate(Rubikcube.cu[0])
    tempf = Rubikcube.cu[2][0], Rubikcube.cu[2][1], Rubikcube.cu[2][2]
    templ = Rubikcube.cu[1][0], Rubikcube.cu[1][1], Rubikcube.cu[1][2]
    tempr = Rubikcube.cu[3][0], Rubikcube.cu[3][1], Rubikcube.cu[3][2]
    tempb = Rubikcube.cu[4][0], Rubikcube.cu[4][1], Rubikcube.cu[4][2]

    templ, tempb,tempf, tempr = tempf,templ,tempr,tempb
    Rubikcube.cu[2][0], Rubikcube.cu[2][1], Rubikcube.cu[2][2] = tempf
    Rubikcube.cu[1][0], Rubikcube.cu[1][1], Rubikcube.cu[1][2] = templ
    Rubikcube.cu[3][0], Rubikcube.cu[3][1], Rubikcube.cu[3][2] = tempr
    Rubikcube.cu[4][0], Rubikcube.cu[4][1], Rubikcube.cu[4][2] = tempb
    Rubikcube.updatedata()
    

def turnD(Rubikcube):
    rotate(Rubikcube.cu[5])
    tempf = Rubikcube.cu[2][6], Rubikcube.cu[2][7], Rubikcube.cu[2][8]
    templ = Rubikcube.cu[1][6], Rubikcube.cu[1][7], Rubikcube.cu[1][8]
    tempr = Rubikcube.cu[3][6], Rubikcube.cu[3][7], Rubikcube.cu[3][8]
    tempb = Rubikcube.cu[4][6], Rubikcube.cu[4][7], Rubikcube.cu[4][8]

    tempr,tempf,tempb,templ = tempf,templ,tempr,tempb
    Rubikcube.cu[2][6], Rubikcube.cu[2][7], Rubikcube.cu[2][8] = tempf
    Rubikcube.cu[1][6], Rubikcube.cu[1][7], Rubikcube.cu[1][8] = templ
    Rubikcube.cu[3][6], Rubikcube.cu[3][7], Rubikcube.cu[3][8] = tempr
    Rubikcube.cu[4][6], Rubikcube.cu[4][7], Rubikcube.cu[4][8] = tempb
    Rubikcube.updatedata()
    

def turnF(Rubikcube):
    rotate(Rubikcube.cu[2])
    tempd = Rubikcube.cu[5][0], Rubikcube.cu[5][1], Rubikcube.cu[5][2]
    tempu = Rubikcube.cu[0][6], Rubikcube.cu[0][7], Rubikcube.cu[0][8]
    templ = Rubikcube.cu[1][2], Rubikcube.cu[1][5], Rubikcube.cu[1][8]
    tempr = Rubikcube.cu[3][0], Rubikcube.cu[3][3], Rubikcube.cu[3][6]

    templ, tempr,tempu,tempd = tempd,tempu,templ,tempr
    Rubikcube.cu[5][2], Rubikcube.cu[5][1], Rubikcube.cu[5][0] = tempd
    Rubikcube.cu[0][8], Rubikcube.cu[0][7], Rubikcube.cu[0][6] = tempu
    Rubikcube.cu[1][2], Rubikcube.cu[1][5], Rubikcube.cu[1][8] = templ
    Rubikcube.cu[3][0], Rubikcube.cu[3][3], Rubikcube.cu[3][6] = tempr
    Rubikcube.updatedata()
    

def turnB(Rubikcube):
    rotate(Rubikcube.cu[4])
    tempd = Rubikcube.cu[5][6], Rubikcube.cu[5][7], Rubikcube.cu[5][8]
    tempu = Rubikcube.cu[0][0], Rubikcube.cu[0][1], Rubikcube.cu[0][2]
    templ = Rubikcube.cu[1][0], Rubikcube.cu[1][3], Rubikcube.cu[1][6]
    tempr = Rubikcube.cu[3][2], Rubikcube.cu[3][5], Rubikcube.cu[3][8]

    tempd,tempu,templ,tempr = templ,tempr,tempu,tempd
    Rubikcube.cu[5][6], Rubikcube.cu[5][7], Rubikcube.cu[5][8] = tempd
    Rubikcube.cu[0][0], Rubikcube.cu[0][1], Rubikcube.cu[0][2] = tempu
    Rubikcube.cu[1][6], Rubikcube.cu[1][3], Rubikcube.cu[1][0] = templ
    Rubikcube.cu[3][8], Rubikcube.cu[3][5], Rubikcube.cu[3][2] = tempr
    Rubikcube.updatedata()

def rotcube(Rubikcube, axis):
    axis = axis.lower()
    tempu,templ,tempf,tempr,tempb,tempd = Rubikcube.cu[0], Rubikcube.cu[1], Rubikcube.cu[2], Rubikcube.cu[3], Rubikcube.cu[4], Rubikcube.cu[5]
    match axis:
        case 'x':
            Rubikcube.cu[0], Rubikcube.cu[1], Rubikcube.cu[2], Rubikcube.cu[3], Rubikcube.cu[4], Rubikcube.cu[5] = tempf,templ,tempd,tempr,tempu,tempb
            for i in range(0,2): rotate(Rubikcube.cu[4])
            for i in range(0,2): rotate(Rubikcube.cu[5])
            for i in range(0,3): rotate(Rubikcube.cu[1])
            rotate(Rubikcube.rface)
        case 'y':
            Rubikcube.cu[0], Rubikcube.cu[1], Rubikcube.cu[2], Rubikcube.cu[3], Rubikcube.cu[4], Rubikcube.cu[5] = tempu, tempf, tempr, tempb, templ, tempd
            for i in range(0,3): rotate(Rubikcube.cu[5])
            rotate(Rubikcube.cu[0])
        case 'z':
            Rubikcube.cu[0], Rubikcube.cu[1], Rubikcube.cu[2], Rubikcube.cu[3], Rubikcube.cu[4], Rubikcube.cu[5] = templ, tempd, tempf, tempu, tempb, tempr
            rotate(Rubikcube.cu[0])
            rotate(Rubikcube.cu[1])
            rotate(Rubikcube.cu[2])
            rotate(Rubikcube.cu[3])
            rotate(Rubikcube.cu[5])
            for i in range(0,3):rotate(Rubikcube.cu[4])
               

def maketurns(tempcube, theturn):
    for turn in theturn:
        turn  = turn.upper()
        match turn:
            case 'R':
                turnR(tempcube)
            case 'L':
                turnL(tempcube)
            case 'U':
                turnU(tempcube)
            case 'D':
                turnD(tempcube)
            case 'F':
                turnF(tempcube)
            case 'B':
                turnB(tempcube)
            case 'RP':
                for x in range(0,3): turnR(tempcube)
            case 'LP':
                for x in range(0,3):turnL(tempcube)
            case 'UP':
                for x in range(0,3):turnU(tempcube)
            case 'DP':
                for x in range(0,3):turnD(tempcube)
            case 'FP':
                for x in range(0,3):turnF(tempcube)
            case 'BP':
                for x in range(0,3):turnB(tempcube)
            case 'R2':
                for x in range(0,2): turnR(tempcube)
            case 'L2':
                for x in range(0,2):turnL(tempcube)
            case 'U2':
                for x in range(0,2):turnU(tempcube)
            case 'D2':
                for x in range(0,2):turnD(tempcube)
            case 'F2':
                for x in range(0,2):turnF(tempcube)
            case 'B2':
                for x in range(0,2):turnB(tempcube)

#count the number of specific facelets color in face
def checkcolorinface(face, color):
    count = 0
    for items in face:
        if items[0] == color:
            count += 1
    return count

#check if any specified facelets in the face
def checkanyfacelets(face, facelets):
    containAny = False
    if any(x in face for x in facelets):
        containAny = True
    return containAny
#find edges with the face inputted
'''def findedgeswithface(Rubikcube, face):
    for key in self.edges:
        if any()'''