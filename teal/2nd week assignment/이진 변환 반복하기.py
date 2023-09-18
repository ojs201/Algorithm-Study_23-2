def solution(s):
    cnt, zeros= 0,0
    
    # 1이 남을 때까지 반복
    while s != '1':
        zeros += s.count("0")
        s = s.replace("0","")
        s = bin(len(s))[2:] # 0b는 생략
        cnt += 1
    
    answer = [cnt, zeros]
    return answer
