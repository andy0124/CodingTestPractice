num_location = {
    0 : {'x' : 0, 'y' : 0},
    1 : {'x' : -1, 'y' : 3},
    2 : {'x' : 0, 'y' : 3},
    3 : {'x' : 1, 'y' : 3},
    4 : {'x' : -1, 'y' : 2},
    5 : {'x' : 0, 'y' : 2},
    6 : {'x' : 1, 'y' : 2},
    7 : {'x' : -1, 'y' : 1},
    8 : {'x' : 0, 'y' : 1},
    9 : {'x' : 1, 'y' : 1},
}




def solution(numbers, hand):
    answer = ''
    rHand = { 'x':1,'y':0}
    lHand = { 'x':-1,'y':0}

    sL = []
    for num in numbers :
        if num == 1 or num == 4 or num == 7 :
            sL.append('L')
            lHand['x'] = num_location[num]['x']
            lHand['y'] = num_location[num]['y']
        elif num == 3 or num == 6 or num == 9 :
            sL.append('R')
            rHand['x'] = num_location[num]['x']
            rHand['y'] = num_location[num]['y']

        else :
            rdis = distance(rHand,num_location[num])
            ldis = distance(lHand,num_location[num])

            if rdis == ldis :
                if hand == "right" :
                    sL.append('R')
                    rHand['x'] = num_location[num]['x']
                    rHand['y'] = num_location[num]['y']
                elif hand == "left" :
                    sL.append('L')
                    lHand['x'] = num_location[num]['x']
                    lHand['y'] = num_location[num]['y']
            elif rdis < ldis :
                sL.append('R')
                rHand['x'] = num_location[num]['x']
                rHand['y'] = num_location[num]['y']
            else :
                sL.append('L')
                lHand['x'] = num_location[num]['x']
                lHand['y'] = num_location[num]['y']

    if len(sL)>0 :
        answer = "".join(sL)

    return answer


def distance(a,b) :
    return (abs(a['x'] - b['x']) + abs(a['y']-b['y']))


if __name__ == '__main__' :
    result = solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2],"left")

    print(result)



    """
    https://programmers.co.kr/learn/courses/30/lessons/67256
    """