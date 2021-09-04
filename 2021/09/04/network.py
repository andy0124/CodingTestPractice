
def solution(n, computers):
    answer = 0
    queue = list()
    visit = list()
    for i in range(n):
        if i not in visit :
            #bfs 시작
            queue.append(i)
            answer +=1
            while queue :
                current_com = queue[0]
                queue.pop(0) # 맨앞 쪽 제거
                if current_com in visit : continue
                visit.append(current_com)
                for num, connect in enumerate(computers[current_com]) :
                    if connect and num != current_com :
                        queue.append(num)
    return answer


if __name__ == '__main__' :
    result = solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]])
    print(result)


"""
https://programmers.co.kr/learn/courses/30/lessons/43162
"""