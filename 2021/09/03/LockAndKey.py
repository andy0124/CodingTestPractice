def solution(key, lock):
    
    keySize = len(key)
    lockSize = len(lock)

    way = 2*keySize + lockSize

    checkingList = []

    for x in range(way) :
        temp = []
        for y in range(way) :
            temp.append(0)
        checkingList.append(temp)

    

    for ridx, row in enumerate(lock) :
        for cidx, col in enumerate(row) :
            checkingList[ridx+keySize][cidx+keySize] = col

    
    for i in range(4):
        #키돌리기
        key = turn(key)
        for rowidx in range(keySize+lockSize):
            for colidx in range(keySize+lockSize):
                attach(rowidx,colidx,key,checkingList)
                if check(keySize,lockSize,checkingList) : return True
                dettach(rowidx,colidx,key,checkingList)
                
    return False

def turn(key):
    turnedKdy = []
    length = len(key)
    for col in range(length):
        tempRow = []
        for row in key :
            tempRow.append(row[col])
        tempRow.reverse()
        turnedKdy.append(tempRow)
    return turnedKdy

def attach(rowidx,colidx, key, lockMap):
    temp = lockMap
    for ir, row in enumerate(range(rowidx,rowidx+len(key),1)) :
        for ic, col in enumerate(range(colidx,colidx+len(key),1)) :
            temp[row][col] += key[ir][ic]


def dettach(rowidx,colidx, key, lockMap):
    temp = lockMap
    for ir, row in enumerate(range(rowidx,rowidx+len(key),1)) :
        for ic, col in enumerate(range(colidx,colidx+len(key),1)) :
            temp[row][col] -= key[ir][ic]

def check(keysize, locksize,resultMatrix):

    #하나라도 1을 넘기거나 0이 나오면 False
    for rowidx in range(keysize,keysize+locksize,1) :
        for colidx in range(keysize,keysize+locksize,1) :
            if resultMatrix[rowidx][colidx] == 0 or resultMatrix[rowidx][colidx] > 1 : 
                return False

    return True




if __name__ == '__main__' :
    result = solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],[[1, 1, 1], [1, 1, 0], [1, 0, 1]])
    print(result)



"""
https://programmers.co.kr/learn/courses/30/lessons/60059
"""