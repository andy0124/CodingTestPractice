
def solution(n, k, cmd):
    answer = ''
    answer_list = []
    answer_check = dict()
    for i in range(n):
        answer_list.append(i)
        answer_check[i] = 'O'
    deleted_list = []
    currentIdx = k

    for element in cmd :
        currentIdx = command(element, currentIdx ,answer_list, deleted_list, answer_check)
    
    answer = "".join(list(answer_check.values()))
    return answer

def command(CMDString, currentIdx ,answer_list, deleted_list, answer_check) :
    CMDList = CMDString.split()
    if len(CMDList) > 1 :
        if CMDList[0] == "U":
            currentIdx -= int(CMDList[1])
            return currentIdx
        elif CMDList[0] == "D":
            currentIdx += int(CMDList[1])
            return currentIdx
    elif CMDList[0] == "C" :
        deleted_list.append((currentIdx,answer_list[currentIdx]))
        answer_check[answer_list[currentIdx]] = 'X'
        answer_list.pop(currentIdx)
        if currentIdx >= len(answer_list) :
            currentIdx -= 1
        return currentIdx
    elif CMDList[0] == "Z" :
        if currentIdx >= deleted_list[-1][0] :
            currentIdx += 1
        answer_list.insert(deleted_list[-1][0],deleted_list[-1][1])
        answer_check[deleted_list[-1][1]] = 'O'
        deleted_list.pop()
        return currentIdx


if __name__ == '__main__' :
    result = solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"])
    print(result)


"""
https://programmers.co.kr/learn/courses/30/lessons/81303
"""