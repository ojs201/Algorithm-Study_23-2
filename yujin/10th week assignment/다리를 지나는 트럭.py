# sum 함수를 쓰는 경우 시간초과 -> 현재 다리에 있는 트럭의 무게를 따로 추적하면서 처리
from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0]*bridge_length)
    curr_weights = 0
    
    while bridge:
        answer += 1
        curr_weights -= bridge.popleft()
        if truck_weights:
            if truck_weights[0] + curr_weights <= weight:
                truck = truck_weights.pop(0)
                bridge.append(truck)
                curr_weights += truck
            else:
                bridge.append(0)
    return answer