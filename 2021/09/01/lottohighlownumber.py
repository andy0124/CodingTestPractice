
def solution(lottos, win_nums):
    zero_count = 0
    matched_count = 0
    for i in lottos :
        if i == 0 :
            zero_count += 1
            continue
        else :
            if i in win_nums :
                matched_count += 1
                del win_nums[win_nums.index(i)]

    high = 7 -(zero_count + matched_count)
    low = 7 -(matched_count)
    if high == 7 :
        high = 6
    if low == 7 : 
        low = 6
    
    return [high, low]


if __name__ == '__main__' :
    result = solution([45, 4, 35, 20, 3, 9],[20, 9, 3, 45, 4, 35])
    print(result)


"""
https://programmers.co.kr/learn/courses/30/lessons/77484
"""