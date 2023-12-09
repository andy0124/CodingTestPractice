def solution(v):
    answer = []
    global ttt
    ttt = 1
    print('Hello Python')
    tt = temp_def()
    answer.append(tt)
    return answer


def temp_def() :
    print("test def")
    global ttt
    print(ttt)
    ttt += 1
    print("add ttt")
    print(ttt)
    return 1


if __name__ == '__main__':
    print('Hello World!')
    aa =solution(1)
    print(aa)
