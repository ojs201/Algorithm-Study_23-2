#1번과 연결된 도시를 파고들면서 각 마을에 도착하는 최소시간을 구한다.

#1번 도시와 연결된 2번 도시가 있다고 할 때,
#IF 현재 2번 도시까지 걸리는 시간 > 1번 도시까지 걸리는 시간 + 1번도시 에서 2번도시까지 가는데 걸리는 시간 이라면 
#2번 도시까지의 최소시간이 갱신되는것 -> 갱신하고 다시 2번 도시를 큐에 넣어서 2번을 거쳐갈 다른 도시들도 갱신하도록 한다.

from collections import deque

def solution(N, road, K):
    answer = 0
    deliveryTimes = [0, 0] + [500000]*(N-1)
    #그래프 만들기
    graph =  [[] for i in range(N+1)]
    for edge1, edge2, time in road:
        graph[edge1].append([edge2, time])
        graph[edge2].append([edge1, time])
    dq = deque()
    dq.append(1)
    while(dq):
        city = dq.popleft()
        for connectCity, time in graph[city]:
            if(deliveryTimes[connectCity] >= deliveryTimes[city] + time):
                deliveryTimes[connectCity] = deliveryTimes[city] + time
                dq.append(connectCity)
    for i in deliveryTimes[1:]:
        if(i <= K):
            answer += 1
    return answer