import copy

def solution(weather, k):
    answer = 0
    global real_weather
    global maximum_match_count
    real_weather = weather
    maximum_match_count = 0

    for l in range(k):
        L_size = l + 1
        for rainy_day in range(L_size):
            expect_weather_list = list()
            dfs(L_size,rainy_day,expect_weather_list)

    answer = maximum_match_count
    return answer


def dfs(L_size, rainy_day, expect_weather_list):
    global real_weather
    global maximum_match_count
    if len(expect_weather_list) == len(real_weather):

        match_count = count_match(expect_weather_list,real_weather)
        if match_count > maximum_match_count :
            maximum_match_count = match_count
        return

    for day_weather_forcast in range(2) :
        stacking_expect_weather_list = copy.deepcopy(expect_weather_list)
        stacking_expect_weather_list.append(day_weather_forcast)
        if len(stacking_expect_weather_list) < L_size :
            dfs(L_size,rainy_day,stacking_expect_weather_list)
        else:
            if window_check_rain_count_by_idx(stacking_expect_weather_list,L_size,rainy_day):
                dfs(L_size,rainy_day,stacking_expect_weather_list)
            else : 
                continue

    return


def count_match(first_list,second_list):
    answer = 0
    # first_list와 second_list의 길이가 같다는 가정하에 몇개의 원소가 같은지 센다.
    for idx in range(len(first_list)) :
        if first_list[idx] == second_list[idx] :
            answer += 1

    return answer





def window_check_rain_count_by_idx(weather,L_size,rainy_count) :
    # start_idx ~ end_idx weather를 sub list로 만든다.
    start_idx = -1 * L_size
    sub_weather = weather[start_idx:]
    # sub_weather에 '비'(1)의 갯수를 센다.
    expect_rain_count = sub_weather.count(1)
    if expect_rain_count == rainy_count :
        return True
    else :
        return False



if __name__ == '__main__':
    print('Hello World!')
    weather = [0, 1, 1, 0, 1, 0, 1]
    k = 4
    answer = solution(weather, k)
    print(answer)