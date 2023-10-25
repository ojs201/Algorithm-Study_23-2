from collections import deque

def solution(priorities, location):
    answer = 0
    dq = deque()
    for i in range(len(priorities)):
        dq.append((priorities[i], i))
    while(dq):
        prioritie = dq.popleft()
        if(prioritie[0] == max(priorities)):
            answer += 1
            priorities.remove(prioritie[0])
            if(prioritie[1] == location):
                return answer
        else:
            dq.append(prioritie)
            