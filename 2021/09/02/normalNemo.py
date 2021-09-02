import math

def solution(w,h):
    answer = 1

    # if h > w :
    #     diff = math.ceil(h/w)
    #     return (h-diff)*w
    # elif w > h :
    #     diff = math.ceil(w/h)
    #     return h * (w-diff)

    # else :
    #     return w*h - w

    yaksu = math.gcd(w,h)

    return w*h - (w + h -yaksu)



if __name__ == '__main__' :
    result = solution(8,12)
    print(result)


"""
https://programmers.co.kr/learn/courses/30/lessons/62048
"""