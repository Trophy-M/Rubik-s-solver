from cube import Rubikcube
from varstore import solved

def getcolorpos(Rubikcube, color, solved):
    for c,x in enumerate(Rubikcube.cu):
        for d,y in enumerate(x):
            if color == y:
                coord = [c,d]
    colorcoord = solved[coord[0]][coord[1]]
    return colorcoord

def whitecross(Rubikcube):
    isWhitecross = False
    whitecross = ['u2','u4','u5','u6','u8']
    ucrosspos, ucross = [],[]
    if isWhitecross == False:
        if [Rubikcube.cu[0][1],Rubikcube.cu[0][3],Rubikcube.cu[0][4],Rubikcube.cu[0][5],Rubikcube.cu[0][7]] == whitecross:
            isWhiteCross = True
        for faces in Rubikcube.cu:
            for color in faces:
                if color in whitecross and color != 'u5':
                    ucross.append(color)
                    ucrosspos.append(getcolorpos(Rubikcube, color, solved))
        

    


