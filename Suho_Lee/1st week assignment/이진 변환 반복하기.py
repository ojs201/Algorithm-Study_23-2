# 나의 1차 풀이 -> 리스트로 풀기 실패..!
def solution(s):
    
    change_cnt = 0 # 변환횟수
    zero_cnt = 0 # 제거된 0의 개수
    
    #리스트로 풀자
    s_list = [i for i in s]
    
    while True:
        if len(s_list) == 1:
            break
        
        for i in s_list:
            if i == '0':
                s_list.remove(i)
                zero_cnt+=1
        
        tmp = bin(len(s_list))[2:]
        s_list = [i for i in tmp]
        change_cnt += 1
    
    return [change_cnt, zero_cnt]



# 나의 2차 풀이 : 굳이 for문을 쓰지 않았음
def solution(s):
    change_cnt = 0 # 변환횟수
    zero_cnt = 0 # 제거된 0의 개수
    
    while s!='1':

        zero_cnt += s.count('0') # 0의 개수만 세어주기
        tmp = '1'*s.count('1') # 임시변수에 1의 개수만큼 문자열만들기
        s = bin(len(tmp))[2:] # 이진변환 실행
        change_cnt+=1 #변환횟수 증가시키기
        
    
    return [change_cnt, zero_cnt]
    