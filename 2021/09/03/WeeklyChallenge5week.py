
"""
1단계 올리기 : 2단계 5번 (+1) -> 1+ 5 * 156 = 781

2단계 올리기 : 3단계 5번 (+1) -> 1+ 5*31 = 156

3단계 올리기 : 4단계 5번 (+1) -> 1 + 5*6 = 31

4단계 올리기 : 5단계 6번 -> 6
"""

count = {
    0 : 781,
    1 : 156,
    2 : 31,
    3 : 6,
    4 : 1
}

ch2num ={
    'A' : 1,
    'E' : 2,
    'I' : 3,
    'O' : 4,
    'U' : 5
}

def solution(string):
    answer = 0
    tempList = []
    for idx in range(len(string)) :
        chNum = ch2num[string[idx]]
        tempList.append(chNum)
    
    for i, num in enumerate(tempList) :
        answer += 1 + (num - 1)*count[i]
        

    return answer


if __name__ == '__main__' :
    result = solution("EIO")
    print(result)


"""
https://programmers.co.kr/learn/courses/30/lessons/84512
"""