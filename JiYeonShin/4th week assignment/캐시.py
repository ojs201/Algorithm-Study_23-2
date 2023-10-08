from collections import deque

def solution(cacheSize, cities):
    answer = 0
    dq = deque()
    for city in cities:
        city = city.upper()
        if(city in dq):
            answer += 1
            dq.remove(city)
            dq.appendleft(city)
        else:
            answer += 5
            if(cacheSize == 0):
                continue
            if(len(dq) >= cacheSize):
                dq.pop()
            dq.appendleft(city)
    return answer