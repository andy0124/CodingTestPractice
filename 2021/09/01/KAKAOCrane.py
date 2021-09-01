def solution(board, moves):
    answer = 0

    #각 열의 최상위 위치를 뽑는다
    check = dict()
    for idxy, y in enumerate(board) :
        for dixx, x in enumerate(y) :
            if x != 0 and (dixx+1 not in check) :
                check[dixx+1] = idxy

    # moves 대로 한곳에 넣는다
    cum_list = []
    max_depth = len(board[0])
    for mv in moves :
        if check[mv] < max_depth :
            cum_list.append(board[check[mv]][mv-1])
            check[mv] +=1
            if len(cum_list) >1 and cum_list[-1] == cum_list[-2] :
                answer +=2
                del cum_list[-1]
                del cum_list[-1]
    return answer


if __name__ == '__main__' :
    result = solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4])
    print(result)


"""
https://programmers.co.kr/learn/courses/30/lessons/64061
"""