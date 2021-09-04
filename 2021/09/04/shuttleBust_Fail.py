def solution(n, t, m, timetable):
    answer = ''
    timetable_list = []
    firstTime = 9*60
    for time in timetable:
        temp = time.split(":")
        timetable_list.append(int(temp[0])*60 + int(temp[1]))
    timetable_list.sort()
    
    #maxTime = firstTime + (n-1) * t
    count = 0
    shuttleTime = firstTime
    beforeTime = -1
    shuttleDict = dict()
    for i in range(n):
        shuttleDict[firstTime + t*i] = []
    
    temp = []
    for idx, time in enumerate(timetable_list) :
        if time <= shuttleTime and len(shuttleDict[shuttleTime]) < m:
            shuttleDict[shuttleTime].append(time)
        else :
            if time > firstTime + (n-1)*t : break
            if n > 1:
                shuttleTime += t
                while time > shuttleTime and shuttleTime < firstTime + (n-1)*t :
                    shuttleTime += t
                shuttleDict[shuttleTime].append(time)
            
    correctTime= 1000        
    if len(shuttleDict[firstTime + (n-1)*t]) < m :
        correctTime = firstTime + (n-1)*t
    else : 
        correctTime = shuttleDict[firstTime + (n-1)*t][m-1] - 1



    
    answer = str(correctTime//60).zfill(2) + ":" +str(correctTime%60).zfill(2)
    
    return answer


if __name__ == '__main__' :
    result = solution(10,60,45,["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"])
    print(result)


"""
https://programmers.co.kr/learn/courses/30/lessons/17678
"""