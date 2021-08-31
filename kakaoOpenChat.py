def solution(record):
    answer = []
    temp = dict()

    for msg in record :
        splited_msg = msg.split(" ")
        if len(splited_msg) == 3 and (splited_msg[0] == "Enter" or splited_msg[0] == "Change"):
            temp[splited_msg[1]] = splited_msg[2]


    for msg in record :
        splited_msg = msg.split(" ")
        if len(splited_msg) == 2 and splited_msg[0] == "Leave" :
            answer.append(temp[splited_msg[1]]+"님이 나갔습니다.")
        elif len(splited_msg) == 3 and splited_msg[0] == "Enter" :
            answer.append(temp[splited_msg[1]]+"님이 들어왔습니다.")

    return answer


if __name__ == '__main__' :
    result = solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])

    print(result)