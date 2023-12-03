from collections import deque


def solution(queue1, queue2):
    answer = 0
    q1,q2 = deque(queue1), deque(queue2)
    s1, s2 = sum(queue1), sum(queue2)
    answer, r = 0, len(q1) * 3
    
    if (s1 + s2) % 2 != 0:
        return -1
    while True:
        if s1 > s2:
            x = q1.popleft()
            q2.append(x)
            s1 -= x
            s2 += x
            answer += 1
        elif s2 > s1:
            x = q2.popleft()
            q1.append(x)
            s2 -= x
            s1 += x
            answer += 1
        else:
            break
            
        if answer == r:
            return -1
            
    return answer