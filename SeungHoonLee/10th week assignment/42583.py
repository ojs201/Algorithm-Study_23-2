"""
LV2. 다리를 지나는 트럭
[https://school.programmers.co.kr/learn/courses/30/lessons/42583]

풀이:
0. 현재 남아 있는 트럭의 무게와 다리에 있는 트럭의 무게를 큐로 만든다.
    - 남아 있는 트럭의 무게 => trucks
    - 다리에 남아 있는 트럭의 무게 => bridge

1. trucks에서 트럭 하나를 꺼낸다.
2. 꺼낸 트럭이 다리를 건널 수 있는지 검사한다.

    - 현재 무게 + 트럭.무게 <= 다리 무게
    - len(bridge) < 최대 다리 길이

3-1. <2>번에서 조건에 만족하면 트럭을 bridge에 집어넣는다.
3-2. <2>번에서 조건에 만족하지 않으면 트럭을 다시 trucks의 최상단에 집어넣는다.

4. bridge에 있는 트럭들을 이동시킨다.

5. bridge에 있는 트럭을 갱신한다.
    1. bridge에서 트럭 하나를 꺼낸다.
    2. 꺼낸 트럭이 다리를 건넜는지 검사한다.
        - 트럭.거리 > 다리 길이
        - 트럭이 다리를 건넜을 경우 다음을 계산한다.
            - 현재 무게 += 트럭.무게
    3. <2>번의 조건을 만족하지 않은 경우 트럭을 다시 bridge의 최상단에 집어넣는다.

6. 시간을 +1 증가시킨다.
7. 이후 <1> 과정부터 반복한다.
8. 최종적으로 소요된 시간(초)를 반환한다.
"""
from collections import deque


def solution(bridge_length, weight, truck_weights):
    trucks = deque([(truck, 0) for truck in truck_weights])
    bridge = deque([])

    max_weight = weight
    curr_weight = 0

    answer = 0

    while trucks or bridge:
        if trucks:
            truck_weight, dist = trucks[0]

            if not bridge or curr_weight + truck_weight <= max_weight and len(bridge) < bridge_length:
                bridge.append(trucks.popleft())
                curr_weight += truck_weight

        if bridge:
            for _ in range(len(bridge)):
                truck_weight, dist = bridge.popleft()
                bridge.append((truck_weight, dist + 1))

            for _ in range(len(bridge)):
                truck_weight, dist = bridge.popleft()

                if dist < bridge_length:
                    bridge.appendleft((truck_weight, dist))
                    break

                curr_weight -= truck_weight

        answer += 1

    return answer + 1
