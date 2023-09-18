def solution(s):
    answer = [0, 0]
    while(s != "1"):
        answer[0] += 1
        answer[1] += s.count("0")
        s = s.replace("0", "")
        s = bin(len(s))[2:] #반환값은 항상 0b 접두어로 시작
    return answer
