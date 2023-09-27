from collections import deque

def solution(s):
    answer = 1
    dq = deque()
    for i in s:
        if(dq):
            if(dq[-1] == i):
                dq.pop()
                continue
        dq.append(i)
    if(dq):
        answer = 0
    return answer