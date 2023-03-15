
class test:
    def __init__(self):
        self.min = 10000000
        self.max = 0
    def solution(self,input_num):
        answer = []
        self.repeat(input_num,0)
        answer.append(self.min)
        answer.append(self.max)

        #입력을 받아 온다.
        # 재귀 돌리면서 최소 최대 를 파악한다.
        return answer

##
    def repeat(self,num, cnt):
        #숫자가 몇자리수 인지 파악하고 한자리수면 return 하면서 결과값을 보낸다.
        if int(num / 10) == 0 :
            temp_num = cnt
            if num % 2 == 1: temp_num = temp_num + 1
            if temp_num > self.max : self.max = temp_num
            if temp_num < self.min : self.min = temp_num
            return

        #2자리수면 그 두개를 합치고 다시 repeat 한다.
        if int(num / 100) == 0 :
            temp_cnt = cnt
            first = int(num / 10)
            if first % 2 == 1 : temp_cnt = temp_cnt + 1
            second = num % 10
            if second % 2 ==1 : temp_cnt = temp_cnt + 1
            temp_num = first + second
            self.repeat(temp_num, temp_cnt)
            return

        #3자리 이상이면 이때 부터 분리 시점을 파악한다.
        #숫자를 분리한다.
        temp_num_array = []
        temp_num = num
        while temp_num // 10 > 0 :
            temp_num_array.append(temp_num % 10)
            temp_num = temp_num // 10
        temp_num_array = temp_num_array.reverse()
        




if __name__ == '__main__' :
    ttt = test()
    result = ttt.solution(12)
    print(result)

