from collections import deque

def calRemainDay(progresse, speed):
    share, remain = divmod(100-progresse, speed)
    if(remain == 0):
        return share
    else:
        return share+1

def solution(progresses, speeds):
    answer = []
    remainDays = deque()
    for i in range(len(progresses)):
        remainDays.append(calRemainDay(progresses[i], speeds[i]))
        
    while(remainDays):
        cnt = 1
        day = remainDays.popleft()
        while(remainDays and remainDays[0] <= day):
            remainDays.popleft()
            cnt += 1
        answer.append(cnt)
    return answer