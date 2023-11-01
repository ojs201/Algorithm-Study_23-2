from heapq import heapify, heappush, heappop

def solution(scoville, K):
    answer = 0
    heapify(scoville)
    while(scoville):
        if(scoville[0] >= K):
            return answer
        first_min = heappop(scoville)
        second_min = heappop(scoville)
        heappush(scoville, first_min + second_min*2)
        answer += 1
    return -1