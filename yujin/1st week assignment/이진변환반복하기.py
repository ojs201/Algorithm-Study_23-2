def solution(s):
    zero = 0
    cnt = 0
    while s != "1":
        zero += s.count("0")
        s = s.replace("0","")
        s = bin(len(s))[2:] # bin : 이진 표현을 나타내는 접두사 '0b'로 시작
        cnt += 1
    return cnt, zero