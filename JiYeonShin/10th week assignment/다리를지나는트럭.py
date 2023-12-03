#다리 길이만큼의 deque를 만든다. 이때, 트럭이 지나가지 않고 있는 자리는 0으로 채운다.

#다음을 반복한다.
#다리 deque의 제일 앞에 있는 트럭을 빼서 현재 다리 무게 갱신 (시간도 1초 더하기)
#만약 현재 지나가야할 트럭 + 현재 다리 무게가 감당가능하다면 트럭을 다리 deque에 투입
#                                            아니라면 0을 투입

from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    now_weight = 0
    bridge = deque([0]*bridge_length)
    truck = deque(truck_weights)
    while bridge:
        time += 1
        now_weight -= bridge.popleft()
        if truck:
            if now_weight + truck[0] <= weight:
                now_weight += truck[0]
                bridge.append(truck.popleft())
            else:
                bridge.append(0)
    return time