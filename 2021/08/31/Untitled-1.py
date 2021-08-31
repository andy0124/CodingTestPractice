


def solution(new_id):
    answer = ''
    
    #1단계
    new_id_low = new_id.lower()
    #2단계
    new_id_eli = []
    for ch in new_id_low :
        if not ((ch >= 'a' and ch <= 'z') or ch == '-' or ch == '_' or ch == '.' or (ch >= '0' and ch <= '9')) :
            continue
        new_id_eli.append(ch)
        
    #3단계
    beforeCh = ''
    new_id_dup = []
    for idx, ch in enumerate(new_id_eli):
        if idx == 0 : 
            beforeCh = ch
            new_id_dup.append(ch)
            continue
        if ch == '.' and beforeCh == '.' :
            continue
        new_id_dup.append(ch)
        beforeCh = ch
        
    #4단계
    if new_id_dup and new_id_dup[0] == '.' : new_id_dup.pop(0)
    if new_id_dup and new_id_dup[-1] == '.' : new_id_dup.pop(-1)
        
    #5단계
    if not new_id_dup : 
        new_id_dup = ['a']
        
    #6단계
    new_id_cut = ""
    if len(new_id_dup) > 15 :
        new_id_cut = new_id_dup[0:15]
    else :
        new_id_cut = new_id_dup
    
    #7단계
    while len(new_id_cut) <= 2 :
        new_id_cut.append(new_id_cut[-1])
        
    answer = ''.join(new_id_cut)
        
        
    return answer

if __name__ == '__main__':

    result = solution("abcdefghijklmn.p")

    print(result)