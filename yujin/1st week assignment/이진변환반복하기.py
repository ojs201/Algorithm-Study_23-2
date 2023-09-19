def solution(s):
    zero = 0
    cnt = 0
    for _ in range(len(s)):
        zero += s.count("0")
        s = s.replace("0","")
        s = bin(len(s))[2:]
        cnt += 1
        if s == '1':
            break
    return cnt, zero