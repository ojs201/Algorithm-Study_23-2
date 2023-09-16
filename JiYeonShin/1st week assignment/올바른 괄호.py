from collections import deque

def solution(s):
    answer = True
    dq = deque()
    for i in s:
        if(i == "("):
            dq.append("(")
            continue
        
        if(dq):
            dq.pop()
        else:
            dq.append(")")
            break
            
    if(dq):
        return False
    return True