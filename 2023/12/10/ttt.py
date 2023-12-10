
import copy


def solution(maze):
    answer = 0
    
    red_pos = [0,0]
    blue_pos = [0,0]
    
    for row_idx,row_list in enumerate(maze) :
        for col_idx,value in enumerate(row_list) :
            if value == 1 :
                red_pos = [row_idx,col_idx]
            elif value == 2 :
                blue_pos = [row_idx, col_idx]
    
    # 0 : 빈칸, 1 : 빨간구슬, 2 : 파란구슬, 3 : 구멍, 4 : 빨간구슬이 지나간 자리, 5 : 파란구슬이 지나간 자리

    #maze 크기만큼 visited 배열을 만든다.
    red_visited = [[0 for col in range(len(maze[0]))] for row in range(len(maze))]
    blue_visited = [[0 for col in range(len(maze[0]))] for row in range(len(maze))]
    # 각각의 배열의 시작점을 1로 만든다.
    red_visited[red_pos[0]][red_pos[1]] = 1
    blue_visited[blue_pos[0]][blue_pos[1]] = 1
    
    global SUCCESS
    global MIN_TRY
    SUCCESS = False
    MIN_TRY = 1000000000000

    #maze를 print 한다.
    for row in maze :
        print(row)


    dps(red_pos,blue_pos,red_visited,blue_visited,maze,0)
    
    
    if not SUCCESS : 
        answer = 0
    else :
        answer = MIN_TRY
    
    return answer


#6 : 빨간게 지나간거, 7: 파란게 지나간거 8, 둘다 지나간거
# _pos : (x,y)
# 방향 -> 0 : 좌, 1: 상 , 2: 우, 3 : 하


def dps(red_pos,blue_pos, red_visited,blue_visited,edited_maze,term_count):
    
    
    print("red_pos : ",red_pos," blue_pos : ",blue_pos," red_visited : ",red_visited," blue_visited : ",blue_visited," term_count : ",term_count)


    global SUCCESS
    global MIN_TRY
    
    
    dir_list = [[0,-1],[-1,0],[0,1],[1,0]]
    temp_red_pos = red_pos
    temp_blue_pos = blue_pos
    
    if edited_maze[red_pos[0]][red_pos[1]] == 3 and edited_maze[blue_pos[0]][blue_pos[1]] != 4 :
        for blue_dir in dir_list:
            temp_blue_pos = [blue_pos[0] + blue_dir[0], blue_pos[1] + blue_dir[1]]
            if check(temp_red_pos,temp_blue_pos,red_visited,blue_visited,edited_maze) :
                    next_red_visited, next_blue_visited = move_dot(temp_red_pos,temp_blue_pos,red_visited,blue_visited)
                    dps(temp_red_pos, temp_blue_pos, next_red_visited, next_blue_visited,edited_maze,term_count+1)
            
    elif edited_maze[blue_pos[0]][blue_pos[1]] == 4 and edited_maze[red_pos[0]][red_pos[1]] != 3:
        for red_dir in dir_list :
            temp_red_pos = [red_pos[0] + red_dir[0], red_pos[1] + red_dir[1]]
            if check(temp_red_pos,temp_blue_pos,red_visited,blue_visited,edited_maze) :
                    next_red_visited, next_blue_visited = move_dot(temp_red_pos,temp_blue_pos,red_visited,blue_visited)
                    dps(temp_red_pos, temp_blue_pos, next_red_visited, next_blue_visited, edited_maze,term_count+1)
                    
    elif  edited_maze[blue_pos[0]][blue_pos[1]] == 4 and edited_maze[red_pos[0]][red_pos[1]] == 3 :
        SUCCESS = True
        if term_count < MIN_TRY :
            MIN_TRY = term_count
            
    else : 
        for red_dir in dir_list :
            temp_red_pos = [red_pos[0] + red_dir[0], red_pos[1] + red_dir[1]]
            for blue_dir in dir_list:
                temp_blue_pos = [blue_pos[0] + blue_dir[0], blue_pos[1] + blue_dir[1]]
                #이전 redpos와 현재bluepos가 같고, 이전 bluepos와 현재 redpos가 같으면 continue
                if temp_red_pos[0] == blue_pos[0] and temp_red_pos[1] == blue_pos[1] and temp_blue_pos[0] == red_pos[0] and temp_blue_pos[1] == red_pos[1] :
                    continue
                if check(temp_red_pos,temp_blue_pos,red_visited,blue_visited,edited_maze) :
                    next_red_visited, next_blue_visited = move_dot(temp_red_pos,temp_blue_pos,red_visited,blue_visited)
                    dps(temp_red_pos, temp_blue_pos, next_red_visited, next_blue_visited, edited_maze,term_count+1)
                    
    return


def check(red_pos,blue_pos, red_visited,blue_visited, edited_maze) :

    # 각각 범위를 넘겼는지
    if red_pos[0] < 0 or red_pos[0] >= len(edited_maze) :
        return False
    if red_pos[1] < 0 or red_pos[1] >= len(edited_maze[0]) :
        return False
    if blue_pos[0] < 0 or blue_pos[0] >= len(edited_maze) :
        return False
    if blue_pos[1] < 0 or blue_pos[1] >= len(edited_maze[0]) :
        return False
    

    #벽에 부딪혔는지
    if edited_maze[red_pos[0]][red_pos[1]] == 5 or edited_maze[blue_pos[0]][blue_pos[1]] == 5 :
        return False
    
    #겹치는지
    if red_pos[0] == blue_pos[0] and red_pos[1] == blue_pos[1] :
        return False
    
    #빨강이 자기가 방문했던곳인지
    if red_visited[red_pos[0]][red_pos[1]] == 1 and edited_maze[red_pos[0]][red_pos[1]] != 3:
        return False
    
    
    #파랑이 자기가 방문했던곳인지
    if blue_visited[blue_pos[0]][blue_pos[1]] == 1 and edited_maze[blue_pos[0]][blue_pos[1]] != 4:
        return False
    
    
    return True


def move_dot(red_pos,blue_pos, red_visited,blue_visited) :
    
    # 각각의 visited 배열을 복사한다.
    result_red_visited = copy.deepcopy(red_visited)
    result_blue_visited = copy.deepcopy(blue_visited)

    # 각각의 visited 배열의 red_pos, blue_pos 위치를 1로 만든다.
    result_red_visited[red_pos[0]][red_pos[1]] = 1
    result_blue_visited[blue_pos[0]][blue_pos[1]] = 1
    
    #각각의 배열을 return 한다.
    return result_red_visited,result_blue_visited
    
    

if __name__ :
    answer = solution([[4, 1, 2, 3]])
    print(answer)