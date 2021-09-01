
check = {
    1 : 1,
    2 : 2,
    3 : 4
}

def solution(n):
    answer = ''

    q, r = divmod(n-1, 3)

    if q ==0 :
        return str(check[r+1])

    q = n
    while q >= 1:
        q, r = divmod(q-1, 3)
        answer = str(check[r+1]) +answer
    
    
    return answer


if __name__ == '__main__' :
    result = solution(3)
    print(result)


"""
https://programmers.co.kr/learn/courses/30/lessons/12899
"""