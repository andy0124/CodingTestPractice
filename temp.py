def solution(s):
    answer = 0
    number = ["zero","one","two","three","four","five","six","seven","eight","nine"]

    for id, num in enumerate(number) :
        if num in s :
            s= s.replace(num,str(id))

    answer = int(s)
    return answer



if __name__ == '__main__' :
    result = solution("one4seveneight")

    print(result)