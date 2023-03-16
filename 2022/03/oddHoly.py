
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



        # 현재 숫자에서 홀수 카운트
        temp_num = num
        temp_cnt = cnt
        temp_array = list()
        while temp_num // 10 > 0 :
            aa = temp_num % 10
            if aa % 2 == 1 :
                temp_cnt = temp_cnt + 1
            temp_array.append(aa % 10)
            temp_num = temp_num // 10

        if temp_num % 2 == 1:
            temp_cnt = temp_cnt + 1
        temp_array.append(temp_num)

        # 3자리 이상인 이 숫자를 여러 케이스로 분리하고 더한다.

        temp_array.reverse()
        for idx_f in range(len(temp_array)) :
            if idx_f >= len(temp_array) - 1 : break
            for idx_s in range(idx_f+1,len(temp_array)) :
                #각 구간의 숫자 임시 저장
                if idx_s >= len(temp_array) - 1 : break
                first = 0
                second = 0
                third = 0
                for f in range(0, idx_f + 1) :
                    first = first * 10 + temp_array[f]
                for s in range(idx_f + 1, idx_s + 1) :
                    second = second * 10 + temp_array[s]
                for th in range(idx_s + 1, len(temp_array)):
                    third = third * 10  + temp_array[th]

                tmp_sum = first + second + third
                self.repeat(tmp_sum,temp_cnt)











if __name__ == '__main__' :
    ttt = test()
    result = ttt.solution(999999999)
    print(result)


